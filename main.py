from PIL import Image
import pytesseract
import os




#image = Image.open('image-to-text.png')

#text = pytesseract.image_to_string( image )



dirtolist = '/Users/erickmunz/Documents/DEV/python/OCR/video/out/'

dirs = os.listdir(dirtolist)

imgs = [i for i in dirs if i.endswith('jpg')]

print(imgs)

for i in imgs:
    print(f'convirtiendo imagen ... {i}')
    img = Image.open(dirtolist+'/'+str(i))
    text = pytesseract.image_to_string(img)
    with open('./out/part3.txt','+a') as file:
        file.write("######################################### \n")
        file.write(text+"   \n")
        print("borrando...")
        os.remove(dirtolist+'/'+str(i))