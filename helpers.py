import random
import string
from faker import Faker

fake = Faker()


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_user_data():
    return {
        "name": generate_random_string(10),
        "password": generate_random_string(10),
        "email": fake.email()
    }
