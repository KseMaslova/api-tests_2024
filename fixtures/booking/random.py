from faker import Faker
import random

fake = Faker()


# Генерация случайных данных
def random_create() -> dict:
    return {"firstname": fake.first_name(), "lastname": fake.last_name(), "totalprice": random.randint(100, 1000),
            "depositpaid": random.choice([True, False]),
            "bookingdates": {
                "checkin": fake.date_this_decade().isoformat(),
                "checkout": fake.date_between_dates(date_start=fake.date_this_decade(), date_end=fake.future_date(end_date="+1y")).isoformat()
            },
            "additionalneeds": fake.word()}
