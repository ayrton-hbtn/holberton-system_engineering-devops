#!/usr/bin/python3
"""using the JSONPlaceholder API"""


if __name__ == "__main__":
    import requests as req
    from sys import argv
    import csv
    todos = req.get('https://jsonplaceholder.typicode.com/todos').json()
    users = req.get('https://jsonplaceholder.typicode.com/users').json()
    user = {}
    for elem in users:
        if elem["id"] == int(argv[1]):
            user = dict(elem)
            break
    user_todos = []
    for elem in todos:
        if elem["userId"] == int(argv[1]):
            user_todos.append(dict(elem))
    export_to_cvs = []
    for elem in user_todos:
        line = []
        line.append(argv[1])
        line.append(user["username"])
        if elem["completed"]:
            line.append(True)
        else:
            line.append(False)
        line.append(elem["title"])
        export_to_cvs.append(line)
    with open('{}.csv'.format(argv[1]), 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for line in export_to_cvs:
            writer.writerow(line)
