from sense_hat import SenseHat
from time import sleep
from math import floor

sense = SenseHat()

sense.set_rotation(180)

try:
    while True:
        temp = round(sense.get_temperature(), 1) # Temperature in celsius
        hum = floor(sense.get_humidity())       
    
        sense.show_message(f'Temperature: {temp} C')
        sleep(1)
        sense.show_message(f'Humidity: {hum}%')

        sleep(300)
except KeyboardInterrupt:
    sense.show_message('Goodbye!')
    exit()


