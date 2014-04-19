#!/usr/bin/python
# -*- coding: cp1252 -*-
import numpy as np
import cv2
import os
import shutil
import glob



def nothing(*arg):
    pass

def thresholdTrackBar(Image, WindowName):
    # Generate trackbar Window Name
    TrackbarName = WindowName + "Trackbar"

    # Make Window and Trackbar
    cv2.namedWindow(WindowName,cv2.CV_WINDOW_AUTOSIZE)
    cv2.createTrackbar(TrackbarName, WindowName, 182, 255, nothing)

    #Reduce para visualizarlo mejor
    Imageres = cv2.resize(Image,(Image.shape[1]/4,Image.shape[0]/4))

    # Allocate destination image
    Threshold2 = np.zeros(Imageres.shape, np.uint8)

    while True:
        # Get position in trackbar
        TrackbarPos = cv2.getTrackbarPos(TrackbarName, WindowName)
        # Apply threshold
        cv2.threshold(Imageres, TrackbarPos, 255, cv2.THRESH_BINARY_INV, Threshold2)
        # Show in window
        cv2.imshow(WindowName, Threshold2)

        # If you press "ESC", it will return value
        ch = cv2.waitKey(5)
        if ch == 27 or ch == ord(' '):
            break

    cv2.destroyAllWindows()

    #Como se ha hecho con la imagen reducida, se coge el umbral y se pasa por la imagen real a devolver
    ret,Threshold = cv2.threshold(Image,TrackbarPos,255,cv2.THRESH_BINARY_INV)
    
    return Threshold


def mask():
    # Read image
    mask = cv2.imread('mask.JPG',-1)

    # Se pasa a un canal, unicamente cogiendo el "azul", por haber mayor contraste en la mascara
    blue_mask = cv2.split(mask)[0]

    #cv2.namedWindow('Mascara', cv2.WINDOW_NORMAL)

    #Se binariza para obtener solo las manchas
    #ret,thresh = cv2.threshold(blue_mask,180,255,cv2.THRESH_BINARY_INV)
    print 'Elegir umbral de la mascara, y pulsar "ESC" o espacio para continuar'
    thresh = thresholdTrackBar(blue_mask, 'Mascara')

    #Se localiza los contornos de esas manchas, y el centro de estas con propiedades de contornos 
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    return contours

def smoothingImages(name, contours):
    #Read image
    image = cv2.imread(name,-1)
    rows_h,cols_w,channels = image.shape        

    for element in contours:
        
        (x,y),radius = cv2.minEnclosingCircle(element)
        center = (int(x),int(y))
        cx,cy = center

        roirange = int (radius) + int (radius/2)
        img0 = image[cy-roirange:cy+roirange, cx-roirange:cx+roirange]
    
        median = cv2.medianBlur(img0,57)

        image[cy-roirange:cy+roirange, cx-roirange:cx+roirange] = median

        #cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        #cv2.circle(image,(cx,cy), int (radius),(0,0,255),5)
        #cv2.circle(image,(cx,cy), 20,(0,0,255),5)
        #cv2.imshow('image',image)
        #cv2.waitKey(0)

    cv2.destroyAllWindows()

    pos = name.find('.JPG')
    nameresult = name[:pos] + '_2.JPG'

    cv2.imwrite(nameresult,image,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
    print 'Procesada imagen ' + name


def main():

    contours = mask()

    filelist = glob.glob("*.JPG")

    for names in filelist:
        if names != "mask.JPG":
            smoothingImages(names, contours)

    print 'Limpiado de imagenes completo\n'
    


if __name__ == "__main__":
    main()

