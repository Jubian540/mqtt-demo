#!/usr/bin/env python3

import os
import paho.mqtt.client as mqtt_client

server = '8.210.186.207'
port = 1883
user_id = 'res_client'
temp_topic = 'resp/temp'
co_topic = 'resp/co'
hi_top = 'resp/hi'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(rc))

def on_message(client, userdata, msg):
    print(msg.payload)

client = mqtt_client.Client(user_id)

def main():
    client.connect(server, port, 60)
    client.subscribe(temp_topic)
    client.subscribe(co_topic)
    client.subscribe(hi_top)
    client.on_message = on_message
    client.loop_forever()

if __name__ == '__main__':
    main()
