TKN_TELE_IWB = '1743661214:FAB8i-1238zJaF_ZXYszKj1dOpHB5t3lSz8f3' # Use t.me/BotFather to create your bot and get token

# Here you emulate your iPhone to get Instagram Stories JSON data from URL request
# https://curl.trillworks.com/ — cUrl to python requests converter
story_headers = {
	'dnt': '1',
	'accept-encoding': 'gzip, deflate, br',
	'x-ig-capabilities': '3brTAw==',
	'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6,bg;q=0.5,pl;q=0.4,la;q=0.3',
	'user-agent': 'Instagram 10.26.0 (iPhone7,2; iOS 10_1_1; en_US; en-US; scale=2.00; gamut=normal; 750x1334) AppleWebKit/420+',
	'accept': '*/*',
	'authority': 'i.instagram.com',
	'cookie': 'ds_user_id=4423694191; sessionid=IGSCa13405e1193ff09c178036499fc06fd1234197ba6192c4a78cd394%3A2yNM4UwhBrqMMHV7n88lmzXr6nTYo5XF%3A%7B%22_auth_user_id%22%23442969501234C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiv123ackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%312342C%22_token_ver%22%3A2234%22_token%22%3A%225429695034%3Au4Kbwimq5mIDjGToQGDPmQjSjMTB6Y35%3A28ccb0bae7ce5d4e9fba57e99543005fdb9c18073d2aba8e0c5e035c407b876c%22%2C%22last_refreshed%22%3A1526405999.5123459189%7D; csrftoken=aF9d9HasdfFyBRwCfadfJB61tSjXeyRa7C;',
}

INST_ATKN = '013051502.f1a3623.4b8296d0fa443141920cd64s86f46f918' # Instagram Access Token with all scopes,use this to get token https://elfsight.com/service/generate-instagram-access-token/