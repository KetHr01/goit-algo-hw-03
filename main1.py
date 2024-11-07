from datetime import datetime
from random import randint
import re

# --------FIRST-TASK--------

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference =  date - today
        return difference.days
    except ValueError:
        return "Incorect data"

print('\n', '_'*10, "FIRST TASK", '_'*10)
print(get_days_from_today("2025-04-11"))


# --------SECOND-TASK--------

def get_numbers_ticket(min, max, quantity):
    try:
        numbers = set()
        if quantity > (max - min + 1):
            return []
        if min >= 1 and max <= 1000:
            while len(numbers) != quantity:
                numbers.add(randint(min, max))
        numbers_list = sorted(numbers)
        return numbers_list
    except (TypeError, ValueError):
        return []

print('\n', '_'*10, "SECOND TASK", '_'*10)
print(get_numbers_ticket(40, 14, 6))


# --------THIRD-TASK--------

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)
    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('380'):
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = '+38' + cleaned_number
    return cleaned_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

print('\n', '_'*10, "THIRD TASK", '_'*10)
for num in raw_numbers:
    print(normalize_phone(num))


