2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 21:59:07 2021

@author: Tom Marvollo Riddle
"""
def choice():
    print("\n1.Check Prime\n2.Armstrong\n3.Factorial\n4.Function Info\n5.Exit")
    ch_oice = int(input("\nEnter your choice : "))
    print("\n")
    return ch_oice
def condition(ch):
    if ch == 1:
        checkprime()
    elif ch == 2:
        checkarm()
    elif ch == 3:
        checkfact()
    elif ch == 4:
        info()
    else:
        print("Thank you..")
def checkprime():
    check_prime = int(input("Enter number to check it is prime or not : "))
    if check_prime == 1:
        print("1 is neither prime nor composite.\n")
        print("---------------------------------\n")
    elif check_prime == 2:
        print("2 is even prime number.\n")
        print("---------------------------------\n")
    else:
        for i in range(3, check_prime):
            if check_prime % i == 0:
                print("Number entered is not prime.\n")
                print("---------------------------------\n")
                break
        else:
            print("prime number.")
            print("---------------------------------\n")
    cont_cp()
def cont_cp():
    con = int(input("1.Want to check more number ?\n2.Main menu\n3.Exit\nEnter your choice : "))
    if con == 1:
        checkprime()
    elif con == 2:
        repeat()
    else:
        print("Thank you..")
def checkarm():
    number = int(input("Enter number to check armstrong or not : "))
    csum = 0
    temp = number
    while temp > 0:
        cube = (temp % 10) ** 3
        csum = csum + cube
        temp = temp // 10
    if number == csum:
        print("Armstrong number\n")
        print("---------------------------------\n")
    else:
        print("Not armstrong number\n")
        print("---------------------------------\n")
    cont_ca()
def cont_ca():
    con = int(input("1.Want to check more number ?\n2.Main menu\n3.Exit\nEnter your choice : "))
    if con == 1:
        checkarm()
    elif con == 2:
        repeat()
    else:
        print("Thank you..\n")
        print("---------------------------------\n")
def checkfact():
    print("Enter number for factorial : ", end="")
    number = int(input())
    i = 1
    factorial = 1
    while i <= number:
        factorial = factorial * i
        i += 1
    print("Factorial of " + str(number) + " is " + str(factorial) + ".\n")
    print("---------------------------------\n")
    cont_cf()
def cont_cf():
    con = int(input("1.Want to check more number ?\n2.Main menu\n3.Exit\nEnter your choice : "))
    if con == 1:
        checkfact()
    elif con == 2:
        repeat()
    else:
        print("Thank you..\n")
        print("---------------------------------\n")
def repeat():
    ch = choice()
    condition(ch)
def info():
    print("function info :")
    print("\tchoice() :\n\t\tprints main menu and take users choice")
    print("\tcondition() :\n\t\ttake choice of user from choice() and checks condition and calls respective function")
    print("\tcheckprime() :\n\t\ttake number from user and checks it is prime or not special answer for 1 and 2")
    print("\tcont_XX() : [common for all cont]\n\t\task your want to check more number? or return to main menu or exit")
    print("\tcheckarm() :\n\t\ttake number from user and checks whether number is armstrong or not")
    print("\tcheckfact() :\n\t\ttake number from user and gives factorial of entered number")
    print("\trepeat() :\n\t\tif user want to check more number then cont_XX() will call it")
    cont_info()
def cont_info():
    con = int(input("1.Main menu\n2.Exit\nEnter your choice : "))
    if con == 1:
        repeat()
    else:
        print("Thank you..")
        print("---------------------------------\n")
repeat()
