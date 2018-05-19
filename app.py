#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from models import *
from inst import updInstPostDB, getInstPostJSON, updInstStoryDB, getInstStoryJSON, getGeolocation
from tele import teleSendMediaGroup

# Olyasha and Sharisha
updInstPostDB(INST2_NM)
sleep(5)
updInstStoryDB(INST2_NM, INST2_ID)
sleep(5)
updInstPostDB(INST1_NM)
sleep(5)
updInstStoryDB(INST1_NM, INST1_ID)
sleep(5)

# Olyasha friends
updInstPostDB(INST8_NM)
sleep(5)
updInstStoryDB(INST8_NM, INST8_ID)
sleep(5)
updInstPostDB(INST9_NM)
sleep(5)
updInstStoryDB(INST9_NM, INST9_ID)

# Friends
updInstPostDB(INST7_NM)
sleep(5)
updInstStoryDB(INST7_NM, INST7_ID)
sleep(5)
updInstPostDB(INST10_NM)
sleep(5)
updInstStoryDB(INST10_NM, INST10_ID)
