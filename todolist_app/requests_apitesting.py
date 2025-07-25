import requests

task_data = {
    "title": "Learn REST API",
    "description": "Practice Flask and requests module",
    "deadline": "2025-08-01",
    "completed": False
    }

response = requests.post("http://127.0.0.1:5000/tasks", json=task_data)
print(response.status_code)
print(response.json())

response = requests.get("http://127.0.0.1:5000/tasks")
print(response.status_code)
print(response.json())

task_id = 24
response = requests.get(f"http://127.0.0.1:5000/tasks/{task_id}")
print(response.status_code)
print(response.json())


task_id = 24
updated_task={
    "title": "updated task",
    "description": "updated description",
    "deadline": "2025-08-10",
    "completed" : True
    }

response = requests.put(f"http://127.0.0.1:5000/tasks/{task_id}", json=updated_task)
print(response.status_code)
try:
    print(response.json())
except Exception as e:
    print("Error parsing json", response.text)


task_id = 23
response = requests.delete(f"http://127.0.0.1:5000/tasks/{task_id}")
print(response.status_code)
print(response.json())
