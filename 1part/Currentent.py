import cv2
import numpy as np
import pyautogui
import PIL.ImageGrab
import array
import win32gui
import time
from matplotlib import pyplot as plt

class Wndowsize:
    x=None
    y=None
    w=None
    h=None
    def callback(self,hwnd, extra):
        rect = win32gui.GetWindowRect(hwnd)
        s="poker.txt"
        if not win32gui.GetWindowText(hwnd).find(s):
            self.x = rect[0]
            self.y = rect[1]
            self.w = rect[2] #- self.y
            self.h = rect[3] #- self.x
            print ("Window %s:" % win32gui.GetWindowText(hwnd))
            print ("\tLocation: (%d, %d)" % (self.x, self.y))
            print ("\t    Size: (%d, %d)" % (self.w, self.h))
            return hwnd

call=Wndowsize()
win32gui.EnumWindows(call.callback,None)

#h,w=pyautogui.size()
print(call.x,call.y,call.h,call.w)
#test(call.x,call.y,call.h,call.w)
box = (call.x,call.y,call.w,call.h)
screen = PIL.ImageGrab.grab(box)
img_rgb = np.array(screen)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template=[]
for i in range(3):
    print(str(i))
    template.append(cv2.imread(str(i+1)+'.png'))
#    print(template[i].shape[:-1])
#template = cv2.imread('xx.png')
    w, h = template[i].shape[:-1]
    print(template[i].shape[:-1])
    x = cv2.cvtColor(template[i], cv2.COLOR_BGR2GRAY)

    point=[]
    res = cv2.matchTemplate(img_gray, x,cv2.TM_CCOEFF_NORMED)
    threshold = .9
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        pyautogui.moveTo(pt)
    #    pyautogui.click()
        cv2.rectangle(img_rgb, pt, (pt[0] + h, pt[1] + w), (0, (i+1)*255, i*255), 2)
    #    time.sleep(0.5)
        res = cv2.matchTemplate(img_gray, x,cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        point.append(pt)
        print(pt)
    print(point)
cv2.imshow("result",img_rgb)
cv2.imwrite('result.png', img_rgb)

def test(x,y,h,w):
    h,w=pyautogui.size()
    box=(x,y,h,w)
#сделать авто только для окно/\
    screen = PIL.ImageGrab.grab(box)
    #скріншот
    img_rgb = np.array(screen)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    colodas=[]
    point=[]
    for i in range(52):
        colodos.append(cv2.imread(str(i)+'.png'))
#        template = cv2.imread('xx.png')
        w, h = colodos[i].shape[:-1]
        x = cv2.cvtColor(colodos[i], cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, x,cv2.TM_CCOEFF_NORMED)
        threshold = .6
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):  # Switch collumns and rows
    #        cv2.rectangle(img_rgb, pt, (pt[0] + h, pt[1] + w), (0, 0, 255), 2)
        #    time.sleep(0.5)
        #находім  і заносім
            point.append(i)
            print(pt)
            point.append(pt)
    #    cv2.imwrite('result.png', img_rgb)
    return pt
