import firebase_admin
from firebase_admin import credentials, storage
import numpy as np
import cv2
import time
from io import BytesIO
from PIL import Image

fb_id = {
  #credenciais
}

cred = credentials.Certificate(fb_id)

app = None

if not app:
    app = firebase_admin.initialize_app(cred, {
        #credenciais
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
        print()
        return None