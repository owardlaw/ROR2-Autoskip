import pyautogui
import cv2
import numpy as np
import pytesseract
import time 


beatle = 14
stone = 0
while True:
    # Capture screenshot from a region
    # screenshot = pyautogui.screenshot(region=(1170, 360, 210, 150)) # x,y,w,h POS for RoR2
    screenshot = pyautogui.screenshot(region=(2190, 505, 65, 60)) # x,y,w,h POS for RoR2

    # Convert the PIL(Pillow) image to OpenCV format (numpy array), and then convert RGB to BGR
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    cv2.imwrite(f"monster/stone/stone-enity-{time.time()}.jpg",screenshot)
    stone += 1
    if stone == 75:
        print("done")
        break
    time.sleep(0.2)

    # If 'q' is pressed on the keyboard, break the loop and close the window
    if cv2.waitKey(1) == ord('q'):
        break

# Close the OpenCV window
cv2.destroyAllWindows()
