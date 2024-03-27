import re
import chardet
import mysql.connector
import os
import json

player_folder = './test1'
race_folder = "./test"

def change(line, start, end):
    if (line[start:end] == "A1"):
        return 1
    elif (line[start:end] == "A2"):
        return 2
    elif (line[start:end] == "B1"):
        return 3
    else:
        return 4
    
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

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="txt2sql"
)
cursor = db.cursor()

print("[player_info]テーブル　作成中")
ii = 1
# Create table to store names and ages
cursor.execute("CREATE TABLE IF NOT EXISTS player_info (number INT AUTO_INCREMENT PRIMARY KEY, date VARCHAR(7), Race_Number INT, Class INT, Gender INT, Age INT, \
                Win_Rate FLOAT, Place_Rate FLOAT, 1st_Place_Count INT, 2nd_Place_Count INT, Start_Count INT, Top_Finish_Count INT, First_Place_Count INT, Average_Start_Timing FLOAT, \
                Lane_1_Entry_Count INT, Lane_1_Place_Rate FLOAT, Lane_1_Average_Start_Timing FLOAT, Lane_1_Average_Start_Position FLOAT, \
                Lane_2_Entry_Count INT, Lane_2_Place_Rate FLOAT, Lane_2_Average_Start_Timing FLOAT, Lane_2_Average_Start_Position FLOAT, \
                Lane_3_Entry_Count INT, Lane_3_Place_Rate FLOAT, Lane_3_Average_Start_Timing FLOAT, Lane_3_Average_Start_Position FLOAT, \
                Lane_4_Entry_Count INT, Lane_4_Place_Rate FLOAT, Lane_4_Average_Start_Timing FLOAT, Lane_4_Average_Start_Position FLOAT, \
                Lane_5_Entry_Count INT, Lane_5_Place_Rate FLOAT, Lane_5_Average_Start_Timing FLOAT, Lane_5_Average_Start_Position FLOAT, \
                Lane_6_Entry_Count INT, Lane_6_Place_Rate FLOAT, Lane_6_Average_Start_Timing FLOAT, Lane_6_Average_Start_Position FLOAT, \
                Previous_Class INT, Previous_Previous_Class INT, Previous_Previous_Previous_Class INT, Previous_Class_Ability_Index FLOAT, Current_Class_Ability_Index FLOAT, \
                Lane_1_First_Place_Count INT, Lane_1_Second_Place_Count INT, Lane_1_Third_Place_Count INT, Lane_1_Fourth_Place_Count INT, Lane_1_Fifth_Place_Count INT, Lane_1_Sixth_Place_Count INT, \
                Lane_1_Fall_Count INT, Lane_1_Lost_by_0_Lengths_Count INT, Lane_1_Lost_by_1_Length_Count INT, Lane_1_Kept_Lead_by_0_Lengths_Count INT, \
                Lane_1_Kept_Lead_by_1_Length_Count INT, Lane_1_Surged_by_0_Lengths_Count INT, Lane_1_Surged_by_1_Length_Count INT, Lane_1_Surged_by_2_Lengths_Count INT, \
                Lane_2_First_Place_Count INT, Lane_2_Second_Place_Count INT, Lane_2_Third_Place_Count INT, Lane_2_Fourth_Place_Count INT, Lane_2_Fifth_Place_Count INT, Lane_2_Sixth_Place_Count INT, \
                Lane_2_Fall_Count INT, Lane_2_Lost_by_0_Lengths_Count INT, Lane_2_Lost_by_1_Length_Count INT, Lane_2_Kept_Lead_by_0_Lengths_Count INT, \
                Lane_2_Kept_Lead_by_1_Length_Count INT, Lane_2_Surged_by_0_Lengths_Count INT, Lane_2_Surged_by_1_Length_Count INT, Lane_2_Surged_by_2_Lengths_Count INT, \
                Lane_3_First_Place_Count INT, Lane_3_Second_Place_Count INT, Lane_3_Third_Place_Count INT, Lane_3_Fourth_Place_Count INT, Lane_3_Fifth_Place_Count INT, Lane_3_Sixth_Place_Count INT, \
                Lane_3_Fall_Count INT, Lane_3_Lost_by_0_Lengths_Count INT, Lane_3_Lost_by_1_Length_Count INT, Lane_3_Kept_Lead_by_0_Lengths_Count INT, \
                Lane_3_Kept_Lead_by_1_Length_Count INT, Lane_3_Surged_by_0_Lengths_Count INT, Lane_3_Surged_by_1_Length_Count INT, Lane_3_Surged_by_2_Lengths_Count INT, \
                Lane_4_First_Place_Count INT, Lane_4_Second_Place_Count INT, Lane_4_Third_Place_Count INT, Lane_4_Fourth_Place_Count INT, Lane_4_Fifth_Place_Count INT, Lane_4_Sixth_Place_Count INT, \
                Lane_4_Fall_Count INT, Lane_4_Lost_by_0_Lengths_Count INT, Lane_4_Lost_by_1_Length_Count INT, Lane_4_Kept_Lead_by_0_Lengths_Count INT, \
                Lane_4_Kept_Lead_by_1_Length_Count INT, Lane_4_Surged_by_0_Lengths_Count INT, Lane_4_Surged_by_1_Length_Count INT, Lane_4_Surged_by_2_Lengths_Count INT, \
                Lane_5_First_Place_Count INT, Lane_5_Second_Place_Count INT, Lane_5_Third_Place_Count INT, Lane_5_Fourth_Place_Count INT, Lane_5_Fifth_Place_Count INT, Lane_5_Sixth_Place_Count INT, \
                Lane_5_Fall_Count INT, Lane_5_Lost_by_0_Lengths_Count INT, Lane_5_Lost_by_1_Length_Count INT, Lane_5_Kept_Lead_by_0_Lengths_Count INT, \
                Lane_5_Kept_Lead_by_1_Length_Count INT, Lane_5_Surged_by_0_Lengths_Count INT, Lane_5_Surged_by_1_Length_Count INT, Lane_5_Surged_by_2_Lengths_Count INT, \
                Lane_6_First_Place_Count INT, Lane_6_Second_Place_Count INT, Lane_6_Third_Place_Count INT, Lane_6_Fourth_Place_Count INT, Lane_6_Fifth_Place_Count INT, Lane_6_Sixth_Place_Count INT, \
                Lane_6_Fall_Count INT, Lane_6_Lost_by_0_Lengths_Count INT, Lane_6_Lost_by_1_Length_Count INT, Lane_6_Kept_Lead_by_0_Lengths_Count INT, \
                Lane_6_Kept_Lead_by_1_Length_Count INT, Lane_6_Surged_by_0_Lengths_Count INT, Lane_6_Surged_by_1_Length_Count INT, Lane_6_Surged_by_2_Lengths_Count INT, INDEX Race_Number_index (Race_Number))")

