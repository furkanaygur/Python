import requests


class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"

    def getUser(self, username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()

    def getRepositories(self, username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()


# ********************** Main ***************************

github = Github()

while True:
    choice = input("1- Find User\n2- Get Repositories\n3- Exit\nYour Choice :")

    if choice == '3':
        break
    else:
        if choice == "1":
            username = input('username :')
            result = github.getUser(username)
            print(f"Name: {result['name']} \nPublic Repos: {result['public_repos']} \nFollowers: {result['followers']}")

        elif choice == "2":
            username = input('username :')
            result = github.getRepositories(username)
            for repo in result:
                print(repo["name"])

        else:
            print("You can input only 1-2-3")
