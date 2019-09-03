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
        D: Editorials - Guardian
        E: Editorials -  Project Syndicate
        F: Management -  Harvard Business Review
        G: Sports - Formula1
        H: Sports - PremierLeague
        I: Startups - YourStory:Social 
        Q: Quit/Log Out

        Please enter your choice: """)

    if choice == "A" or choice =="a":
        viewhindu()
    elif choice == "B" or choice =="b":
        viewet()
    elif choice == "C" or choice =="c":
        viewindexp()
    elif choice == "D" or choice =="d":
        viewguardian()
    elif choice == "E" or choice =="e":
        viewprojsyndicate()
    elif choice == "F" or choice == "f":
        viewhbrlatest()
    elif choice == "G" or choice == "g":
        viewf1()
    elif choice == "H" or choice == "h":
        viewepl()
    elif choice == "I" or choice == "i":
        viewyssocial()
    elif choice=="Q" or choice=="q":
        print('\nGoodbye!\n\n')
        sys.exit
    else:
        print("You must only select either A-I or Q.")
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
