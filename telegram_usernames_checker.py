# Libraries
import requests
import datetime
import traceback
from bs4 import BeautifulSoup
from progress.bar import IncrementalBar
# /. Libraries


def main():
	# Hello message
	print('''\n\n\n--- Telegram Usernames Checker ---

Create a file that will contain any words under each other. They will be checked for availability in Telegram.

----------------------------------\n\n\n''')
	# /. Hello message

	array_type = input('Select array type ( file / list ): ')
	output_type = input('Select output type ( file / list ): ')

	if output_type in ['file', 'list']:
		if array_type == 'file':
			# File settings

			file_with_words = input('Write text file name which contains words: ')

			try:
				with open(f'{file_with_words}.txt', 'r+') as f:
					if f.readlines()[-1] != '':
						f.write('') # insert empty line to file

				check_usernames(words_array=file_with_words, usernames_output=output_type, progress_bar=True)

			except FileNotFoundError:
				print('File with this name not found.')
			
			# /. File settings

		elif array_type == 'list':
			list_with_words = input('Write words seperated by commas: ').split(',')

			check_usernames(words_array=list_with_words, usernames_output=output_type, progress_bar=True)

		else:
			print('You selected non-existed array type.')

	else:
		print('You selected non-existed output type.')

# Main block

def check_usernames(words_array, usernames_output: str, progress_bar=False):
	''' Check usernames
	
	Checking usernames from words_array for avaibility in Telegram.

	words_array - accepts text file name or list. In this array there should be
	words ( AKA usernames ) which will be checked with this function.
	
	usernames_output - in what format will be returned availbility usernames ( "file" / "list" )'''

	try:
		if isinstance(words_array, str):
			words = open(f'{words_array}.txt')
			words_count = sum(1 for line in open(f'{words_array}.txt'))

		elif isinstance(words_array, list):
			words = words_array
			words_count = len(words_array)

		checked_words = [] # words which checked for availlable

		if progress_bar == True: bar = IncrementalBar('Checking words', max=words_count) # show progress bar

		for word in words:
			if progress_bar == True: bar.next() # next % in progress bar

			if isinstance(words_array, str): word = word.replace("\n", "") # remove line breaks
			elif isinstance(words_array, list): word = word.replace(" ", "") # remove spaces

			# Checking symbols in word

			symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r',
				's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_']
					
			word_symbols = list(word)

			valid_symbols = 0

			for symbol in word_symbols:
				if symbol in symbols:
					valid_symbols += 1
				
			# /. # Checking symbols in word

			if len(word_symbols) == valid_symbols:
				# Checking word for used by peoples in Telegram
				telegram_web = requests.get(f'https://t.me/{word.lower()}')
				soup = BeautifulSoup(telegram_web.text, 'html.parser')
				elements_list = soup.find_all("div", {"class": "tgme_page_extra"})
				# /. Checking word for used by peoples in Telegram

				if len(elements_list) == 0:
					# Checking word for sale/sold in Fragment.com
					fragment = requests.get(f'https://fragment.com/username/{word.lower()}')
					soup = BeautifulSoup(fragment.text, 'html.parser')
					avail_status = soup.find_all("tr", {"class": "tm-section-header-status tm-status-avail"})
					sold_status = soup.find_all("tr", {"class": "tm-section-header-status tm-status-unavail"})
					# /. Checking word for sale/sold in Fragment.com

					if len(avail_status) == 0 and len(sold_status) == 0:
						checked_words.append(word)  

		if progress_bar == True: bar.finish() # remove progress bar 

		if len(checked_words) != 0:
			if usernames_output == 'file':
				if isinstance(words_array, str): words.close()

				# Create file with availlable usernames
				current_datetime = datetime.datetime.now().strftime('%H-%M_(%Y-%m_%d)')
				avail_usernames_file = f'avail_usernames-[{current_datetime}]'

				with open(f'{avail_usernames_file}', 'w') as avail_usernames:
					for word in checked_words:
						avail_usernames.write(f'{word}\n')
				# /. Create file with availlable usernames

				print(f'''Successfully!

Availlable usernames finded: {len(checked_words)}
File name which contain this usernames: {avail_usernames_file}

Attention - words can wiil be reserved the Telegram itself.''')

			elif usernames_output == 'list':
				return checked_words

		else:
			print('''It didn't work out :(
			
All words unavailable in Telegram.''')

	except:
		if progress_bar == True: bar.finish() # remove progress bar 
		
		print(f'''An unknown error has occurred :(
			
Error text: {traceback.format_exc()}''')

# /. Main block

if __name__ == '__main__':
	main()


