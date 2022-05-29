import sys
import cv2
from numpy import asarray
from PIL import Image
from numpy import array
import numpy as np

input_file=input("Enter the image file name: ")

image=cv2.imread(input_file)

image_for_use=Image.open(input_file)

#cv2.imshow("Original Image: ",image)

img_3d=asarray(image_for_use)

img=img_3d.reshape(img_3d.shape[0],(img_3d.shape[1]*img_3d.shape[2]))

third=img_3d.shape[2]

n=len(img)
m=len(img[1])

print(img)




#n = 5
#m = 5
'''img = [[2,8,6,3,10,20,1,0],
       [4,9,2,1,12,15,7,6],
       [3,14,7,4,5,6,8,9],
       [11,3,4,6,2,12,17,20],
       [12,2,3,8,13,3,4,14],
       [9,6,11,10,15,16,9,10],
       [1,8,12,22,6,8,11,2],
       [2,9,10,1,20,24,4,3]]'''

#img = [[12,15,12,14,13],[14,1,16,3,14],[20,14,0,18,19],[12,12,14,12,2],[1,0,15,12,4]]

choice = int(input("Please select the type of cascaded pooling that needs to get applied on the image\n1) Max-max Pooling\n2) Max-average Pooling\nEnter your choice: "))

if choice==1:
    r = n - 1
    c = m - 1
    cas_img = []
    for i in range(r):
        cas_img.append([])
        for j in range(c):
            l = [img[i][j], img[i+1][j], img[i][j+1], img[i+1][j+1]]
            cas_img[i].append(max(l))

    if r%2==1:
        cas_img.append([])
        for i in range(c):
            cas_img[r].append(0)
        r = r + 1

    if c%2==1:
        for i in range(r):
            cas_img[i].append(0)
        c = c + 1

    cascaded_img = []
    for i in range(0,r,2):
        cascaded_img.append([])
        for j in range(0,c,2):
            l = [cas_img[i][j], cas_img[i][j+1], cas_img[i+1][j], cas_img[i+1][j+1]]
            cascaded_img[int(i/2)].append(max(l))

    cascaded_img=array(cascaded_img)
    new_image=Image.fromarray(cascaded_img)
    new_image.save("_modified1_"+input_file)
    image_modified=cv2.imread("_modified1_"+input_file)
    #cv2.imshow("After applying pooling: ",image_modified)


    
elif choice==2:
    r = n - 1
    c = m - 1
    cas_img = []
    for i in range(r):
        cas_img.append([])
        for j in range(c):
            l = [img[i][j], img[i+1][j], img[i][j+1], img[i+1][j+1]]
            cas_img[i].append(max(l))

    if r%2==1:
        cas_img.append([])
        for i in range(c):
            cas_img[r].append(0)
        r = r + 1

    if c%2==1:
        for i in range(r):
            cas_img[i].append(0)
        c = c + 1

    cascaded_img = []
    for i in range(0,r,2):
        cascaded_img.append([])
        for j in range(0,c,2):
            l = [cas_img[i][j], cas_img[i][j+1], cas_img[i+1][j], cas_img[i+1][j+1]]
            cascaded_img[int(i/2)].append((sum(l)/len(l)))

    cascaded_img=array(cascaded_img)
    print(cascaded_img)
    new_image=Image.fromarray(np.uint8(cascaded_img))
    new_image.save("_modified2_"+input_file)
    #image_modified=cv2.imread("_modified2_"+input_file)
    #cv2.imshow("After applying pooling: ",image_modified)

    
else:
    print("Invalid choice")
 
