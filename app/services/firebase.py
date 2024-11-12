import pyrebase


config = {
  "apiKey": "PUT-YOUR-API-KEY-HERE",
  "authDomain": "sentia-ae613.firebaseapp.com",
  "storageBucket": "sentia-ae613.firebasestorage.app",
  "databaseURL": "https://sentia-ae613-default-rtdb.firebaseio.com/",
  "serviceAccount": "./app/services/PUT-YOUR-CONFIG-KEY-HERE.json"
}


firebase = pyrebase.initialize_app(config)

db = firebase.database()


#auth = firebase.auth()