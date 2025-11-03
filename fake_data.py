import os
import django
import random
from faker import Faker

# Project root path आणि settings set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF.settings')  # project folder name
django.setup()

from restapi.models import Student

fake = Faker()

for _ in range(200):   # 20 fake records
    student = Student.objects.create(
        name=fake.name(),
        email=fake.unique.email(),
        age=random.randint(18, 30),
        address=fake.address()
    )
    print(f"Inserted -> {student.name} | {student.email}")
