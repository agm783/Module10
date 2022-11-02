"""
employee.py

Author: Andrew May

Date Modified: 10/28/2022

===============================

This program declares a class ('Employee') that takes in 7 arguments (last name, first name,

address, phone number, a boolean value (indicating whether employee is salaried/paid by the hour),

salary/pay rate, and starting date). The driver (included below) facilitates all argument passing, function calls,

and returned values.

"""
import datetime


class Employee:
    # Constructor
    today = datetime.date.today()
    s_date = today.strftime('%m-%d-%Y')

    def __init__(self, l_name, f_name, addr='', phone='', sal_bool=bool(True or False), sal=float(), start=s_date):
        """
        This function initializes, and accepts, the 7 primary arguments/parameters.
        :param l_name: Employee's last name (str)
        :param f_name: Employee's first name (str)
        :param addr: Street/Home Address (str)
        :param phone: Phone Number (str)
        :param sal_bool: A boolean value indicating the nature of employment;
        True = Salaried | False = Paid Hourly (bool)
        :param sal: A positive-integer dollar amount, either yearly salary or hourly wage (float)
        :param start: Employee's start date (datetime)
        """
        self._last_name = l_name
        self._first_name = f_name
        self._address = addr
        self._phone_number = phone
        self._salaried = sal_bool
        self._start_date = start
        self._salary = sal

        if sal_bool is True:
            self._salary = f"Salaried Employee: ${sal}/year"
        else:
            self._salary = f"Hourly Employee: ${sal}/hour"

    def display(self):
        """
        This function takes in all user-generated input,
        and outputs it in the proper format for an end-user.
        :returns: Employee data in proper format
        """
        return str(self._first_name) + " " + str(self._last_name) + " " + '\n' + str(self._address) + '\n' + str(self._salary) + '\n' + str(f'Start Date: {self._start_date}')

    def __str__(self):
        """
        This function takes in all user-generated input
        and returns it in an 'unofficial' format.
        :return: Informal representation of user input
        """
        print("(__str__):")
        return 'Employee(last_name={}, first_name={}, address={}, phone={}, salaried={},\nsalary={}, start_date={})'.format(self._last_name, self._first_name, self._address, self._phone_number, self._salaried, self._salary, self._start_date)

    def __repr__(self):
        """
        This function takes in all user-generated input
        and returns it in an 'official' format
        (used for debugging; likely viewed by devs and engineers).
        :returns: Formal representation of user input
        """
        print("(__repr__):")
        return 'Employee(last_name={}, first_name={}, address={}, phone={}, salaried={},\nsalary={}, start_date={})'.format(self._last_name, self._first_name, self._address, self._phone_number, self._salaried, self._salary, self._start_date)


# Driver
emp1 = Employee('Patel', 'Sasha', '123 Main Street\nUrban, Iowa', '1-515-888-4747', True, 40000)
print(emp1.display())
print("")
print(str(emp1))
print("")
print(repr(emp1))
del emp1


print("")

emp2 = Employee('Patel', 'Sasha', '123 Main Street\nUrban, Iowa', '1-515-888-4747', False, 7.25)
print(emp2.display())
print("")
print(str(emp2))
print("")
print(repr(emp2))
del emp2

