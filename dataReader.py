import json
import dataAnalysis
import google_images_download
import pygame 
import os 
import time


response = google_images_download.googleimagesdownload()


def downloadimages(item):
	args = {
		"keywords":item,  
		"format":"jpg",
		"limit":1,
		"print_urls":True,
		"size":"medium",
		"no_directory":True
	}
	try:
		response.download(args)
	except FileNotFoundError:
		args = {
			"keywords": query, 
        	"format": "jpg", 
            "limit":1, 
            "print_urls":True,  
            "size": "medium",
			"no_directory": True
		} 
                       
		try: 
			response.download(arguments)
		except:
			pass
def findFilm(films, s):
	for film in films:
		if (film["title"].lower() == s.strip()):
			return film
	return -1
		


def main():
	with open("netflix_title.json", encoding = "utf8") as f:
		films = json.load(f)
	cur_film = input("Please enter the film you just watched: ")
	#cur_film.strip("")
	x = -1
	for film in films:
		if (film["title"].lower().strip() == cur_film.lower().strip()):
			x = film
			break
		
	while(x == -1):
		s = input("Film name was entered incorrectly, or is not on Netflix, please enter another: ")
		x = findFilm(films, s.lower())
	y = dataAnalysis.analysis(x,films)
	results = (y.findNearest())
	images = []
	for result in results:
		print (result['title'] + " " + str(result['score']))
		images.append(result['title'].replace(":","") + " Netflix Cover")
	for image in images:
		downloadimages(image)
	path = r"C:\Users\Michael Lin\Documents\datathon2020\datathon2020linwetzel-\downloads"
	pygame.init()
	white = (255,255,255)
	transparent = (0,0,0,0)
	width = 600
	height = 600
	display = pygame.display.set_mode((width,height))
	pygame.display.set_caption("Poster")
	while True:
		display.fill(white)
		for pictures in os.listdir(path):
				input_path = os.path.join(path, pictures)
				picture = pygame.image.load(input_path)
				display.blit(picture,(0,0))
				pygame.display.update()
				pygame.time.delay(1000)
				
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
main()
