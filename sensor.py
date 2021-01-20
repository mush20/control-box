import random

def get_temperature():
    return random.randrange(20, 30)

def get_humidity():
    return round(random.uniform(0,1), 1)