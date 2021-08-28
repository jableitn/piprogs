from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import board
import adafruit_si7021
import time

sensor = adafruit_si7021.SI7021(board.I2C())
lcd = LCD()

print("Temp F = ", (sensor.temperature*1.8 + 32.))
print("%RH = ", (sensor.relative_humidity))
dewpt = (sensor.temperature - ((100 - sensor.relative_humidity)/5.))*1.8+32
print("Dewpoint F = ", dewpt)

try:
    while True:
        prh = sensor.relative_humidity
        dewpt = (sensor.temperature - ((100 - prh)/5.))*1.8+32
        tempf = (sensor.temperature*1.8+32.0)
        strtop = "T=" + str(tempf)[0:5] + "F"
        strbot = "H=" + str(prh)[0:4] + "%, " + str(dewpt)[0:5] + "F" 
        lcd.text(strtop, 1)
        lcd.text(strbot, 2)
        time.sleep(1)
except KeyboardInterrupt:
    pass

# def safe_exit(signum, frame):
#     exit(1)
# try:
#     signal(SIGTERM, safe_exit)
#     signal(SIGHUP, safe_exit)
#     lcd.text("Hello,", 1)
#     lcd.text("Raspberry Pi!", 2)
#     pause()
# except KeyboardInterrupt:
#     pass
# finally:
#     lcd.clear()