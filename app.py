#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import pdb
from time import sleep
from models import *
from inst import updInstPostDB, getInstPostJSON, updInstStoryDB, getInstStoryJSON, getGeolocation
from tele import teleSendMediaGroup
from vkt import updVK

#updVK(VK_GROUP_TEST)

# updInstStoryDB(INST3_NM, INST3_ID)
# updInstPostDB(INST3_NM)

#Olyasha and Sharisha
#pdb.set_trace()
#print('hello world')
updInstPostDB(INST2_NM)
sleep(2)
updInstStoryDB(INST2_NM, INST2_ID)
sleep(2)
updInstPostDB(INST1_NM)
sleep(2)
updInstStoryDB(INST1_NM, INST1_ID)
sleep(2)

# Olyasha friends
updInstPostDB(INST8_NM)
sleep(2)
updInstStoryDB(INST8_NM, INST8_ID)
sleep(2)
updInstPostDB(INST9_NM)
sleep(2)
updInstStoryDB(INST9_NM, INST9_ID)
sleep(2)
updInstPostDB(INST5_NM)
sleep(2)
updInstStoryDB(INST5_NM, INST5_ID)
sleep(2)
updInstPostDB(INST11_NM)
sleep(3)
updInstStoryDB(INST11_NM, INST11_ID)
# Friends
updInstPostDB(INST7_NM)
sleep(2)
updInstStoryDB(INST7_NM, INST7_ID)
sleep(2)
updInstPostDB(INST10_NM)
sleep(2)
updInstStoryDB(INST10_NM, INST10_ID)

updVK(VK_GROUP_OLYA)
sleep(3)
updVK(VK_ID_OLYA)
sleep(3)
updVK(VK_ID_SHARISHA)