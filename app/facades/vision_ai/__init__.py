from google.cloud import vision
from google.oauth2.service_account import Credentials
import app.config as config

credentials = Credentials.from_service_account_file(config.cred_path)
client = vision.ImageAnnotatorClient(credentials=credentials)
