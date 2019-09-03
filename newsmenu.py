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
        D: Editorials - HinduBusinessLine
        E: Editorials - Guardian
        F: Editorials -  Project Syndicate
        G: Management -  Harvard Business Review
        H: Sports - Formula1
        I: Sports - PremierLeague
        J: Startups - YourStory:Social 
        Q: Quit/Log Out

        Please enter your choice: """)

    if choice == "A" or choice =="a":
        viewhindu()
    elif choice == "B" or choice =="b":
        viewet()
    elif choice == "C" or choice =="c":
        viewindexp()
    elif choice == "D" or choice =="d":
        viewhbline()
    elif choice == "E" or choice =="e":
        viewguardian()
    elif choice == "F" or choice == "f":
        viewprojsyndicate()
    elif choice == "G" or choice == "g":
        viewhbrlatest()
    elif choice == "H" or choice == "h":
        viewf1()
    elif choice == "I" or choice == "i":
        viewepl()
    elif choice == "J" or choice == "j":
        viewyssocial()
    elif choice=="Q" or choice=="q":
        print('\nGoodbye!\n\n')
        sys.exit
    else:
        print("You must only select either A-J or Q.")
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

def viewhbline():
    cmd = 'node index eds hbl'
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

def viewprojsyndicate():
    cmd ='node index projsyn all'
    os.system(cmd)
    readfurther()

def viewhbrlatest():
    cmd = 'node index hbr latest'
    os.system(cmd)
    readfurther()

def readfurther():
    choice = input("""
        Do you want to read further? 
        Press any-key to continue.
        Press 'Q/q' to quit : """)
    if choice == "Q" or choice == "q":
        print('\nGoodbye!\n\n')
        sys.exit()
    else:
        menu()

main()
