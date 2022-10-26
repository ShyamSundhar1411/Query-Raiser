from . choices import DEPARTMENT_CHOICES
from django.contrib.auth.models import User

def department_finder(roll_no):
    department = ''
    for i in roll_no:
        if not i.isdigit():
            department+=i
    department = department.upper()
    for i,j in DEPARTMENT_CHOICES:
        if department in i:
            return i
def admitted_year_finder(roll_no):
    return "AY - "+roll_no[:2]
def is_program_representative(user):
    if user.profile.role == "Program Representative" or user.profile.role=="Head of Department":
        return True
    return False
def email_checker(email):
    email_splitted = email.split('@')
    if email_splitted[-1] in ['vit.ac.in','vitstudent.ac.in']:
        return True
    return False
def email_parser(email):
    email_splitted = email.split('@')
    return email_splitted[-1]