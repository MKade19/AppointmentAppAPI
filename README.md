## How to start

1. Clone `https://github.com/MKade19/appointmentAppAPI/tree/main` to local
2. Run `python manage.py migrate`
3. Run `python manage.py loaddata ./initial-dataload.json`
4. Run `python -m pip install -U channels`
5. Run `pip install channels==3.0.5`
6. Run `python manage.py runserver`

## Initial requirements

Back-end (Python Django)

DBMS of your choice.

Please provide 4 modals (Customer, User (employee), Appointment).
      
Customer (
id, fullname, email, phone, address, appointments
)
Employee (
id, fullname, email, phone, address, department, appointments
)
Departments (
id, fullname, address, employees
)
Appointment (
id, date, start, end, employee, customer
)

Provide JWT auth.

Provide REST API (GET, POST, PUT, DELETE).

Roles
	Admin: Full access
	Doctor: Access to own appointments, Read access only to all DB
Reception: Access to create/edit/delete an appointment and customer.
Only Admin has permission to add/edit/delete an Employee!
