# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:04:29 2020

@author: mchoubey
"""
letters = {'a':'apple', 'b':'bat', 'c':'cat', 'd':'dog'}
for x in letters:
    print(x, "for", letters[x])
letters['e']='elephant'
print(letters)


phone = {
        'andy':'1111',
        'bob':'2222',
        'charl':'3333'
        }
phone['doug'] = '4444'
for key, value in phone.items():
    print(key, "---", value)
    
#for key, value in phone.items():
#    user_input = input('Enter name:-')
#    if user_input == 'done':
#       break
        
#    print([phone[user_input]])
    
music = {
        'Jazz':['song1', 'song2', 'song3'],
        'electronic': ['song1', 'song2', ['edm1', 'edm2', 'edm3']]
        }
music.update(phone)
print(music)
   

x = {'a':'apple', 'b':'berry', 'c':'cherry'}  
x.update({'l':'lemon'})
print(x)
    
    
