from datetime import datetime




def check_birthdate(year,month,day):
    todays_date = datetime(2020,1,26)  # January 26, 2020
    birthday = datetime(year,month,day)
    if birthday > todays_date:
        return False
    elif birthday < todays_date:
        return True



# age = int(todays_date) - (birthday)
# print("You are %i years old. ") % (age)
    
    
year = int(input("Enter year of birth: "))
month =  int(input("Enter month of birth: "))
day = int(input("Enter day of birth: "))



def calculate_age(year, month, day):
    todays_date = datetime(2020,1,26)  # January 26, 2020
    birthday = datetime(year, month, day)
    difference_age = int((todays_date-birthday).days /365)
    print("you are %s years old." % (difference_age))
    
    


if check_birthdate(year,month,day) == True:
    calculate_age(year,month,day)
else: 
    print("invalid")


