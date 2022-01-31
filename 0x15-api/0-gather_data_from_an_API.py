#!/usr/bin/python3
"""using the JSONPlaceholder API"""


if __name__ == "__main__":
    import requests as req
    from sys import argv
    todos = req.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    users = req.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()
    user = {}
    for elem in users:
        if elem["id"] == int(argv[1]):
            user = dict(elem)
            break
    user_todos = []
    user_todos_compl = []
    completed_tasks = 0
    for elem in todos:
        if elem["userId"] == int(argv[1]):
            user_todos.append(dict(elem))
            if elem["completed"]:
                completed_tasks = completed_tasks + 1
                user_todos_compl.append(dict(elem))
    total_tasks = len(user_todos)
    print("Employee {} is done with tasks ({}/{}):"
          .format(user["name"], completed_tasks, total_tasks))
    for task in user_todos_compl:
        print("\t{}".format(task["title"]))
