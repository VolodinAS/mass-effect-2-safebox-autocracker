import cv2
import imutils
import numpy as np
import pyautogui
from bindglobal import BindGlobal
import datetime
from matplotlib import pyplot as plt
import os
import glob

bg = BindGlobal()
method = cv2.TM_CCOEFF_NORMED

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

anglelt = (195, 205)
anglerb = (1500, 1243)


# testimage = cv2.imread('images/main_screen.png')


def callback(event):
    template = cv2.imread('images/defect_element_cut_1.png', 0)
    files = glob.glob('images/result/*')
    for f in files:
        os.remove(f)

    now = datetime.datetime.now()
    dt = now.strftime("%d-%m-%Y %H.%M")
    # СКРИНШОТ
    # ss = pyautogui.screenshot(region=(0, 0, 2560, 1440))
    # img_gray = cv2.cvtColor(np.array(ss), cv2.COLOR_BGR2GRAY)

    # ТЕСТФАЙЛ
    img_rgb = cv2.imread('images/main_screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    w, h = template.shape[::-1]
    print(w, h)
    res = cv2.matchTemplate(img_gray, template, method)
    threshold = 0.99
    loc = np.where(res >= threshold)
    n = 1
    oldpt = 0

    for pt in zip(*loc[::-1]):

        if oldpt == 0:
            oldpt = pt

            cv2.rectangle(img_gray, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            cv2.line(img_gray, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            cv2.line(img_gray, (pt[0] + w, pt[1]), (pt[0], pt[1] + h), (0, 0, 255), 2)
        else:
            abs0 = abs(pt[0] - oldpt[0])
            abs1 = abs(pt[1] - oldpt[1])
            # print('abs01:', abs0, abs1)
            if abs0 < 5 or abs1 < 5:
                continue
            else:
                cv2.rectangle(img_gray, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                cv2.line(img_gray, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                cv2.line(img_gray, (pt[0] + w, pt[1]), (pt[0], pt[1] + h), (0, 0, 255), 2)
            oldpt = pt
        n = n + 1

    cv2.imwrite('images/result.png', img_gray)

    print('done')
    cv2.waitKey(0)

    # closing all open windows
    cv2.destroyAllWindows()


def stopit(event):
    bg.stop()


bg.gbind("<Double-Alt_L>", callback)
bg.gbind("<Double-Control_L>", stopit)
