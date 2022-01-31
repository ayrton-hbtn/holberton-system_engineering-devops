#!/usr/bin/python3
"""using the JSONPlaceholder API"""
import requests as req
from sys import argv


if __name__ == "__main__":
    user_id = int(argv[1])
    def get_user():
        """function to get user from json response, matching by 'id' from argv"""
        users = req.get('https://jsonplaceholder.typicode.com/users').json()
        user = {}
        for elem in users:
            if elem["id"] == user_id:
                user = dict(elem)
                break
        return user


    def get_todos():
        """function to get list of Employee's completed tasks"""
        user = get_user()
        todos = req.get('https://jsonplaceholder.typicode.com/todos').json()
        user_todos = []
        user_todos_compl = []
        completed_tasks = 0
        for elem in todos:
            if elem["userId"] == user_id:
                user_todos.append(dict(elem))
                if elem["completed"]:
                    completed_tasks = completed_tasks + 1
                    user_todos_compl.append(dict(elem))
        total_tasks = len(user_todos)
        print("Employee {} is done with tasks({}/{}):"
            .format(user["name"], completed_tasks, total_tasks))
        for task in user_todos_compl:
            print("\t {}".format(task["title"]))
    
    get_todos()
