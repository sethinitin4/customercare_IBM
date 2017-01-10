# Customer Care App for IBM
A customer care app for IBM which help in priority sorting of complaints recieved by IBM for the bluemix cloud service. This app uses API provided by the bluemix cloud solutions and sorts the complaints according to an algorithm based on different parameters such as severity of the complaint as well as the details of the client.

### Prerequisites
> Django  
> Watson Developer Cloud  
> service credentials are to be inserted in testingapi.py, toneanalyzer.api, app/views.py
**NOTE: To use the app one must have a bluemix account and access to the apis**

## How does the app work?
* The app needs a superuser which will be the designated employee which looks at the complaints of lodged.
* The user must populate the database with the clients and fill in the information pertaining to but not restricting to the shares of the client, registraition of the client with the service etc.
* Now the user must login with the client side and lodge a complaint.
* After the complaint has been lodged the user can visit the employee login and look at the complaint.
* The complaints are filtered and modified through an algorithm that orders them according to the severity of the complaint.
* The employee can then look at the complaint and will know which of the complaints are high alert.


## Running the project for the first time
* Clone the project into your home folder.
* Go into the root of the project and open the terminal.
* In root run ```pip install -r requirements.txt```
* replace service credentials (as in prerequisites).
* In root run ```python manage.py migrate```
* In root run ```python manage.py createsuperuser``` and follow the instructions that follow
* In root run ```python manage.py runserver```

## Adding the client models
* After creating the superuser and running the server goto the following [link](http://localhost:8000/admin/login/)
* Go to the user model and add the clients.
* Enter all the information for optimum performance of the algorithm.
* Once entered goto the [link](http://localhost:8000/)
* Login with one of the clients and lodge a complaint.
* Goto to the employee login and login with the super user and look at the sorted complaints.

## Feature of the App and further development
The current version deals with objective parmaters and queries.

Further development is to be done using the tone analyzer for subjective queries which returns emotional raings.
Parameters like sadness and anger are minimized and others like happiness are maximized.

Other Features like instant results using Retrieve and Rank API and assigning personalized support by choosing tne right employee using Personality Insights API can be added.

## API USAGE
API general use can be seen in files api.y, testingapi.py and toneanalyzer.py.
Tutorials and API references can be seen in API documentation at Bluemix account.

## Author
Nitin Sethi  
[Github](https://www.github.com/setin666)
[E-Mail](nitinsethi.iitr@gmail.com)
