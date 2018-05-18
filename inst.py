#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import requests
import json
import re
from bs4 import BeautifulSoup

from models import *
from tele import teleSendURL, teleReportError, teleSendMediaGroup
from tkn import story_headers, INST_ATKN

def getGeolocation(id):
	url = 'https://api.instagram.com/v1/locations/'+ id +'?access_token=' + INST_ATKN
	r = requests.get(url)
	if r.status_code == 200:
		r_obj = json.loads(r.text)
		geo = str(r_obj['data']['latitude']) + ';' + str(r_obj['data']['longitude'])
		return geo
	else:
		teleReportError(r.text)

def getInstPageJSON(inst):
	web = urllib.request.urlopen('https://www.instagram.com/' + inst).read()
	soup = BeautifulSoup(web, 'html.parser')
	data  = soup.find_all("script")[2].string
	p = re.compile('window._sharedData = (.*?);')
	m = p.match(data)
	stocks = json.loads(m.groups()[0])
	return stocks

def getInstPostJSON(code):
	web = urllib.request.urlopen('https://www.instagram.com/p/' + code).read()
	soup = BeautifulSoup(web, 'html.parser')
	data  = soup.find_all("script")[2].string
	p = re.compile('window._sharedData = (.*?);')
	m = p.match(data)
	stocks = json.loads(m.groups()[0])
	return stocks

def getInstStoryJSON(id):
	URL_INST_STORY = 'https://i.instagram.com/api/v1/feed/user/' + str(id) + '/reel_media/'
	r = requests.get(URL_INST_STORY, headers=story_headers)
	r_obj = json.loads(r.text)
	if r.status_code == 400:
		print (r.text)
		teleReportError(r.text)
	if not r_obj['latest_reel_media']:
		print('empty, quit')
		return False
	else:
		return r_obj


def updInstPostDB(who):
	key = who + '_post'
	js = getInstPageJSON(who)
	inst_post_time = js['entry_data']['ProfilePage'][0]['graphql']['user'] \
		['edge_owner_to_timeline_media']['edges'][0]['node']['taken_at_timestamp']
	inst_post_url = js['entry_data']['ProfilePage'][0]['graphql']['user'] \
		['edge_owner_to_timeline_media']['edges'][0]['node']['display_url']
	inst_post_code = js['entry_data']['ProfilePage'][0]['graphql']['user'] \
		['edge_owner_to_timeline_media']['edges'][0]['node']['shortcode']
	#print(inst_post_time)
	#print(inst_post_url)
	q = Inst.select().where(Inst.key == key)
	if q.exists():
		for s in q:
			#s.time = 0
			if s.time < inst_post_time:
				print ('new inst post')
				js = getInstPostJSON(inst_post_code)
				#print (json.dumps(js))
				#json = getInstPostJSON('Biy2diHAMGi') # 1 video
				#json = getInstPostJSON('Biy16WCAybt') # photo video photo
				#json = getInstPostJSON('Biy1szygW3l') # 3x photo
				#json = getInstPostJSON('qdtny9s3xR') # 1 photo
				media = js['entry_data']['PostPage'][0]['graphql']['shortcode_media']
				if media['edge_media_to_caption']['edges']: 
						caption = media['edge_media_to_caption']['edges'][0]['node']['text']
						if media['location']:
							caption = caption[:160]
							geo = getGeolocation(media['location']['id'])
							geo_link = '\n\n[🌎 Геолокация](yandex.ru/maps/?mode=search&text='+ geo +')'
							desc = '[Новый пост в #Instagram](instagram.com/p/'+ inst_post_code +')\n\n' + caption + geo_link
						else:
							caption = caption[:175]
							desc = '[Новый пост в #Instagram](instagram.com/p/'+ inst_post_code +')\n\n' + caption
				else:
						desc = ''
				#print (media)
				if media['__typename'] == 'GraphImage':
					print('GraphImage')
					url = media['display_url']
					r = teleSendURL(url, who, desc, inst_post_code, 0)
				elif media['__typename'] == 'GraphVideo':
					print('GraphVideo')
					url = media['video_url']
					print (url)
					r = teleSendURL(url, who, desc, inst_post_code, 1)
				elif media['__typename'] == 'GraphSidecar':
					print('GraphSidecar')
					inpmedia = []
					# Prepare InputMedia array for telegram sendMediaGroup	
					for s in range(len(media['edge_sidecar_to_children']['edges'])):
						if media['edge_sidecar_to_children']['edges'][s]['node']['is_video'] == True:
							if s == 0:
								inpmedia.append({'type': 'video', 'media': media['edge_sidecar_to_children']['edges'][s]['node']['video_url'], 'caption': desc, 'parse_mode': 'Markdown'})
							else:
								inpmedia.append({'type': 'video', 'media': media['edge_sidecar_to_children']['edges'][s]['node']['video_url']})
						else:
							if s == 0:
								inpmedia.append({'type': 'photo', 'media': media['edge_sidecar_to_children']['edges'][s]['node']['display_url'], 'caption': desc, 'parse_mode': 'Markdown'})
							else:
								inpmedia.append({'type': 'photo', 'media': media['edge_sidecar_to_children']['edges'][s]['node']['display_url']})	
					r = teleSendMediaGroup(who, inpmedia)
				if r.status_code == 200:
					q = Inst.update(key=key, time=inst_post_time).where(Inst.key == key)
					q.execute()
				else:
					teleReportError(r.text)
				print(key + ' inst post updated')
	else:
		q = Inst.create(key=key, time=inst_post_time)
		print(who + ' inst post DB does not exists, creating...')

