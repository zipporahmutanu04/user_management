# Django User Management Project

A simple Django project for user account management, including registration, mock email verification, profile management, and admin panel functionality.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/user_management.git
   cd user_management
   ```
2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Create a superuser for admin access:
```bash
python manage.py createsuperuser
```
6. Collect static files:
```bash
python manage.py collectstatic
```


![Admin Panel](static/my_images/admin.JPG)


