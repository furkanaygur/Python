import requests


# ************ Classes ************************
class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = " "  # its your api key

    def getPopulars(self):
        response = requests.get(f"{self.api_url}movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def searchMoive(self, moviename):
        response = requests.get(f"{self.api_url}search/keyword?api_key={self.api_key}&query={moviename}&page=1")
        return response.json()


# ********************* Main ******************
movieApi = theMovieDb()

while True:
    choice = input("1- Popular Movies\n2- Find Movie\n3- Exit\nYour Choice: ")
    if choice == "3":
        break
    else:
        if choice == "1":
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])
        elif choice == "2":
            moviename = input("Movie Name: ")
            movies = movieApi.searchMoive(moviename)
            for movie in movies['results']:
                print(movie['name'])

        else:
            print("You can only input 1-2-3")
