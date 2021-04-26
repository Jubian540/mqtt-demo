#!/usr/bin/env python3

import os
import paho.mqtt.client as mqtt_client

server = '8.210.186.207'
port = 1883
user_id = 'sensor'
topic = 'resp/temp'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(rc))

client = mqtt_client.Client(user_id)

def main():
    client.connect(server, port, 60)
    while True:
        msg = input('Publish msg: ')
        client.publish(topic, msg)
    pass

if __name__ == '__main__':
    main()
