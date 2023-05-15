#mod7
#module 7.1 Ex1
#Створи клас, який зберігатиме інформацію з однієї візитки. Припустимо, що кожна візитка містить такі дані, як: ім'я, прізвище, назва компанії, посада, адреса електронної пошти
#create class
class BaseContact:
    
  def __init__(self, name, surname, phone_number, email):
    self.name = name
    self.surname = surname
    self.phone_number = phone_number
    self.email = email

  def contact(self):
    print(f"I am dialing {self.phone_number} and calling {self.name} {self.surname}")
  
  @property
  def get_name_length(self):
    return len(self.name) + len(self.surname)
#вправа 7.2.1. Зміни код із попередньої вправи про адресну книгу так, щоб об’єкт візитки представлений у вигляді string, містив ім’я, прізвище та адресу електронної пошти особи, яка є власником цієї візитки.
  def __str__(self):
        return f'{self.name} {self.surname} {self.email}'
  
  def __repr__(self):
    return f"{self.name} - {self.surname} ({self.get_name_length}) {self.email}"

  #Покращ ще більш нашу програму зберігання візиток. Додай до класу, який описує візитку, метод contact()який виведе на консоль "Зв'язуюсь з ..." і, нарешті, відобразить ім'я, прізвище, посаду та адресу електронної пошти особи, з якою ти хочеш зв'язатися. .


class BusinessContact(BaseContact):
    def __init__(self, company, position, work_phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.work_phone_number = work_phone_number

    
    def contact(self):
        print(f"I am dialing {self.work_phone_number} and calling {self.name} {self.surname}")

p1 = BaseContact(name="Anna",
            surname="Tokar",
            phone_number="11111111",
            email="a.tokar@gmail.com")
p1b = BusinessContact(name="Anna",
            surname="Tokar",
            phone_number="11111111",
            email="a.tokar@gmail.com",
            company="Lifecell",
            position="SEO",
            work_phone_number='11111119')

p2 = BaseContact(name="Yuriy",
            surname="Kasenych",
            phone_number="22222222",
            email="yu.kasenych@gmail.com")
p2b = BusinessContact(name="Yuriy",
            surname="Kasenych",
            email="yu.kasenych@gmail.com",
            company="Kyivstar",
            position="HR",
            phone_number="22222222",
            work_phone_number='22222229')

p3 = BaseContact(name="Iryna",
            surname="Baranova",
            phone_number="33333333",
            email="i.baranova@gmail.com")
p3b = BusinessContact(name="Iryna",
            surname="Baranova",
            company="Vodafone",
            position="Manager",
            phone_number="33333333",
            work_phone_number="33333339",
            email="i.baranova@gmail.com")

p4 = BaseContact(name="Max",
            surname="Panchenko",
            phone_number="44444444",
            email="m.pancenko@gmail.com")
p4b = BusinessContact(name="Max",
            surname="Panchenko",
            company="Kyivstar",
            position="Manager",
            phone_number="44444444",
            work_phone_number="44444449",
            email="m.pancenko@gmail.com")

p5 = BaseContact(name="Ivan",
            surname="Derkach",
            phone_number="55555555",
            email="i.derkach@gmail.com")
p5b = BusinessContact(name="Ivan",
            surname="Derkach",
            company="Vodafone",
            position="Manager",
            phone_number="55555555",
            work_phone_number="55555559",
            email="i.derkach@gmail.com")

# creating list
people_list = [p1, p2, p3, p4, p5]
people_list_business = [p1b, p2b, p3b, p4b, p5b]
all_people_lists = people_list + people_list_business

# Побудуй цикл, який відображатиме весь вміст списку візиток так, щоб ім’я, прізвище та адреса електронної пошти власника візитки відображалися в одному рядку.
for n in people_list:
  print(n)

print("______Faker_________________________________________________")

#module 7.1 Ex2 Faker
#Напиши функцію, яка створює екземпляри твого класу потрібної візитки. Використовуючи описану вище бібліотеку 'faker`. Переконайся в випадковості даних у кожній візитці, яку поверне твоя функція.

from faker import Faker
faker = Faker()

def card():
    for i in range(9):
        name = faker.name()
        job = faker.job()
        company = faker.company()
        email = faker.email()
        phone_number = faker.phone_number(),
        print(f'{name}, {job}, {company},{email}')

card()

print("______Faker__ варіант 2_________________________________________________")


from faker import Faker
faker = Faker()

def card():
  for i in range(11):
    p = BaseContact(name=faker.name(),
               surname='',
               phone_number=faker.phone_number(),
               email=faker.email())
    print(i, str(p))
    people_list.append(p)
card()

print("_______________________________________________________")
#7.2.2. Створи список візиток, а потім за допомогою функції sorted() впорядкуй їх трьома способами - за ім'ям, прізвищем та адресою електронної пошти.
people_list = [p1, p2, p3, p4, p5]
print("--------- Sorted by name -------")
by_name = sorted(people_list, key=lambda people: people.name)
print(by_name)
print("--------- Sorted by surname ----")
by_surname = sorted(people_list, key=lambda people: people.surname)
print(by_surname)
print("--------- Sorted by email ------")
by_email = sorted(people_list, key=lambda people: people.email)

print(by_email)

print("_______________________________________________________")
#Використовуючи успадкування, розділи основний клас візитки на два окремі: перший (BaseContact’) повинен зберігати основні контактні дані, такі як ім’я, прізвище,особистий номер телефону, адреса електронної пошти. Використовуючи ж наступний клас (BusinessContact`), розшир базовий клас для зберігання інформації, пов’язаної з роботою даної особи – посада, назва компанії, робочий номер телефону.
#Обидва типи візиток повинні пропонувати метод contact(), який відображатиме повідомлення на консолі зі змістом "Я набираю +48 123456789 і телефоную Ігор Шевченко". При виборі фірмової візитки повинен вибиратися робочий номер телефону, а при виборі основної візитки- особистий номер.

p1.contact()
p1b.contact()

p2.contact()
p2b.contact()

p3.contact()
p3b.contact()

p4.contact()
p4b.contact()

print("________________get_name_length_______________________________________")
#Обидва типи візиток повинні мати динамічний атрибут label_length, який повертає нам довжину імені та прізвища особи.
print(p1.get_name_length)  
print(p1b.get_name_length) 
print(p2.get_name_length) 
print(p2b.get_name_length)  
