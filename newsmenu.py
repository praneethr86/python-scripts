import sys 
import os

def main():
    print("\nGood Morning, Praneeth")
    menu()

def menu():
    path = '/Users/ppatakota/Desktop/reactDev/newscast-cli/';
    os.chdir(path)
    print("\nSelect Your Favorite News : ")
    choice = input("""
        A: Editorials - Hindu
        B: Editorials - ET
        C: Sports - F1
        D: Sports - EPL
        Q: Quit/Log Out

        Please enter your choice: """)

    if choice == "A" or choice =="a":
        viewhindu()
    elif choice == "B" or choice =="b":
        viewet()
    elif choice == "C" or choice =="c":
        viewf1()
    elif choice == "D" or choice =="d":
        viewepl()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A,B,C, or Q.")
        print("Please try again")
        menu()

def viewhindu():
    cmd = 'node index eds hindu';
    os.system(cmd);
    readfuther();

def viewet():
    cmd = 'node index eds et';
    os.system(cmd);
    readfuther();

def viewf1():
    cmd = 'node index sports f1';
    os.system(cmd);
    readfuther();

def viewepl():
    cmd = 'node index sports epl';
    os.system(cmd);
    readfuther();

def readfuther():
    choice = input("""
        Do you want to read further? 
        Press 'y' to continue
        Press any other key to quit : """)
    if choice == 'Y' or choice == 'y':
        menu();
    else:
        print('Goodbye!')
        sys.exit

main()
