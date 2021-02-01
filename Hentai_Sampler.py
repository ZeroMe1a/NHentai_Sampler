# This is a simple program that uses the NHentai API to get random doujins
# dev: Zero Meia#8828

from NHentai import NHentai
from os import system, name
from time import sleep
from colorama import init
from termcolor import colored
from random import randrange

init()

nhentai = NHentai()

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def title_render(sub, link):
	clear()
	print(colored(f'Last Link: {link}\n', 'magenta'))
	print(colored('██╗  ██╗███████╗███╗  ██╗████████╗ █████╗ ██╗', 'cyan'))
	print(colored('██║  ██║██╔════╝████╗ ██║╚══██╔══╝██╔══██╗██║', 'cyan'))
	print(colored('███████║█████╗  ██╔██╗██║   ██║   ███████║██║', 'cyan'))
	print(colored('██╔══██║██╔══╝  ██║╚████║   ██║   ██╔══██║██║', 'cyan'))
	print(colored('██║  ██║███████╗██║ ╚███║   ██║   ██║  ██║██║', 'cyan'))
	print(colored(f'╚═╝  ╚═╝╚══════╝╚═╝  ╚══╝   ╚═╝   ╚═╝  ╚═╝╚═╝ {sub}\n\n', 'cyan'))

def search_tags():
	clear()
	title_render('Search Tags', 'None')
	ch = input(colored('Tags: ', 'white'))
	search_obj = nhentai.search(query=ch, sort='popular', page=1)

	if search_obj.total_results == 0:
		print(colored('\nNo Results...\n', 'red'))
		print(colored('1 - Return to Start', 'yellow'))
		print(colored('2 - Quit HentaiPicker\n', 'yellow'))

		ch = input(colored('?: ', 'yellow'))

		if ch == '1':
			main_menu()

		elif ch == '2':
			quit()

		else:
			print(colored('Unexpected Error, Returning...', 'red'))
			sleep(1.5)
			main_menu('None')

	elif search_obj.total_results > 0:
		with open('results.txt', 'w') as f:
			for i in range(search_obj.total_pages):
				for i in range(len(search_obj.doujins)):
					search_results = ' https://nhentai.net/g/'+search_obj.doujins[i].id+'\n'
					f.write(search_results)

		print(colored('\nSearch Results Saved to results.txt\n', 'green'))

		print(colored('1 - Return to Start', 'yellow'))
		print(colored('2 - Quit HentaiPicker', 'yellow'))

		ch = input(colored('?: ', 'yellow'))

		if ch == '1':
			main_menu('None')

		elif ch == '2':
			quit()

		else:
			print(colored('Unexpected Error, Returning', 'red'))
			sleep(0.75)
			main_menu('None')

def rnd_doujin():
	random_doujin: dict = nhentai.get_random()
	title_render('Random', 'None')

	print(colored(f"Title: {random_doujin.title}\n", 'yellow'))
	print(colored(f"Tags: {random_doujin.tags}\n", 'yellow'))
	print(colored(f"Link: {'https://nhentai.net/g/'+random_doujin.id}\n", 'magenta'))
	print(colored(f"Artists: {random_doujin.artists}\n", 'yellow'))
	print(colored(f"Pages: {random_doujin.total_pages}\n", 'yellow'))

	print(colored('Returning to the start page in 5 seconds!', 'yellow'))
	sleep(5)
	main_menu('https://nhentai.net/g/'+random_doujin.id)

def main_menu(link):
	title_render('Menu', link)
	print('1 - Search With Tags')
	print('2 - Random Dounjin\n')
	ch = input('?: ')

	if ch == '1':
		search_tags()

	elif ch == '2':
		rnd_doujin()

main_menu('None')