for filename in os.listdir(player_folder):
    if filename.endswith('.txt') and len(filename) == 11:
        print(filename + " 処理中")
        year = '20' + filename[3:5]
        month = filename[5:7]
        date = f"{year}-{month}"
        # print(date)
        # Read the text document into a string variable
        with open(os.path.join(player_folder, filename), 'rb') as file:
            result = chardet.detect(file.read())
        # Read the file with the detected encoding
        with open(os.path.join(player_folder, filename), 'r', encoding=result['encoding'], errors='ignore') as file:
            for line in file:
                if len(line) < 2:
                    continue
                Race_Number = line[0:4]
                Class = change(line,29,31)
                Gender = line[38]
                Age = line[39:41]
                Win_Rate = float(line[48:52])/100
                Place_Rate = float(line[52:56])/10
                fst_Place_Count = line[56:59]
                snd_Place_Count = line[59:62]
                Start_Count = line[62:65]
                Top_Finish_Count = line[65:67]
                First_Place_Count = line[67:69]
                Average_Start_Timing = float(line[69:72])/100
                Lane_1_Entry_Count = line[72:75]
                Lane_1_Place_Rate = float(line[75:79])/10
                Lane_1_Average_Start_Timing = float(line[79:82])/100
                Lane_1_Average_Start_Position = float(line[82:85])/100
                Lane_2_Entry_Count = line[85:88]
                Lane_2_Place_Rate = float(line[88:92])/10
                Lane_2_Average_Start_Timing = float(line[92:95])/100
                Lane_2_Average_Start_Position = float(line[95:98])/100
                Lane_3_Entry_Count = line[98:101]
                Lane_3_Place_Rate = float(line[101:105])/10
                Lane_3_Average_Start_Timing = float(line[105:108])/100
                Lane_3_Average_Start_Position = float(line[108:111])/100
                Lane_4_Entry_Count = line[111:114]
                Lane_4_Place_Rate = float(line[114:118])/10
                Lane_4_Average_Start_Timing = float(line[118:121])/100
                Lane_4_Average_Start_Position = float(line[121:124])/100
                Lane_5_Entry_Count = line[124:127]
                Lane_5_Place_Rate = float(line[127:131])/10
                Lane_5_Average_Start_Timing = float(line[131:134])/100
                Lane_5_Average_Start_Position = float(line[134:137])/100
                Lane_6_Entry_Count = line[137:140]
                Lane_6_Place_Rate = float(line[140:144])/10
                Lane_6_Average_Start_Timing = float(line[144:147])/100
                Lane_6_Average_Start_Position = float(line[147:150])/100
                Previous_Class = change(line,150,152)
                Previous_Previous_Class = change(line,152,154)
                Previous_Previous_Previous_Class = change(line,154,156)
                Previous_Class_Ability_Index = float(line[156:160])/100
                Current_Class_Ability_Index = float(line[160:164])/100
                
                Lane_1_First_Place_Count = line[188:191]
                Lane_1_Second_Place_Count = line[191:194]
                Lane_1_Third_Place_Count = line[194:197]
                Lane_1_Fourth_Place_Count = line[197:200]
                Lane_1_Fifth_Place_Count = line[200:203]
                Lane_1_Sixth_Place_Count = line[203:206]
                Lane_1_Fall_Count = line[206:208]
                Lane_1_Lost_by_0_Lengths_Count = line[208:210]
                Lane_1_Lost_by_1_Length_Count = line[210:212]
                Lane_1_Kept_Lead_by_0_Lengths_Count = line[212:214]
                Lane_1_Kept_Lead_by_1_Length_Count = line[214:216]
                Lane_1_Surged_by_0_Lengths_Count = line[216:218]
                Lane_1_Surged_by_1_Length_Count = line[218:220]
                Lane_1_Surged_by_2_Lengths_Count = line[220:222]
                
                Lane_2_First_Place_Count = line[222:225]
                Lane_2_Second_Place_Count = line[225:228]
                Lane_2_Third_Place_Count = line[228:231]
                Lane_2_Fourth_Place_Count = line[231:234]
                Lane_2_Fifth_Place_Count = line[234:237]
                Lane_2_Sixth_Place_Count = line[237:240]
                Lane_2_Fall_Count = line[240:242]
                Lane_2_Lost_by_0_Lengths_Count = line[242:244]
                Lane_2_Lost_by_1_Length_Count = line[244:246]
                Lane_2_Kept_Lead_by_0_Lengths_Count = line[246:248]
                Lane_2_Kept_Lead_by_1_Length_Count = line[248:250]
                Lane_2_Surged_by_0_Lengths_Count = line[250:252]
                Lane_2_Surged_by_1_Length_Count = line[252:254]
                Lane_2_Surged_by_2_Lengths_Count = line[254:256]
                
                Lane_3_First_Place_Count = line[256:259]
                Lane_3_Second_Place_Count = line[259:262]
                Lane_3_Third_Place_Count = line[262:265]
                Lane_3_Fourth_Place_Count = line[265:268]
                Lane_3_Fifth_Place_Count = line[268:271]
                Lane_3_Sixth_Place_Count = line[271:274]
                Lane_3_Fall_Count = line[274:276]
                Lane_3_Lost_by_0_Lengths_Count = line[276:278]
                Lane_3_Lost_by_1_Length_Count = line[278:280]
                Lane_3_Kept_Lead_by_0_Lengths_Count = line[280:282]
                Lane_3_Kept_Lead_by_1_Length_Count = line[282:284]
                Lane_3_Surged_by_0_Lengths_Count = line[284:286]
                Lane_3_Surged_by_1_Length_Count = line[286:288]
                Lane_3_Surged_by_2_Lengths_Count = line[288:290]
                
                Lane_4_First_Place_Count = line[290:293]
                Lane_4_Second_Place_Count = line[293:296]
                Lane_4_Third_Place_Count = line[296:299]
                Lane_4_Fourth_Place_Count = line[299:302]
                Lane_4_Fifth_Place_Count = line[302:305]
                Lane_4_Sixth_Place_Count = line[305:308]
                Lane_4_Fall_Count = line[308:310]
                Lane_4_Lost_by_0_Lengths_Count = line[310:312]
                Lane_4_Lost_by_1_Length_Count = line[312:314]
                Lane_4_Kept_Lead_by_0_Lengths_Count = line[314:316]
                Lane_4_Kept_Lead_by_1_Length_Count = line[316:318]
                Lane_4_Surged_by_0_Lengths_Count = line[318:320]
                Lane_4_Surged_by_1_Length_Count = line[320:322]
                Lane_4_Surged_by_2_Lengths_Count = line[322:324]
                
                Lane_5_First_Place_Count = line[324:327]
                Lane_5_Second_Place_Count = line[327:330]
                Lane_5_Third_Place_Count = line[330:333]
                Lane_5_Fourth_Place_Count = line[333:336]
                Lane_5_Fifth_Place_Count = line[336:339]
                Lane_5_Sixth_Place_Count = line[339:342]
                Lane_5_Fall_Count = line[342:344]
                Lane_5_Lost_by_0_Lengths_Count = line[344:346]
                Lane_5_Lost_by_1_Length_Count = line[346:348]
                Lane_5_Kept_Lead_by_0_Lengths_Count = line[348:350]
                Lane_5_Kept_Lead_by_1_Length_Count = line[350:352]
                Lane_5_Surged_by_0_Lengths_Count = line[352:354]
                Lane_5_Surged_by_1_Length_Count = line[354:356]
                Lane_5_Surged_by_2_Lengths_Count = line[356:358]
                
                Lane_6_First_Place_Count = line[358:361]
                Lane_6_Second_Place_Count = line[361:364]
                Lane_6_Third_Place_Count = line[364:367]
                Lane_6_Fourth_Place_Count = line[367:370]
                Lane_6_Fifth_Place_Count = line[370:373]
                Lane_6_Sixth_Place_Count = line[373:376]
                Lane_6_Fall_Count = line[376:378]
                Lane_6_Lost_by_0_Lengths_Count = line[378:380]
                Lane_6_Lost_by_1_Length_Count = line[380:382]
                Lane_6_Kept_Lead_by_0_Lengths_Count = line[382:384]
                Lane_6_Kept_Lead_by_1_Length_Count = line[384:386]
                Lane_6_Surged_by_0_Lengths_Count = line[386:388]
                Lane_6_Surged_by_1_Length_Count = line[388:390]
                Lane_6_Surged_by_2_Lengths_Count = line[390:392]

                val = (ii,date,Race_Number,Class,Gender,Age,Win_Rate,Place_Rate,fst_Place_Count,snd_Place_Count,Start_Count,Top_Finish_Count,First_Place_Count,Average_Start_Timing, \
                    Lane_1_Entry_Count,Lane_1_Place_Rate,Lane_1_Average_Start_Timing,Lane_1_Average_Start_Position,Lane_2_Entry_Count,Lane_2_Place_Rate,Lane_2_Average_Start_Timing,Lane_2_Average_Start_Position,\
                    Lane_3_Entry_Count,Lane_3_Place_Rate,Lane_3_Average_Start_Timing,Lane_3_Average_Start_Position,Lane_4_Entry_Count,Lane_4_Place_Rate,Lane_4_Average_Start_Timing,Lane_4_Average_Start_Position,\
                    Lane_5_Entry_Count,Lane_5_Place_Rate,Lane_5_Average_Start_Timing,Lane_5_Average_Start_Position,Lane_6_Entry_Count,Lane_6_Place_Rate,Lane_6_Average_Start_Timing,Lane_6_Average_Start_Position,\
                    Previous_Class,Previous_Previous_Class,Previous_Previous_Previous_Class,Previous_Class_Ability_Index,Current_Class_Ability_Index,\
                    Lane_1_First_Place_Count,Lane_1_Second_Place_Count,Lane_1_Third_Place_Count,Lane_1_Fourth_Place_Count,Lane_1_Fifth_Place_Count,Lane_1_Sixth_Place_Count,Lane_1_Fall_Count,Lane_1_Lost_by_0_Lengths_Count,\
                    Lane_1_Lost_by_1_Length_Count,Lane_1_Kept_Lead_by_0_Lengths_Count,Lane_1_Kept_Lead_by_1_Length_Count,Lane_1_Surged_by_0_Lengths_Count,Lane_1_Surged_by_1_Length_Count,Lane_1_Surged_by_2_Lengths_Count,\
                    Lane_2_First_Place_Count,Lane_2_Second_Place_Count,Lane_2_Third_Place_Count,Lane_2_Fourth_Place_Count,Lane_2_Fifth_Place_Count,Lane_2_Sixth_Place_Count,Lane_2_Fall_Count,Lane_2_Lost_by_0_Lengths_Count,\
                    Lane_2_Lost_by_1_Length_Count,Lane_2_Kept_Lead_by_0_Lengths_Count,Lane_2_Kept_Lead_by_1_Length_Count,Lane_2_Surged_by_0_Lengths_Count,Lane_2_Surged_by_1_Length_Count,Lane_2_Surged_by_2_Lengths_Count,\
                    Lane_3_First_Place_Count,Lane_3_Second_Place_Count,Lane_3_Third_Place_Count,Lane_3_Fourth_Place_Count,Lane_3_Fifth_Place_Count,Lane_3_Sixth_Place_Count,Lane_3_Fall_Count,Lane_3_Lost_by_0_Lengths_Count,\
                    Lane_3_Lost_by_1_Length_Count,Lane_3_Kept_Lead_by_0_Lengths_Count,Lane_3_Kept_Lead_by_1_Length_Count,Lane_3_Surged_by_0_Lengths_Count,Lane_3_Surged_by_1_Length_Count,Lane_3_Surged_by_2_Lengths_Count,\
                    Lane_4_First_Place_Count,Lane_4_Second_Place_Count,Lane_4_Third_Place_Count,Lane_4_Fourth_Place_Count,Lane_4_Fifth_Place_Count,Lane_4_Sixth_Place_Count,Lane_4_Fall_Count,Lane_4_Lost_by_0_Lengths_Count,\
                    Lane_4_Lost_by_1_Length_Count,Lane_4_Kept_Lead_by_0_Lengths_Count,Lane_4_Kept_Lead_by_1_Length_Count,Lane_4_Surged_by_0_Lengths_Count,Lane_4_Surged_by_1_Length_Count,Lane_4_Surged_by_2_Lengths_Count,\
                    Lane_5_First_Place_Count,Lane_5_Second_Place_Count,Lane_5_Third_Place_Count,Lane_5_Fourth_Place_Count,Lane_5_Fifth_Place_Count,Lane_5_Sixth_Place_Count,Lane_5_Fall_Count,Lane_5_Lost_by_0_Lengths_Count,\
                    Lane_5_Lost_by_1_Length_Count,Lane_5_Kept_Lead_by_0_Lengths_Count,Lane_5_Kept_Lead_by_1_Length_Count,Lane_5_Surged_by_0_Lengths_Count,Lane_5_Surged_by_1_Length_Count,Lane_5_Surged_by_2_Lengths_Count,\
                    Lane_6_First_Place_Count,Lane_6_Second_Place_Count,Lane_6_Third_Place_Count,Lane_6_Fourth_Place_Count,Lane_6_Fifth_Place_Count,Lane_6_Sixth_Place_Count,Lane_6_Fall_Count,Lane_6_Lost_by_0_Lengths_Count,\
                    Lane_6_Lost_by_1_Length_Count,Lane_6_Kept_Lead_by_0_Lengths_Count,Lane_6_Kept_Lead_by_1_Length_Count,Lane_6_Surged_by_0_Lengths_Count,Lane_6_Surged_by_1_Length_Count,Lane_6_Surged_by_2_Lengths_Count)
                new_val = "(" + ",".join([f"\'{x}\'" for x in val]) + ")"
                cursor.execute('INSERT INTO player_info VALUES' + new_val)
                ii += 1
                db.commit()
