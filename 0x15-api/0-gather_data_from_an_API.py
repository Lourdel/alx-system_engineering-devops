#!/usr/bin/python3
"""
 script that returns information about employee TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user_id = int(argv[1])
        url = "https://jsonplaceholder.typicode.com/users/"
        response = requests.get("{}/{}".format(url, user_id))
        nem = response.json().get("name")
        if nem is not None:
            tasks = requests.get("{}{}/todos".format(url, user_id))
            tasks = tasks.json()
            n_tk = len(tasks)
            taskscompleted = []
            for task in tasks:
                if task.get("completed") is True:
                    taskscompleted.append(task)
            n_cp = len(taskscompleted)
            print("Employee {} is done with tasks({}/{}):". format(nem,
                                                                   n_cp, n_tk))
            for task in taskscompleted:
                title = task.get("title")
                print("\t {}".format(title))
