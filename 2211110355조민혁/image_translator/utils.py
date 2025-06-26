import easyocr
import numpy as np
from PIL import Image
import qrcode

reader = easyocr.Reader(['en', 'ko'])

def extract_text_from_image(uploaded_file):

    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)


    result = reader.readtext(image_np)
    texts = [text[1] for text in result]
    return " ".join(texts)



def generate_qr_code(data, filename="qr_code.png"):
    img = qrcode.make(data)
    img.save(filename)
    return filename