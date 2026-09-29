import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sachin_portfolio.settings')
django.setup()

from django.contrib.auth.models import User

def create_super():
    username = 'admin'
    email = 'slad20401@gmail.com'
    password = 'admin'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser created successfully!\nUsername: {username}\nPassword: {password}")
    else:
        print("Superuser 'admin' already exists.")

if __name__ == '__main__':
    create_super()
