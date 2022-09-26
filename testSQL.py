#!/usr/bin/env python

import os
import time
import datetime
import glob
import MySQLdb
from time import strftime
#from Adafruit_BME280 import *

#sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

#Variables for MySQL
db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="sensor") # replace password with your password
cur = db.cursor()

def dateTime(): #get UNIX time
        secs = float(time.time())
        secs = secs*1000
        return secs

def tempRead(): #read temperature, return float with 3 decimal places
        degrees = float('{0:.3f}'.format(sensor.read_temperature()))
        return degrees

def pressRead():#read pressure, return float with 3 decimal places
        pascals = float('{0:.3f}'.format(sensor.read_pressure()/100))
        return pascals

def humidityRead(): #read humidity, return float with 3 decimal places
        humidity = float('{0:.3f}'.format(sensor.read_humidity()))
        return humidity

secs = dateTime()
temperature = 0 #tempRead()
pressure = 0 #pressRead()
humidity = 0 #humidityRead()

sql = ("""INSERT INTO bmesensor (datetime,temperature,pressure,humidity) VALUES (%s,%s,%s,%s)""", (secs, temperature, pressure, humidity))

try:
    print ("Writing to the database...")
    cur.execute(*sql)
    db.commit()
    print ("Write complete")

except:
    db.rollback()
    print ("We have a problem")

cur.close()
db.close()

print (secs)
print (temperature)
print (pressure)
print (humidity)