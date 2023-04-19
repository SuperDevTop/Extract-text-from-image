from PIL import Image
from pytesseract import pytesseract
import os

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

#Define path to images folder
path_to_images = r'images/'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract
filenames = os.listdir(path_to_images)

i = 0

#Get the file names in the directory
for file_name in filenames:
    
    i += 1
    print(str(i) + ' page\n')
    img = Image.open(path_to_images + file_name)

        #Extract text from image
    text = pytesseract.image_to_string(img)

    file = open(str(i) + '.txt', 'w')
    file.write(text)
    file.close()

    print(text)


# img = Image.open('images/2.png')

# #         #Extract text from image
# text = pytesseract.image_to_string(img)
# print(text)