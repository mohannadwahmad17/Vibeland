from secrets.secrets import PATH_TO_FIREBASE_SERVICE_ACCOUNT_KEY, FIREBASE_DATABSE_URL
from constants.constants import FIREBASE_ROOT_NODE_REF, FIREBASE_USER_TOKEN_REF, FIREBASE_USERS_NODE_NAME
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
import json
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, PATH_TO_FIREBASE_SERVICE_ACCOUNT_KEY)

# Use a service account
if not firebase_admin._apps:
    cred = credentials.Certificate(filename)
    firebase_admin.initialize_app(cred, {'databaseURL': FIREBASE_DATABSE_URL})

#db = firestore.client()
db_ref = db.reference(FIREBASE_ROOT_NODE_REF)

def writeJsonToRealtimeDatabase(data):
    pass

#Retrieve the user's access token
def getUserAccessToken(username):
    db_ref.child(FIREBASE_USERS_NODE_NAME).child(username).get(FIREBASE_USER_TOKEN_REF)

#Update the user's access token
def updateUserAccessToken(username, token):
    db_ref.child(FIREBASE_USERS_NODE_NAME).child(username).child(FIREBASE_USER_TOKEN_REF).update(token)