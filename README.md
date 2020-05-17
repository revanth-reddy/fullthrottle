
# Backend FullThrottle
## Steps :
* Clone the Repo
* Activate the virtual environment using:  source myvenv/bin/activate
* install packages using:  pip install -r requirements.txt
* run django server using:  python manage.py runserver
* visit [http://127.0.0.1:8000/members/](http://127.0.0.1:8000/members/) to see the member data at the endpoint.

## Custom Commands
Two custom commands are made
* To Save Member data at first
* To Save Activity Period dDataof the Member

### Saving Member Data:
In terminal change directory to manage.py then execute the commands :
* python manage.py save_member_data  <_id_> <_name_> <_timezone_>
#### For Example: python manage.py save_member_data W012 Egon Spengler America/Los_Angeles

Here the name requires two words ("Egon" "Spengler") just like First Name and Last Name.

### Saving Activity Period of Member :
* python manage.py save_activity_data <_id_> <_start_time_> <_end_time_>

#### For Example: python manage.py save_activity_data W012 Mar 16 2020  5:33PM Mar 16 2020 8:02PM

Here the time format is Month<_space_>DD<_space_>YYYY<_space_>HH:MMAM

Also the id of the member must exist before i.e. it must be already added to database using the previous command.

You can see the newly added data at the endpoint

##