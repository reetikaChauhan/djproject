from firebase import firebase
# Get a database reference to our blog.
import firebase_admin
from firebase_admin import credentials

if (not len(firebase_admin._apps)):
    cred = credentials.Certificate('service-account.json')
    default_app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://fproject-97fa3.firebaseio.com/'})

fbconn = firebase.FirebaseApplication('https://fproject-97fa3.firebaseio.com//')
# To get Data from fireBase

result = fbconn.get('/MyInfo', None)
print(result)