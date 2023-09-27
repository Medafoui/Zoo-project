CONTRIBUTORS

	- MOHAMED AFIF CHIFAOUI - 100452024
	- DIMITAR-DELYAN ILEV   - 100491346



TEMPLATES used

1) animal and animals to display information of corresponding animal
2) activity and activities to see activities offered by the zoo
3) login and register for accounts creation
4) base and home to display main page for unauthenticated users
5) reservation of an activity 
6) reservations table and customer where user can see his history of bookings
7) scheduled table so customer can see available scheduled activities when booking
8) featured so a manager can mark/unmark an activity
9) delete and manager_edit for the additional functionality
10) manager_add template is used to create a new activity
11) manager template is used to select an existing activity and schedule it 






USERS to try

	- Customer 1

		email: customer1@gmail.com
		password: 123
	

	- Customer 2

		email: uc3mzoo@gmail.com
		password: webapps2022
	

	- Manager/administrator
	
		email:manager1@manager1.com
		password:123



ADDITIONAL FUNCTIONALITIES


We added a few additional functionalities in the following views:

1) Manager view:

	- A manager can edit the date of a scheduled date
	- A manager can delete a scheduled activity when it is still not reserved 		  by any customer

2) Confirmation email

Implemented in views.py (controllers file) where the customer can receive a confirmation email with details of the booked activity.


ADDITIONAL LIBRARIES 

1) Flask_Mail library for confirmation email



