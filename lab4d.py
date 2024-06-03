#!/usr/bin/env python3
#Author: Eliza Silvetsre
#Author ID: esilvestre
#File name: lab4d.py
#Date Created: June 3, 2024
#Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(f5):
    # Place code here - refer to function specifics in section below
    return f5[:5]

def last_seven(l7):
    # Place code here - refer to function specifics in section below
    return l7[-7:]

def middle_number(mnum):
    # Place code here - refer to function specifics in section below
    return str(mnum)[1:3]

def first_three_last_three(a1, a2):
    # Place code here - refer to function specifics in section below
    return a1[:3] + a2[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
