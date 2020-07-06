from github import Github
import stdiomask

# Github username and password
username = input("Enter GitHub username: ")
print("To include private repos as well, GitHub needs to be authenticated.\n\
        This will require you to enter your password.")
print("If you don't wish to do so, simply press Enter when asked for password")
password = stdiomask.getpass(prompt='Enter Password: ')

# pygithub object
if password == "":
    g = Github()
    user = g.get_user(username)
    private = 0
else:
    g = Github(username, password)
    user = g.get_user()
    private = 1


def findreadme(repo):
    try:
        if repo.get_contents("README.md"):
            return False
    except:
        return True


no_readme_repos = []
for repo in user.get_repos():
    if findreadme(repo):
        no_readme_repos.append(repo)
        print(repo)
