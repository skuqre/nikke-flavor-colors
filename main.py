from PIL import Image
import pyscreenshot as pss
import pygetwindow as pgw
import pytesseract
import os
import pyautogui as pag
from dotenv import load_dotenv
from time import sleep
import win32gui
import cv2
import json

load_dotenv()

WINDOW_NAME = "NIKKE"

pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_LOCATION')

def main():
    FIRST_NIKKE = None
    SECONDS_BEFORE_START = 5

    rei_passed = False

    color_table = {}

    while SECONDS_BEFORE_START > 0:
        print("Starting in " + str(SECONDS_BEFORE_START) + " seconds... Click on NIKKE now and wait for me to start...")
        SECONDS_BEFORE_START -= 1
        sleep(1);

    while True:

        # get the window
        window = pgw.getWindowsWithTitle(WINDOW_NAME)[0]

        # get the window coordinates
        x, y, w, h = window.left, window.top, window.width, window.height

        # box coords
        bx, by, bw, bh = (530/1452) * w, (550/817) * h, (w / 1452) * 190, (h / 817) * 39

        # final coords
        x1, y1, x2, y2 = x + bx, y + by, x + bx + bw, y + by + bh

        ss = pss.grab(bbox=(round(x1), round(y1), round(x2), round(y2)))
        ss.save(__file__ + '\..\\name.png')

        # perform edits
        img = cv2.imread((__file__ + '\..\\name.png'));
        edit = cv2.convertScaleAbs(img, alpha=1.5, beta=5)
        cv2.imwrite((__file__ + '\..\\name.png'), edit)

        # color coords
        cx, cy, cw, ch = (724/1452) * w, (568/817) * h, (w / 1452) * 10, (h / 817) * 10

        cs = pss.grab(bbox=(round(x + cx), round(y + cy), round(x + cx + cw), round(y + cy + ch)))
        cs.save(__file__ + '\..\\color.png')

        # get color
        pixels = Image.open(__file__ + '\..\\color.png').getcolors()
        color = None
        maxcount = 0

        # get all colors
        for c in pixels:
            if maxcount < c[0]:
                color = c[1]
                maxcount = c[0]

        text = pytesseract.image_to_string(Image.open(__file__ + '\..\\name.png'), config='--psm 7')

        if text.strip() == "Rei":
            if rei_passed:
                text = "Rei Ayanami"
            else:
                rei_passed = True
        
        print("WHO: " + text + "\nCOLOR: " + str('#%02x%02x%02x' % color))

        if text == FIRST_NIKKE:
            break
        else:
            color_table[text.strip()] = '#%02x%02x%02x' % color

        if FIRST_NIKKE == None:
            FIRST_NIKKE = text

        win32gui.SetForegroundWindow(win32gui.FindWindow(None, WINDOW_NAME))
        pag.click(x + w - 32, y + round(h / 2) + 32, button='left')

        with open(__file__ + '\..\\colors.json', 'w') as f:
            json.dump(color_table, f, indent='\t')

        sleep(0.3)

    print(color_table)

if __name__ == "__main__":
    main()