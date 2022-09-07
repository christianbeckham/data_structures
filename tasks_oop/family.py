from sibling import Sibling


class Family:
    def __init__(self):
        self.siblings = [Sibling('Homer', 'Simpson', 'Father'), Sibling('Marge', 'Simpson', 'Mother'), Sibling(
            'Bart', 'Simpson', 'Brother'), Sibling('Lisa', 'Simpson', 'Sister')]

    def display_family(self):
        for sibling in self.siblings:
            print(f'{sibling.first_name} - {sibling.relation}')
