#!/usr/bin/python3
""" Gather data from an api"""
import csv
import json
import requests
import sys


def employee_data(emp_id):
    """ Returns information about employee TODO list progress"""
    url_home = "https://jsonplaceholder.typicode.com"
    url_todo = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    url_usr = f"https://jsonplaceholder.typicode.com/users/{emp_id}"

    # user info
    user_data = requests.get(url_usr).json()
    name = user_data.get('username')
    # todo list
    todo_data = requests.get(url_todo).json()
    total_tasks = len(todo_data)
    complete = [todo for todo in todo_data if todo['completed']]
    completed = len(complete)
    """print(f"Employee {name} is done with tasks({completed}/{total_tasks}):")
    for todo in complete:
        print(f"\t {todo['title']}")"""

    # export to csv
    """filename = f"{emp_id}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todo_data:
            writer.writerow([emp_id, name,
            todo['completed'], todo['title']])"""
    return todo_data, user_data


def to_json(emp_id, todo_data, user_data):
    """ Returns a json formatting"""
    filename = f"{emp_id}.json"
    username = user_data.get('username')
    data = {
        emp_id: [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": username
            }
            for todo in todo_data
        ]
    }

    with open(filename, 'w', newline='') as f:
        json.dump(data, f)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: <employees_id>")
        sys.exit(1)

    emp_id = int(sys.argv[1])
    todo, usr_data = employee_data(emp_id)
    to_json(emp_id, todo, usr_data)
