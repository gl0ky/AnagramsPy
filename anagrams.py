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
        string_2_sorted = stringSorter(string_2)

        if (stringComparer(string_1_sorted, string_2_sorted) == True):

            print("los strings son anagramas")
        
        elif (stringComparer(string_1_sorted, string_2_sorted) == False):

            print("los strings no son anagramas")

def usage():

    print(f"Usage: {sys.argv[0]} ejemplo string 1 ejemplo string 2")

def main():

    if len(sys.argv) > 3:
        print("Debes poner dos strings como maximo para la comparacion..")
        usage()
        sys.exit(1)

    if len(sys.argv) < 3:
        print("Debes poner dos strings como minimo para la comparacion..")
        usage()
        sys.exit(1)

    if len(sys.argv) == 3:
        anagrams(sys.argv[1], sys.argv[2])
        sys.exit(0)


if __name__ == '__main__':
    main();