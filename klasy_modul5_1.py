from typing import MutableMapping

from faker import Faker
fake = Faker()

name = fake.name()
company = fake.company()
job = fake.job()
email = fake.email()

class businessCard:
    def __init__ (self, name, company, job, email):
        self.name = name
        self.company = company
        self.job = job
        self.email = email

card = businessCard(fake.name(), fake.company(), fake.job(), fake.email())

for _ in range(5):
    print(businessCard(fake.name(),fake.company(),fake.job(),fake.email()))