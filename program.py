#Initializing file

import sys
import threading
import os

cwd = os.getcwd()
choice = input("The data store will be created in the Current Working Directory - '"+cwd+"\mydatastore.txt'\nPress 'y' to continue or 'n' to Enter your desired path\n")
if choice is 'y' or choice is 'Y':
    path = cwd + '\mydatastore.txt'
    f = open(path,"a")
else:
    path = input("Enter the Absolute path of your desired location ")
    path = path + '\mydatastore.txt'
    f = open(path,'a')
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
    size = True
    if os.path.getsize(path) > 1000000000:
        size = False
    if len(key)>32 or sys.getsizeof(value)>16000:
        limit = False
    with open(path,'r') as f:
        searchlines = f.readlines()
        phrase = key + " -"
        for line in searchlines:
            if phrase in line:
                present = True
    if not present and limit and size:
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
    elif not size:
        print("Data Store exceeds 1 GB")
        
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

print("\n\n**** You can try 4 commands ****\n\n")
print("1. create(key , value , <time to live> )\n2. read(key)\n3. delete(key)\n4.exit()\n")

running = True
while(running):
    cmd = input('Enter Command ')
    cmd = cmd.split(",",1)
    choice = cmd[0].split('(')
    key = choice[1]
    choice = choice[0]
    if choice == 'create':
        value = cmd[1].rsplit(')',1)[0]
        li = list(value)
        if li[-1] == '}':
            create(key,value)
        else:
            value = value.rsplit(',',1)
            ttl = int(value[1])
            value = value[0]
            create(key,value,ttl)
    elif choice == 'read':
        key = key.split(')')[0]
        read(key)
    elif choice == 'delete':
        key = key.split(')')[0]
        delete(key)
    elif choice == 'exit':
        running = False
    else:
        print("Enter Valid Command!")
