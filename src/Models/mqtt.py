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
                 ADAFRUIT_IO_URL = b'io.adafruit.com',
                 ADAFRUIT_USERNAME = b'Dreambot',
                 ADAFRUIT_IO_KEY = b'aio_NHOL62OFWkfrvNC1Li5AvL8rUO0L',
                 mqtt_client_id = bytes('client_'+str(int.from_bytes(os.urandom(3), 'little')), 'utf-8'),
                 WIFI_SSID = 'Bendix',
                 WIFI_PASSWORD = 'DetVirkerIkke',
                 MAX_ATTEMPTS=20,
                 attempt_count = 0
                 ):

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
                          b'RPM',
                          b'Fan',
                          b'P',
                          b'I',
                          b'D',
                          b'',
                          ]

        for feedname in self.feednames:
            txt = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, feedname), 'utf-8')
            self.client.subscribe(txt)
            self.client.publish(bytes('{:s}/get'.format(txt), 'utf-8'), '\0')

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
        except:
            print("missing key in " + topic)
