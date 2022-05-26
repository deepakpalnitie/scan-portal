import config
from datetime import datetime
from mongoengine import *

connect(host=config.DB_URI)

class Scan(Document):
  filepath = StringField(required=True)
  submitter = StringField(required=True)
  submitted_at = DateTimeField(default=datetime.utcnow)
  reference_id: StringField (required=True) # (Reference of current result/prediction)
  results: StringField (required=True) # JSON String (Whatever prediction we are get from the model)
  results_user: StringField (required=True) # JSON String (What we finally show to the user after processing/modifying the model's result)
  rating: IntField # Int (on a scale of 1-5, provided by the user)
  result_path: StringField (required=True) #(Result Image path)
  model_ver: StringField (required=True) # String (Model version used for current scan prediction)
  
  meta = {
    "indexes": [
      ("submitter", "-submitted_at")
    ]
  }


class User(Document):
  phone_number = StringField(required=True)
  joined_at = DateTimeField(default=datetime.utcnow)
  
