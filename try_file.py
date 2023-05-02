from pydantic import BaseModel, ValidationError
from data.data_faker import DataFaker

import json
from jsonschema import validate, exceptions

# from marshmallow import Schema, fields, validate
#
# from dataclasses import dataclass
# from typing import Optional, List
#
#
# @dataclass
# class Book:
#     title: str
#     isbn: str
#
#
# @dataclass
# class User:
#     email: int
#     books: Optional[List[Book]] = None
#
#
# def validate_isbn(isbn: str) -> None:
#     """ Код проверки isbn (опущено), бросает исключение
#     marshmallow.ValidationError если валидация не прошла"""
#
#
# class BookSchema(Schema):
#     title = fields.String(required=True, validate=validate.Length(max=120))
#     isbn = fields.String(required=True)
#
#
#
# class UserSchema(Schema):
#     email = fields.Email(required=True)
#     books = fields.Nested(BookSchema, many=True, required=False)
#
#
#
#
#
#
#
# raw_data_str = """{
#     "email": "foobar.com",
#     "books": [
#         {"title": "Автостопом по Галактике", "isbn": "123456789"},
#         {"title": "Идеальный программист", "isbn": "987654321"}
#     ]
# }"""
# json_data = json.loads(raw_data_str)
# schema = UserSchema()
# print(schema)
# user = schema.load(json_data)
# print(user)# бросает исключение если валидация не прощла

# class User(BaseModel):
#     id: int
#     name = DataFaker().get_first_name()
#
# a = User(id=1)
#
#
#
#
# class UserResponce(BaseModel):
#     name: str
#     job: str
#     id: str
#     createdAt: str
#
# row = """{"name": [], "job": "Pharmacist, hospital", "id": "913", "createdAt": "2023-03-01T07:37:10.552Z"}"""
#
# try:
#     UserResponce.parse_raw(row)
# except ValidationError as e:
#     print(e.json())


# shhema = """{
# jsonData = json.loads('{"id" : "10","name": "DonOfDen","contact_number":1234567890}')
#
# try:
#     validate(instance=jsonData, schema=shhema)
# except exceptions.ValidationError as err:
#     print(err)

# class Addition:
#     def __call__(self, *args, **kargs):
#         result = sum(filter(lambda x: isinstance(x, int), args))
#         return f"Сумма переданных значений = {result}"
#
# # Ниже код для проверки методов класса Addition
# add = Addition()
# assert add(10, 20) == "Сумма переданных значений = 30"
# assert add(1, 2, 3.4) == "Сумма переданных значений = 6.4"
# assert add(1, 2, 'hello', [1, 2], 3) == "Сумма переданных значений = 6"


# class DictMixin:
#     def to_dict(self):
#         string = json.dumps(self.__dict__)
#         print(string)
#         return json.loads(string)
#
#
# # Ниже код для проверки миксина DictMixin
#
# class Phone(DictMixin):
#     def __init__(self, number):
#         self.number = number
#
#
# class Person(DictMixin):
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#
# class Address(DictMixin):
#     def __init__(self, street, city, state, zip_code):
#         self.street = street
#         self.city = city
#         self.state = state
#         self.zip_code = zip_code
#
#
# class Company(DictMixin):
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#
#
# address = Address("123 Main St", "Anytown", "CA", "12345")
# john_doe = Person("John Doe", 30, address)
#
# # print(john_doe.__dict__)
# john_doe_dict = john_doe.to_dict()

a = {'address': {'city': 'Albuquerque',
                 'state': 'NM',
                 'street': '123 Main St',
                 'zip_code': '987654'},
     'age': 30,
     'name': 'Walter White',
     'phone': {'number': '555-1234'}}
#
# def _finditem(obj, key):
#     if key in obj: return obj[key]
#     for k, v in obj.items():
#         if isinstance(v,dict):
#             return _finditem(v, key)  #added return statement
#
# print()


# Напишите определение класса DictMixin
import json


# class DictMixin:
#     def to_dict(self):
#         def dict_recur(self):
#             result = {}
#             for key, value in self.__dict__.items():
#                 if isinstance(value, (Phone, Person, Address, Company)):
#                     result[key] = dict_recur(value)
#
#                 elif isinstance(value, list):
#                     list_res = []
#                     for elem in value:
#                         list_res.append(dict_recur(elem))
#                     result[key] = list_res
#                 else:
#                     result[key] = value
#             return result
#
#         return dict_recur(self)
#
#
# # Ниже код для проверки миксина DictMixin
#
# class Phone(DictMixin):
#     def __init__(self, number):
#         self.number = number
#
#
# class Person(DictMixin):
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#
# class Address(DictMixin):
#     def __init__(self, street, city, state, zip_code):
#         self.street = street
#         self.city = city
#         self.state = state
#         self.zip_code = zip_code
#
#
# class Company(DictMixin):
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address


