class Movie:

    def __init__(self, name, runningTime, genre, isHit):
        self.name=name
        self.runningTime=runningTime
        self.genre=genre
        self.isHit=isHit


movie= Movie("Office Space", 2, "Comedy", True)
print(movie.name)
print(movie.genre)