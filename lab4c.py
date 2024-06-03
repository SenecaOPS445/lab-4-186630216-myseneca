#!/usr/bin/env python3
#Author: Eliza Silvetsre
#Author ID: esilvestre
#File name: lab4c.py
#Date Created: June 3, 2024

# Dictionaries

dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}

# Lists

list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below
    a = 0
    result = {}
    while a < len(keys):
        result[keys[a]] = values[a]
        a += 1
    return result

def shared_values(dict1, dict2):
    # Place code here - refer to function specifics in section below
    s1 = set(dict1.values())
    s2 = set(dict2.values())
    return set(dict1.values()) & set(dict2.values())

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)