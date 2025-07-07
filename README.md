# Django User Management Project

A simple Django project for user account management, including registration, mock email verification, profile management, and admin panel functionality.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/user_management.git
   cd user_management
   ```
![Alt text](\my_images\clone.JPG)
2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
![Alt text](\my_images\evniron.JPG)

3. Install dependencies:
```bash
pip install -r requirements.txt
```
![Alt text](\my_images\installation.JPG)
4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
![Alt text](\my_images\migrate.JPG)
5. Create a superuser for admin access:
```bash
python manage.py createsuperuser
```
![Alt text](\my_images\superuser.JPG)
6. Collect static files:
```bash
python manage.py collectstatic
```
![Alt text](\my_images\static.JPG)