print("[player_info]テーブルが作成しました。")
print("==============================================================================")
                
print("[analysis_data]テーブル　作成中")
cursor.execute("CREATE TABLE IF NOT EXISTS analysis_data (number INT AUTO_INCREMENT PRIMARY KEY, date date, location INT, \
                race_number INT, trifecta_payout INT, weather INT, wind_direction INT, wind_speed INT, wave_height INT, judge INT, \
                1st_Class INT, 1st_Gender INT, 1st_Age INT, 1st_Win_Rate FLOAT, 1st_Place_Rate FLOAT, \
                1st_1st_Place_Count INT, 1st_2nd_Place_Count INT, 1st_Start_Count INT, 1st_Top_Finish_Count INT, 1st_First_Place_Count INT, 1st_Average_Start_Timing FLOAT, \
                1st_Lane_1_Entry_Count INT, 1st_Lane_1_Place_Rate FLOAT, 1st_Lane_1_Average_Start_Timing FLOAT, 1st_Lane_1_Average_Start_Position FLOAT, \
                1st_Lane_2_Entry_Count INT, 1st_Lane_2_Place_Rate FLOAT, 1st_Lane_2_Average_Start_Timing FLOAT, 1st_Lane_2_Average_Start_Position FLOAT, \
                1st_Lane_3_Entry_Count INT, 1st_Lane_3_Place_Rate FLOAT, 1st_Lane_3_Average_Start_Timing FLOAT, 1st_Lane_3_Average_Start_Position FLOAT, \
                1st_Lane_4_Entry_Count INT, 1st_Lane_4_Place_Rate FLOAT, 1st_Lane_4_Average_Start_Timing FLOAT, 1st_Lane_4_Average_Start_Position FLOAT, \
                1st_Lane_5_Entry_Count INT, 1st_Lane_5_Place_Rate FLOAT, 1st_Lane_5_Average_Start_Timing FLOAT, 1st_Lane_5_Average_Start_Position FLOAT, \
                1st_Lane_6_Entry_Count INT, 1st_Lane_6_Place_Rate FLOAT, 1st_Lane_6_Average_Start_Timing FLOAT, 1st_Lane_6_Average_Start_Position FLOAT, \
                1st_Previous_Class INT, 1st_Previous_Previous_Class INT, 1st_Previous_Previous_Previous_Class INT, 1st_Previous_Class_Ability_Index FLOAT, 1st_Current_Class_Ability_Index FLOAT, \
                1st_Lane_1_First_Place_Count INT, 1st_Lane_1_Second_Place_Count INT, 1st_Lane_1_Third_Place_Count INT, 1st_Lane_1_Fourth_Place_Count INT, 1st_Lane_1_Fifth_Place_Count INT, 1st_Lane_1_Sixth_Place_Count INT, \
                1st_Lane_1_Fall_Count INT, 1st_Lane_1_Lost_by_0_Lengths_Count INT, 1st_Lane_1_Lost_by_1_Length_Count INT, 1st_Lane_1_Kept_Lead_by_0_Lengths_Count INT, \
                1st_Lane_1_Kept_Lead_by_1_Length_Count INT, 1st_Lane_1_Surged_by_0_Lengths_Count INT, 1st_Lane_1_Surged_by_1_Length_Count INT, 1st_Lane_1_Surged_by_2_Lengths_Count INT, \
                1st_Lane_2_First_Place_Count INT, 1st_Lane_2_Second_Place_Count INT, 1st_Lane_2_Third_Place_Count INT, 1st_Lane_2_Fourth_Place_Count INT, 1st_Lane_2_Fifth_Place_Count INT, 1st_Lane_2_Sixth_Place_Count INT, \
                1st_Lane_2_Fall_Count INT, 1st_Lane_2_Lost_by_0_Lengths_Count INT, 1st_Lane_2_Lost_by_1_Length_Count INT, 1st_Lane_2_Kept_Lead_by_0_Lengths_Count INT, \
                1st_Lane_2_Kept_Lead_by_1_Length_Count INT, 1st_Lane_2_Surged_by_0_Lengths_Count INT, 1st_Lane_2_Surged_by_1_Length_Count INT, 1st_Lane_2_Surged_by_2_Lengths_Count INT, \
                1st_Lane_3_First_Place_Count INT, 1st_Lane_3_Second_Place_Count INT, 1st_Lane_3_Third_Place_Count INT, 1st_Lane_3_Fourth_Place_Count INT, 1st_Lane_3_Fifth_Place_Count INT, 1st_Lane_3_Sixth_Place_Count INT, \
                1st_Lane_3_Fall_Count INT, 1st_Lane_3_Lost_by_0_Lengths_Count INT, 1st_Lane_3_Lost_by_1_Length_Count INT, 1st_Lane_3_Kept_Lead_by_0_Lengths_Count INT, \
                1st_Lane_3_Kept_Lead_by_1_Length_Count INT, 1st_Lane_3_Surged_by_0_Lengths_Count INT, 1st_Lane_3_Surged_by_1_Length_Count INT, 1st_Lane_3_Surged_by_2_Lengths_Count INT, \
                1st_Lane_4_First_Place_Count INT, 1st_Lane_4_Second_Place_Count INT, 1st_Lane_4_Third_Place_Count INT, 1st_Lane_4_Fourth_Place_Count INT, 1st_Lane_4_Fifth_Place_Count INT, 1st_Lane_4_Sixth_Place_Count INT, \
                1st_Lane_4_Fall_Count INT, 1st_Lane_4_Lost_by_0_Lengths_Count INT, 1st_Lane_4_Lost_by_1_Length_Count INT, 1st_Lane_4_Kept_Lead_by_0_Lengths_Count INT, \
                1st_Lane_4_Kept_Lead_by_1_Length_Count INT, 1st_Lane_4_Surged_by_0_Lengths_Count INT, 1st_Lane_4_Surged_by_1_Length_Count INT, 1st_Lane_4_Surged_by_2_Lengths_Count INT, \
                1st_Lane_5_First_Place_Count INT, 1st_Lane_5_Second_Place_Count INT, 1st_Lane_5_Third_Place_Count INT, 1st_Lane_5_Fourth_Place_Count INT, 1st_Lane_5_Fifth_Place_Count INT, 1st_Lane_5_Sixth_Place_Count INT, \
                1st_Lane_5_Fall_Count INT, 1st_Lane_5_Lost_by_0_Lengths_Count INT, 1st_Lane_5_Lost_by_1_Length_Count INT, 1st_Lane_5_Kept_Lead_by_0_Lengths_Count INT, \
                1st_Lane_5_Kept_Lead_by_1_Length_Count INT, 1st_Lane_5_Surged_by_0_Lengths_Count INT, 1st_Lane_5_Surged_by_1_Length_Count INT, 1st_Lane_5_Surged_by_2_Lengths_Count INT, \
                1st_Lane_6_First_Place_Count INT, 1st_Lane_6_Second_Place_Count INT, 1st_Lane_6_Third_Place_Count INT, 1st_Lane_6_Fourth_Place_Count INT, 1st_Lane_6_Fifth_Place_Count INT, 1st_Lane_6_Sixth_Place_Count INT, \
                1st_Lane_6_Fall_Count INT, 1st_Lane_6_Lost_by_0_Lengths_Count INT, 1st_Lane_6_Lost_by_1_Length_Count INT, 1st_Lane_6_Kept_Lead_by_0_Lengths_Count INT, \
                1st_Lane_6_Kept_Lead_by_1_Length_Count INT, 1st_Lane_6_Surged_by_0_Lengths_Count INT, 1st_Lane_6_Surged_by_1_Length_Count INT, 1st_Lane_6_Surged_by_2_Lengths_Count INT, \
                2nd_Class INT, 2nd_Gender INT, 2nd_Age INT, 2nd_Win_Rate FLOAT, 2nd_Place_Rate FLOAT, \
                2nd_1st_Place_Count INT, 2nd_2nd_Place_Count INT, 2nd_Start_Count INT, 2nd_Top_Finish_Count INT, 2nd_First_Place_Count INT, 2nd_Average_Start_Timing FLOAT, \
                2nd_Lane_1_Entry_Count INT, 2nd_Lane_1_Place_Rate FLOAT, 2nd_Lane_1_Average_Start_Timing FLOAT, 2nd_Lane_1_Average_Start_Position FLOAT, \
                2nd_Lane_2_Entry_Count INT, 2nd_Lane_2_Place_Rate FLOAT, 2nd_Lane_2_Average_Start_Timing FLOAT, 2nd_Lane_2_Average_Start_Position FLOAT, \
                2nd_Lane_3_Entry_Count INT, 2nd_Lane_3_Place_Rate FLOAT, 2nd_Lane_3_Average_Start_Timing FLOAT, 2nd_Lane_3_Average_Start_Position FLOAT, \
                2nd_Lane_4_Entry_Count INT, 2nd_Lane_4_Place_Rate FLOAT, 2nd_Lane_4_Average_Start_Timing FLOAT, 2nd_Lane_4_Average_Start_Position FLOAT, \
                2nd_Lane_5_Entry_Count INT, 2nd_Lane_5_Place_Rate FLOAT, 2nd_Lane_5_Average_Start_Timing FLOAT, 2nd_Lane_5_Average_Start_Position FLOAT, \
                2nd_Lane_6_Entry_Count INT, 2nd_Lane_6_Place_Rate FLOAT, 2nd_Lane_6_Average_Start_Timing FLOAT, 2nd_Lane_6_Average_Start_Position FLOAT, \
                2nd_Previous_Class INT, 2nd_Previous_Previous_Class INT, 2nd_Previous_Previous_Previous_Class INT, 2nd_Previous_Class_Ability_Index FLOAT, 2nd_Current_Class_Ability_Index FLOAT, \
                2nd_Lane_1_First_Place_Count INT, 2nd_Lane_1_Second_Place_Count INT, 2nd_Lane_1_Third_Place_Count INT, 2nd_Lane_1_Fourth_Place_Count INT, 2nd_Lane_1_Fifth_Place_Count INT, 2nd_Lane_1_Sixth_Place_Count INT, \
                2nd_Lane_1_Fall_Count INT, 2nd_Lane_1_Lost_by_0_Lengths_Count INT, 2nd_Lane_1_Lost_by_1_Length_Count INT, 2nd_Lane_1_Kept_Lead_by_0_Lengths_Count INT, \
                2nd_Lane_1_Kept_Lead_by_1_Length_Count INT, 2nd_Lane_1_Surged_by_0_Lengths_Count INT, 2nd_Lane_1_Surged_by_1_Length_Count INT, 2nd_Lane_1_Surged_by_2_Lengths_Count INT, \
                2nd_Lane_2_First_Place_Count INT, 2nd_Lane_2_Second_Place_Count INT, 2nd_Lane_2_Third_Place_Count INT, 2nd_Lane_2_Fourth_Place_Count INT, 2nd_Lane_2_Fifth_Place_Count INT, 2nd_Lane_2_Sixth_Place_Count INT, \
                2nd_Lane_2_Fall_Count INT, 2nd_Lane_2_Lost_by_0_Lengths_Count INT, 2nd_Lane_2_Lost_by_1_Length_Count INT, 2nd_Lane_2_Kept_Lead_by_0_Lengths_Count INT, \
                2nd_Lane_2_Kept_Lead_by_1_Length_Count INT, 2nd_Lane_2_Surged_by_0_Lengths_Count INT, 2nd_Lane_2_Surged_by_1_Length_Count INT, 2nd_Lane_2_Surged_by_2_Lengths_Count INT, \
                2nd_Lane_3_First_Place_Count INT, 2nd_Lane_3_Second_Place_Count INT, 2nd_Lane_3_Third_Place_Count INT, 2nd_Lane_3_Fourth_Place_Count INT, 2nd_Lane_3_Fifth_Place_Count INT, 2nd_Lane_3_Sixth_Place_Count INT, \
                2nd_Lane_3_Fall_Count INT, 2nd_Lane_3_Lost_by_0_Lengths_Count INT, 2nd_Lane_3_Lost_by_1_Length_Count INT, 2nd_Lane_3_Kept_Lead_by_0_Lengths_Count INT, \
                2nd_Lane_3_Kept_Lead_by_1_Length_Count INT, 2nd_Lane_3_Surged_by_0_Lengths_Count INT, 2nd_Lane_3_Surged_by_1_Length_Count INT, 2nd_Lane_3_Surged_by_2_Lengths_Count INT, \
                2nd_Lane_4_First_Place_Count INT, 2nd_Lane_4_Second_Place_Count INT, 2nd_Lane_4_Third_Place_Count INT, 2nd_Lane_4_Fourth_Place_Count INT, 2nd_Lane_4_Fifth_Place_Count INT, 2nd_Lane_4_Sixth_Place_Count INT, \
                2nd_Lane_4_Fall_Count INT, 2nd_Lane_4_Lost_by_0_Lengths_Count INT, 2nd_Lane_4_Lost_by_1_Length_Count INT, 2nd_Lane_4_Kept_Lead_by_0_Lengths_Count INT, \
                2nd_Lane_4_Kept_Lead_by_1_Length_Count INT, 2nd_Lane_4_Surged_by_0_Lengths_Count INT, 2nd_Lane_4_Surged_by_1_Length_Count INT, 2nd_Lane_4_Surged_by_2_Lengths_Count INT, \
                2nd_Lane_5_First_Place_Count INT, 2nd_Lane_5_Second_Place_Count INT, 2nd_Lane_5_Third_Place_Count INT, 2nd_Lane_5_Fourth_Place_Count INT, 2nd_Lane_5_Fifth_Place_Count INT, 2nd_Lane_5_Sixth_Place_Count INT, \
                2nd_Lane_5_Fall_Count INT, 2nd_Lane_5_Lost_by_0_Lengths_Count INT, 2nd_Lane_5_Lost_by_1_Length_Count INT, 2nd_Lane_5_Kept_Lead_by_0_Lengths_Count INT, \
                2nd_Lane_5_Kept_Lead_by_1_Length_Count INT, 2nd_Lane_5_Surged_by_0_Lengths_Count INT, 2nd_Lane_5_Surged_by_1_Length_Count INT, 2nd_Lane_5_Surged_by_2_Lengths_Count INT, \
                2nd_Lane_6_First_Place_Count INT, 2nd_Lane_6_Second_Place_Count INT, 2nd_Lane_6_Third_Place_Count INT, 2nd_Lane_6_Fourth_Place_Count INT, 2nd_Lane_6_Fifth_Place_Count INT, 2nd_Lane_6_Sixth_Place_Count INT, \
                2nd_Lane_6_Fall_Count INT, 2nd_Lane_6_Lost_by_0_Lengths_Count INT, 2nd_Lane_6_Lost_by_1_Length_Count INT, 2nd_Lane_6_Kept_Lead_by_0_Lengths_Count INT, \
                2nd_Lane_6_Kept_Lead_by_1_Length_Count INT, 2nd_Lane_6_Surged_by_0_Lengths_Count INT, 2nd_Lane_6_Surged_by_1_Length_Count INT, 2nd_Lane_6_Surged_by_2_Lengths_Count INT, \
                3rd_Class INT, 3rd_Gender INT, 3rd_Age INT, 3rd_Win_Rate FLOAT, 3rd_Place_Rate FLOAT, \
                3rd_1st_Place_Count INT, 3rd_2nd_Place_Count INT, 3rd_Start_Count INT, 3rd_Top_Finish_Count INT, 3rd_First_Place_Count INT, 3rd_Average_Start_Timing FLOAT, \
                3rd_Lane_1_Entry_Count INT, 3rd_Lane_1_Place_Rate FLOAT, 3rd_Lane_1_Average_Start_Timing FLOAT, 3rd_Lane_1_Average_Start_Position FLOAT, \
                3rd_Lane_2_Entry_Count INT, 3rd_Lane_2_Place_Rate FLOAT, 3rd_Lane_2_Average_Start_Timing FLOAT, 3rd_Lane_2_Average_Start_Position FLOAT, \
                3rd_Lane_3_Entry_Count INT, 3rd_Lane_3_Place_Rate FLOAT, 3rd_Lane_3_Average_Start_Timing FLOAT, 3rd_Lane_3_Average_Start_Position FLOAT, \
                3rd_Lane_4_Entry_Count INT, 3rd_Lane_4_Place_Rate FLOAT, 3rd_Lane_4_Average_Start_Timing FLOAT, 3rd_Lane_4_Average_Start_Position FLOAT, \
                3rd_Lane_5_Entry_Count INT, 3rd_Lane_5_Place_Rate FLOAT, 3rd_Lane_5_Average_Start_Timing FLOAT, 3rd_Lane_5_Average_Start_Position FLOAT, \
                3rd_Lane_6_Entry_Count INT, 3rd_Lane_6_Place_Rate FLOAT, 3rd_Lane_6_Average_Start_Timing FLOAT, 3rd_Lane_6_Average_Start_Position FLOAT, \
                3rd_Previous_Class INT, 3rd_Previous_Previous_Class INT, 3rd_Previous_Previous_Previous_Class INT, 3rd_Previous_Class_Ability_Index FLOAT, 3rd_Current_Class_Ability_Index FLOAT, \
                3rd_Lane_1_First_Place_Count INT, 3rd_Lane_1_Second_Place_Count INT, 3rd_Lane_1_Third_Place_Count INT, 3rd_Lane_1_Fourth_Place_Count INT, 3rd_Lane_1_Fifth_Place_Count INT, 3rd_Lane_1_Sixth_Place_Count INT, \
                3rd_Lane_1_Fall_Count INT, 3rd_Lane_1_Lost_by_0_Lengths_Count INT, 3rd_Lane_1_Lost_by_1_Length_Count INT, 3rd_Lane_1_Kept_Lead_by_0_Lengths_Count INT, \
                3rd_Lane_1_Kept_Lead_by_1_Length_Count INT, 3rd_Lane_1_Surged_by_0_Lengths_Count INT, 3rd_Lane_1_Surged_by_1_Length_Count INT, 3rd_Lane_1_Surged_by_2_Lengths_Count INT, \
                3rd_Lane_2_First_Place_Count INT, 3rd_Lane_2_Second_Place_Count INT, 3rd_Lane_2_Third_Place_Count INT, 3rd_Lane_2_Fourth_Place_Count INT, 3rd_Lane_2_Fifth_Place_Count INT, 3rd_Lane_2_Sixth_Place_Count INT, \
                3rd_Lane_2_Fall_Count INT, 3rd_Lane_2_Lost_by_0_Lengths_Count INT, 3rd_Lane_2_Lost_by_1_Length_Count INT, 3rd_Lane_2_Kept_Lead_by_0_Lengths_Count INT, \
                3rd_Lane_2_Kept_Lead_by_1_Length_Count INT, 3rd_Lane_2_Surged_by_0_Lengths_Count INT, 3rd_Lane_2_Surged_by_1_Length_Count INT, 3rd_Lane_2_Surged_by_2_Lengths_Count INT, \
                3rd_Lane_3_First_Place_Count INT, 3rd_Lane_3_Second_Place_Count INT, 3rd_Lane_3_Third_Place_Count INT, 3rd_Lane_3_Fourth_Place_Count INT, 3rd_Lane_3_Fifth_Place_Count INT, 3rd_Lane_3_Sixth_Place_Count INT, \
                3rd_Lane_3_Fall_Count INT, 3rd_Lane_3_Lost_by_0_Lengths_Count INT, 3rd_Lane_3_Lost_by_1_Length_Count INT, 3rd_Lane_3_Kept_Lead_by_0_Lengths_Count INT, \
                3rd_Lane_3_Kept_Lead_by_1_Length_Count INT, 3rd_Lane_3_Surged_by_0_Lengths_Count INT, 3rd_Lane_3_Surged_by_1_Length_Count INT, 3rd_Lane_3_Surged_by_2_Lengths_Count INT, \
                3rd_Lane_4_First_Place_Count INT, 3rd_Lane_4_Second_Place_Count INT, 3rd_Lane_4_Third_Place_Count INT, 3rd_Lane_4_Fourth_Place_Count INT, 3rd_Lane_4_Fifth_Place_Count INT, 3rd_Lane_4_Sixth_Place_Count INT, \
                3rd_Lane_4_Fall_Count INT, 3rd_Lane_4_Lost_by_0_Lengths_Count INT, 3rd_Lane_4_Lost_by_1_Length_Count INT, 3rd_Lane_4_Kept_Lead_by_0_Lengths_Count INT, \
                3rd_Lane_4_Kept_Lead_by_1_Length_Count INT, 3rd_Lane_4_Surged_by_0_Lengths_Count INT, 3rd_Lane_4_Surged_by_1_Length_Count INT, 3rd_Lane_4_Surged_by_2_Lengths_Count INT, \
                3rd_Lane_5_First_Place_Count INT, 3rd_Lane_5_Second_Place_Count INT, 3rd_Lane_5_Third_Place_Count INT, 3rd_Lane_5_Fourth_Place_Count INT, 3rd_Lane_5_Fifth_Place_Count INT, 3rd_Lane_5_Sixth_Place_Count INT, \
                3rd_Lane_5_Fall_Count INT, 3rd_Lane_5_Lost_by_0_Lengths_Count INT, 3rd_Lane_5_Lost_by_1_Length_Count INT, 3rd_Lane_5_Kept_Lead_by_0_Lengths_Count INT, \
                3rd_Lane_5_Kept_Lead_by_1_Length_Count INT, 3rd_Lane_5_Surged_by_0_Lengths_Count INT, 3rd_Lane_5_Surged_by_1_Length_Count INT, 3rd_Lane_5_Surged_by_2_Lengths_Count INT, \
                3rd_Lane_6_First_Place_Count INT, 3rd_Lane_6_Second_Place_Count INT, 3rd_Lane_6_Third_Place_Count INT, 3rd_Lane_6_Fourth_Place_Count INT, 3rd_Lane_6_Fifth_Place_Count INT, 3rd_Lane_6_Sixth_Place_Count INT, \
                3rd_Lane_6_Fall_Count INT, 3rd_Lane_6_Lost_by_0_Lengths_Count INT, 3rd_Lane_6_Lost_by_1_Length_Count INT, 3rd_Lane_6_Kept_Lead_by_0_Lengths_Count INT, \
                3rd_Lane_6_Kept_Lead_by_1_Length_Count INT, 3rd_Lane_6_Surged_by_0_Lengths_Count INT, 3rd_Lane_6_Surged_by_1_Length_Count INT, 3rd_Lane_6_Surged_by_2_Lengths_Count INT, \
                4th_Class INT, 4th_Gender INT, 4th_Age INT, 4th_Win_Rate FLOAT, 4th_Place_Rate FLOAT, \
                4th_1st_Place_Count INT, 4th_2nd_Place_Count INT, 4th_Start_Count INT, 4th_Top_Finish_Count INT, 4th_First_Place_Count INT, 4th_Average_Start_Timing FLOAT, \
                4th_Lane_1_Entry_Count INT, 4th_Lane_1_Place_Rate FLOAT, 4th_Lane_1_Average_Start_Timing FLOAT, 4th_Lane_1_Average_Start_Position FLOAT, \
                4th_Lane_2_Entry_Count INT, 4th_Lane_2_Place_Rate FLOAT, 4th_Lane_2_Average_Start_Timing FLOAT, 4th_Lane_2_Average_Start_Position FLOAT, \
                4th_Lane_3_Entry_Count INT, 4th_Lane_3_Place_Rate FLOAT, 4th_Lane_3_Average_Start_Timing FLOAT, 4th_Lane_3_Average_Start_Position FLOAT, \
                4th_Lane_4_Entry_Count INT, 4th_Lane_4_Place_Rate FLOAT, 4th_Lane_4_Average_Start_Timing FLOAT, 4th_Lane_4_Average_Start_Position FLOAT, \
                4th_Lane_5_Entry_Count INT, 4th_Lane_5_Place_Rate FLOAT, 4th_Lane_5_Average_Start_Timing FLOAT, 4th_Lane_5_Average_Start_Position FLOAT, \
                4th_Lane_6_Entry_Count INT, 4th_Lane_6_Place_Rate FLOAT, 4th_Lane_6_Average_Start_Timing FLOAT, 4th_Lane_6_Average_Start_Position FLOAT, \
                4th_Previous_Class INT, 4th_Previous_Previous_Class INT, 4th_Previous_Previous_Previous_Class INT, 4th_Previous_Class_Ability_Index FLOAT, 4th_Current_Class_Ability_Index FLOAT, \
                4th_Lane_1_First_Place_Count INT, 4th_Lane_1_Second_Place_Count INT, 4th_Lane_1_Third_Place_Count INT, 4th_Lane_1_Fourth_Place_Count INT, 4th_Lane_1_Fifth_Place_Count INT, 4th_Lane_1_Sixth_Place_Count INT, \
                4th_Lane_1_Fall_Count INT, 4th_Lane_1_Lost_by_0_Lengths_Count INT, 4th_Lane_1_Lost_by_1_Length_Count INT, 4th_Lane_1_Kept_Lead_by_0_Lengths_Count INT, \
                4th_Lane_1_Kept_Lead_by_1_Length_Count INT, 4th_Lane_1_Surged_by_0_Lengths_Count INT, 4th_Lane_1_Surged_by_1_Length_Count INT, 4th_Lane_1_Surged_by_2_Lengths_Count INT, \
                4th_Lane_2_First_Place_Count INT, 4th_Lane_2_Second_Place_Count INT, 4th_Lane_2_Third_Place_Count INT, 4th_Lane_2_Fourth_Place_Count INT, 4th_Lane_2_Fifth_Place_Count INT, 4th_Lane_2_Sixth_Place_Count INT, \
                4th_Lane_2_Fall_Count INT, 4th_Lane_2_Lost_by_0_Lengths_Count INT, 4th_Lane_2_Lost_by_1_Length_Count INT, 4th_Lane_2_Kept_Lead_by_0_Lengths_Count INT, \
                4th_Lane_2_Kept_Lead_by_1_Length_Count INT, 4th_Lane_2_Surged_by_0_Lengths_Count INT, 4th_Lane_2_Surged_by_1_Length_Count INT, 4th_Lane_2_Surged_by_2_Lengths_Count INT, \
                4th_Lane_3_First_Place_Count INT, 4th_Lane_3_Second_Place_Count INT, 4th_Lane_3_Third_Place_Count INT, 4th_Lane_3_Fourth_Place_Count INT, 4th_Lane_3_Fifth_Place_Count INT, 4th_Lane_3_Sixth_Place_Count INT, \
                4th_Lane_3_Fall_Count INT, 4th_Lane_3_Lost_by_0_Lengths_Count INT, 4th_Lane_3_Lost_by_1_Length_Count INT, 4th_Lane_3_Kept_Lead_by_0_Lengths_Count INT, \
                4th_Lane_3_Kept_Lead_by_1_Length_Count INT, 4th_Lane_3_Surged_by_0_Lengths_Count INT, 4th_Lane_3_Surged_by_1_Length_Count INT, 4th_Lane_3_Surged_by_2_Lengths_Count INT, \
                4th_Lane_4_First_Place_Count INT, 4th_Lane_4_Second_Place_Count INT, 4th_Lane_4_Third_Place_Count INT, 4th_Lane_4_Fourth_Place_Count INT, 4th_Lane_4_Fifth_Place_Count INT, 4th_Lane_4_Sixth_Place_Count INT, \
                4th_Lane_4_Fall_Count INT, 4th_Lane_4_Lost_by_0_Lengths_Count INT, 4th_Lane_4_Lost_by_1_Length_Count INT, 4th_Lane_4_Kept_Lead_by_0_Lengths_Count INT, \
                4th_Lane_4_Kept_Lead_by_1_Length_Count INT, 4th_Lane_4_Surged_by_0_Lengths_Count INT, 4th_Lane_4_Surged_by_1_Length_Count INT, 4th_Lane_4_Surged_by_2_Lengths_Count INT, \
                4th_Lane_5_First_Place_Count INT, 4th_Lane_5_Second_Place_Count INT, 4th_Lane_5_Third_Place_Count INT, 4th_Lane_5_Fourth_Place_Count INT, 4th_Lane_5_Fifth_Place_Count INT, 4th_Lane_5_Sixth_Place_Count INT, \
                4th_Lane_5_Fall_Count INT, 4th_Lane_5_Lost_by_0_Lengths_Count INT, 4th_Lane_5_Lost_by_1_Length_Count INT, 4th_Lane_5_Kept_Lead_by_0_Lengths_Count INT, \
                4th_Lane_5_Kept_Lead_by_1_Length_Count INT, 4th_Lane_5_Surged_by_0_Lengths_Count INT, 4th_Lane_5_Surged_by_1_Length_Count INT, 4th_Lane_5_Surged_by_2_Lengths_Count INT, \
                4th_Lane_6_First_Place_Count INT, 4th_Lane_6_Second_Place_Count INT, 4th_Lane_6_Third_Place_Count INT, 4th_Lane_6_Fourth_Place_Count INT, 4th_Lane_6_Fifth_Place_Count INT, 4th_Lane_6_Sixth_Place_Count INT, \
                4th_Lane_6_Fall_Count INT, 4th_Lane_6_Lost_by_0_Lengths_Count INT, 4th_Lane_6_Lost_by_1_Length_Count INT, 4th_Lane_6_Kept_Lead_by_0_Lengths_Count INT, \
                4th_Lane_6_Kept_Lead_by_1_Length_Count INT, 4th_Lane_6_Surged_by_0_Lengths_Count INT, 4th_Lane_6_Surged_by_1_Length_Count INT, 4th_Lane_6_Surged_by_2_Lengths_Count INT, \
                5th_Class INT, 5th_Gender INT, 5th_Age INT, 5th_Win_Rate FLOAT, 5th_Place_Rate FLOAT, \
                5th_1st_Place_Count INT, 5th_2nd_Place_Count INT, 5th_Start_Count INT, 5th_Top_Finish_Count INT, 5th_First_Place_Count INT, 5th_Average_Start_Timing FLOAT, \
                5th_Lane_1_Entry_Count INT, 5th_Lane_1_Place_Rate FLOAT, 5th_Lane_1_Average_Start_Timing FLOAT, 5th_Lane_1_Average_Start_Position FLOAT, \
                5th_Lane_2_Entry_Count INT, 5th_Lane_2_Place_Rate FLOAT, 5th_Lane_2_Average_Start_Timing FLOAT, 5th_Lane_2_Average_Start_Position FLOAT, \
                5th_Lane_3_Entry_Count INT, 5th_Lane_3_Place_Rate FLOAT, 5th_Lane_3_Average_Start_Timing FLOAT, 5th_Lane_3_Average_Start_Position FLOAT, \
                5th_Lane_4_Entry_Count INT, 5th_Lane_4_Place_Rate FLOAT, 5th_Lane_4_Average_Start_Timing FLOAT, 5th_Lane_4_Average_Start_Position FLOAT, \
                5th_Lane_5_Entry_Count INT, 5th_Lane_5_Place_Rate FLOAT, 5th_Lane_5_Average_Start_Timing FLOAT, 5th_Lane_5_Average_Start_Position FLOAT, \
                5th_Lane_6_Entry_Count INT, 5th_Lane_6_Place_Rate FLOAT, 5th_Lane_6_Average_Start_Timing FLOAT, 5th_Lane_6_Average_Start_Position FLOAT, \
                5th_Previous_Class INT, 5th_Previous_Previous_Class INT, 5th_Previous_Previous_Previous_Class INT, 5th_Previous_Class_Ability_Index FLOAT, 5th_Current_Class_Ability_Index FLOAT, \
                5th_Lane_1_First_Place_Count INT, 5th_Lane_1_Second_Place_Count INT, 5th_Lane_1_Third_Place_Count INT, 5th_Lane_1_Fourth_Place_Count INT, 5th_Lane_1_Fifth_Place_Count INT, 5th_Lane_1_Sixth_Place_Count INT, \
                5th_Lane_1_Fall_Count INT, 5th_Lane_1_Lost_by_0_Lengths_Count INT, 5th_Lane_1_Lost_by_1_Length_Count INT, 5th_Lane_1_Kept_Lead_by_0_Lengths_Count INT, \
                5th_Lane_1_Kept_Lead_by_1_Length_Count INT, 5th_Lane_1_Surged_by_0_Lengths_Count INT, 5th_Lane_1_Surged_by_1_Length_Count INT, 5th_Lane_1_Surged_by_2_Lengths_Count INT, \
                5th_Lane_2_First_Place_Count INT, 5th_Lane_2_Second_Place_Count INT, 5th_Lane_2_Third_Place_Count INT, 5th_Lane_2_Fourth_Place_Count INT, 5th_Lane_2_Fifth_Place_Count INT, 5th_Lane_2_Sixth_Place_Count INT, \
                5th_Lane_2_Fall_Count INT, 5th_Lane_2_Lost_by_0_Lengths_Count INT, 5th_Lane_2_Lost_by_1_Length_Count INT, 5th_Lane_2_Kept_Lead_by_0_Lengths_Count INT, \
                5th_Lane_2_Kept_Lead_by_1_Length_Count INT, 5th_Lane_2_Surged_by_0_Lengths_Count INT, 5th_Lane_2_Surged_by_1_Length_Count INT, 5th_Lane_2_Surged_by_2_Lengths_Count INT, \
                5th_Lane_3_First_Place_Count INT, 5th_Lane_3_Second_Place_Count INT, 5th_Lane_3_Third_Place_Count INT, 5th_Lane_3_Fourth_Place_Count INT, 5th_Lane_3_Fifth_Place_Count INT, 5th_Lane_3_Sixth_Place_Count INT, \
                5th_Lane_3_Fall_Count INT, 5th_Lane_3_Lost_by_0_Lengths_Count INT, 5th_Lane_3_Lost_by_1_Length_Count INT, 5th_Lane_3_Kept_Lead_by_0_Lengths_Count INT, \
                5th_Lane_3_Kept_Lead_by_1_Length_Count INT, 5th_Lane_3_Surged_by_0_Lengths_Count INT, 5th_Lane_3_Surged_by_1_Length_Count INT, 5th_Lane_3_Surged_by_2_Lengths_Count INT, \
                5th_Lane_4_First_Place_Count INT, 5th_Lane_4_Second_Place_Count INT, 5th_Lane_4_Third_Place_Count INT, 5th_Lane_4_Fourth_Place_Count INT, 5th_Lane_4_Fifth_Place_Count INT, 5th_Lane_4_Sixth_Place_Count INT, \
                5th_Lane_4_Fall_Count INT, 5th_Lane_4_Lost_by_0_Lengths_Count INT, 5th_Lane_4_Lost_by_1_Length_Count INT, 5th_Lane_4_Kept_Lead_by_0_Lengths_Count INT, \
                5th_Lane_4_Kept_Lead_by_1_Length_Count INT, 5th_Lane_4_Surged_by_0_Lengths_Count INT, 5th_Lane_4_Surged_by_1_Length_Count INT, 5th_Lane_4_Surged_by_2_Lengths_Count INT, \
                5th_Lane_5_First_Place_Count INT, 5th_Lane_5_Second_Place_Count INT, 5th_Lane_5_Third_Place_Count INT, 5th_Lane_5_Fourth_Place_Count INT, 5th_Lane_5_Fifth_Place_Count INT, 5th_Lane_5_Sixth_Place_Count INT, \
                5th_Lane_5_Fall_Count INT, 5th_Lane_5_Lost_by_0_Lengths_Count INT, 5th_Lane_5_Lost_by_1_Length_Count INT, 5th_Lane_5_Kept_Lead_by_0_Lengths_Count INT, \
                5th_Lane_5_Kept_Lead_by_1_Length_Count INT, 5th_Lane_5_Surged_by_0_Lengths_Count INT, 5th_Lane_5_Surged_by_1_Length_Count INT, 5th_Lane_5_Surged_by_2_Lengths_Count INT, \
                5th_Lane_6_First_Place_Count INT, 5th_Lane_6_Second_Place_Count INT, 5th_Lane_6_Third_Place_Count INT, 5th_Lane_6_Fourth_Place_Count INT, 5th_Lane_6_Fifth_Place_Count INT, 5th_Lane_6_Sixth_Place_Count INT, \
                5th_Lane_6_Fall_Count INT, 5th_Lane_6_Lost_by_0_Lengths_Count INT, 5th_Lane_6_Lost_by_1_Length_Count INT, 5th_Lane_6_Kept_Lead_by_0_Lengths_Count INT, \
                5th_Lane_6_Kept_Lead_by_1_Length_Count INT, 5th_Lane_6_Surged_by_0_Lengths_Count INT, 5th_Lane_6_Surged_by_1_Length_Count INT, 5th_Lane_6_Surged_by_2_Lengths_Count INT, \
                6th_Class INT, 6th_Gender INT, 6th_Age INT, 6th_Win_Rate FLOAT, 6th_Place_Rate FLOAT, \
                6th_1st_Place_Count INT, 6th_2nd_Place_Count INT, 6th_Start_Count INT, 6th_Top_Finish_Count INT, 6th_First_Place_Count INT, 6th_Average_Start_Timing FLOAT, \
                6th_Lane_1_Entry_Count INT, 6th_Lane_1_Place_Rate FLOAT, 6th_Lane_1_Average_Start_Timing FLOAT, 6th_Lane_1_Average_Start_Position FLOAT, \
                6th_Lane_2_Entry_Count INT, 6th_Lane_2_Place_Rate FLOAT, 6th_Lane_2_Average_Start_Timing FLOAT, 6th_Lane_2_Average_Start_Position FLOAT, \
                6th_Lane_3_Entry_Count INT, 6th_Lane_3_Place_Rate FLOAT, 6th_Lane_3_Average_Start_Timing FLOAT, 6th_Lane_3_Average_Start_Position FLOAT, \
                6th_Lane_4_Entry_Count INT, 6th_Lane_4_Place_Rate FLOAT, 6th_Lane_4_Average_Start_Timing FLOAT, 6th_Lane_4_Average_Start_Position FLOAT, \
                6th_Lane_5_Entry_Count INT, 6th_Lane_5_Place_Rate FLOAT, 6th_Lane_5_Average_Start_Timing FLOAT, 6th_Lane_5_Average_Start_Position FLOAT, \
                6th_Lane_6_Entry_Count INT, 6th_Lane_6_Place_Rate FLOAT, 6th_Lane_6_Average_Start_Timing FLOAT, 6th_Lane_6_Average_Start_Position FLOAT, \
                6th_Previous_Class INT, 6th_Previous_Previous_Class INT, 6th_Previous_Previous_Previous_Class INT, 6th_Previous_Class_Ability_Index FLOAT, 6th_Current_Class_Ability_Index FLOAT, \
                6th_Lane_1_First_Place_Count INT, 6th_Lane_1_Second_Place_Count INT, 6th_Lane_1_Third_Place_Count INT, 6th_Lane_1_Fourth_Place_Count INT, 6th_Lane_1_Fifth_Place_Count INT, 6th_Lane_1_Sixth_Place_Count INT, \
                6th_Lane_1_Fall_Count INT, 6th_Lane_1_Lost_by_0_Lengths_Count INT, 6th_Lane_1_Lost_by_1_Length_Count INT, 6th_Lane_1_Kept_Lead_by_0_Lengths_Count INT, \
                6th_Lane_1_Kept_Lead_by_1_Length_Count INT, 6th_Lane_1_Surged_by_0_Lengths_Count INT, 6th_Lane_1_Surged_by_1_Length_Count INT, 6th_Lane_1_Surged_by_2_Lengths_Count INT, \
                6th_Lane_2_First_Place_Count INT, 6th_Lane_2_Second_Place_Count INT, 6th_Lane_2_Third_Place_Count INT, 6th_Lane_2_Fourth_Place_Count INT, 6th_Lane_2_Fifth_Place_Count INT, 6th_Lane_2_Sixth_Place_Count INT, \
                6th_Lane_2_Fall_Count INT, 6th_Lane_2_Lost_by_0_Lengths_Count INT, 6th_Lane_2_Lost_by_1_Length_Count INT, 6th_Lane_2_Kept_Lead_by_0_Lengths_Count INT, \
                6th_Lane_2_Kept_Lead_by_1_Length_Count INT, 6th_Lane_2_Surged_by_0_Lengths_Count INT, 6th_Lane_2_Surged_by_1_Length_Count INT, 6th_Lane_2_Surged_by_2_Lengths_Count INT, \
                6th_Lane_3_First_Place_Count INT, 6th_Lane_3_Second_Place_Count INT, 6th_Lane_3_Third_Place_Count INT, 6th_Lane_3_Fourth_Place_Count INT, 6th_Lane_3_Fifth_Place_Count INT, 6th_Lane_3_Sixth_Place_Count INT, \
                6th_Lane_3_Fall_Count INT, 6th_Lane_3_Lost_by_0_Lengths_Count INT, 6th_Lane_3_Lost_by_1_Length_Count INT, 6th_Lane_3_Kept_Lead_by_0_Lengths_Count INT, \
                6th_Lane_3_Kept_Lead_by_1_Length_Count INT, 6th_Lane_3_Surged_by_0_Lengths_Count INT, 6th_Lane_3_Surged_by_1_Length_Count INT, 6th_Lane_3_Surged_by_2_Lengths_Count INT, \
                6th_Lane_4_First_Place_Count INT, 6th_Lane_4_Second_Place_Count INT, 6th_Lane_4_Third_Place_Count INT, 6th_Lane_4_Fourth_Place_Count INT, 6th_Lane_4_Fifth_Place_Count INT, 6th_Lane_4_Sixth_Place_Count INT, \
                6th_Lane_4_Fall_Count INT, 6th_Lane_4_Lost_by_0_Lengths_Count INT, 6th_Lane_4_Lost_by_1_Length_Count INT, 6th_Lane_4_Kept_Lead_by_0_Lengths_Count INT, \
                6th_Lane_4_Kept_Lead_by_1_Length_Count INT, 6th_Lane_4_Surged_by_0_Lengths_Count INT, 6th_Lane_4_Surged_by_1_Length_Count INT, 6th_Lane_4_Surged_by_2_Lengths_Count INT, \
                6th_Lane_5_First_Place_Count INT, 6th_Lane_5_Second_Place_Count INT, 6th_Lane_5_Third_Place_Count INT, 6th_Lane_5_Fourth_Place_Count INT, 6th_Lane_5_Fifth_Place_Count INT, 6th_Lane_5_Sixth_Place_Count INT, \
                6th_Lane_5_Fall_Count INT, 6th_Lane_5_Lost_by_0_Lengths_Count INT, 6th_Lane_5_Lost_by_1_Length_Count INT, 6th_Lane_5_Kept_Lead_by_0_Lengths_Count INT, \
                6th_Lane_5_Kept_Lead_by_1_Length_Count INT, 6th_Lane_5_Surged_by_0_Lengths_Count INT, 6th_Lane_5_Surged_by_1_Length_Count INT, 6th_Lane_5_Surged_by_2_Lengths_Count INT, \
                6th_Lane_6_First_Place_Count INT, 6th_Lane_6_Second_Place_Count INT, 6th_Lane_6_Third_Place_Count INT, 6th_Lane_6_Fourth_Place_Count INT, 6th_Lane_6_Fifth_Place_Count INT, 6th_Lane_6_Sixth_Place_Count INT, \
                6th_Lane_6_Fall_Count INT, 6th_Lane_6_Lost_by_0_Lengths_Count INT, 6th_Lane_6_Lost_by_1_Length_Count INT, 6th_Lane_6_Kept_Lead_by_0_Lengths_Count INT, \
                6th_Lane_6_Kept_Lead_by_1_Length_Count INT, 6th_Lane_6_Surged_by_0_Lengths_Count INT, 6th_Lane_6_Surged_by_1_Length_Count INT, 6th_Lane_6_Surged_by_2_Lengths_Count INT)")

