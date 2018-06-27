##Password as a Service

**Service for displaying information from the etc/passwd and etc/groups files on Linux.**
##### Requirements
* Python 3
* Django

##### Api folder
* urls.py
Contains all the url rules and destinations.
* views.py
Contains all the methods for displaying the necessary information
* models.ini
Contains all the logic and file interaction.
* tests.py
Contains test cases for the models

##### Testing Instructions
	python manage.py test api.tests - Running all tests
	python manage.py test api.tests.UserTestCase - Running user tests
	python manage.py test api.tests.GroupTestCase - Running group tests

##### Running Instruction
	python manage.py runserver