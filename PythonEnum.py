from datetime import date
from enum import Enum, auto

class Weekdays(Enum):
    Monday = auto()
    Tuesday = auto()
    Wednesday = auto()
    Thursday = auto()
    Friday = auto()
    Saturday = auto()
    Sunday = auto()
    pass

    @classmethod
    def current_weekday(weekdayClass, current_date: date):
        try:
            return weekdayClass(current_date.isoweekday())
        except ValueError as error:
            print(f"Error: {error}")
            return error

if __name__ == '__main__':
    current_day: Weekdays = Weekdays.current_weekday(current_date=date.today())
    if current_day:
        print(f"Today is {current_day}")