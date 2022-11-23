import firebase_admin
from firebase_admin import credentials, storage
import numpy as np
import cv2
import time
from io import BytesIO
from PIL import Image

cred = credentials.Certificate(open('../Firebase_Key.txt', 'r'))
if not app:
    app = firebase_admin.initialize_app(cred, {
        'storageBucket': 'esp32-38197.appspot.com',
    }, name='storage')

bucket = storage.bucket(app=app)

def get_enter_image():
    try:
        blob = bucket.get_blob("data/enter.jpg")
        if blob:
            arr = (blob.download_as_string(), np.uint8) #array of bytes
            img = Image.open(BytesIO(blob.download_as_bytes()))
            return img
    except:
        print('error404')
    time.sleep(1)