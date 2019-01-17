#import the libraries that are requied for the program
#import sqlite3 by using $ sudo apt-get install sqlite3
#import Adafruit_DHT by using $ git clone https://github.com/adafruit/Adafruit_Python_DHT.git


import sqlite3
from time import gmtime, strftime
import Adafruit_DHT
import time

#Here we are connecting the database 
conn=sqlite3.connect('dht.db')   #enter the name of the database with extension .db
c = conn.cursor()

#create a table with name sensors in the database of dht
#save the type,pin which is connect with gpio and name of the sensors in the table manually
c.execute('select * from sensors') 

sensors=[]
for row in c:
    name,dht_type,pin=row
    print ('Found sensor:{0} of type:{1} on pin:{2}'.format(name,dht_type,pin))
    if dht_type=='DHT22':    #checking wheather the type of sensor is present in database or not
        dht_type=Adafruit_DHT.AM2302
    elif dht_type=='DHT11':  #checking wheather the type of sensor is present in database or not
        dht_type=Adafruit_DHT.AM2302
    else:
        raise RuntimeError('Unknow sensor type:{0}'.format(dht_type))
    sensors.append((name,dht_type,pin))

while True:
    for s in sensors:
        name,dht_type,pin=s
        reading_time=strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        humidity,temperature=Adafruit_DHT.read_retry(dht_type,pin)
        print('sensor:{0} humidity={1:0.1f}% temperature = {2:0.1f}*C'.format(name, humidity,temperature) ,reading_time)

        #create a table with name readings and the values must be four in dht database
        c.execute('insert into readings values(?, ?, ?, ?)',
                  (reading_time,'{0} sensor'.format(name),temperature,humidity))
        conn.commit()
    time.sleep(2)
