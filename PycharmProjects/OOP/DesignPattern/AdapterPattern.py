import datetime
class AgeCalculator(object):
    def __init__(self, birthday):
        self.year, self.month, self.day = (int(x) for x in birthday.split('-'))
    def calculate_age(self, date):
        year, month, day = (int(x) for x in date.split('-'))
        age = year - self.year
        if (month, day) < (self.month, self.day):
            age -= 1
        return age

class DateAgeAdapter(object):
    def _str_date(self, date):
        return date.strftime('%Y-%m-%d')

    def __init__(self, birthday):

        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)

    def get_age(self, date):
        date = self._str_date(date)
        print( self.calculator.calculate_age(date))

birthdate = datetime.date(1982, 3, 25)
calcudate = datetime.date(2015,2,22)

adapter = DateAgeAdapter(birthdate)
adapter.get_age(calcudate)