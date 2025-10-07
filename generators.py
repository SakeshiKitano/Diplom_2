from faker import Faker

fake = Faker()

def generate_user_data():
    return {
        "email": fake.unique.email(),
        "password": fake.password(length=10),
        "name": fake.first_name()
    }