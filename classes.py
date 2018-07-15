#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self , **kwargs):
        self.varibles = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def set_variables(self , k , v):
        self.varibles[k] = v

    def get_variables(self , k):
        return self.varibles.get(k , None)

def main():
    donald = Duck(feet = 2)
        print(donald.get_variables('feet'))

if __name__ == "__main__": main()
