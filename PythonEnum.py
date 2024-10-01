from datetime import date
from enum import Enum, auto
from typing import List


class Weekdays(Enum):
    Monday = auto()  #auto sets the enum number automatically
    Tuesday = auto()
    Wednesday = auto()
    Thursday = auto()
    Friday = auto()
    Saturday = auto()
    Sunday = auto()
    pass

    @classmethod  #converts function to a class method
    def current_weekday(weekdayClass, current_date: date):
        try:
            return weekdayClass(current_date.isoweekday())
        except ValueError as error:
            print(f"Error: {error}")
            return error

    @classmethod
    def show_all_weekdays(weekdayClass) -> List[str]:
        #for day in Weekdays:
        #    return weekdayClass(day.name)
        return [day.name for day in weekdayClass]


if __name__ == '__main__':
    current_day: Weekdays = Weekdays.current_weekday(current_date=date.today())
    days: list[str] = Weekdays.show_all_weekdays()
    print(f"All weekdays: {days}")
    if current_day:
        print(f"Today is {current_day}")
