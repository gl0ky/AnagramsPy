#!/bin/python3
import sys
import os

def stringSorter(string):

    string = string.strip(" ")
    string = string.lower()
    txt = sorted(string)
    txt = ''.join(txt)
    return txt

def stringComparer(string_1, string_2):

    if(string_1 == string_2):

        return True
    
    elif(string_1 != string_2):

        return False

def anagrams(string_1, string_2):

    if string_1 == string_2:

        print ("Los strings son iguales...")
    
    else:

        string_1_sorted = stringSorter(string_1)
        string_1_sorted = stringSorter(string_1)


def usage():

    print(f"Usage: {sys.argv[0]} ejemplo string 1 ejemplo string 2")

def main():

    print(stringSorter("Claudio Garcia"))

if __name__ == '__main__':
    main();