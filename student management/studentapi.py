'''
	Student API
    **kwargs (key word argument) - a dictionary data at the module
                                parameter

'''
#data container
from os import system
from data import slist

index:int = 999


#student modules
def addstudent(**kwargs)->None: 
    slist.append(kwargs)
    
def deletestudent(student)->None:
    slist.remove(student)
   
def updatestudent(**kwargs)->None:
    slist[index] = kwargs
    
def findstudent(**kwargs)->None:
    global index
    keys = list(kwargs.keys()) #return the keys of the kwargs
    values = list(kwargs.values())
    for student in slist:
        if student[keys[0]] == values[0]:
            index = slist.index(student)
            return student
    return None
    
def displayall()->None:
    system('cls')
    header:list = list(slist[0].keys())
    print("-"*100)
    print("STUDENT LIST".center(100))
    print("-"*100)
    [print(f"{head.upper():>15}",end=" ") for head in header]
    print()
    print("-"*100)
    for student in slist:
        print(f"{student['idno']:>15}",end=" ")
        print(f"{student['lastname']:>15}",end=" ")
        print(f"{student['firstname']:>15}",end=" ")
        print(f"{student['course']:>15}",end=" ")
        print(f"{student['level']:>15}",end=" ")
        print()
    print("-"*100)
    print("Nothing Follows".center(100))   

    