import sys 
import os

def main():
    print("\nGood Morning, Praneeth")
    menu()

def menu():
    path = '/Users/ppatakota/Desktop/reactDev/newscast-cli/'
    os.chdir(path)
    print("\nSelect Your Favorite News : ")
    choice = input("""
        A: Editorials - Hindu
        B: Editorials - EconomicTimes
        C: Editorials - IndianExpress
        D: Sports - Formula1
        E: Sports - PremierLeague
        Q: Quit/Log Out

        Please enter your choice: """)

    if choice == "A" or choice =="a":
        viewhindu()
    elif choice == "B" or choice =="b":
        viewet()
    elif choice == "C" or choice =="c":
        viewindexp()
    elif choice == "D" or choice =="d":
        viewf1()
    elif choice == "E" or choice =="e":
        viewepl()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A,B,C, or Q.")
        print("Please try again")
        menu()

def viewhindu():
    cmd = 'node index eds hindu'
    os.system(cmd)
    readfuther()

def viewet():
    cmd = 'node index eds et'
    os.system(cmd)
    readfuther()

def viewindexp():
    cmd = 'node index eds ie'
    os.system(cmd)
    readfuther()

def viewf1():
    cmd = 'node index sports f1'
    os.system(cmd)
    readfuther()

def viewepl():
    cmd = 'node index sports epl'
    os.system(cmd)
    readfuther()

def readfuther():
    choice = input("""
        Do you want to read further? 
        Press any-key to continue
        Press 'Q/q' to quit : """)
    if choice == 'Q' or choice == 'q':
        print('Goodbye!')
        sys.exit()
    else:
        menu()

main()
