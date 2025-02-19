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
default_values = {"id":1,"description":sys.argv[2], "createdAt":currentTime, "updatedAt":currentTime}





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


if sys.argv[1] == "add":
    add()

