#!/usr/bin/python3
""" Gather data from an api"""
import requests
import sys


def employee_data(emp_id):
    """ Returns information about employee TODO list progress"""
    url_home = "https://jsonplaceholder.typicode.com"
    url_todo = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    url_usr = f"https://jsonplaceholder.typicode.com/users/{emp_id}"

    # user info
    user_data = requests.get(url_usr).json()
    name = user_data.get('name')
    # todo list
    todo_data = requests.get(url_todo).json()
    total_tasks = len(todo_data)
    complete = [todo for todo in todo_data if todo['completed']]
    completed = len(complete)
    print(f"Employee {name} is done with tasks({completed}/{total_tasks}):")
    for todo in complete:
        print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: <employees_id>")
        sys.exit(1)

    emp_id = int(sys.argv[1])
    employee_data(emp_id)
