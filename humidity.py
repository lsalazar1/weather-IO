from sense-hat import SenseHat
from math import floor

def get_average_humidity(x):
    '''
    Calculates the average of all the humidity
    data from a list

    @params x: list
    @return average humidity
    '''
    return sum(x) / len(x)

try:
    sense = SenseHat()
    data = []

    while True:
        hum = floor(sense.get_humidity())
        
        data.push(hum)
        sense.show_message(f'Humidity: {hum}')
        sleep(60)
except KeyboarInterrupt:
    avg = get_average_humidity(data)
    sense.show_message(f'Average humidity: {avg}')
    exit()
