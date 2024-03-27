import re
import chardet
import mysql.connector
import os
import json

txt_folder = './test'

def location_change(location):
    if location == "桐　生": return 1
    elif location == "戸　田": return 2
    elif location == "江戸川": return 3
    elif location == "平和島": return 4
    elif location == "多摩川": return 5
    elif location == "浜名湖": return 6
    elif location == "蒲　郡": return 7
    elif location == "常　滑": return 8
    elif location == "津": return 9
    elif location == "三　国": return 10
    elif location == "びわこ": return 11
    elif location == "住之江": return 12
    elif location == "尼　崎": return 13
    elif location == "鳴　門": return 14
    elif location == "丸　亀": return 15
    elif location == "児　島": return 16
    elif location == "宮　島": return 17
    elif location == "徳　山": return 18
    elif location == "下　関": return 19
    elif location == "若　松": return 20
    elif location == "芦　屋": return 21
    elif location == "福　岡": return 22
    elif location == "唐　津": return 23
    else: return 24
def weather_change(weather):
    if weather == "晴": return 1
    elif weather == "曇り": return 2
    elif weather == "雨": return 3
    else: return 4
def direction_change(direction):
    if direction == "北": return 1
    elif direction == "北東": return 2
    elif direction == "東": return 3
    elif direction == "南東": return 4
    elif direction == "南": return 5
    elif direction == "南西": return 6
    elif direction == "西": return 7
    else: return 8
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="txt2sql"
)
cursor = db.cursor()
# Create table to store names and ages
cursor.execute("CREATE TABLE IF NOT EXISTS race1 (number INT AUTO_INCREMENT PRIMARY KEY, date date, location INT, \
                race_number INT, trifecta_payout INT, weather INT, wind_direction INT, wind_speed INT, wave_height INT, \
                first_place_horse_number INT, second_place_horse_number INT, third_place_horse_number INT, \
                fourth_place_horse_number INT, fifth_place_horse_number INT, sixth_place_horse_number INT)")
ii = 1
for filename in os.listdir(txt_folder):
    if filename.endswith('.TXT'):
        # Read the text document into a string variable
        with open(os.path.join(txt_folder, filename), 'rb') as file:
            result = chardet.detect(file.read())
        # Read the file with the detected encoding
        with open(os.path.join(txt_folder, filename), 'r', encoding=result['encoding'], errors='ignore') as file:
            # Read the contents of the file
            lines = file.readlines()
        pattern_location = r'(.+?)［成績］'
        pattern_date = r'\d{4}/\s*\d{1,2}/\s*\d{1,2}'
        index = 0
        location = []
        date = []
        race_number = [[] for i in range(len(lines))]
        trifecta_payout = [[] for i in range(len(lines))]
        start_line = len(lines)
        start_line1 = len(lines)
        place_horse_number = []
        
        for i, line in enumerate(lines):
            if '[払戻金]' in line:
                start_line = i
                # if index == 1:
                #     break
            match_location = re.search(pattern_location, line)
            if match_location != None:
                # print(match_location.group(1))
                location.append(match_location.group(1))
            match_date = re.search(pattern_date, line)
            if match_date != None:
                # print(match_date.group())
                date.append(match_date.group())
            
            if i > start_line:
                changed_line = line.split()
                amount = 0
                if "R" in changed_line[0]:
                    race_number[index].append(changed_line[0])
                    trifecta_payout[index].append(changed_line[2])
                else: 
                    if (trifecta_payout[index][-1] < changed_line[1]):
                        del trifecta_payout[index][-1]
                        trifecta_payout[index].append(changed_line[1])
                        trifecta_payout[index][-1] = changed_line[1]
                if len(race_number[index]) == 12:
                    start_line = len(lines)
                    # print(race_number[index])
                    # print(trifecta_payout[index])
                    index += 1
            if 'cm' in line:
                start_line1 = i
                changed_line = line.split()
                race_num = changed_line[0]
                position = race_number[index-1].index(race_num)
                payout = trifecta_payout[index-1][position]
                weather = changed_line[-6]
                wind_direction = changed_line[-4]
                wind_speed = re.search(r'\d?',changed_line[-3]).group()
                wave_height = re.search(r'\d?',changed_line[-1]).group()
                #    print(changed_line[0], changed_line[3], changed_line[5], re.search(r'\d?',changed_line[6]).group(), re.search(r'\d?',changed_line[8]).group())
                place_horse_number = []
            if i > (start_line1+2) and i <= (start_line1+8):
                changed_line = line.split()
                place_horse_number.append(changed_line[2])
                if i == (start_line1+8):
                    start_line1 = len(lines)
                    val = (ii, date[index-1].replace('/ ', '-'),location_change(location[index-1]), race_num, payout, weather_change(weather), direction_change(wind_direction), wind_speed, wave_height) + tuple(place_horse_number[0:6])
                    print(val)
                    new_val = "(" + ",".join([f"\'{x}\'" for x in val]) + ")"
                    cursor.execute('INSERT INTO race1 VALUES' + new_val)
                    ii += 1
                    db.commit()
db.close()
exit(0)