import json 

def mergeSort(films):
        if (len(films) > 1):
            mid = len(films)//2
            left = films[:mid]
            right = films[mid:]
            mergeSort(left)
            mergeSort(right)
            x = 0
            y = 0
            k = 0
            while x < len(left) and y < len(right):
                if left[x]['score'] < right[y]['score']:
                    films[k] = left[x]
                    x += 1 
                else:
                    films[k] = right[y]
                    y += 1 
                k += 1 
            while x < len(left):
                films[k] = left[x]
                x += 1 
                k += 1
            while y < len(right):
                films[k] = right[y]
                y += 1 
                k += 1 
class analysis:
    def __init__(self,object,films):
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
        self.films = films
    def findNearest(self):
        recommended = []
        index = 0
        scores = {}
        for film in self.films:
            if (film['title'] != self.title):
                score = 0
                if (film['type'].lower().strip() == 'TV Show'.lower().strip()):
                    score = score + 5
                score = score + calculateGenre(self.listing, film['listed_in']) 
                score = score + calculateCast(self.cast, film['cast']) 
                score = score + calculateCountry(self.country, film['country'])
                score = score + calculateDirector(self.director, film['director']) 
                score = score + calculateYear(self.release_year, film['release_year'])
                score = score + calculateRating(self.rating, film['rating'])
                film['score'] = score 
                if (score > 55):
                    recommended.append(film)
                    index = index + 1 
                    scores[film['title']] = score
        mergeSort(recommended)
            #if (film['title'] == self.title):
                #print (film['type'])
                #print ("Cast score " + str(calculateCast(self.cast, film['cast'])))
                #print ("Genre score " + str(calculateGenre(self.listing, film['listed_in'])))
                #print ("Director score " + str(calculateDirector(self.director, film['director'])))
                #print ("Year score " + str(calculateYear(self.release_year, film['release_year'])))
                #print ("Country Score " + str(calculateCountry(self.country, film['country'])))
                #print ("Rating score" + str(calculateRating(self.rating, film['rating'])))
        
        return recommended
    

def calculateGenre(g1, g2):
    genre1 = g1.split(',')
    genre2 = g2.split(',')
    x = len(genre1)
    y = 0
    weight = (25/x)
    for b in genre2:
        if b in genre1:
            y = y+1
    return (y * weight)
def calculateYear(g1,g2):
    x = abs(g1-g2)
    if (x == 0):
        return 10
    if (x <= 30):
        return 10-(0.33*x)
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
            return 20
        if (g2 in older_kids):
            return 10
        if (g2 in teens or g2 in mature):
            return -10
    if (g1 in older_kids):
        if (g2 in little_kids):
            return 10
        if (g2 in older_kids):
            return 20
        if (g2 in teens):
            return 10
        if (g2 in mature):
            return -10
    if (g1 in teens):
        if (g2 in little_kids):
            return -10
        if (g2 in older_kids):
            return -5
        if (g2 in teens):
            return 20
        if (g2 in mature):
            return 10
    if (g1 in mature):
        if (g2 in little_kids):
            return -10
        if (g2 in older_kids):
            return 0
        if (g2 in teens):
            return 5
        if (g2 in mature):
            return 20
    return 0
def calculateCast(g1,g2):
    cast1 = g1.split(',')
    cast2 = g2.split(',')
    
    x = len(cast1)
    if (x == 0):
        return 10
    y = 0
    weight = (25/x)
    for x in range(len(cast1)):
        if cast1[x] in cast2:
            y = y + 1
    return (y * weight)
def calculateDirector(g1,g2):
    directors1 = g1.split(',')
    directors2 = g2.split(',')
    x = len(g1)
    if (x == 0):
        return 0
    y = 0
    weight = (5/x)
    for a in directors1:
        for b in directors2:
            if a == b:
                y = y+1
                break
    return (y * weight)
