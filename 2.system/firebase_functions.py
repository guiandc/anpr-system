import firebase_admin
from firebase_admin import credentials, storage
import numpy as np
import cv2
import time
from io import BytesIO
from PIL import Image

fb_id = {
  "type": "service_account",
  "project_id": "esp32-38197",
  "private_key_id": "a4ab817807d8cb934d7c106f568843cb36e462b6",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDER+V/K6sP8OED\nWPH8hhCuMGmi4tZVM8EJgeIyQs1MmHgJtureETS5RLTfoWW3YWyI410lg7M2nzWw\n7oMzpHhy/+dp1uPHj/JpyAKI9sE/m8jLXZOP0hWc8uUNrVDtNalnMUBYM0jjH2Nn\n4vcOf1uLL3RDDZ4+MaWQsEFvn47kuRDQe5VjN4rpiNUiKBTDJ/hbCZWVjaZPhr2x\nZEtkFn6eLNk4QnjSWkd6zN4MOEqcEL6zmQMCOa8WfnAZvAoGSDt/YF12BUscDBxJ\n7P+Hxc2l5K6Y4WqoM0F5ELL/5GTv6q/Zm7m7OTrQ6dSSGycKH/wY9ZxBEO0VUAFN\nk+UsrLITAgMBAAECggEAEIWOw1QdK5PWlO4NPHjaeZcYpT3b1cMr+g1lSV7HIi3p\nWMP9ZCDlo7ytTu+qfLOmK6WbxxcdZDklj1WcVKIBA4kX5RhSBw/OU2ojEH1Yye5m\nifu/+oiwCgyGDE8s8zKjpkyGgoYamgef2fRIYH+G6KHfcu94BPsv2QyFDYzMPeNS\nN9t6+wJKOt28J71Xq+iZ7LF23Ivw6i4RwiRXlJEleKmRX6NpztFja0UnahT2UF9V\nCJqAUxenqBL4fpyGgUi1KCZcEcwHPtW8XXNqTggF8E0Qhp33TjQjBLzH1W+P4vhg\nrZbOSWoA3gfZao26cIK32SphvMecA417UmgN9kky2QKBgQDxgwNyAj9uxdi0O5kM\n/YrWo+rs0tySHFVO3hWqzwSbhFYggIvbDwwm+WVCWOJARCukXOWVzNKmtt8syDT6\nwp8rVAQvUHYN93xn0P0PlYfM3rVgGSvL78JkfjozV3Y4sQ6239GC6hfQ0VVD3Xba\ncvugEgG3v1+Z7TH4B0NG/I0aOQKBgQDQDkE5VFWJrJCYMGQhxV59s7bMra3JLb24\nyYLBHgcAyV5XlG5pIKRoizdcQJRGp+prtwnifvsCuXtdU0pDFfC9hseTytSvDaM1\norCap3F9/YDN1EMR3qLJN3QpGaqaHF3+9rRiwN/33FMiiq8Q1M8AcylPiPxNviwO\nhhUzaiWeqwKBgDPPIi8T8l2mDa3kVxnlTiJreZsiRPUHJPnNRKKm1Fs0UXGZgecV\nXEsEF0fbX3Xf6ejRkOLI1Ku08T1fGZZtp82YsWkg/qJSZBq1R4RPVJmLcSdTXwTZ\nwz7hoUSgT5kryndKnlxSMZe3QG5VlQiZwAb/teSgJjcUHjMSA8m3peFpAoGASlcd\nlRd+LOA9FjQMQ0jbl3y0b3QLaZvvc2yFTO2mwPAyxoZh4SxpsnU0BcGJeamcCHrx\njD2lAPc3jkQpf8kCKSZUf4l070unKo4EHm6ADe2brXAPuv3bGpy248yo+cHzEBwk\nnjiejljqV6hIH3J6uIVtmF6xEDJIWbQtNR7TbFsCgYAQC5B+Mmc3QPYCozpYtFcw\njPL2rqDdzqHDqpIMGm9ptoAbO1ywSlXtLRsK1uPWd62C0Cyh5/9+JJ0K/dmnF9Uu\n/uNRF3zQOtQWfgzs+XhPRt9LZAGltG2S+GmjKwXPN8iRgToI2bUJMZIF8xonBPUO\nB1CvisT0hLCQwCcJrDiUMg==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-880zy@esp32-38197.iam.gserviceaccount.com",
  "client_id": "109418049353316664463",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-880zy%40esp32-38197.iam.gserviceaccount.com"
}

cred = credentials.Certificate(fb_id)

app = None

if not app:
    app = firebase_admin.initialize_app(cred, {
        'storageBucket': 'esp32-38197.appspot.com',
    }, name='storage')

bucket = storage.bucket(app=app)

def get_image(image_path, image_name):
    try:
        blob = bucket.get_blob("{}/{}.jpg".format(image_path, image_name))
        if blob:
            arr = (blob.download_as_string(), np.uint8) #array of bytes
            img = Image.open(BytesIO(blob.download_as_bytes()))
            return img
    except:
        print('error404')
    time.sleep(1)
    
