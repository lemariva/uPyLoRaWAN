import sys
import os
import time
import machine
import ubinascii

def mac2eui(mac):
    mac = mac[0:6] + 'fffe' + mac[6:]
    return hex(int(mac[0:2], 16) ^ 2)[2:] + mac[2:]

def get_millis():
    millisecond = time.ticks_ms()
    return millisecond

def get_nodename():
    uuid = ubinascii.hexlify(machine.unique_id()).decode()
    node_name = "ESP_" + uuid
    return node_name
