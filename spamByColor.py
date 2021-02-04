#!/usr/bin/python3
from PIL import Image   #Pillow==8.1.0
import numpy            #numpy==1.20.0
import re
import sys

#Get average color of provided image
def avgColor(picArray):
    picArray = numpy.asarray(picArray)
    pixels = picArray.shape[0]*picArray.shape[1]
    colors = list([0,0,0])
    for row in picArray:
        for pixel in row:
            colors[0] += pixel[0]
            colors[1] += pixel[1]
            colors[2] += pixel[2]
    colors[0] /= pixels
    colors[1] /= pixels
    colors[2] /= pixels
    return colors

#imgPath is the path to the image, bordersize is the % size of the image to go inward when checking borders
#and threshold is the sensitivity of the color difference with which to check for Spam
def detectSpam(imgPath,borderSize=10,threshold=0.5):
    #Open image and grab its dimentions
    bait = Image.open(imgPath)
    w,h = bait.size

    #Exit early if image too tiny
    if not (w > 50 and h > 50):
        return
    #Max border size is 20% (beyond that would be intersecting the center region)
    if borderSize > 20:
        borderSize = 20

    #Get crops of image to consider
    left = (0,0,round(w/borderSize),h)
    right = (w-round(w/borderSize),0,w,h)
    top = (0,0,w,round(h/borderSize))
    bottom = (0,h-round(h/borderSize),w,h)
    center = (round(w/5),round(h/5),w-round(w/5),h-round(h/5))

    #Do the cropping
    left = bait.crop(left)
    right = bait.crop(right)
    top = bait.crop(top)
    bottom = bait.crop(bottom)
    centerImg = bait.crop(center)

    #Calculate average colors for each region of the image
    res = {
        'left': avgColor(left),
        'right': avgColor(right),
        'top': avgColor(top),
        'bottom': avgColor(bottom),
        'centerImg': avgColor(centerImg)
    }


    #For each cropped region
    for k in res:
        #Store the color averages for the current region into edgeM
        edgeM = res[k]
        elseM = list([0,0,0])

        #Average the other 4 regions of the image together into elseM
        for kt in res:
            if not (kt == k):
                elseM[0] += res[kt][0]
                elseM[1] += res[kt][1]
                elseM[2] += res[kt][2]
        elseM[0] /= 4
        elseM[1] /= 4
        elseM[2] /= 4

        #Calculate the average difference between the current edge and the rest of the image. if > 0.5, it's probably spam. Also don't report as spam if the center is different
        diff = (abs(edgeM[0]/255 - elseM[0]/255) + abs(edgeM[1]/255 - elseM[1]/255) + abs(edgeM[2]/255 - elseM[2]/255))/3
        if diff > threshold:
            if k != 'centerImg':
                return k

#Call the program like "./spamByColor.py sketchyImage.png"
if len(sys.argv) > 1 and __name__ == "__main__":
    #Some brief regex to make sure the input filename at least has the right file extention
    if re.match(r"^.+\.(png|jpg|jpeg)$",sys.argv[1]):

        #Run with default parameters, and print results accordingly
        res = detectSpam(sys.argv[1],borderSize=10,threshold=0.5)
        if res:
            print(f"Spam was detected on the {res} side of {sys.argv[1]}")
        else:
            print(f"{sys.argv[1]} is either too tiny, or no spam was found in it!")
