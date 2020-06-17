# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:32:04 2020

@author: mchoubey
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 17:34:11 2020

@author: mchoubey
"""
hosts = open ('C:/Users/mchoubey/Desktop/rsvp')
content = hosts.read()  
print(content)
print(hosts.tell())
hosts.seek(0)  
print(hosts.tell())
print(hosts.read(100), hosts.tell())
hosts.close()

"""with supports opening file and closing automatically at the end """

print("starting to read the file")
with open('C:/Users/mchoubey/Desktop/temp.py') as file:
    print ('File closed?{}'.format(file.closed))
    print(file.read())
    print(file.tell())
    
"""We can use for to do line level operation"""
with open('C:/Users/mchoubey/Desktop/temp.py') as File:
    for line in File:
        print(line)
        print('***********************')

"""We can use rstrip to remove extra lines"""
with open('C:/Users/mchoubey/Desktop/temp.py') as File:
    for line in File:
        print(line.rstrip())
        print('***********************')
        
"""To write file, open with w"""
with open('C:/Users/mchoubey/Desktop/python_write', 'w') as file:
    file.write("This is trying to write file using python")
    file.write("New line with python")
  
    
with open('C:/Users/mchoubey/Desktop/python_write') as file:
    print(file.read())
    
with open('C:/Users/mchoubey/Desktop/python_write', 'w') as file:
    for i in range(100):
        file.write("This is trying to write file using python \n")
        file.write("New line with python ")
        j = str(i)
        file.write(j)
        file.write('\n')
  
    
with open('C:/Users/mchoubey/Desktop/python_write') as file:
    print(file.read())
    
try:
    code = open('C:/Users/mchoubey/Desktop/python_write').read()
except:
    code = "file open failed"
print(len(code))



        

        

    



