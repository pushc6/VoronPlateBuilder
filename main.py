import os
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def get_menu():
    print("Menu:")
    print("1. Update repos")
    print("2. Build plates")

def pull_repos():
    os.system("cd ~/Downloads; ls")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_menu()
    choice = input("Enter your choice [1-2]:")

    if choice == '1':
        print("Pulling repos!")
        pull_repos()
    else:
        print("Wrong value entered, try again.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
