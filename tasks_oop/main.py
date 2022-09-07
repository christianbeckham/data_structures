from year import Year
from basket import Basket
from profile import UserProfile
from family import Family

# Task 1.1 - OOP
year = Year()

pi = 3.14
month_number = int(pi)

month = year.get_month_by_number(month_number)
print('\nMonth:', month)

# Task 1.2 - OOP
basket = Basket()
fruits_to_add = ['mango', 'watermelon', 'apple', 'strawberry', 'orange']

for fruit in fruits_to_add:
    basket.add_fruit(fruit)

basket.add_fruit('pineapple')
basket.add_fruit('grapes')
print('')
basket.display_fruits()

# Task 1.3

user = UserProfile('Homer', 'Simpson', 'homer@gmail', '123-456-7890')
user.get_info()

# Task 2
simpsons = Family()
simpsons.display_family()
