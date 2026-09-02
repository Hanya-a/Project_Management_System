# Project Management REST API

**Python • Django • Django REST Framework • JWT**

## 1. Project Overview

The Project Management REST API is a Django REST Framework application designed to allow authenticated users to create and manage projects and tasks while enforcing ownership, authentication, authorization, and data isolation.

The API supports:

* User registration and JWT authentication
* Project CRUD operations
* Task CRUD operations
* Task assignment
* Multiple tags for tasks
* Validation
* Filtering
* Searching
* Ordering
* Pagination
* Authentication and authorization
* Automated testing
* Postman API testing

The project follows a RESTful API structure and uses Django's ORM for database operations.

## 2. Technologies Used

* Python
* Django
* Django REST Framework
* Simple JWT
* django-filter
* SQLite
* Postman
* Git

## 3. Project Structure

```text
Project_Management_System/
│
├── authentication/
│   ├── migrations/
│   ├── serializers/
│   │   ├── LoginSerializer.py
│   │   ├── LogoutSerializer.py
│   │   └── RegisterSerializer.py
│   ├── views/
│   │   ├── LoginView.py
│   │   ├── LogoutView.py
│   │   └── RegisterView.py
│   ├── tests.py
│   └── urls.py
│
├── project_manager/
│   ├── migrations/
│   ├── models/
│   │   ├── ProjectModel.py
│   │   ├── TagModel.py
│   │   └── TaskModel.py
│   ├── serializers/
│   │   ├── ProjectSerializer.py
│   │   ├── TagSerializer.py
│   │   └── TaskSerializer.py
│   ├── views/
│   │   ├── ProjectView.py
│   │   └── TaskView.py
│   ├── pagination.py
│   └── tests.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── .env.example
├── .gitignore
├── manage.py
├── main.py
├── requirements.txt
└── README.md
```

## 4. Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/Hanya-a/Project_Management_System.git
cd Project_Management_System
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows:**

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Environment Variables

Create a `.env` file in the project root using `.env.example` as a reference.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

The `.env.example` file demonstrates the expected environment variables without containing real secrets.

The actual `.env` file is excluded from Git using `.gitignore` and must not be committed to the repository.

## 6. Database Migrations

Apply the existing migrations:

```bash
python manage.py migrate
```

To create new migrations after modifying models:

```bash
python manage.py makemigrations
```

Then apply them:

```bash
python manage.py migrate
```

## 7. Running the Server

Start the Django development server:

```bash
python manage.py runserver
```

The API can then be accessed through the Django development server.

## 8. Authentication

The API uses JWT authentication.

Protected requests must include:

```text
Authorization: Bearer <access_token>
```

### Register

**POST**

```text
/authentication/register/
```

Example request:

```json
{
    "username": "john",
    "email": "john@example.com",
    "password": "password123"
}
```

### Login

**POST**

```text
/authentication/login/
```

Example request:

```json
{
    "username": "john",
    "password": "password123"
}
```

A successful login returns:

```json
{
    "username": "john",
    "access": "access_token",
    "refresh": "refresh_token"
}
```

### Refresh Token

**POST**

```text
/authentication/token/refresh/
```

Example request:

```json
{
    "refresh": "refresh_token"
}
```

The refresh endpoint returns a new access token.

### Logout

**POST**

```text
/authentication/logout/
```

Example request:

```json
{
    "refresh": "refresh_token"
}
```

The refresh token is blacklisted when the user logs out.

## 9. Authorization and Data Isolation

Project and task endpoints are protected using DRF authentication permissions.

### Projects

Each project belongs to one user through the `owner` field.

The owner is automatically assigned using the authenticated user when a project is created.

The client cannot choose the project owner through the request body.

Users can only access projects that they own.

### Tasks

Each task belongs to a project and records the user who created it.

The `created_by` field is automatically assigned from the authenticated user.

A user can access a task if:

* They own the project associated with the task, or
* They are assigned to the task.

A task cannot be created under a project owned by another user.

## 10. Project API

### List Projects

**GET**

```text
/project_manager/projects/
```

Returns projects owned by the authenticated user.

### Create Project

**POST**

```text
/project_manager/projects/
```

Example:

```json
{
    "name": "Website Development",
    "description": "Development of a new company website."
}
```

The project owner is automatically assigned from the authenticated user.

### Project Detail

**GET**

```text
/project_manager/projects/{id}/
```

### Full Project Update

**PUT**

```text
/project_manager/projects/{id}/
```

### Partial Project Update

**PATCH**

```text
/project_manager/projects/{id}/
```

### Delete Project

**DELETE**

```text
/project_manager/projects/{id}/
```

## 11. Task API

### List Tasks

**GET**

```text
/project_manager/tasks/
```

Returns tasks that the authenticated user is authorized to access.

### Create Task

**POST**

```text
/project_manager/tasks/
```

Example:

```json
{
    "title": "Implement authentication",
    "description": "Add JWT authentication to the API.",
    "project": 1,
    "status": "TODO",
    "priority": "HIGH",
    "assigned_to": 2,
    "due_date": "2026-09-15T18:00:00Z",
    "completed": false
}
```

