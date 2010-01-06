import os
#settings for where to get ical file from
url = "http://localhost:8008/calendars/users/admin/calendar/"
user = "admin" 
passwd = "admin"

def retrive():
	os.system("wget --user "+user+" --password "+passwd+" "+url+" -O calender.ical")

if __name__ == "__main__":
	retrive()
