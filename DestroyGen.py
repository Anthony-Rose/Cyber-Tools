#!/usr/bin/env python3

import sys
import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException

#retrieving the IP, port, and registry bit of interest from the user
ip = sys.argv[1]
port = int(sys.argv[2])
registry = int(sys.argv[3])
value = True

#this loop starts the generator and stops it after max speed is achieved
while True:
    client = ModbusClient(ip, port)
    client.connect()
    client.write_register(registry, value)
    print("Cycling power...")
    print("On") if value == True else print("Off")
    time.sleep(7)
    value = not value
