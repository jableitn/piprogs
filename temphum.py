import board
import adafruit_si7021
sensor = adafruit_si7021.SI7021(board.I2C())

print(sensor.temperature*1.8+32.0)
print(sensor.relative_humidity)