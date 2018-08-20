#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 00:43:17 2018

@author: dustinscarter
"""
import os
import schedule
import time

def job(t):
    os.system('sh daily.txt')
    return

schedule.every().day.at("02:32").do(job,'It is 01:15')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute