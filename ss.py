from selenium import webdriver
from io import BytesIO, StringIO
from selenium.webdriver.chrome.options import Options
from PIL import Image
#import StringIO
import os

from tele import teleSendPhotoSS


def vkSS(url):
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--window-size=800x900")
	chrome_options.add_argument("--force-device-scale-factor=2")
	chrome_options.add_argument("--disable-gpu")
	chrome_options.add_argument("--disable-impl-side-painting")
	chrome_options.add_argument("--disable-gpu-sandbox")
	chrome_options.add_argument("--disable-accelerated-2d-canvas")
	chrome_options.add_argument("--disable-accelerated-jpeg-decoding")
	chrome_options.add_argument("--no-sandbox")
	
	chrome_driver = "chromedriver"
	
	chrome = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
	chrome.get(url)
	#chrome.get("https://vk.com/wall-110043365_33800")
	element = chrome.find_element_by_css_selector('div.wall_text')
	# capture_element(element, chrome)
	location = element.location
	#print(location)
	size = element.size
	#print(size)
	png = chrome.get_screenshot_as_png()
	chrome.quit()

	im = Image.open(BytesIO(png))

	left = location['x'] * 2
	top = (location['y'] * 2) - 130
	right = (location['x'] + size['width']) * 2
	bottom = (location['y'] + size['height']) * 2

	im = im.crop((left, top, right, bottom))
	#im = im.crop((360, 122, 500, 222))
	#im.save('s.png')
	img = StringIO.StringIO()
	print (im)
	im.save(img, format="png")
	return img

img = vkSS('https://vk.com/wall-110043365_33563')
print(img)
teleSendPhotoSS ('artembaccardi', img, 'pook')