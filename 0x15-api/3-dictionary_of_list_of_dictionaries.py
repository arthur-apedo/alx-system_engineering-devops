#!/usr/bin/python3
""" Gather data from an api"""
import csv
import json
import requests


def employee_data():
    """ Returns information about employee TODO list progress"""
    url_home = "https://jsonplaceholder.typicode.com"
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    url_usr = "https://jsonplaceholder.typicode.com/users"

    # all users info
    user_data = requests.get(url_usr).json()
    # name = user_data.get('username')
    # todo list
    todo_data = requests.get(url_todo).json()
    # total_tasks = len(todo_data)
    # complete = [todo for todo in todo_data if todo['completed']]
    # completed = len(complete)
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

    # all employees data
    dataset = {}
    for user in user_data:
        user_id = user['id']
        username = user['username']
        usr_todos = [todo for todo in todo_data if todo['userId'] == user_id]
        user_todo_format = [
                {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                for todo in usr_todos
            ]
        dataset[user_id] = user_todo_format
    return dataset


def to_json(dataset):
    """ Returns a json formatting"""
    filename = "todo_all_employees.json"
    with open(filename, 'w', newline='') as f:
        json.dump(dataset, f)


if __name__ == "__main__":
    usr_data = employee_data()
    to_json(usr_data)
