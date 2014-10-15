#!/usr/bin/env python
from random import randint

def __main__():

    f = open('./lottery.list')
    name_list = f.readlines()

    winnerSet = set()
    while( len(winnerSet) < 2):
        winnerSet.add(randint(0,4))
    
    result = 'The winner is '
    
    for index in winnerSet:
        result += name_list[index].strip() + ' '

    print result

if __name__ == '__main__':
    __main__()
