#!/usr/bin/env python3
#Author: Eliza Silvetsre
#Author ID: esilvestre
#File name: lab4a.py
#Date Created: June 3, 2024


s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

def join_sets(s1, s2):
    # join_sets will return a set that contains every value from both s1 and s2
    return (s1 | s2)

def match_sets(s1, s2):
    # match_sets will return a set that contains all values found in both s1 and s2
    return (s1 & s2)

def diff_sets(s1, s2):
    # diff_sets will return a set that contains all different values which are not shared between the sets
    return (s1 ^ s2)

if __name__ == '__main__':
    set1 = set(range(1,10))
    set2 = set(range(5,15))
    print('set1: ', set1)
    print('set2: ', set2)
    print('join: ', join_sets(set1, set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))