def updInstStoryDB(who, id):
	key = who + '_story'
	js = getInstStoryJSON(id)
	if js == False:
		return
	inst_story_time = js['latest_reel_media']
	q = Inst.select().where(Inst.key == key)
	if q.exists():
		for i in q:
			#i.time = 0
			if i.time < inst_story_time:
				print ('new story')
				stories = []
				inpmedia = []
				#desc = '[instagram.com/' + who + '](Новая #InstagramStory)'
				#print (desc)
				#geo_link = '\n\n[Геолокация](yandex.ru/maps/?mode=search&text='+ geo +')'
				for s in range(len(js['items'])):
					if js['items'][s]['taken_at'] > i.time:
						print('number: ' + str(s))
						stories.append(js['items'][s])
						print('Adding new story to InputMedia!: ' + js['items'][s]['image_versions2']['candidates'][0]['url'])
				for s in range(len(stories)):
					#print('stories: ' + str(s))
					desc = '[Новая #InstagramStory](instagram.com/' + who + ')'
					#print (desc)
					if stories[s]['caption']:
						caption = stories[s]['caption']['text']
						caption = caption[:146]
						desc = desc + '\n\n' + caption
						#print (desc)
					if 'ad_action' in stories[s]:
						promo_link = '[🔗 Промо-ссылка](' + stories[s]['story_cta'][0]['links'][0]['webUri'] + ')'
						#promo_link = '[🔗 Промо-ссылка](yandex.ru/maps/?mode=search&text='+ stories[s]['story_cta'][0]['links'][0]['webUri'] +')'
						desc = desc + '\n\n' + promo_link
						#print (desc)
					if stories[s]['story_locations']:
						geo = str(stories[s]['story_locations'][0]['location']['lat']) + ';' + str(stories[s]['story_locations'][0]['location']['lng'])
						geo_link = '[🌎 Геолокация](yandex.ru/maps/?mode=search&text='+ geo +')'
						desc = desc + '\n\n' + geo_link
						#print (desc)
					if stories[s]['media_type'] == 1: # image type
						inpmedia.append({'type': 'photo', 'media': stories[s]['image_versions2']['candidates'][0]['url'], 'caption': desc, 'parse_mode': 'Markdown'})
					else:
						inpmedia.append({'type': 'video', 'media': stories[s]['video_versions'][0]['url'], 'caption': desc, 'parse_mode': 'Markdown'})
				#print (inpmedia)
				r = teleSendMediaGroup(who, inpmedia)

				if r.status_code == 200:
					q = Inst.update(key=key, time=inst_story_time).where(Inst.key == key)
					q.execute()
				else:
					teleReportError(r.text)
				print(key + ' inst post updated')
	else:
		q = Inst.create(key=key, time=inst_story_time)
		print(who + 'inst story DB does not exists, creating...')