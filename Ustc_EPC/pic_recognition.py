import pytesseract
from PIL import Image

def image_grayscale_deal(image):
    image = image.convert('L')
    # image.show()
    return image

def image_thresholding_method(image):
    threshold = 160
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image=image.point(table, '1')
    # image.show()
    return image

for i in range(40):
    image = Image.open('./image/checkcode'+str(i)+'.bmp')
    # image=image_grayscale_deal(image)
    # image=image_thresholding_method(image)
    # image = image.resize((image.width*10, image.height*10),Image.ANTIALIAS)
    # image.show()
    pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

    # image = Image.open('./image/1.jpg')
    vcode = pytesseract.image_to_string(image)
    print (vcode)
