class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
        #calculate birth_year
    def calculate_birth_year(self, current_year):
        birth_year = current_year - self.age
        return birth_year
    #printing the person
    def print_person(self):
        return f"Hello! I am {self.name} and I am {self.age} years old {self.nationality}. I am born in {self.calculate_birth_year(current_year)}"

size = int(input('set size'))
current_year = int(input('set current_year'))
people = []

for i in range(size):
    name = input('name')
    age = int(input('age'))
    nationality = input('nationality')
    person = Person(name, age, nationality).print_person()
    
    people.append(person)

print(people)