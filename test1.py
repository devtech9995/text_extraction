import re
import chardet
import mysql.connector
import os
import json

txt_folder = './test2'

def change(line, start, end):
    if (line[start:end] == "A1"):
        return 1
    elif (line[start:end] == "A2"):
        return 2
    elif (line[start:end] == "B1"):
        return 3
    else:
        return 4

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="txt2sql"
)
cursor = db.cursor()

ii = 1
# Create table to store names and ages
cursor.execute("CREATE TABLE IF NOT EXISTS race_new (number INT AUTO_INCREMENT PRIMARY KEY, date VARCHAR(7), Race_Number INT, Class INT, Gender INT, Age INT, \
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
                Lane_6_Kept_Lead_by_1_Length_Count INT, Lane_6_Surged_by_0_Lengths_Count INT, Lane_6_Surged_by_1_Length_Count INT, Lane_6_Surged_by_2_Lengths_Count INT, INDEX Race_Number_index (Race_Number, date))")

for filename in os.listdir(txt_folder):
    if filename.endswith('.txt') and len(filename) == 11:
        print(filename)
        year = '20' + filename[3:5]
        month = filename[5:7]
        date = f"{year}-{month}"
        print(date)
        # Read the text document into a string variable
        with open(os.path.join(txt_folder, filename), 'rb') as file:
            result = chardet.detect(file.read())
        # Read the file with the detected encoding
        with open(os.path.join(txt_folder, filename), 'r', encoding=result['encoding'], errors='ignore') as file:
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
                cursor.execute('INSERT INTO race_new VALUES' + new_val)
                ii += 1
                db.commit()
db.close()
            