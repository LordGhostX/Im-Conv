from random import randint
from PIL import Image
from io import BytesIO
import base64

def clean_base64(data):
    return data.split(",")[1]

def converter(img_token, orig_ext, extension="PNG", rand_min=1, rand_max=10000):
    img_token = clean_base64(img_token)
    img = Image.open(BytesIO(base64.b64decode(img_token)))

    filename = '{}-{}-{}-{}'.format(randint(rand_min, rand_max), randint(rand_min, rand_max), randint(rand_min, rand_max), randint(rand_min, rand_max))

    img.save(filename + "." + extension.lower(), extension.lower())
    return filename
