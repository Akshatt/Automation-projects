from github import Github
import stdiomask


def userInput():
    # Github username and password
    username = input("Enter GitHub username: ")
    print("Enter password to consider private repos as well, else just press Enter")
    password = stdiomask.getpass(prompt='Enter Password: ')
    return userAuth(username, password)


def userAuth(username, password):
    if password == "":
        user = Github().get_user(username)
        private = 0
    else:
        user = Github(username, password).get_user()
        private = 1
    return assign_repos(user, private)


def assign_repos(user, private):
    try:
        for repo in user.get_repos():
            try:
                repo.get_contents("README.md")
            except:
                if private == 1 and repo.private:
                    private_repos.append(repo.name)
                else:
                    public_repos.append(repo.name)
    except:
        print("Oops! Check if:\n1. No password was entered -->> the user has no public repo with a missing readme\
         \n2. A password was entered -->> it didn't match the username\nTry again")
        return userInput()

    print_repos("PUBLIC", public_repos)
    if private == 1:
        print_repos("PRIVATE", private_repos)


def print_repos(status, repos):
    print("\nFollowing {} repos don't have a README.md file:".format(status))
    for repo in repos:
        print(repo)
    return


private_repos = []
public_repos = []
userInput()
