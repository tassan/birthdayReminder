from datetime import date
from birthdayReminder.core.models import BirthdayReminder


def check_birthdays():
    today = date.today()
    query = BirthdayReminder.objects.filter(birthday_date=today)

    if not query:
        pass

    for birthday in query:
        pass

