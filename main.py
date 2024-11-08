import cv2
import numpy as np

img = cv2.resize(cv2.imread("image.jpg",0),(500,500))/255

def input_value():
    value=int(input())
    return value

def more_bright(value):
    print("Enter a value")
    input_value(value)
    h,w=np.shape(img)
    for col in range(w):
        for row in range(h):
            img[col][row]=img[col][row]*value
    cv2.imshow("Bright Image",img)
    

def more_dark(value):
    print("Enter a value")
    input_value(value)
    h,w=np.shape(img)
    for col in range(w):
        for row in range(h):
            img[col][row]=img[col][row]/value
    cv2.imshow("Dark Image",img)
    
def negative():
    h,w=np.shape(img)
    for col in range(w):
        for row in range(h):
            img[col][row]=1-img[col][row]



# cv2.imshow("Log Transformation", log_img)
# cv2.imshow('Original', original)
# cv2.imshow('Negative', img)
# cv2.waitKey()
# cv2.destroyAllWindows()