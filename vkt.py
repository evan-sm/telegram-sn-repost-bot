#!/usr/bin/env python3
# -*- coding: utf-8 -*-s
import json, html, re
import requests
import vk
from models import *
from cfg import *
from tkn import *
from ss import vkSS
from tele import teleSendURL, teleReportError, teleSendMediaGroup, teleForwardMSG, teleSendPhotoMem


def cvtHtmlToText(txt):
	#txt = html.unescape(txt)
	txt = re.sub('<br\s*?>', '\n', txt)
	#print (txt)
	return txt
def updVK(who):
	key = str(who) + '_post'
	# Initialize VK API
	session = vk.Session(access_token=TKN_VK_WMW)
	api = vk.API(session)
	# Get last wall post
	wall_post_obj = api.wall.get(owner_id=who, count=2, filter='owner', version=4.104, extended=1)
	#print (wall_post_obj)
	#print(str(key)+' checking VK')
	if wall_post_obj['wall'][1]['date'] < wall_post_obj['wall'][2]['date']:
		i = 2
	else:
		i = 1
	if 'post' in wall_post_obj['wall'][i]['post_type']:
		date = wall_post_obj['wall'][i]['date']
		desc = wall_post_obj['wall'][i]['text']
		link = 'https://vk.com/wall%s_%s' % (who, wall_post_obj['wall'][i]['id']) # example: https://vk.com/wall153162173_416168
		q = VK.select().where(VK.who == key)
		if q.exists():
			for s in q:
				#print (link) 
				#print (date)
				#s.date = 0
				if s.date < date:
					print('New VK ' + str(who) + ' post found, updating')
					img = vkSS(link)
					desc = desc[:194]
					desc = desc + '\n\n<a href="' + link + '">🔗 VK</a>'
					r = teleSendPhotoMem(who, img, cvtHtmlToText(desc), 'HTML')
					#r = teleSendPhotoMem(who, img, desc)
					r_obj = json.loads(r.text)
					if r.status_code == 200:
						q = VK.update(date=date, url=link).where(VK.who == key)
						q.execute()
					else:
						print('Cannot send telegram message, something went wrong!\n %s' & (r.text))
						teleReportError(r.text)
				#else:
					#print('Nah, it is old vk wall post')
		else:
			print(str(who) + ' vk wall post row does not exists, creating...')
			q = VK.create(who=key, date=date, url=link)
			#print (date)
			#print (link)
	#print('VK Group Olyasha Done checking\n')
