class UserProfile:
    def __init__(self, first_name, last_name, email_address, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number

    def get_info(self):
        print(f'''
        Profile Info:
            First Name: {self.first_name}
            Last Name: {self.last_name}
            Email Address: {self.email_address}
            Phone Number: {self.phone_number}
        ''')
