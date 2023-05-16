
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-b9b88-default-rtdb.europe-west1.firebasedatabase.app/"
})

ref = db.reference('Students')

data = {
    "0000":
        {
            "name": "Elon Musk",
            "date_of_birth": "1971-06-28",
            "address": "USA",
            "phone_number": "999 000 000",
            "email": "someemail@gmail.com",
            "total_attendance": 1,
            "last_attendance_time": "2023-04-10 17:35:43"
        },
    "412398":
        {
            "name": "Malgorzata Kuczera",
            "date_of_birth": "2002-04-18",
            "address": "Kraków, ul. Warszawska 24",
            "phone_number": "000 000 100",
            "email": "mkuczera@student.agh.edu.pl",
            "total_attendance": 21,
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
        },
    "414147":
        {
            "name": "Eunseo Ko",
            "date_of_birth": "2001-01-13",
            "address": "aleja Adama Mickiewicza 30",
            "phone_number": "497 284 303",
            "email": "eunseo@student.agh.edu.pl",
            "total_attendance": 14,
            "last_attendance_time": "2023-04-03 19:23:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
