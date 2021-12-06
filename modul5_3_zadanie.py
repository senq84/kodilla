from random import choice
from faker import Faker
fake = Faker()
lista =[]

class BusinessCard:
    
    def __init__ (self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    
    def __str__ (self):
        return self.name

    def __repr__(self):
        return self.name

    @property 
    def label_length(self):
        return len(self.name) 
   
    def contact(self):
        print(f"Wybieram numer{self.phone} i dzownię do {self.name}")
        
class BaseContact(BusinessCard):
    pass
    # gdy nic nie ma innego 
      
class BusinessContact(BusinessCard):
    
    def __init__(self, job, company, phone_2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.phone_2 = phone_2

    def contact(self):
        print(f"Wybieram numer{self.phone_2} i dzownię do {self.name}")

def generate_contacts(n, choice):
    
    for _ in range(n):
        name = fake.name()
        phone = fake.msisdn()
        email = fake.email()
        
        job = fake.job()
        company = fake.company()
        phone_2 = fake.msisdn()
        
        if choice == 1:
            contact = BusinessCard(name, phone, email)
        else:
            contact = BusinessContact(job, company, phone_2, name, phone, email)    

        contact.contact()

        lista.append(contact)

    
#    print(f"name:{name}, {len(name)}, msisdn@home:{msisdn_home}, email:{email}, job:{job}, company:{company},  msisdn job:{msisdn_job}")
#    osoba = BusinessCard(name, msisdn_home, email)
#    print(osoba)
#    print(fake.name())

generate_contacts(5, 2)
print(lista)

for l in lista:
    print(l.label_length)
