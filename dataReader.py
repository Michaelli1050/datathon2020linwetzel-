import json
import dataAnalysis
import google_images_download
import pygame 
import os 
pygame.init()
white = (255,255,255)
width = 800
height = 800 
display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Poster")
response = google_images_download.googleimagesdownload()


def downloadimages(item):
	args = {
		"keywords":item,  
		"format":"jpg",
		"limit":2,
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
            "limit":2, 
            "print_urls":True,  
            "size": "medium",
			"no_directory": True
		} 
                       
        # Providing arguments for the searched query
		try: 
            # Downloading the photos based 
            # on the given arguments
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
	path = "C:\Users\Michael Lin\Documents\datathon2020\datathon2020linwetzel-\downloads"
	while True:
		for event in pygame.event.get():
			display.fill(white)
			for image in os.listdir(path):
				input_path = os.path.join(path, image)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			pygame.display.update()
main()
