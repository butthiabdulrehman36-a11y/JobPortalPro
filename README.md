## JobPortal Pro

A professional Django-based Job Portal web application with user authentication, job search, job listings, job details, and a personalized user dashboard.

## Features

* Professional homepage
* User registration
* User login and logout
* Protected user dashboard
* Job listings
* Job search
* Job detail pages
* Jobs data management through Django Admin
* User management through Django Admin
* Applications foundation
* Companies foundation
* Profiles foundation
* Environment-based Django secret key configuration
* SQLite database for local development

## Technologies

* Python 3.13
* Django 6.1.1
* SQLite
* HTML
* CSS
* python-dotenv
* Git
* GitHub

## Project Structure

```text
JobPortalPro/
|-- accounts/
|-- applications/
|-- companies/
|-- core/
|-- jobs/
|-- profiles/
|-- jobportal/
|-- static/
|   `-- css/
|-- templates/
|-- .env.example
|-- .gitignore
|-- manage.py
`-- requirements.txt
```

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/butthiabdulrehman36-a11y/JobPortalPro.git
cd JobPortalPro
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Create the environment file

Create a file named `.env` in the project root.

Use `.env.example` as the reference:

```text
DJANGO_SECRET_KEY=replace-with-your-own-secret-key
```

Replace the example value with your own secure Django secret key.

**Do not commit `.env` to GitHub.**

### 5. Apply database migrations

```powershell
python manage.py migrate
```

### 6. Create an administrator account

```powershell
python manage.py createsuperuser
```

Follow the prompts to create the Django administrator account.

### 7. Run the development server

```powershell
python manage.py runserver
```

Open the development server in your browser:

```text
http://127.0.0.1:8000/
```

## Django Admin

The Django administration area is available at:

```text
http://127.0.0.1:8000/admin/
```

Use the superuser account created during setup to access the admin area.

## Environment Variables

The project uses an environment variable for the Django secret key.

Required variable:

```text
DJANGO_SECRET_KEY
```

The actual `.env` file is intentionally excluded from Git through `.gitignore`.

## Security

Sensitive environment configuration should not be committed to the public repository.

The repository includes:

* `.env` in `.gitignore`
* `.env.example` as a safe configuration template
* Environment-based Django `SECRET_KEY`

## Project Status

JobPortal Pro has completed its planned development and final GitHub publication.

The project is currently maintained as a completed portfolio/learning project. No live production deployment is planned at this stage.

## Repository

GitHub:

https://github.com/butthiabdulrehman36-a11y/JobPortalPro
