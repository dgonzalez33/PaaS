[![Password as a Service])]

**Service for displaying information from the etc/passwd and etc/groups files on Linux.**
#### Requirements
Python 3
Django
#### Api folder

* urls.py
Contains all the url rules and destinations.
* views.py
Contains all the methods for displaying the necessary information
* models.ini
Contains all the logic and file interaction.
* tests.py
Contains test cases for the models

##### Testing Instructions
python manage.py test  -- All test
python manage.py user.tests -- All User tests
python manage.py group.tests    -- All Group tests
##### Deployment Instructions
python manage.py check --deploy

