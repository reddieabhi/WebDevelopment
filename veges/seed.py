from faker import Faker
fake = Faker()

import random
from .models import *

def seed_db(n=10):
    try:
        for i in range(10):
            departments_objs = Department.objects.all()
            random_index = random.randint(0,len(departments_objs)-1)
            department = departments_objs[random_index]
            student_id = f'STU-0{random.randint(100,999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(15,30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)
            
            student_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_address = student_address,
                student_age = student_age,
                
                )
            
    except Exception as e:
        print(e)

