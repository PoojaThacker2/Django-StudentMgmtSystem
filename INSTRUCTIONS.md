### Django - Backend Project

A basic school management system using the Django Rest Framework.
The basic functionality includes:
● Schools can signup using email, name, city, pin code, and password.
● Once signed up, the school shall be able to add students for grades 1-12th in bulk.
(eg. 20 students for grade 8)
● Each student shall have a name, username, and password.
● Both students and the school shall be able to log in to the system.
● The school shall be able to list and filter the students based on grade
● Both the school and student shall be able to change the student's name and
password.

ADMIN Panel:
● Admin should be able to see schools onboarded.
● Admin should be able to filter students based on school and grade.
● Admin should be able to add grades.

What to deliver:
● A postman collection for all the APIs
● The codebase of the project.

Guidelines:
● DRF Serializers shall be used.
● All the post request data shall be in JSON format.
● Basic error handling shall be done.
● Basic data validation shall be done.
● Database atomicity shall be maintained.
● The JWT shall be used as Auth Token.
● While creating the bulk of students, the student name can be empty.