from dataclasses import dataclass
from abc import ABC

class Address:
    def __init__(self, street:str, city:str, zip_code:str):
        if not street.strip():
            raise ValueError("A rua nao pode ser um campo vazio")
        if not city.strip():
            raise ValueError("A cidade nao pode ser um campo vazio")
        if not zip_code.strip():
            raise ValueError("O CEP nao pode ser um campo vazio")
        
        self._street = street
        self._city = city
        self._zip_code = zip_code

    @property
    def street(self):
        return self.street
    
    @property
    def city(self):
            return self.city
        
    @property
    def zip_code(self):
            return self._zip_code
        
    @property
    def __str__(self):
        return f"{self._street}, {self.city} - {self.zip_code}"
    
class Contact:
    def __init__(self, email: str, phone: str):
        if not email.strip():
            raise ValueError("O email nao pode estar vazio")
        if not phone.strip():
            raise ValueError("O telefone nao pode estar vazio")
        
        self._email = email
        self._phone = phone

    @property
    def email(self):
        return self._email
        
    @property
    def phone(self):
        return self._phone
    
    def __str__(self):
        return f"{self.email} / {self.phone}"

class Person(ABC):
    def __init__(self, name: str, address: Address, contact: Contact):
        if not name.strip():
            raise ValueError("O campo nome nao pode estar vazio")
        self._name = name
        self._address = address
        self._contact = contact

    @property
    def name(self):
        return self._name
    @property
    def address(self):
        return self._address
    @property
    def contact(self):
        return self._contact