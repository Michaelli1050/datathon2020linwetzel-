import json 


class dataAnalysis:
    def __init__(self,films):
        self.id= object["show_id"]
        self.type = object["type"]
        self.title = object["title"]
        self.director = object["director"]
        self.cast = object["cast"]
        self.country = object["country"]
        self.release_year = object["release_year"]
        self.duration = object["duration"]
        self.listing = object["listed_in"]
        self.description = object["description"]
        self.rating = object["rating"]
        self.films = objects
    def findNearest(data):
        recommended = []
        index = 0
        for film in films:
            score = 0
            score = calculateGenre(listing, film['listed_in']) + calculateCast(cast, film['cast']) + calculateCountry(country, film['country'])
            score = score + calculateDirector(director, film['director']) + calculateYear(release_year, film['releaseyear'])
            score = score + calculateRating(rating, film['rating'])
            if (score > 50):
                recommended[index] = film
                index = index + 1 
        return recommended 
    
    
def calculateGenre(g1, g2):
    genre1 = g1.split(',')
    genre2 = g2.split(',')
    x = len(g1)
    y = 0
    weight = (25/x)
    for a in genre1:
        for b in genre2:
            if a == b:
                y = y+1
                break
    return (y * weight)
def calculateYear(g1,g2):
    x = abs(g1-g2)
    if (x == 0):
        return 15
    if (x <= 30):
        return 15-(0.5*x)
    else:
        return 0
def calculateCountry(g1,g2):
    if (g1 == g2):
        return 15 
    else:
        return 0
def calculateRating(g1,g2):
    little_kids = ['G', 'TV-Y','TV-G']
    older_kids = ['PG','TV-Y7','TV-Y7-FV','TV-PG']
    teens = ['PG13','TV-14']
    mature = ['TV-MA', 'R', "NC-17",]
    if (g1 in little_kids):
        if (g2 in little_kids):
            return 15
        if (g2 in older_kids):
            return 5
        if (g2 in teens or g2 in mature):
            return 0
    if (g1 in older_kids):
        if (g2 in little_kids):
            return 5
        if (g2 in older_kids):
            return 15
        if (g2 in teens):
            return 5
        if (g2 in mature):
            return 0 
    if (g1 in teens):
        if (g2 in little_kids):
            return 0
        if (g2 in older_kids):
            return 5
        if (g2 in teens):
            return 15
        if (g2 in mature):
            return 5
    if (g1 in mature):
        if (g2 in little_kids):
            return 0
        if (g2 in older_kids):
            return 0
        if (g2 in teens):
            return 5
        if (g2 in mature):
            return 15
def calculateCast(g1,g2):
    cast1 = g1.split(',')
    cast2 = g2.split(',')
    x = len(g1)
    y = 0
    weight = (25/x)
    for a in cast1:
        for b in cast2:
            if a == b:
                y = y+1
                break
    return (y * weight)
def calculateDirector(g1,g2):
    directors1 = g1.split(',')
    directors2 = g2.split(',')
    x = len(g1)
    y = 0
    weight = (5/x)
    for a in cast1:
        for b in cast2:
            if a == b:
                y = y+1
                break
    return (y * weight)
