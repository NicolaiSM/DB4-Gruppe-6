# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:44:24 2020

@author: William
"""

import network
import time
from umqtt.robust import MQTTClient
import os
import sys


class Mqtt:
    def __init__(self,
                 mqttapi,
                 ADAFRUIT_IO_URL=b'io.adafruit.com',
                 ADAFRUIT_USERNAME=b'Dreambot',
                 ADAFRUIT_IO_KEY=b'aio_OXzV507xu9Od0J7uMXSEXm0OxCNU',
                 mqtt_client_id=bytes('client_' + str(int.from_bytes(os.urandom(3), 'little')), 'utf-8'),
                 WIFI_SSID='Bendix',
                 WIFI_PASSWORD='DetVirkerIkke',
                 MAX_ATTEMPTS=20,
                 attempt_count=0
                 ):

        self.ADAFRUIT_USERNAME = ADAFRUIT_USERNAME

        self.mqttapi = mqttapi

        self.client = MQTTClient(client_id=mqtt_client_id,
                                 server=ADAFRUIT_IO_URL,
                                 user=ADAFRUIT_USERNAME,
                                 password=ADAFRUIT_IO_KEY,
                                 ssl=False)

        # turn off the WiFi Access Point
        self.ap_if = network.WLAN(network.AP_IF)
        self.ap_if.active(False)

        # connect the device to the WiFi network
        self.wifi = network.WLAN(network.STA_IF)
        self.wifi.active(True)
        self.wifi.connect(WIFI_SSID, WIFI_PASSWORD)

        # wait until the device is connected to the WiFi network
        while not self.wifi.isconnected() and attempt_count < MAX_ATTEMPTS:
            attempt_count += 1
            time.sleep(1)
            print(attempt_count)

        if attempt_count == MAX_ATTEMPTS:
            print('could not connect to the WiFi network')
            sys.exit()

        try:
            self.client.connect()
        except Exception as e:
            print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
            sys.exit()

        self.client.set_callback(self.cb)

        self.feednames = [b'Peltier Element',
                          b'Fan',
                          b'P',
                          b'I',
                          b'D',
                          ]

        for feedname in self.feednames:
            txt = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, feedname), 'utf-8')
            self.client.subscribe(txt)

    def __call__(self):
        try:
            self.client.wait_msg()
        except KeyboardInterrupt:
            print('Ctrl-C pressed...exiting')
            self.client.disconnect()
            sys.exit()

    def cb(self, topic, msg):
        try:
            self.mqttapi[topic](str(msg, 'utf-8'))
        except Exception as e:
            print(e)
            print("missing key in " + str(topic, 'utf-8'))
        finally:
            print(topic)
            print(msg)

    def publish(self, topic, value):
        try:
            mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(self.ADAFRUIT_USERNAME, topic), 'utf-8')
            self.client.publish(mqtt_feedname, bytes(str(value), 'utf-8'), qos=0)
        except KeyboardInterrupt:
            print('Ctrl-C pressed...exiting')
            self.client.disconnect()
            sys.exit()
        finally:
            return value
