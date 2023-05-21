from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\new_program\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string(Image.open('bridge_game.JPG')))