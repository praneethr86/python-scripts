import sys 
import os

def main():
    print("\nHappy Reading!")
    menu()

def menu():
    path = '/Users/ppatakota/Desktop/reactDev/newscast-cli/'
    os.chdir(path)
    print("\nSelect Your News source : ")
    choice = input("""
        A: Editorials - Hindu
        B: Editorials - EconomicTimes
        C: Editorials - IndianExpress
        D: Sports - Formula1
        E: Sports - PremierLeague
        F: YourStory - Social
        G: Editorials - Guardian
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
    elif choice == "F" or choice == "f":
        viewyssocial()
    elif choice == "G" or choice == "g":
        viewguardian()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A-G or Q.")
        print("Please try again")
        menu()

def viewhindu():
    cmd = 'node index eds hindu'
    os.system(cmd)
    readfurther()

def viewet():
    cmd = 'node index eds et'
    os.system(cmd)
    readfurther()

def viewindexp():
    cmd = 'node index eds ie'
    os.system(cmd)
    readfurther()

def viewf1():
    cmd = 'node index sports f1'
    os.system(cmd)
    readfurther()

def viewepl():
    cmd = 'node index sports epl'
    os.system(cmd)
    readfurther()

def viewyssocial():
    cmd = 'node index yourstory social'
    os.system(cmd)
    readfurther()

def viewguardian():
    cmd = 'node index eds guardian'
    os.system(cmd)
    readfurther()

def readfurther():
    choice = input("""
        Do you want to read further? 
        Press any-key to continue.
        Press 'Q/q' to quit : """)
    if choice == "Q" or choice == "q":
        print('Goodbye!')
        sys.exit()
    else:
        menu()

main()
