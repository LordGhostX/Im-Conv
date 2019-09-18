from random import randint
import base64
import re

def decode_base64(data, altchars=b'+/'):
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'='* (4 - missing_padding)
    return base64.b64decode(data, altchars)

def converter(img_token, orig_ext, extension="PNG", rand_min=1, rand_max=10000):
    imgdata = decode_base64(img_token.encode())
    filename = '{}-{}-{}-{}.{}'.format(randint(rand_min, rand_max), randint(rand_min, rand_max), randint(rand_min, rand_max), randint(rand_min, rand_max), orig_ext.lower())
    with open(filename, 'wb') as f:
        f.write(imgdata)

    return filename
