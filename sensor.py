from sense_hat import SenseHat

sense = SenseHat()

while True:
    temp = sense.get_temperature() # Temperature in celsius
    pres = sense.get_pressure() # Air pressure in millibars

