from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import time
lcd = LCD()

str1 = " this is only a test..."

try:
    while True:
        lcd.text("Raspberry Pi!", 2)
        for j in range (0,22):
            str2 = str1[j:21]+str1[0:j]
            lcd.text(str2[0:15], 1)
            time.sleep(0.2)
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