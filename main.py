import cv2
import numpy as np

img = cv2.resize(cv2.imread("image.jpg",0),(500,500))/255

def input_value():
    value=int(input())
    return value

def more_bright(value):
    print("Enter a value")
    input_value(value)
    image=np.copy(img)
    h,w=np.shape(image)
    for col in range(w):
        for row in range(h):
            image[col][row]=image[col][row]*value
    cv2.imshow("Bright Image",image)
    

def more_dark(value):
    print("Enter a value")
    input_value(value)
    image=np.copy(img)
    h,w=np.shape(image)
    for col in range(w):
        for row in range(h):
            image[col][row]=image[col][row]/value
    cv2.imshow("Dark Image",image)
    
def negative():
    image=np.copy(img)
    h,w=np.shape(image)
    for col in range(w):
        for row in range(h):
            image[col][row]=1-image[col][row]
    cv2.imshow("Image",image)
def power_law(value):
    gamma_value=input_value(value)
    image=np.copy(img)
    h,w=np.shape(img)
    for col in range(w):
        for row in range(h):
            image[col][row]=(2*image[col][row])**gamma_value
    cv2.imshow("Image",image)



# cv2.imshow("Log Transformation", log_img)
# cv2.imshow('Original', original)
# cv2.imshow('Negative', img)
# cv2.waitKey()
# cv2.destroyAllWindows()