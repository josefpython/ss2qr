from PIL import Image, ImageGrab
from pyzbar import pyzbar
import sys

def main(args):

    if len(args) > 0:
        imgSrc = args[0]
        im = Image.open(imgSrc)
    else:
        im = ImageGrab.grabclipboard()
    
    dcd = pyzbar.decode(im)
    print(dcd[0][0].decode("utf-8"))

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:
        print("Something went wrong\nContent in clipboard may not be an image")