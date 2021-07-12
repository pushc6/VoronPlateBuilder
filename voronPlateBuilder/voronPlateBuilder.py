import os
import urwid
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

repos = []
dlPath = "/Users/ryan/Downloads/Voron/"


def get_menu():
    print("Menu:")
    print("1. Update repos")
    print("2. Build plates")
    print("3. Initial setup")

def pull_repos():
    for dir in os.listdir(dlPath):
        if(os.path.isdir(dlPath+dir)):
            print(os.system("cd "+ dlPath+ dir+ "; git pull -r"))


def read_repos_from_file():
    f = open("../repos.txt")
    try:
        global repos
        repos = f.readlines()
    finally:
        f.close()


def checkout_repos():
    global repos
    for repo in repos:
        index = repo.rindex("/", 0, len(repo))
        repoName = repo[index+1:-4]  #end of github project name minus .git
        if os.path.isdir(dlPath+repoName):
            print("Repo: ", repoName, " already exists, skipping clone.")
        else:
            print("Cloning repo: ", repoName)
            os.system("git clone ", repo)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    txt = urwid.Text(u"Hello World")
    fill = urwid.Filler(txt, 'top')
    loop = urwid.MainLoop(fill)
    loop.run()

    get_menu()
    choice = input("Enter your choice [1-2]:")

    if choice == '1':
        print("Pulling repos!")
        pull_repos()
    elif choice == '3':
        print("downloading plater")
        #TODO download and build plater cmdline
        print("Fresh pull of repos!")
        read_repos_from_file()
        checkout_repos()
    else:
        print("Wrong value entered, try again.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
