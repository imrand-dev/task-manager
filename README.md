<div align="center">
<h2>Task Management REST APIs</h2>

<img src="https://img.shields.io/badge/Python 3.12.0-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
<img src="https://img.shields.io/badge/Django 4.2.8-092E20?style=for-the-badge&logo=django&logoColor=green">
<img src="https://img.shields.io/badge/REST Framework 3.14.0-092E20?style=for-the-badge&logo=django&logoColor=red">

</div>

## Technologies

* Django for the backend application structure and ORM.
* Django Rest Framework for RESTful APIs.
* [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) for API authentication.
* [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/) for API endpoints schema.
* Git & GitHub for project version management.
* PostgreSQL database for storing data.
* Django templates, CSS, and Bootstrap for the frontend.
* Hosted photos on [Cloudinary](https://cloudinary.com/).

## Features

### User Authentication:

* Users can register, log in, and log out.
* User roles: Regular users and administrators.

### Task Management:

* Users can create, update, and delete tasks.
* Tasks have the following properties:
    * title
    * description
    * photos
    * due date
    * priority (High, Medium, Low)
    * status (To Do, In Progress, Done)

### User-specific Tasks:

* Each user can only view and manage their own tasks.
* Tasks are associated with the user who created them.

### Task Filtering and Sorting:

* Users can filter tasks based on creation date, status, priority, and due date.
* Sorting tasks by various criteria (e.g., due date, priority, status).

### API Testing and Documentation:

* comprehensive testing for models, views, and API endpoints.
* comprehensive documentation to guide users on interacting with the API, including authentication and endpoints.

## To run locally, follow these steps

### Clone the Repository:

```shell
>> git clone https://github.com/imrand-dev/task-manager.git
>> cd task-manager
```

### Version Mismatch Resolution:

If your version does not match mine (Python 3.12), follow these steps to update the project configuration.

* Update Pipfile:
    * Open `Pipfile` from your project directory.
    * Change the "python_version" to "3.10" in the "[requires]" section.
    ```py
    [requires]
    python_version = "3.10"
    ```
* Update Pipfile.lock:
    * Open `Pipfile.lock` from your project directory.
    * Change the "python_version" in the "requires" section to "3.10".
    ```py
    "requires": {
        "python_version": "3.10"
    },
    ```
* After making changes to the "Pipfile", regenerate the "Pipfile.lock" using `pipenv lock` command.

### Setup a Virtual Environment:

Before creating a virtual environment, make sure you've already installed `pipenv` globally on your machine.

```shell
>> pipenv install (To create a new virtual env)
>> pipenv shell (To activate the virtual env)
```

### Install Dependencies:

Although when you run `pipenv install` this command for the first time to create a virtual environment, all project dependencies are also installed inside the new environment.

So run this command kinda optional `pip install -r requirements/dev.txt`.

### Setup Environment Variables:

* Enter the main project directory `cd projectile`.
* There you'll see `.env.example` file, rename it to `.env` and fill out all the fields.

### Apply Migrations:

```py
>> python manage.py makemigrations
>> python manage.py migrate
```

### Create a Superuser:

I've already added a command that will generate a superuser with predefined fields.

```py
>> python manage.py superuser

then use this email and password
Email - john@gmail.com
Password - 123456
```

If you want to create a superuser on your own, run this command instead.

```py
python manage.py create_superuser
```

### Run the Development Server:

```py
>> python manage.py runserver
```

This command will start the development server, now open your browser and got to `http://127.0.0.1:8000/tasks` to see all tasks.

### Access Django Admin:

Go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created. This will allow you to manage users, tasks and other data using the Django admin interface.