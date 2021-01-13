"""
Task 1
School
Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
and another one called Teacher. Try to find as many methods and attributes as you can which
belong to different classes, and keep in mind which are common and which are not. For example, the name should be a
Person attribute, while salary should only be available to the teacher.
"""


class Person:
    def __init__(self, name, lastname, age, gender):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.gender = gender


class Teacher(Person):
    def __init__(self, name, lastname, age, gender, subject, salary, university):
        super().__init__(name, lastname, age, gender)
        self.subject = subject
        self.salary = salary
        self.university = university

    def __repr__(self):
        return self.name.title() + ' ' + self.lastname + " " + self.age + " " + self.gender + " " + self.subject + " " + \
               self.salary + " " + self.university


class Student(Person):
    def __init__(self, name, lastname, age, gender, stClass, averageRating):
        super().__init__(name, lastname, age, gender)
        self.stClass = stClass
        self.averageRate = averageRating

    def __repr__(self):
        return self.name.title() + ' ' + self.lastname + " " + self.age + " " + self.gender + " " + self.stClass + " " + \
               self.averageRate


if __name__ == "__main__":
    teach = Teacher("valentyna", "honchar", "35", "fem", "history", "7000", "TNPU")
    stud = Student('tetyana', "snigur", "12", "fem", "8", '9.5')
    print(teach)
    print(stud)

"""
Task 2
Mathematician
Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:
square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
```
class Mathematician:
    pass
m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
```
"""


class Mathematician:
    def __init__(self):
        pass

    def square_nums(self, num):
        for i in range(len(num)):
            num[i] = num[i] ** 2
        return num

    def remove_positives(self, num):
        neg = []
        for i in range(len(num)):
            if num[i] < 0:
                neg.append(num[i])
        return neg

    def filter_leaps(self, num):
        leap = []
        for i in range(len(num)):
            if num[i] % 4 == 0:
                if num[i] % 100 == 0:
                    if num[i] % 400 == 0:
                        leap.append(num[i])
                else:
                    leap.append(num[i])

        return leap


if __name__ == "__main__":
    m = Mathematician()
    print(m.square_nums([7, 11, 5, 4]))
    print(m.remove_positives([26, -11, -8, 13, -90]))
    print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

"""
Task 3
Product Store
Write a class Product that has three attributes:
type
name
price
Then create a class ProductStore, which will have some Products and will operate with all products in the store. All 
methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional 
classes to operate on a certain type of product, etc.
Also, the ProductStore class must have the following methods:
add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your 
store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input 
identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other 
case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
```
class Product:
    pass
class ProductStore:
pass
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product(Food, 'Ramen, 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell(‘Ramen’, 10)
assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)
"""