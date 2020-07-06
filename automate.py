from github import Github
import stdiomask

# Github username and password
username = input("Enter GitHub username: ")
print("To include private repos as well, GitHub needs to be authenticated.\n\
        This will require you to enter the password for {}.\n\
If you don't wish to do so, simply press Enter when asked for password".format(username))
password = stdiomask.getpass(prompt='Enter Password: ')

# pygithub object
if password == "":
    user = Github().get_user(username)
    private = 0
else:
    g = Github(username, password)
    user = g.get_user()
    private = 1


def assignrepos(repo):
    try:
        if repo.get_contents("README.md"):
            return False
    except:
        if private == 1 and repo.private:
            private_repos.append(repo)
        else:
            public_repos.append(repo)
        return True


private_repos = []
public_repos = []
for repo in user.get_repos():
    assignrepos(repo)


def repoprint(status, repos):
    print("\nFollowing {} repos don't have a README.md file:".format(status))
    for repo in repos:
        print(repo)
    return print()


repoprint("public", public_repos)
if private == 1:
    repoprint("private", private_repos)
