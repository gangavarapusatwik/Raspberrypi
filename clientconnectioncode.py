import json
import socket
import sqlite3
import sys
#import serial as serial
import time
#import serial as serial
import re, uuid
import asyncio
import websockets

#mac=.join(re.findall('..', '%012x' % uuid.getnode()))
  
# joins elements of getnode() after each 2 digits. 
# using regex expression 
#print ("The MAC address in formatted and less complex way is : ", end="")
import time
from datetime import date
from datetime import datetime
my_date = date.today()
timestamp=time.mktime(my_date.timetuple())
mac=(':'.join(re.findall('..', '%012x' % uuid.getnode()))) 
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)
print(mac)
print(timestamp)

#ser = serial.Serial('/dev/ttyACM0',9600)
#ser.flushInput()
#ser = serial.Serial('/dev/ttyACM0',9600)
#ser.flushInput()
#data=ser.readline()
#my_json = data.decode('utf8').replace('"', '"')
#if "{" in my_json:
#     final_dictionary = eval(my_json)
#    json_str =json.dumps(final_dictionary)
#else:
#     ser=serial.Serial('/dev/ttyACM0',9600)
#     ser.flushInput()
#     data=ser.readline()
#     my_json=data.decode('utf8').replace('"','"')
#     final_dictionary = eval(data)
#     json_str =json.dumps(final_dictionary)
#     resp = json.loads(json_str)
#     temp=resp["TEMPERATURE"]
#     hum=resp["HUMIDITY"]
#     alchol_mq3=resp["ALCHOL_MQ3"]
#     smoke_mq2=resp["SMOKE_MQ2"]
#     methane_mq4=resp["METHANE_MQ4"]
#     lpg_mq9=resp["LPG_MQ9"]
#     mq135_aq=resp["MQ135_AQ"]
#     co_mq7=resp["CO_MQ7"]
    
    #print(temp)
    #print(resp)
    #print(data)
temp=60
hum=80
alchol_mq3=1.22
smoke_mq2=1.22
methane_mq4=1.22
lpg_mq9=1.22
mq135_aq=1.22
co_mq7=1.22


jdata = {}
jdata['IP_ADDRESS'] = IPAddr
jdata['MAC_ADDRESS'] = mac
jdata['DEVICE_NO'] = 1
jdata['READING_NO'] = 1
jdata['PASSWORD'] = 'OptimizedSolDemo'
jdata['TEMPERATURE'] = temp
jdata['TIMESTAMP'] = timestamp
jdata['HUMIDITY'] = hum
jdata['METHANE_MQ4'] = timestamp
jdata['ALCHOL_MQ3'] = alchol_mq3
jdata['MQ135_AQ'] = mq135_aq
jdata['SMOKE_MQ2'] = smoke_mq2
jdata['CO_MQ7'] = co_mq7
jdata['LPG_MQ9'] = lpg_mq9
jdata['LONGITUDE'] = 78.442641
jdata['LATITUDE'] = 17.410532

json_data = json.dumps(jdata)
print(json_data)    
time.sleep(1)
@asyncio.coroutine
def hello():
    websocket = yield from websockets.connect(
        'ws://96.233.68.54:8090')

    try:
       
        yield from websocket.send(json_data)
        
        greeting = yield from websocket.recv()
        print("< {}".format(greeting))
        

    finally:
        yield from websocket.close()

asyncio.get_event_loop().run_until_complete(hello())
