from faker import Faker

class Fake:
    def __init__(self, faker: Faker) -> None:
        self.faker = faker

    def email(self):
        return self.faker.email()

    def first_name(self):
        return self.faker.first_name()

    def last_name(self):
        return self.faker.last_name()

    def company_name(self):
        return self.faker.company()

    def fake_number(self):
        return self.faker.random_number(digits=3)

    def fake_job(self):
        return self.faker.job()


fake = Faker()
