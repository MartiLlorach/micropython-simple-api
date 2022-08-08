import usocket as socket
import time
import network
import esp
import gc
import json
from machine import Pin

# disable debugging
esp.osdebug(None) 

# run garbage collection
gc.collect() 

# get configuration from file
config = json.loads(open('.conf', 'r').read())

# connect to wifi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(config['ssid'], config['password'])

# wait for wifi connection
print('Connecting to network', end='')
while not station.isconnected():
    time.sleep(0.5)
    print('.', end='')
    pass
print('\nNetwork config:', station.ifconfig())

# define led pin
led = Pin(2, Pin.OUT)