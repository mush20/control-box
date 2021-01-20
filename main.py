import time
import control
import sensor

## DEFAULT SETTINGS ###
TEMPERATURE = 25
HUMIDITY = 0.8
HOURS_LIGHT = 12
MINUTES_BEFORE_CHECK = 1

while True:
    temperature = sensor.get_temperature()
    humidity = sensor.get_humidity()
    print("current temperature % (C)", str(temperature))
    print("current humidity %", str(humidity))
    
    # TEMPERATURE CHECK
    if temperature < TEMPERATURE:
        control.heat()
    elif temperature > TEMPERATURE:
        control.cool()

    # HUMIDITY CHECK
    if humidity < HUMIDITY:
        control.humidify()

    time.sleep(60*MINUTES_BEFORE_CHECK)