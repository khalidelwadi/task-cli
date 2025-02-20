from datetime import datetime
import json
import os
import sys

# get the time now and assign the value to currentTime
now = datetime.now()
currentTime = now.strftime("%D:%H:%M:%S")

# Specify the name of the json file i'm going to work with
mypath = "/home/kw9/task-cli/task_cli.json"

# set a default value for dict key/values that are not going to change
try:
    default_values = {"id":1,"description":sys.argv[2], "createdAt":currentTime, "updatedAt":currentTime}
except Exception:
    pass




def add():
    if os.path.isfile(mypath) != True:
        with open("task_cli.json", "w") as json_file:
            # add status to the end of the dictionnary
            default_values["status"] = "Not done"
            # add the dict to the json file with a new line at the end
            json_file.write(f'{default_values}\n')
           
    else:
        with open("task_cli.json", "r+") as json_file:
            default_values["status"] = "Not done"

            # reads how many line are in the json file
            default_values["id"] = len(json_file.readlines()) + 1
            json_file.write(f'{default_values}\n')


def update():
    empty_dict = []
    with open("task_cli.json", "r+") as json_file:
            for i in json_file.readlines():
                b = eval(i)
                if str(b["id"]) == sys.argv[2]:
                    b["description"] = sys.argv[3]
                    b["updatedAt"] = currentTime
                    empty_dict.append(b)
                    
                    
                else :
                    empty_dict.append(b)
    with open("task_cli.json", "w") as json_file :
        for i in empty_dict:
            json_file.write(f'{i}\n')


def delete():
    saved_dict = []
    with open("task_cli.json", "r") as json_file :
        for i in json_file.readlines():
            b = eval(i)
            if str(b["id"]) == sys.argv[2]:
                continue
            saved_dict.append(i)
    with open("task_cli.json", "w") as json_file :
        for i in saved_dict:
            json_file.write(f'{i}')

def mark_in_progress():
    saved_dict = []
    with open("task_cli.json", "r+") as json_file:
        for i in json_file.readlines():
            b = eval(i)
            if str(b["id"]) == sys.argv[2]:
                b["status"] = "In progress"
                saved_dict.append(b)
            else :
                saved_dict.append(b)
    with open("task_cli.json", "w") as json_file :
        for i in saved_dict:
            json_file.write(f'{i}\n')


def mark_done():
    saved_dict = []
    with open("task_cli.json", "r+") as json_file:
        for i in json_file.readlines():
            b = eval(i)
            if str(b["id"]) == sys.argv[2]:
                b["status"] = "Done"
                saved_dict.append(b)
            else :
                saved_dict.append(b)
    with open("task_cli.json", "w") as json_file :
        for i in saved_dict:
            json_file.write(f'{i}\n')

def list_item(stat = None):
    with open("task_cli.json", "r+") as json_file:
        for i in json_file.readlines():
            b = eval(i)
            if stat == "done" and b["status"] == "Done":
                print(b)
                
            elif stat == "in-progress" and b["status"] == "In progress":
                print(b)
                
            elif stat == "todo" and b["status"] == "Not done":
                print(b)
                
            elif stat == None:
                print(b)
            


if sys.argv[1] == "add":
    add()
elif sys.argv[1] == "update":
    update()
elif sys.argv[1] == "delete":
    delete()
elif sys.argv[1] == "mark-in-progress":
    mark_in_progress()
elif sys.argv[1] == "mark-done":
    mark_done()

if len(sys.argv) > 2:
    if  sys.argv[1] == "list" and (sys.argv[2] == "done" or sys.argv[2] == "todo" or sys.argv[2] == "in-progress"):
        list_item(sys.argv[2])
    
elif sys.argv[1] == "list":
     list_item()
     


