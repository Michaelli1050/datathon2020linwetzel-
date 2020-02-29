import json
import requests





def findFilm(films, s):
	for film in films:
		if (film["title"].lower() == s.strip()):
			return film
	return -1
		


def main():
	with open("netflix_title.json", encoding = "utf8") as f:
		films = json.load(f)
	cur_film = input("Please enter the film you just watched: ")
	print(cur_film)
	#cur_film.strip("")
	x = -1
	for film in films:
		if (film["title"].lower().strip() == cur_film.lower().strip()):
			x = film
			
			break
		
	while(x == -1):
		s = input("Film name was entered incorrectly, or is not on Netflix, please enter another: ")
		x = findFilm(films, s.lower())
	print(x)
	#y = findNearest(x)


main()