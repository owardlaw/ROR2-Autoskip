import pyautogui
import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
import time 

def reset():
    pyautogui.keyDown('win')
    pyautogui.keyDown('ctrl')
    pyautogui.press('`')
    pyautogui.keyUp('win')
    pyautogui.keyUp('ctrl')

    # # Simulate typing "exec reset" and pressing Enter
    pyautogui.typewrite("exec reset")
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.press('`')

while True:
    # Capture screenshot from a region
    screenshot = pyautogui.screenshot(region=(1170, 360, 210, 150)) # x,y,w,h POS for RoR2
    # screenshot = pyautogui.screenshot(region=(2190, 505, 65, 60)) # x,y,w,h POS for RoR2

    # Convert the PIL(Pillow) image to OpenCV format (numpy array), and then convert RGB to BGR
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    custom_config = r'-l eng --oem 3 --psm 6' 
    text = pytesseract.image_to_string(screenshot,config=custom_config)
    print(text)

    if "Titanic" in text:
        print(text)
        reset()

    # Display the image
    cv2.imshow('Screenshot', screenshot)

    # If 'q' is pressed on the keyboard, break the loop and close the window
    if cv2.waitKey(1) == ord('q'):
        break

# Close the OpenCV window
cv2.destroyAllWindows()
