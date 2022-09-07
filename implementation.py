# Task 1: Dictionary, Set and Tuple

# 1.1
def find_pi_day():
    months = ('January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December')
    pi = 3.14
    index = int(pi) - 1
    print(months[index])


# 1.2
def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)


# 1.3
def print_profile(profile):
    for item in profile.items():
        print(f'Key: {item[0]} - Value: {item[1]}')


# Task 2: List of Dictionaries
def print_family_members(family):
    for member in family:
        print(member['first_name'], member['relation'])
