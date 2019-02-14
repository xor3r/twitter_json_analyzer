import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
import pprint
import pandas as pd
from pandas.io.json import json_normalize


def get_account_name():
	acct = input('Enter Twitter Account: ').strip()

	if acct == 'q':
		quit(0)
	assert 4 < len(acct)

	while True:
		quantity = input('How much friends to scan (from 1 to 20): ')
		if quantity == 'q':
			quit(0)
		try:
			quantity = int(quantity)
			if 1 <= quantity <= 20:
				break
			else:
				print('Enter a number from 1 to 20!')
				continue
		except ValueError as err:
			print('{} occured, try entering a valid number!'.format(str(err)))
			continue

	try:
		url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': str(quantity)})
		connection = urllib.request.urlopen(url, context=ctx)
	except BaseException:
		print('Seems like this account is private ..')
		quit(0)

	data = connection.read().decode()
	js = json.loads(data)

	return js


def display_content(js):
	proved = {'y', 'yes'}
	user_input = input('Would you like to see the JSON structure (y/n): ')

	if user_input .lower() in proved:
		print('Approved ..')
		pprint.pprint(js)
	elif user_input  == 'q':
		quit(0)
	else:
		print('Declined ..')

	return None


def user_choosings(js):
	data = json_normalize(js['users'])
	headers = [name for name in sorted(set(data))]
	proved = {'y', 'yes'}
	user_choices = list()
	user_choice = input('List all column names? (y/n): ')
	show_columns = True if user_choice in proved else False

	if show_columns:
		available_columns = pd.DataFrame(headers, index=range(1, len(headers) + 1))
		print('Available columns are', available_columns)

	print('Enter "all" if you want to see all of them. Press "Enter" to stop.')

	while True:
		user_input = input('Enter what columns you`d like to see: ').strip()
		if user_input == 'q':
			quit(0)
		elif user_input in headers and user_input not in user_choices:
			user_choices.append(user_input)
		elif user_input == str():
			break
		elif user_input == 'all':
			user_choices.clear()
			break
		else:
			continue

	return user_choices


def build_panda(user_choice):
	data = json_normalize(js['users'])
	columns = [x for x in sorted(set(data))]
	index=[x['name'] for x in js['users']]

	data = pd.DataFrame(js['users'], index=index, columns=columns)

	if user_choice == set():
		return data
	else:
		return data[user_choice]


if __name__ == '__main__':

	TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

	# Ignore SSL certificate errors
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE

	pd.set_option("display.max_rows", 105)
	pd.set_option("display.max_columns", 105)

	print('Welcome! To quit -> type "q" anytime a prompt appears.')

	js = get_account_name()
	display_content(js)

	pd.set_option('display.max_colwidth', 100)
	user_choice = user_choosings(js)

	pd.set_option('display.max_colwidth', 21)
	result = build_panda(user_choice)
	print(result)
