#!/usr/bin/python3
"""
Uses a REST API to retrieve information about about
all employees' TODO list progress, and exports the data in JSON format
as a dictionary of lists of dictionaries.
"""
import json
import requests

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'
    # Fetch all users data
    users_response = requests.get(f"{base_url}users")
    users_data = users_response.json()

    all_tasks = {}
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')

        # Fetch TODO list data for each user
        todos_response = requests.get(f"{base_url}todos?userId={user_id}")
        todos_data = todos_response.json()
        tasks = []
        for task in todos_data:
            tasks.append({
                'username': username,
                'task': task.get('title'),
                'completed': task.get('completed')
            })
        all_tasks[user_id] = tasks

    # JSON filename
    filename = "todo_all_employees.json"

    # Write to JSON
    with open(filename, 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)
