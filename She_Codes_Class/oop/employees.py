class Employee:

    def __init__(self, name, salary, phone_number, start_date):
        self.name = name
        self.salary = salary
        self.phone_number = phone_number
        self.start_date = start_date

    def get_employment_details(self):
        return (self.name, self.salary, self.start_date)

    def get_contact_details(self):
        return (self.name, self.phone_number)

ninja = Employee("Ninja", 200000, "12345676543", "1st June 2020")
print(ninja.name)
print(ninja.salary, ninja.phone_number)

print(ninja.get_employment_details())
print(ninja.get_contact_details())
