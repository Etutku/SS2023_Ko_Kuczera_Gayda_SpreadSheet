#Add Admin SDK to connect with Firebase real-time database

#Create the database reference

#cred = initialize a credential from a JSON certificate keyfile(serviceAccountKey.py)
#initialize and return a new App instance

#ref = reference path to the database

#Personal details in a dictionary format(json)
"""
data = {
  "id" : 
      { 
          "name": String,
          "date_of_birth": String,
          "address": String,
          "phone_number": String,
          "email": String,
          "total_attendance": int,
          "last_attendance_time": datetime
  }
}
"""

#Send data to database
"""
unzip dictionary :
  send data to specific directory in the database and set the value
"""



import firebase_admin
from firebase_admin import credentials

from firebase_admin import db 

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-b9b88-default-rtdb.europe-west1.firebasedatabase.app/"
})

ref = db.reference('Students')

data = {
    "414147":
        {
            "name": "Eunseo Ko",
            "date_of_birth": "2001-01-13",
            "address": "aleja Adama Mickiewicza 30",
            "phone_number": "497 284 303",
            "email": "eunseo@student.agh.edu.pl",
            "total_attendance": 14,
            "last_attendance_time": "2023-04-03 19:23:34"
        },
    "412398":
        {
            "name": "Małgorzata Kuczera",
            "date_of_birth": "2002-04-18",
            "address": "Kraków, ul. Warszawska 24",
            "phone_number": "458 289 982",
            "email": "mkuczera@student.agh.edu.pl",
            "total_attendance": 11,
            "last_attendance_time": "2023-04-04 20:51:47"
        },
    "414151":
        {
            "name": "Edibe Tutku Gayda",
            "date_of_birth": "2002-06-12",
            "address": "Krakow, Biprostal",
            "phone_number": "+48 001 000 000",
            "email": "gayda@student.agh.edu.pl",
            "total_attendance": 23,
            "last_attendance_time": "2023-04-02 20:31:56"
        }
}

for key, value in data.items():
    ref.child(key).set(value)