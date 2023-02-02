#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ME2AutoCrackerUI import Ui_me2
import res_rc

# ПРЕДУСТАНОВКА
bg = BindGlobal()
method = cv2.TM_CCOEFF_NORMED
element_ss_w = 100
# ЧУВСТВИТЕЛЬНОСТЬ ПОИСКА
threshold = 0.90
threshold2 = 0.70
MAINMODE = 0

progmode = 0
progmodename = 'progmode.txt'
if not os.path.exists(progmodename):
    f = open(progmodename, 'w')
    f.write('0')
    f.close()

ElementsImg = dict()
for i in range(5):
    # ElementData = dict()
    template = cv2.imread('images/elements/new_element_' + str(i) + '.png', cv2.IMREAD_COLOR)
    ElementsImg.update({i: template})

# print(ElementsImg)
print('LISTENING COMMAND')


def callback(event):
    # ПРОВЕРКА РЕЖИМА
    f = open(progmodename)
    progmode = int(f.read())

    # ЗАГРУЗКА ШАБЛОНА
    template = cv2.imread('images/element_hidden.png', cv2.IMREAD_COLOR)
    h, w = template.shape[:2]
    print('template.shape (w,h): ', w, h)

    # ОЧИСТКА ПАПКИ С ПРОМЕЖУТОЧНЫМИ СКРИНШОТАМИ
    # files = glob.glob('images/result/*')
    # for f in files:
    #     os.remove(f)

    # ТЕКУЩАЯ ВРЕМЕННАЯ МЕТКА
    now = datetime.datetime.now()
    dt = now.strftime("%d-%m-%Y %H.%M.%S")

    if progmode == 1:
        print('СКРИНШОТ')
        # СКРИНШОТ
        ss = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(ss), cv2.COLOR_RGB2BGR)
        image = cv2.cvtColor(np.array(image), cv2.IMREAD_COLOR)

    if progmode == 0:
        print('ТЕСТФАЙЛ')
        # ТЕСТФАЙЛ
        image = cv2.imread('images/main_screen.png', cv2.IMREAD_COLOR)

    # ПОИСК ПАТТЕРНОВ
    res = cv2.matchTemplate(image, template, method)

    N = 0

    # СОЗДАНИЕ СЛОВАРЯ
    MainData = dict()
    PrintData = dict()
    index = 0

    # ЗАРИСОВКА
    max_val = 1
    while max_val > threshold:
        ElementData = dict()
        ElementData['x'] = 0
        ElementData['y'] = 0
        ElementData['img'] = 0
        ElementData['label'] = -1

        PrintElement = dict()
        PrintElement['x'] = 0
        PrintElement['y'] = 0
        PrintElement['label'] = -1

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val > threshold:
            N += 1
            XX = max_loc[0] + 22
            YY = max_loc[1] + 22
            print('Найдено совпадение №' + str(N) + ' на ', XX, YY)

            if progmode == 1:
                pyautogui.moveTo(XX, YY)

            ElementData['x'] = XX
            ElementData['y'] = YY
            PrintElement['x'] = XX
            PrintElement['y'] = YY

            element_ss_coords = (XX - element_ss_w / 2, YY - element_ss_w / 2, element_ss_w, element_ss_w)

            print('Прямоугольник скрина элемента №' + str(N) + ': ', element_ss_coords)

            if progmode == 1:
                pyautogui.click(button='right')

            res[max_loc[1] - h // 2:max_loc[1] + h // 2 + 1, max_loc[0] - w // 2:max_loc[0] + w // 2 + 1] = 0
            # image = cv2.rectangle(image, (max_loc[0], max_loc[1]), (max_loc[0] + w + 1, max_loc[1] + h + 1), (0, 0, 255, 3))

            element_ss = pyautogui.screenshot(
                region=element_ss_coords)
            element_ss_rgb = cv2.cvtColor(np.array(element_ss), cv2.COLOR_RGB2BGR)
            element_ss_irc = cv2.cvtColor(np.array(element_ss_rgb), cv2.IMREAD_COLOR)
            ElementData['img'] = element_ss_irc
            ssname = 'element-' + str(N) + '.png'
            cv2.imwrite('images/result/' + ssname, element_ss_irc)

            MainData[index] = ElementData
            PrintData[index] = PrintElement
            index += 1

    cv2.imwrite('images/result/result-' + dt + '.png', image)
    print('done')
    #

    print('HERE NEXT STAGE')

    for elementsNew in range(10):
        newNumber = elementsNew + 1
        imagename = 'images/result/element-' + str(newNumber) + '.png'
        # print(imagename)
        img = cv2.imread(imagename, cv2.IMREAD_COLOR)

        for elementsDef in range(5):
            # elementname = 'images/elements/new_element_' + str(elementsDef) + '.png'
            elementname = 'images/elements/inner' + str(elementsDef) + '.png'
            # print(elementname)

            template = cv2.imread(elementname, cv2.IMREAD_COLOR)

            res = cv2.matchTemplate(img, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            if max_val > threshold2:
                print(str(newNumber) + ' = ' + str(elementsDef) + ' (' + str(max_val) + ')')
                MainData[elementsNew]['label'] = elementsDef
                PrintData[elementsNew]['label'] = elementsDef
                break

    SortedMainData = list(MainData.items())
    SortedMainData.sort(key=lambda i: i[1]['label'])

    # print('SortedMainData:')
    #
    # print(SortedMainData)

    if len(SortedMainData) == 10:
        if progmode == 1:
            for SortedElement in SortedMainData:
                SortedElementData = SortedElement[1]
                # print(SortedElementData)
                clickX = SortedElementData['x']
                clickY = SortedElementData['y']
                pyautogui.moveTo(clickX, clickY)
                pyautogui.click(button='right')
                # time.sleep(1)
                pyautogui.click(x=clickX, y=clickY)
                # time.sleep(1)
        playsound('sounds/imdone.mp3')
    else:
        playsound('sounds/error.mp3')

    cv2.waitKey(0)

    # closing all open windows
    cv2.destroyAllWindows()

    print('LISTENING COMMAND')


def stopit(event):
    bg.stop()


bg.gbind("<Double-Alt_L>", callback)
bg.gbind("<Double-Control_L>", stopit)