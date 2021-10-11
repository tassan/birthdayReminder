from django.db import models
import calendar


class BirthdayReminder(models.Model):
    class Meta:
        verbose_name = "Birthday Reminder"
        verbose_name_plural = "Birthday Reminders"

    birthday_date = models.DateField("Birthday Date")
    birthday_person_name = models.CharField("Birthday Person Name", max_length=255)
    birthday_person_email = models.CharField("Birthday Person Email", max_length=255)
    birthday_message = models.TextField("Birthday Message")
    sender_email = models.CharField("Email Sender", max_length=255)

    def __str__(self):
        return (
            f"{self.birthday_person_name} | {calendar.month_name[self.birthday_date.month]},"
            f" {self.birthday_date.day}"
        )
