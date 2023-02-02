import cv2
import imutils
import numpy as np
import pyautogui
from bindglobal import BindGlobal
import datetime
from playsound import playsound
from matplotlib import pyplot as plt
import os
import glob
import time

# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
methods = ['cv2.TM_CCOEFF_NORMED']

# Функция вычисления хэша
def CalcImageHash(FileName):
    image = cv2.imread(FileName)  # Прочитаем картинку
    resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)  # Уменьшим картинку
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Переведем в черно-белый формат
    avg = gray_image.mean()  # Среднее значение пикселя
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  # Бинаризация по порогу

    # Рассчитаем хэш
    _hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x, y]
            if val == 255:
                _hash = _hash + "1"
            else:
                _hash = _hash + "0"

    return _hash


def CompareHash(hash1, hash2):
    l = len(hash1)
    i = 0
    count = 0
    while i < l:
        if hash1[i] != hash2[i]:
            count = count + 1
        i = i + 1
    return count


for elementsNew in range(10):
    newNumber = elementsNew + 1
    imagename = 'images/result/element-' + str(newNumber) + '.png'
    print(imagename)
    img = cv2.imread(imagename, cv2.IMREAD_COLOR)

    for elementsDef in range(5):
        # elementname = 'images/elements/new_element_' + str(elementsDef) + '.png'
        elementname = 'images/elements/inner' + str(elementsDef) + '.png'
        print(elementname)

        template = cv2.imread(elementname, cv2.IMREAD_COLOR)
        w, h = template.shape[::-2]

        for meth in methods:
            method = eval(meth)

            res = cv2.matchTemplate(img, template, method)
            # res = cv2.matchTemplate(template, img, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(img, top_left, bottom_right, 255, 2)
            plt.subplot(121), plt.imshow(res, cmap='gray')
            plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            plt.subplot(122), plt.imshow(img, cmap='gray')
            plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            plt.suptitle(meth)
            plt.show()

            print(meth + ': ', newNumber, elementsDef, min_val, max_val, min_loc, max_loc)
            print('----')
        print('||||||||||||||||||||||||||||||||||||')
    print(' ')
    print(' ')

image = cv2.imread('images/result/element-1.png', cv2.IMREAD_COLOR)
method = cv2.TM_CCOEFF_NORMED
threshold = 0.90

ElementsImg = dict()
for i in range(5):
    # ElementData = dict()
    template = cv2.imread('images/elements/new_element_' + str(i) + '.png', cv2.IMREAD_COLOR)
    ElementsImg.update({i: template})

# print(ElementsImg)

# for elementIndex in ElementsImg:
#     Element = ElementsImg[elementIndex]
#     # print('ELEMENT #'+str(elementIndex)+':')
#     # print(Element)
#
#     res = cv2.matchTemplate(image, Element, method)
#     max_val = 1
#     while max_val > threshold:
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#         if max_val > threshold:
#             XX = max_loc[0] + 22
#             YY = max_loc[1] + 22
#             print('Найдено совпадение №' + str(elementIndex) + ' на ', XX, YY)
#         else:
#             print('Совпадений на №' + str(elementIndex) + ' нет')

cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
