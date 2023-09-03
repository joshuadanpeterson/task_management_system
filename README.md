
# Portfolio Project: Task Management System

## Project Description

The Task Management System is a web application that allows users to manage, track, and organize their tasks. The application provides user authentication features, enabling users to register, log in, and manage their own tasks. Tasks can be created, edited, viewed in detail, and deleted. This system is designed as a portfolio project for the "Modern Software Engineering with DevOps" course.

## Technologies Used

- **Python**: The main programming language used for developing this application.
- **Django**: A high-level Python Web framework that enables rapid development of secure and maintainable websites.
- **Django ORM**: Provides a way to define and manipulate databases in Python code, rather than using SQL.
- **PostgreSQL**: The database used by this project.
- **Docker**: A platform used to develop, ship, and run applications inside containers.
- **HTML**: Markup language for creating web pages.
- **CSS**: Style sheet language for stylizing web pages.

## Installation & Setup

To run the Task Management System, you should have both Docker and Docker Compose installed on your machine. Follow the steps below to set up the application:

1. Clone the GitHub repository:
```bash
git clone https://github.com/joshuadanpeterson/task_management_system.git
```

2. Navigate to the project directory:
```bash
cd path_to_directory
```

3. Use Docker Compose to build and run the application:
```bash
docker-compose build
docker-compose up -d
docker compose exec web python manage.py migrate
```

The application should now be accessible at `http://localhost:8000/`.

## Key Project Details

|   Title     |               Details            |
|-------------|----------------------------------|
| Bootcamp    | Nucamp                           |
| Course      | Modern Software Engineering with DevOps |
| Due Date    | August 19, 2023                  |
| Project Author    | Josh Peterson              |

