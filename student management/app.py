'''
	Student Project APP
'''
from os import system
from studentapi import *

idno:str=""
lastname:str=""
firstname:str=""
course:str=""
level:str=""

student:dict={}

def header(message)->None:
    system('cls')
    print("-"*20)
    print(message.upper().center(20))
    print("-"*20)
    
def inputstudent()->None:
    global idno,lastname,firstname,course,level
    idno = input("IDNO      :")
    lastname = input("LASTNAME  :")
    firstname = input("FIRSTNAME :")
    course = input("COURSE    :")
    level = input("LEVEL     :")

    
def inputstudent_noidno()->None:
    global lastname,firstname,course,level
    lastname = input("LASTNAME  :")
    firstname = input("FIRSTNAME :")
    course = input("COURSE    :")
    level = input("LEVEL     :")


def add()->None:
    header('add student')
    inputstudent()
    #validation
    if idno !="" and lastname !="" and firstname !="" and course !="" and level !="":
        addstudent(idno=idno,lastname=lastname,firstname=firstname,course=course,level=level)
        print(f"\nNew Student Added")
    else:
        print(f"\nFill All fields")
        
def find()->None: 
    global idno,student
    header('findstudent')
    idno = input("STUDENT IDNO :")
    student = findstudent(idno=idno)
    if student:
        print("-"*20)
        for key,value in student.items():
            print(f"{key:>10} : {value:<10}")
        print("-"*20)
    else:
        print(f"Student Not Found !!!")
    
def remove()->None:
    find()
    if student:
        answer:str = input("Do you really want to DELETE this student(Y/N)?")
        if answer.upper() == "Y":
            deletestudent(student)
            print(f"Student Deleted !!!")
        else:
            print(f"Student Deletion CANCELLED !!!")
        
    
def update()->None:
    find()
    if student:
        answer:str = input("Do you really want to UPDATE this student(Y/N)?")
        if answer.upper() == "Y":
            inputstudent_noidno()
            updatestudent(idno=idno,lastname=lastname,firstname=firstname,course=course,level=level)
            print(f"Student UPDATED !!!")
        else:
            print(f"Student update CANCELLED !!!")

def displaymenu()->None:
    system('cls')
    print('-'*5+'Main Menu'+'-'*5)
    print('1. Add Student')
    print('2. Find Student')
    print('3. Update Student')
    print('4. Delete Student')
    print('5. Display All Student')
    print('0. Quit/End')
    print('-'*21)

def terminate()->None: print('Program Ends')

def main()->None:
    option:int = -1
    while option != 0:
        displaymenu()
        try:
            option = int(input('Enter Option(0..5) :'))
            match option:
                case 1: add()
                case 2: find()
                case 3: update()
                case 4: remove()
                case 5: displayall()
                case 0: terminate()
                case _: print("Accept only 0 to 5")
        except Exception as e:
            print(f"Invalid Input :{e}")
        print()
        input("Press any key to continue...")

if __name__ == "__main__":
    main()

