# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 10:11:40 2022
@author: jason
"""
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import board
import adafruit_si7021
import RPi.GPIO as GPIO
import schedule
import datetime
import time

outfile = "watering.csv"
pumpstate = 0
time.sleep(1)
sensor = adafruit_si7021.SI7021(board.I2C())
lcd = LCD()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.output(18, True)
GPIO.output(23, False)
time.sleep(1)
GPIO.output(18, False)
GPIO.output(23, True)
time.sleep(1)
GPIO.output(18, False)
GPIO.output(23, False)
# GPIO.setup(25, GPIO.IN)
# fout = open(outfile, "w")
# fout.write("Time,temp,%RH,dewpt,pump\n")
# fout.close()
schedule.clear()

def dispRH():
    prh = sensor.relative_humidity
    print("dispRH")
    dewpt = (sensor.temperature - ((100 - prh)/5.))*1.8+32
    tempf = (sensor.temperature*1.8+32.0)
    strtop = "T=" + str(tempf)[0:5] + "F"
    strbot = "H=" + str(prh)[0:4] + "%, " + str(dewpt)[0:5] + "F" 
    lcd.text(strtop, 1)
    lcd.text(strbot, 2)
    
def senstring():
    prh = sensor.relative_humidity
    print("senstring")
    dewpt = (sensor.temperature - ((100 - prh)/5.))*1.8+32
    tempf = (sensor.temperature*1.8+32.0)
    print(str(tempf)[0:5])
    print(str(prh)[0:4])
    print(str(dewpt)[0:5] + ",")
    funstring = str(tempf)[0:5] + "," + str(prh)[0:4] + "," + str(dewpt)[0:5]
    print(funstring)
    return str(funstring)

def job():
    fout = open(outfile, "a")
    print("Pump OFF")
    now=datetime.datetime.now()
    str3 = senstring()
    strnow = (str(now) + "," + str3 + ",0\n")
    fout.write(strnow)
    fout.close()
    
def pumpjob(pumpstate):
    fout = open(outfile, "a")
    print("Pump state is " + str(pumpstate))
    now=datetime.datetime.now()
    str3 = senstring()
    strnow = (str(now) + "," + str3 + "," + str(pumpstate) +"\n")
    fout.write(strnow)
    fout.close()

def runpump():
    job()
    GPIO.output(18, True)
    pumpjob(2)
    print("pumping in water")
    time.sleep(14)
    GPIO.output(18, False)
    GPIO.output(23, True)
    pumpjob(-2)
    print("pumping out water")
    time.sleep(22)
    GPIO.output(18, False)
    GPIO.output(23, False)
    job()
    
schedule.every(17).seconds.do(job)
schedule.every(5).seconds.do(dispRH)
schedule.every(60).seconds.do(runpump)

try:
    while True:
        print("in")
        schedule.run_pending()
        print("out")
        time.sleep(1)
except KeyboardInterrupt:
    print('interrupted!')   
    
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("12:03").do(job)