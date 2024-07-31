# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 18:12:08 2023

@author: Joseph Balbuena
"""
def num_to_french(num):
   if num == 0:
       return 'zero'
   if num == 1:
       return 'un'
   if num == 2:
       return 'duex'
   if num == 3:
       return 'trois'
   if num == 4:
       return 'quatre'
   if num == 5:
       return 'cinq'
   if num == 6:
       return 'six'
   if num == 7:
       return 'sept'
   if num == 8:
       return 'huit'
   if num == 9:
       return 'neuf'
   if num == 10:
       return 'dix'
   
def num_to_pinyin(num):
   if num == 0:
       return 'ling'
   if num == 1:
       return 'yi'
   if num == 2:
       return 'er'
   if num == 3:
       return 'san'
   if num == 4:
       return 'si'
   if num == 5:
       return 'wu'
   if num == 6:
       return 'liu'
   if num == 7:
       return 'qi'
   if num == 8:
       return 'ba'
   if num == 9:
       return 'jiu'
   if num == 10:
       return 'shi'
   
def num_to_english(num):
   if num == 0:
       return 'zero'
   if num == 1:
       return 'one'
   if num == 2:
       return 'two'
   if num == 3:
       return 'three'
   if num == 4:
       return 'four'
   if num == 5:
       return 'five'
   if num == 6:
       return 'six'
   if num == 7:
       return 'seven'
   if num == 8:
       return 'eight'
   if num == 9:
       return 'nine'
   if num == 10:
       return 'ten'
   
def english_to_num(word):
    if word == 'zero':
        return 0
    if word == 'one':
        return 1
    if word == 'two':
        return 2
    if word == 'three':
        return 3
    if word == 'four':
        return 4
    if word == 'five':
        return 5
    if word == 'six':
        return 6
    if word == 'seven':
        return 7
    if word == 'eight':
        return 8
    if word == 'nine':
        return 9
    if word == 'ten':
        return 10
    
def french_to_num(word):
    if word == 'zero':
        return 0
    if word == 'un':
        return 1
    if word == 'deux':
        return 2
    if word == 'trois':
        return 3
    if word == 'quatre':
        return 4
    if word == 'cinq':
        return 5
    if word == 'six':
        return 6
    if word == 'sept':
        return 7
    if word == 'huit':
        return 8
    if word == 'neuf':
        return 9
    if word == 'dix':
        return 10
    
def pinyin_to_num(word):
    if word == 'ling':
        return 0
    if word == 'yi':
        return 1
    if word == 'er':
        return 2
    if word == 'san':
        return 3
    if word == 'si':
        return 4
    if word == 'wu':
        return 5
    if word == 'liu':
        return 6
    if word == 'qi':
        return 7
    if word == 'ba':
        return 8
    if word == 'jiu':
        return 9
    if word == 'shi':
        return 10

def french_to_pinyin(word):
    if word == 'zero':
        return 'ling'
    if word == 'un':
        return 'yi'
    if word == 'duex':
        return 'er'
    if word == 'trois':
        return 'san'
    if word == 'quatre':
        return 'si'
    if word == 'cinq':
        return 'wu'
    if word == 'six':
        return 'liu'
    if word == 'sept':
        return 'qi'
    if word == 'huit':
        return 'ba'
    if word == 'neuf':
        return 'jiu'
    if word == 'dix':
        return 'shi'
    
def french_to_pinyin(french_to_num):
    num = french_to_num(num_to_french)
    pinyin_to_num = num_to_pinyin(num)
    return pinyin_to_num
    
'---------- main body ----------'

print( num_to_pinyin(3) ) 
print( french_to_num('sept') ) 