The `created_by` user is automatically assigned from the authenticated user.

### Task Detail

**GET**

```text
/project_manager/tasks/{id}/
```

### Full Task Update

**PUT**

```text
/project_manager/tasks/{id}/
```

### Partial Task Update

**PATCH**

```text
/project_manager/tasks/{id}/
```

### Delete Task

**DELETE**

```text
/project_manager/tasks/{id}/
```

## 12. Tags

Tasks support multiple tags through a Django `ManyToManyField` relationship.

This allows:

* One task to have multiple tags.
* One tag to be associated with multiple tasks.

Tags are managed administratively rather than being created or modified by regular users. This provides a controlled set of available tags while allowing the system to be extended with more advanced or automatic tag selection in the future.

## 13. Status and Priority

Tasks use controlled choices for status and priority.

### Status

* `TODO`
* `IN_PROGRESS`
* `DONE`

### Priority

* `LOW`
* `MEDIUM`
* `HIGH`

Only the defined choices are accepted.

## 14. Validation

The API validates incoming data and returns clear validation errors.

Validation includes:

* Project names cannot be empty.
* Task titles cannot be empty.
* Status values must use the allowed choices.
* Priority values must use the allowed choices.
* Date fields must use valid formats.
* Tasks cannot be created under projects owned by another user.
* Project ownership cannot be selected or changed through the request body.

Invalid input returns:

```text
400 Bad Request
```

## 15. Filtering

The task endpoint supports filtering by:

* `status`
* `priority`
* `completed`
* `project`

Examples:

```text
/project_manager/tasks/?status=DONE
```

```text
/project_manager/tasks/?priority=HIGH
```

```text
/project_manager/tasks/?completed=true
```

```text
/project_manager/tasks/?project=1
```

## 16. Searching

Tasks can be searched by title using the `search` query parameter.

Example:

```text
/project_manager/tasks/?search=django
```

## 17. Ordering

Tasks can be ordered using:

* `created_at`
* `due_date`

Example:

```text
/project_manager/tasks/?ordering=-created_at
```

A `-` before the field indicates descending order.

## 18. Pagination

The task list endpoint uses DRF `PageNumberPagination`.

The default page size is **8** tasks, with a maximum page size of **10**.

Example:

```text
/project_manager/tasks/?page=1&page_size=10
```

The paginated response contains metadata such as:

* `count`
* `next`
* `previous`
* `results`

## 19. HTTP Status Codes

| Status Code | Meaning                                  |
| ----------- | ---------------------------------------- |
| 200         | Successful request                       |
| 201         | Resource successfully created            |
| 204         | Successful request with no response body |
| 400         | Invalid request or validation error      |
| 401         | Authentication required or invalid       |
| 403         | Authenticated but not authorized         |
| 404         | Resource not found or not accessible     |
| 500         | Unexpected server error                  |

## 20. Error Handling

The API returns meaningful error responses for invalid requests.

Example:

```json
{
    "title": [
        "Task title cannot be empty."
    ]
}
```

Authentication errors may return:

```json
{
    "detail": "Authentication credentials were not provided."
}
```

## 21. Testing

Automated tests are included in the project.

Run the test suite with:

```bash
python manage.py test
```

Testing covers important API behavior including:

* User registration
* Login
* Invalid credentials
* Authentication requirements
* Project CRUD operations
* Project ownership and authorization
* Task creation
* Task validation
* Task authorization
* Filtering
* Searching
* Ordering
* Pagination
* Permission cases

## 22. Postman Collection

A Postman Collection named **Project_Manager** is included with the project.

The collection is organized into:

### Authentication

* Register — valid
* Register — missing required field
* Login — valid credentials
* Login — invalid credentials
* Refresh Token

### Projects

* Create project for owner 1
* Create project with whitespace-only name
* Update project

### Tasks

* Create valid task
* Create task with invalid status
* Retrieve task

### Authorization

* List projects as owner 1
* List projects as owner 2

### Filtering

* Filter by completed
* Filter by priority

### Ordering

* Order by `created_at`

### Searching

* Search by title

### Pagination

* Task pagination

The collection contains successful requests as well as important validation and authorization cases.

## 23. Git Version Control

The project is maintained using Git and hosted on GitHub.

The repository includes:

* `.gitignore`
* `.env.example`
* `requirements.txt`
* Database migrations
* Django source code
* Automated tests
* README documentation
* Git commit history

Sensitive configuration files such as `.env` and local virtual environment files are excluded from version control.

## 24. Security

The API implements several security and authorization measures:

* JWT authentication
* Protected project and task endpoints
* Project ownership enforcement
* Task authorization
* Django password hashing
* Environment variables for sensitive configuration
* `.gitignore` protection for secrets
* User-specific queryset filtering

The API does not expose all users' private project data through unrestricted querysets.

## 25. Development Notes

This project was developed as part of an internship backend development task.

The implementation focuses on understanding Django, Django REST Framework, serializers, ViewSets, routers, authentication, authorization, database relationships, validation, filtering, searching, ordering, pagination, testing, and API design.
