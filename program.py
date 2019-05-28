#Initializing file

import sys
import threading
import os

cwd = os.getcwd()
choice = input("The data store will be created in the Current Working Directory - '"+cwd+"\mydatastore.txt'\nPress 'y' to continue or 'n' to Enter your desired path\n")
if choice is 'y' or choice is 'Y':
    path = cwd + '\mydatastore.txt'
    f = open(path,"w")
else:
    path = input("Enter the Absolute path of your desired location")
    path = path + '\mydatastore.txt'
    f = open(path,'w')
f.close()
print("Data Store successfully created!")

#deletes a specific record with given key

def delete(key):
    present = False
    with open(path,"r") as f:
        lines = f.readlines()
    with open(path,"w") as f:
        for line in lines:
            first = line.split(" ")[0]
            if first != key:
                f.write(line)
            elif first == key:
                present = True
                print("\nRecord '"+key+"' Deleted successfully!\n")
    if not present:
        print("\nNo Record Found with the key '"+key+"'\n")
        
        #creates a new record

def create(key,value,ttl=-1):
    present = False
    limit = True
    if len(key)>32 or sys.getsizeof(value)>16000:
        limit = False
    with open(path,'r') as f:
        searchlines = f.readlines()
        phrase = key + " -"
        for line in searchlines:
            if phrase in line:
                present = True
    if not present and limit:
        with open(path,'a') as f:
            f.write(key + ' - ' + value + '\n')
            print("\nRecord created successfully!\n")
        if ttl>-1:
            t = threading.Timer(ttl,delete,[key])
            t.start()
    elif not limit:
        print("\nParameter(s) exceed limit\n")
    elif present:
        print("\nRecord with '"+key+"' already exists.\n")
        
  #retrieves a specific record with a given key

def read(key):
    with open(path,'r') as f:
        searchlines = f.readlines()
        phrase = key + " -"
        for line in searchlines:
            if phrase in line:
                print(line)
                break
        else:
            print("\nNo Record Found with the key '"+key+"'\n")
            
print("\n\n**** You can try 3 commands ****\n\n")
print("1. create(key , value , <time to live> )\n2. read(key)\n3. delete(key)\n4.exit()\n")
running = True
while(running):
    cmd = input('Enter Command ')
    cmd = cmd.split("(")
    if cmd[0] == 'create':
        temp = cmd[1].split('{')
        key = temp[0].split(',')[0]
        value = '{' + temp[1].split('}')[0] + '}'
        ttl = int(temp[1].split(',')[-1].split(')')[0])
        if len(cmd)==2:
            create(key,value)
        elif len(cmd)==3:
            create(key,value,ttl)
    elif cmd[0] == 'read':
        cmd = cmd[1].split(')')
        read(cmd[0])
    elif cmd[0] == 'delete':
        cmd = cmd[1].split(')')
        delete(cmd[0])
    elif cmd[0] == 'exit':
        running = False
    else:
        print("Enter Valid Command!")
