#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, io, json
from tkn import *
from cfg import *

def teleReportError(msg):
	chan = TELE_IWB_ID
	TKN = TKN_TELE_IWB
	URL_TELE_API = 'https://api.telegram.org/bot%s/' % TKN # Telegram API URL
	data = {'chat_id': chan, 'text': '`'+msg+'`', 'parse_mode': 'Markdown'}
	r = requests.post(URL_TELE_API + 'sendMessage', data=data)
	return r

def teleForwardMSG(who, from_chat_id, message_id):
	forward = False
	if who == INST3_NM: #  'artembaccardi'
		chan = TELE_TEST_ID # Chat test bot
		TKN = TKN_TELE_IWB # 
		forward = True
	elif who == INST2_NM:
		print('sharisha')
		chan = TELE_FAG_ID # fag refuge
		TKN = TKN_TELE_SRS # sharishanyaBot
		forward = True
	elif who == INST1_NM:
		chan = TELE_IWB_ID
		TKN = TKN_TELE_OLYA
		forward = True
	if forward == True:
		URL_TELE_API = 'https://api.telegram.org/bot%s/' % TKN # Telegram API URL9
		data = {'chat_id': chan, 'from_chat_id': from_chat_id, 'disable_notification': False, 'message_id': message_id}
		r = requests.post(URL_TELE_API + 'forwardMessage', data=data)
		r = json.loads(r.text)
		print (r)
	return

def teleSendPhotoMem(who, img, desc, parse):
	if who == INST3_NM:
		chan = TELE_IWB_ID 
		TKN = TKN_TELE_IWB
	elif who == VK_GROUP_OLYA or VK_ID_OLYA:
		chan = TELE_OLYA_ID 
		TKN = TKN_TELE_OLYA
	elif who == VK_ID_SHARISHA:
		chan = TELE_SRS_ID 
		TKN = TKN_TELE_SRS
	else:
		chan = TELE_IWB_ID 
		TKN = TKN_TELE_IWB
	URL_TELE_API = 'https://api.telegram.org/bot%s/' % TKN # Telegram API URL
	#remote_file = requests.get(url)
	#file = img.seek(0)
	data = {'chat_id' : chan, 'caption': desc, 'parse_mode': parse}
	files = {'photo': img}
	r = requests.post(URL_TELE_API + 'sendPhoto', files=files, data=data)	
	print (r.text)	
	return r

def teleSendURL(url, who, desc, code, isvid):
	if who == INST3_NM:
		chan = TELE_IWB_ID 
		TKN = TKN_TELE_IWB
	elif who == INST1_NM:
		chan = TELE_OLYA_ID 
		TKN = TKN_TELE_OLYA
	elif who == INST2_NM:
		chan = TELE_SRS_ID 
		TKN = TKN_TELE_SRS
	else:
		chan = TELE_IWB_ID 
		TKN = TKN_TELE_IWB
	URL_TELE_API = 'https://api.telegram.org/bot%s/' % TKN # Telegram API URL
	remote_file = requests.get(url)
	file = io.BytesIO(remote_file.content)
	data = {'chat_id' : chan, 'caption': desc, 'parse_mode': 'HTML'}
	if isvid == False:
		files = {'photo': file}
		r = requests.post(URL_TELE_API + 'sendPhoto', files=files, data=data)
	else:
		files = {'video': file}
		r = requests.post(URL_TELE_API + 'sendVideo', files=files, data=data)	
	#print (r.text)	
	return r

def teleSendMediaGroup(who, media):
	if who == INST3_NM:
		chan = TELE_IWB_ID 
		TKN = TKN_TELE_IWB
	elif who == INST1_NM:
		chan = TELE_OLYA_ID 
		TKN = TKN_TELE_OLYA
	elif who == INST2_NM:
		chan = TELE_SRS_ID 
		TKN = TKN_TELE_SRS
	else:
		chan = TELE_IWB_ID 
		TKN = TKN_TELE_IWB
	media = json.dumps(media)
	URL_TELE_API = 'https://api.telegram.org/bot%s/' % TKN # Telegram API URL
	data = {'chat_id' : chan, 'media': media}
	r = requests.post(URL_TELE_API + 'sendMediaGroup', data=data)
	#print (r.text)
	return r