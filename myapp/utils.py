from myapp.models import *
import jwt 
from django.conf import settings
import pytz 
from datetime import datetime, timedelta
import json
from werkzeug.utils import secure_filename
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import secrets 
import bcrypt
from datetime import timedelta
from django.utils import timezone

secret_key = settings.SECRET_KEY



def current_pst_to_utc():
    return timezone.now()

def generate_jwt_token(user):
    secret_key = settings.SECRET_KEY  # Use your secret key
    expiration_time = current_pst_to_utc() + timedelta(hours=12)
    payload = {
        'emp_id': user.emp_id,
        'exp': expiration_time.timestamp()  # Ensure this is a timestamp
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token



# def generate_jwt_token(user):
#     expiration_time = current_pst_to_utc() + timedelta(hours=12)
#     payload = {
#         'emp_id': user.emp_id,
#         'exp': expiration_time
#     }
#     token = jwt.encode(payload, secret_key, algorithm='HS256')
#     return token



# def current_pst_to_utc():
#     """
#     Convert the current PST time to UTC.

#     Returns:
#     str: Current time in UTC as a string in the format 'YYYY-MM-DD HH:MM:SS'
#     """
#     pst_zone = pytz.timezone('US/Pacific')
#     utc_zone = pytz.timezone('UTC')

#     current_pst_time = datetime.now(pst_zone)

#     utc_time = current_pst_time.astimezone(utc_zone)
    
#     return utc_time