ii = 1
for filename in os.listdir(race_folder):
    if filename.endswith('.TXT'):
        print(filename + " 処理中")
        time = int(filename[3:5])
        if time > 7: 
            new_year = '20' + filename[1:3]
            new_month = '04'
        else:
            new_year = '20' + str(int(filename[1:3]) -1 )
            new_month = '10'
        date_value = f"{new_year}-{new_month}"
        # print(date_value)
        # Read the text document into a string variable
        with open(os.path.join(race_folder, filename), 'rb') as file:
            result = chardet.detect(file.read())
        # Read the file with the detected encoding
        with open(os.path.join(race_folder, filename), 'r', encoding=result['encoding'], errors='ignore') as file:
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
                    try:
                        if int(payout) >= 12000:
                            judge = 1
                        else: judge = 0
                    except ValueError:
                        # Handle the case where payout is not a valid integer
                        print("Payout is not a valid integer")
                        judge = None
                    val = (ii, date[index-1].replace('/ ', '-'),location_change(location[index-1]), race_num, payout, weather_change(weather), direction_change(wind_direction), wind_speed, wave_height, judge)
                    for num in place_horse_number:
                        cursor.execute(f"SELECT * FROM player_info WHERE date = '{date_value}' AND Race_Number = {int(num)}")
                        record = cursor.fetchone()
                        if record is not None:
                            selected_column = record[3:]
                        else:
                            selected_column = tuple([None for _ in range(124)])
                        val = val + selected_column
                    new_val = "(" + ",".join([f"\'{x}\'" for x in val]) + ")"
                    cursor.execute('INSERT INTO analysis_data VALUES' + new_val)
                    ii += 1
                    db.commit()
print("[analysis_data]テーブルが作成しました。")
db.close()
            