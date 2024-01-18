import os
import cv2

capture = cv2.VideoCapture(0)
detail = .2
screenX = round(detail * capture.get(cv2.CAP_PROP_FRAME_WIDTH))
screenY = round(detail * capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

def row_to_ascii(row):
    order = (' ', '.', "'", ',', ':', ';', 'c', 'l',
             'x', 'o', 'k', 'X', 'd', 'O', '0', 'K', 'N')

    return tuple(order[int(x / (255 / 16))] for x in row)[::-1]

def whole_to_ascii(inFrame):
    return tuple(row_to_ascii(row) for row in inFrame)

while cv2.waitKey(1):
    ret,frame = capture.read()
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    newFrame = cv2.resize(grayFrame, (int(screenX), int(screenY)))

    fianlFrame = whole_to_ascii(newFrame)
    os.system("clear")
    print("\n".join((''.join(row) for row in fianlFrame)), end='')

    cv2.imshow('frame',newFrame)