#!/usr/bin/python

import subprocess
import os
import sys

proc = subprocess.Popen(["sudo", "pkill", "-f", "limit7.py"], stdout=subprocess.PIPE)
proc = subprocess.Popen(["ping", "-c", "4", "-s", "2560", "192.168.100.70"], stdout=subprocess.PIPE)
proc.wait()
sys.exit()