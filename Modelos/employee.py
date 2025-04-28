from datetime import date
from uuid import UUID

class Employee:
    def __init__(self, employee_id: UUID, name: str, date_of_birth: date, position: str, email: str, phone_number: str, business: str, status: bool):
        self._employee_id = employee_id
        self._name = name
        self._date_of_birth = date_of_birth
        self._position = position
        self._email = email
        self._phone_number = phone_number
        self._business = business
        self._status = status

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def name(self):
        return self._name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def position(self):
        return self._position

    @property
    def email(self):
        return self._email

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def business(self):
        return self._business

    @property
    def status(self):
        return self._status
