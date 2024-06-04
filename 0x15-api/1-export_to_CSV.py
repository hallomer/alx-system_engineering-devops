#!/usr/bin/python3
"""
Uses a REST API to retrieve information about
an employee's TODO list progress, and exports the data in CSV format.
"""
from sys import argv
import csv
import requests


if __name__ == "__main__":
    employee_id = int(argv[1])
    base_url = 'https://jsonplaceholder.typicode.com/'
    # Fetch employee data
    user_response = requests.get(f"{base_url}users/{employee_id}")
    user_data = user_response.json()
    # Fetch TODO list data
    todos_response = requests.get(f"{base_url}todos?userId={employee_id}")
    todos_data = todos_response.json()

    username = user_data.get('username')

    # CSV filename
    filename = f"{employee_id}.csv"

    # Write to CSV
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': username,
                'TASK_COMPLETED_STATUS': task.get('completed'),
                'TASK_TITLE': task.get('title')
            })