# address = Address("123 Main St", "Anytown", "CA", "12345")
# john_doe = Person("John Doe", 30, address)
#
# john_doe_dict = john_doe.to_dict()
# print(john_doe.__dict__)
# print(john_doe_dict)
#
# assert john_doe_dict == {
#     'name': 'John Doe',
#     'age': 30,
#     'address': {
#         'street': '123 Main St',
#         'city': 'Anytown',
#         'state': 'CA',
#         'zip_code': '12345'
#     }
# }
#
# address = Address("123 Main St", "Albuquerque", "NM", "987654")
# # assert address.to_dict() == {
# #     'street': '123 Main St',
# #     'city': 'Albuquerque',
# #     'state': 'NM',
# #     'zip_code': '987654'
# # }
# walter = Person("Walter White", 30, address)
# # assert walter.to_dict() == {'address': {'city': 'Albuquerque',
# #                                         'state': 'NM',
# #                                         'street': '123 Main St',
# #                                         'zip_code': '987654'},
# #                             'age': 30,
# #                             'name': 'Walter White'}
# #
# walter_phone = Phone("555-1234")
# walter.phone = walter_phone
# # assert walter.to_dict() == {'address': {'city': 'Albuquerque',
# #                                         'state': 'NM',
# #                                         'street': '123 Main St',
# #                                         'zip_code': '987654'},
# #                             'age': 30,
# #                             'name': 'Walter White',
# #                             'phone': {'number': '555-1234'}}
# #
# # company_address = Address("3828 Piermont Dr", "Albuquerque", "NM", "12345")
# # company = Company("SCHOOL", company_address)
# #
# # assert company.to_dict() == {'address': {'city': 'Albuquerque',
# #                                          'state': 'NM',
# #                                          'street': '3828 Piermont Dr',
# #                                          'zip_code': '12345'},
# #                              'name': 'SCHOOL'}
#
# jesse_address = Address("456 Oak St", "Albuquerque", "NM", "12345")
# jesse = Person("Jesse Bruce Pinkman", 27, jesse_address)
# jesse.phone = Phone("555-5678")
#
# fring = Person("Gustavo Fring", 55, Address("Los Pollos Hermanos", "Albuquerque", "NM", "12345"))
# fring.friends = [walter, jesse]
# print(fring.to_dict())
# assert fring.to_dict() == {'address': {'city': 'Albuquerque',
#                                        'state': 'NM',
#                                        'street': 'Los Pollos Hermanos',
#                                        'zip_code': '12345'},
#                            'age': 55,
#                            'friends': [{'address': {'city': 'Albuquerque',
#                                                     'state': 'NM',
#                                                     'street': '123 Main St',
#                                                     'zip_code': '987654'},
#                                         'age': 30,
#                                         'name': 'Walter White',
#                                         'phone': {'number': '555-1234'}},
#                                        {'address': {'city': 'Albuquerque',
#                                                     'state': 'NM',
#                                                     'street': '456 Oak St',
#                                                     'zip_code': '12345'},
#                                         'age': 27,
#                                         'name': 'Jesse Bruce Pinkman',
#                                         'phone': {'number': '555-5678'}}],
#                            'name': 'Gustavo Fring'}
#
# print('Good')




#
# import json
# class JsonSerializableMixin:
#     def to_json(self):
#         return json.dumps(self.__dict__)
#
# # Ниже код для проверки миксина JsonSerializableMixin
# class Car(JsonSerializableMixin):
#     def __init__(self, make: str, color: str):
#         self.make = make
#         self.color = color
#
#
# class Book(JsonSerializableMixin):
#     def __init__(self, title: str, author: str):
#         self.title = title
#         self.author = author
#
#
# class Person(JsonSerializableMixin):
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#
# car = Car("Toyota", "red")
# assert car.to_json() == '{"make": "Toyota", "color": "red"}'
#
# book = Book("The Catcher in the Rye", "J.D. Salinger")
# assert book.to_json() == '{"title": "The Catcher in the Rye", "author": "J.D. Salinger"}'
# book.ratings = [5, 4, 5, 4, 5]
# book.is_bestseller = True
# book.to_json() == '{"title": "The Catcher in the Rye", "author": "J.D. Salinger", "ratings": [5, 4, 5, 4, 5], "is_bestseller": true}'
#
# person = Person("John", 30)
# assert person.to_json() == '{"name": "John", "age": 30}'
# print('Good')




