#!/usr/bin/python

import sys
import time
import random
import signal
import subprocess
import datetime
import telepot
import os
#import RPi.GPIO as GPIO

#GPIO.setwarnings(False)
# to use Raspberry Pi board pin numbers
#GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
#GPIO.setup(40, GPIO.OUT)

#def run_command(commandt):
#    p = subprocess.Popen(commandt,
#                        stdout=subprocess.PIPE,
#                        stderr=subprocess.STDOUT)
#    return iter(p.stdout.readline, b'')

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command

    # if command == 'On':
    #    bot.sendMessage(chat_id, text="Lampu dinyalain")
    #    GPIO.output(40,GPIO.HIGH)
    #    return;
    # elif command == 'Off':
    #    bot.sendMessage(chat_id, text="Lampu dimatiin")
    #    GPIO.output(40,GPIO.LOW)
    #    return;
    if command == 'Limit3':
        bot.sendMessage(chat_id, text="Limited 3Mbps")
        os.system("python /home/pi/limit3.py &")
        raise SystemExit
    elif command == 'Limit7':
        bot.sendMessage(chat_id, text="Limited 7Mbps")
        os.system("python /home/pi/limit7.py &")
        raise SystemExit
    elif command == 'Nolimit3':
        bot.sendMessage(chat_id, text="Limit3 Off")
        os.system("python /home/pi/nolimit3.py &")
        raise SystemExit
    elif command == 'Nolimit7':
        bot.sendMessage(chat_id, text="Limit7 Off")
        os.system("python /home/pi/nolimit7.py &")
        raise SystemExit
    elif command == 'Status':
        vlanlimit7ip = os.system("ping -c 1 192.168.100.7")
        vlanlimit3ip = os.system("ping -c 1 192.168.100.3")
        if (vlanlimit7ip == 0 and vlanlimit3ip == 0):
            bot.sendMessage(chat_id, text="Mblandang!")
        elif (vlanlimit7ip >= 0 and vlanlimit3ip == 0):
            bot.sendMessage(chat_id, text="Limiter 7 ON!")
        elif (vlanlimit7ip == 0 and vlanlimit3ip >= 0):
            bot.sendMessage(chat_id, text="Limiter 3 ON!")
    else:
        pass
            
bot = telepot.Bot('000000000:AAA_AA-AAAAAAAAAAAAAAAAAAAAAAAAAAAA')
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(10)
