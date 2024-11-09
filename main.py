import cv2
import numpy as np

img = cv2.resize(cv2.imread("image.jpg",0),(500,500))/255

def input_value():
    value=int(input())
    return value

def more_bright():
    print("Enter a value")
    value=input_value()
    image=np.copy(img)
    h,w=np.shape(image)
    for row in range(h):
        for col in range(w):
            image[row][col]=image[row][col]*value
    return image    

def more_dark():
    print("Enter a value")
    value=input_value()
    image=np.copy(img)
    h,w=np.shape(image)
    for row in range(h):
        for col in range(w):
            image[row][col]=image[row][col]/value
    return image    
def negative():
    image=np.copy(img)
    h,w=np.shape(image)
    for row in range(h):
        for col in range(w):
            image[row][col]=1-image[row][col]
    return image    
def power_law():
    gamma_value=input_value()
    image=np.copy(img)
    h,w=np.shape(img)
    for row in range(h):
        for col in range(w):
            image[row][col]=(2*image[row][col])**gamma_value
    return image
def log_transformation():
    scaling_factor_value=input_value()
    image=np.copy(img)
    h,w=np.shape(image)
    for row in range(h):
        for col in range(w):
            if image[row][col] > 0:
                image[row][col]=scaling_factor_value*(np.log2(image[row][col]))
            else:
                image[row][col]=0
    return image    

def average_filter():
    image=np.copy(img)
    h,w=np.shape(image)
    for row in range(1,h-1):
        for col in range(1,w-1):
            image[row][col]=np.mean(image[row-1:row+2, col-1:col+2])
    return image
    
def max_filter():
    image=np.copy(img)
    output_image=np.zeros_like(image)
    h,w=np.shape(image)
    for row in range(1,h-1):
        for col in range(1,w-1):
            neighbors=image[row-1:row+2, col-1:col+2]
            output_image[row][col]=np.max(neighbors)
    return output_image

def min_filter():
    image=np.copy(img)
    output_image=np.zeros_like(image)
    h,w=np.shape(image)
    for row in range(1,h-1):
        for col in range(1,w-1):
            neighbors=image[row-1:row+2, col-1:col+2]
            output_image[row][col]=np.min(neighbors)
    return output_image

def median_filter():
    image=np.copy(img)
    output_image=np.zeros_like(image)
    h,w=np.shape(image)
    for row in range(1,h-1):
        for col in range(1,w-1):
            neighbors=image[row-1:row+2, col-1:col+2]
            output_image[row][col]=np.median(neighbors)
    return output_image