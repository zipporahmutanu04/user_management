# Django User Management Project

A simple Django project for user account management, including registration, mock email verification, profile management, and admin panel functionality.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/user_management.git
   cd user_management
   ```
![clone](https://github.com/user-attachments/assets/d8b4069b-f532-4c6f-9be9-baf18df0eec6)

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
![evniron](https://github.com/user-attachments/assets/c141e83f-9ec6-4b2c-8cb5-9603bb0608f0)



3. Install dependencies:
```bash
pip install -r requirements.txt
```
![installation](https://github.com/user-attachments/assets/2394a72f-da07-493c-b0fe-db23e5ada6db)


4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
![migrate](https://github.com/user-attachments/assets/aea89a53-f234-4bf1-aa35-462dc9682761)

5. Create a superuser for admin access:
```bash
python manage.py createsuperuser
```
![superuser](https://github.com/user-attachments/assets/aee33d49-5fe3-439b-86a4-0f72930e1da3)

6. Collect static files:
```bash
python manage.py collectstatic
```
![static](https://github.com/user-attachments/assets/fe6193fb-2633-4db2-b0bb-9f78bf188fe5)
