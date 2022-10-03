from . choices import DEPARTMENT_CHOICES
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