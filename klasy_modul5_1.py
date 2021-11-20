from faker import Faker
fake = Faker()

class businessCard:
    def __init__ (self, name, company, job, email):
        self.name = name
        self.company = company
        self.job = job
        self.email = email

for _ in range(5):
    print(businessCard(fake.name(),fake.company(),fake.job(),fake.email()))