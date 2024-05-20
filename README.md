## This is a simple task management application that performs CRUD functions.
If you are not set up on using Python Flask, take the following steps to get started.

## Installations and setup
- Go to https://www.python.org/downloads/ to download the latest Python version
- Install Pip, the package installer for Python using the command python get-pip.py for Linux or MacOs and C:> py get-pip.py for Windows
- Install PostgreSQL database and create a database server

I provided my virtual environment if you want to run it exactly like I did, otherwise proceed with creating your virtual environment.
- To install virtual environment, use the command python3 -m venv .venv for MacOs and py -m venv .venv for Windows.
- If you face any error run the following command below then try the previous command again:
-- virtualenv --system-site-packages -p python ./env
-- Set-ExecutionPolicy Unrestricted -Scope Process
- Create a virtual environment python -m venv env
- Enter the environment using the command source env/bin/activate for Linux or MacOs and .\env\Scripts\activate
- After entering the virtual environment, install the dependencies by running pip install -r requirements.txt
- Initialise the database using the command flask db init

Run the migration file to update the database using the command flask db upgrade
Run the application using python app.py

## APIs

SignUp
#### Request: `POST http://127.0.0.1:5000/signup`
Json Body:
`
{
    "password": "password123",
    "email": "ayara.faith@gmail.com"
}
`

#### Response:
`
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjE5OTE3NSwianRpIjoiOThjZDM2NjgtOWEyZS00ODEzLWI2NTItZmUzYWM5MmRlZjQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTgwMywibmJmIjoxNzE2MTk5MTc1LCJjc3JmIjoiOTUxZWFjZDgtYjk2Zi00M2Y3LWI1ZTQtYmE3MzdjYzc1MWEzIiwiZXhwIjoxNzE2MjAwMDc1fQ.zJU5K11f3tQWH3QoxITHjXEipawmsbe6UqJjaSgAfxs",
    "msg": "Welcome, your user ID is 1803. Kindly keep it somewhere save as this is required for login"
}
`


Login
#### Request: `POST http://127.0.0.1:5000/login`
Json Body:
`
{
    "user_id": "1803",
    "password": "password123"
}
`

#### Response:
`
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjIwMTc5NywianRpIjoiNzkzMmUzY2MtOWVmYy00NGY5LWE1OTItOTlhNDM4ZmY0MWJmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjE4MDMiLCJuYmYiOjE3MTYyMDE3OTcsImNzcmYiOiI5NDA0NDM4Yy0zNzQyLTQ1ODctOWIzMi1lNmY4OTc5YTc0YWUiLCJleHAiOjE3MTYyMDI2OTd9.WHBWDXNLRPzYDKxPvRUUmxlyNm6rO5vBpRFXzFg4AGY"
}
`


## Home
#### Request: `GET http://127.0.0.1:5000/home`
#### Response:

`
{
    "msg": "Welcome, create new tasks"
}
`

## NewTask
#### Request: `POST http://127.0.0.1:5000/new`
Json Body:

`
{
    "task_title": "Test Task",
    "task": "Complete this assessment",
    "due_date": "20-05-2024"
}
`

#### Response:

`
{
    "msg": "Task added succesfully"
}
`

## ListTasks
#### Request: `GET http://127.0.0.1:5000/tasks`
#### Response:

`
{
    "msg": {
        "id": 1236,
        "task": "Test Task"
    }
}
`


## GetTask
#### Request: `GET http://127.0.0.1:5000/tasks/1236`
#### Response:

`
{
    "msg": {
        "due_date": "20-05-2024",
        "task": "Complete this assessment",
        "title": "Test Task"
    }
}
`


## UpdateTask
#### Request: PUT `http://127.0.0.1:5000/tasks/1236/update`
Json Body:

`
{
    "task": "New Task",
    "due_date": "21-05-2024"
}
`
#### Response:

`
{
    "msg": "Task 1236 updated successfully"
}
`

## DeleteTask
#### Request: `PUT http://127.0.0.1:5000/tasks/1236/delete`
#### Response:

`
{
    "msg": "Task 1236 deleted successfully"
}
`

