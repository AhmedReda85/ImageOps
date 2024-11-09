import cv2
import numpy as np

# img = cv2.resize(cv2.imread("image.jpg",0),(500,500))/255

def input_value():
    return int(input())

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
    # < 0 : Brightens darker regions while compressing brighter regions
    # > 0 : Darkens image while expanding brighter regions
    print("Enter a value")
    gamma_value=input_value()
    image=np.copy(img)
    h,w=np.shape(img)
    for row in range(h):
        for col in range(w):
            image[row][col]=(2*image[row][col])**gamma_value
    return image

def log_transformation():
    # To enhance details in dark regions
    print("Enter a value")
    scaling_factor_value=input_value()
    image=np.copy(img*255)
    h,w=np.shape(image)
    for row in range(h):
        for col in range(w):
            if image[row][col] > 0:
                image[row][col]=scaling_factor_value*(np.log2(image[row][col]))
            else:
                image[row][col]=0
    return image/255  

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



if __name__ == "__main__":
    try:
        img = cv2.resize(cv2.imread("image.jpg",0),(500,500))/255
        
        while True:
            print("\nImage Processing Menu:")
            print("1. Brighten Image")
            print("2. Darken Image")
            print("3. Negative")
            print("4. Power Law")
            print("5. Log Transformation")
            print("6. Average Filter")
            print("7. Median Filter")
            print("8. Max Filter")
            print("9. Min Filter")
            print("0. Exit")
            
            choice = input("\nEnter your choice (0-9): ")
            
            if choice == '0':
                break
                
            if choice == '1':
                result = more_bright()
                cv2.imshow('Brightened Image', result)
            elif choice == '2':
                result = more_dark()
                cv2.imshow('Darkened Image', result)
            elif choice == '3':
                result = negative()
                cv2.imshow('Negative Image', result)
            elif choice == '4':
                result = power_law()
                cv2.imshow('Power Law Transform', result)
            elif choice == '5':
                result = log_transformation()
                cv2.imshow('Log Transform', result)
            elif choice == '6':
                result = average_filter()
                cv2.imshow('Average Filter', result)
            elif choice == '7':
                result = median_filter()
                cv2.imshow('Median Filter', result)
            elif choice == '8':
                result = max_filter()
                cv2.imshow('Max Filter', result)
            elif choice == '9':
                result = min_filter()
                cv2.imshow('Min Filter', result)
            else:
                print("Invalid choice! Please try again.")
                continue
            
            cv2.imshow('Original Image', img)
            
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
    except Exception as e:
        print(f"Error: {str(e)}")