#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, io, json
from tkn import *
from cfg import *

def teleSendURL(url, who, desc, code, isvid):
	if who == INST3_NM:
		chan = TELE_IWB_ID # t.me/InstagramWmwBot
		TKN = TKN_TELE_IWB
	elif who == INST1_NM:
		chan = TELE_OLYA_ID # t.me/OlyashaChan
		TKN = TKN_TELE_OLYA
	elif who == INST2_NM:
		chan = TELE_SRS_ID # t.me/SharishaChan
		TKN = TKN_TELE_SRS
	else:
		chan = TELE_IWB_ID # t.me/InstagramWmwBot
		TKN = TKN_TELE_IWB
	URL_TELE_API = 'https://api.telegram.org/bot%s/' % TKN # Telegram API URL
	remote_file = requests.get(url)
	file = io.BytesIO(remote_file.content)
	data = {'chat_id' : chan, 'caption': desc, 'parse_mode': 'Markdown'}
	if isvid == False:
		files = {'photo': file}
		r = requests.post(URL_TELE_API + 'sendPhoto', files=files, data=data)
	else:
		files = {'video': file}
		r = requests.post(URL_TELE_API + 'sendVideo', files=files, data=data)	
	return r

def teleReportError(msg):
	chan = TELE_IWB_ID
	TKN = TKN_TELE_IWB
	URL_TELE_API = 'https://api.telegram.org/bot%s/' % TKN # Telegram API URL
	data = {'chat_id': chan, 'text': '`'+msg+'`', 'parse_mode': 'Markdown'}
	r = requests.post(URL_TELE_API + 'sendMessage', data=data)
	return r

def teleSendMediaGroup(who, media):
	if who == INST3_NM:
		chan = TELE_IWB_ID # t.me/InstagramWmwBot
		TKN = TKN_TELE_IWB
	elif who == INST1_NM:
		chan = TELE_OLYA_ID # t.me/OlyashaChan
		TKN = TKN_TELE_OLYA
	elif who == INST2_NM:
		chan = TELE_SRS_ID # t.me/SharishaChan
		TKN = TKN_TELE_SRS
	else:
		chan = TELE_IWB_ID # t.me/InstagramWmwBot
		TKN = TKN_TELE_IWB
	media = json.dumps(media)
	URL_TELE_API = 'https://api.telegram.org/bot%s/' % TKN # Telegram API URL
	data = {'chat_id' : chan, 'media': media}
	#args['data']['media'] = JSONEncoder().encode(media)
	#url = "https://api.telegram.org/bot"+bot_token + "/" + method
	r = requests.post(URL_TELE_API + 'sendMediaGroup', data=data)
	#r = requests.post(url, **args)
	return r