# Customer Care App for IBM
A customer care app for IBM which help in priority sorting of complaints recieved by IBM for the bluemix cloud service. This app uses API provided by the bluemix cloud solutions and sorts the complaints according to an algorithm based on different parameters such as severity of the complaint as well as the details of the client.

### Prerequisites
> Django  
> Watson Developer Cloud  
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
Add features and further development plans here

## API USAGE
Put api usage here

## Author
Nitin Sethi  
[Github](https://www.github.com/setin666)