# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 10:11:40 2022

@author: jason
"""

import schedule
import datetime
import time

outfile = "watering.csv"
fout = open(outfile, "w")
fout.write("Time,next water [hrs],pump status\n")
fout.close()
schedule.clear()

def job():
    fout = open(outfile, "a")
    lctr=1
    print("I'm working...")
    now=datetime.datetime.now()
    strnow = (str(now) + "," + str(lctr) + "\n")
    fout.write(strnow)
    fout.close()

schedule.every(17).seconds.do(job)
# schedule.every().hour.do(job)
schedule.every().day.at("12:03").do(job)
schedule.every().day.at("10:47").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

try:
    while True:
        print("in")
        schedule.run_pending()
        print("out")
        time.sleep(1)
except KeyboardInterrupt:
    print('interrupted!')   
    
#     try:
#     while True:
#         IDs2=UpdatePoints(value,IDs2)
#         time.sleep(10)
# except KeyboardInterrupt:
#     print('interrupted!')