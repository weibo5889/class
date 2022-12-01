from PIL import Image,ImageEnhance
import pytesseract
import numpy as np
import cv2
from matplotlib import pyplot as plt
def code_pa():
    pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    img = Image.open('te.jpg')
    code = pytesseract.pytesseract.image_to_string(img)
    return code
code_pa()