#!/usr/bin/python3
"""using the JSONPlaceholder API"""


if __name__ == "__main__":
    import requests as req
    from sys import argv
    import json
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
    for elem in todos:
        if elem["userId"] == int(argv[1]):
            user_todos.append(dict(elem))
    for elem in user_todos:
        del elem['userId']
        del elem['id']
        elem['username'] = user['username']
    user_todos_export_json = {}
    user_todos_export_json[argv[1]] = user_todos
    with open("{}.json".format(argv[1]), "w") as f:
        json.dump(user_todos_export_json, f)
