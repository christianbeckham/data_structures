class Year:
    def __init__(self):
        self.months = ('January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December')

    def get_month_by_number(self, month_number):
        index = month_number - 1
        return self.months[index]
