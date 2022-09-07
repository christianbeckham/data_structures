from implementation import find_pi_day, print_fruits, print_profile, print_family_members

# Task 1
# 1.1

find_pi_day()
print('')

# 1.2
fruits = {'mango', 'watermelon', 'apple', 'strawberry', 'orange'}
fruits.add('pineapple')
fruits.add('grapes')

print_fruits(fruits)
print('')

# 1.3
profile = {
    'first_name': 'Homer',
    'last_name': 'Simpson',
    'email_address': 'homer@gmail.com',
    'phone_number': '123-456-7890'
}

print_profile(profile)
print('')

# Task 2
family = [
    {'first_name': 'Homer', 'last_name': 'Simpson', 'relation': 'Father'},
    {'first_name': 'Marge', 'last_name': 'Simpson', 'relation': 'Mother'},
    {'first_name': 'Bart', 'last_name': 'Simpson', 'relation': 'Brother'},
    {'first_name': 'Lisa', 'last_name': 'Simpson', 'relation': 'Sister'}
]

print_family_members(family)