#!/usr/bin/python
# -*- coding: cp1252 -*-
import numpy as np
import cv2
import os
import shutil
import glob
import sys


def reduceImages(name,format_file, nreduce):
    """ Esta funcion aplica 'resize' de opencv
        Ejemplo de parametros de entrada:
        name = nombreimagen.JPG
        format_file = JPG
        nreduce = 0.5
    """
    image = cv2.imread(name,-1)
    rows_h,cols_w,channels = image.shape

    image = cv2.resize(image,(int(cols_w*nreduce),int(rows_h*nreduce)))
    pos = name.find(format_file)
    nameresult = name[:pos] + '_2' + format_file

    cv2.imwrite(nameresult,image,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
    print 'Procesada imagen: ' + name

def interpreteformat(formatimage):

    format_search=''
    format_file=''

    if(formatimage == 'bmp'):
        format_search = '*.bmp'
        format_file = '.bmp'
    elif(formatimage == 'BMP'):
        format_search = '*.BMP'
        format_file = '.BMP'

    elif(formatimage == 'jpg'):
        format_search = '*.jpg'
        format_file = '.jpg'
    elif(formatimage == 'JPG'):
        format_search = '*.JPG'
        format_file = '.JPG'

    elif(formatimage == 'png'):
        format_search = '*.png'
        format_file = '.png'
    elif(formatimage == 'PNG'):
        format_search = '*.PNG'
        format_file = '.PNG'

    elif(formatimage == 'tiff'):
        format_search = '*.tiff'
        format_file = '.tiff'
    elif(formatimage == 'TIFF'):
        format_search = '*.TIFF'
        format_file = '.TIFF'

    else:
        return format_search,format_file

    return format_search,format_file


def interprete_compression(number):

    correctnumber = False

    if(number <= 5 and number > 0):
        correctnumber = True

    return correctnumber

def main():

    formatimage = raw_input ('Formato de imagen: (bmp, jpg, png, tiff)\n')

    format_search,format_file = interpreteformat(formatimage)
    if(format_search == ''):
        print 'Formato archivo erroneo'
        sys.exit()

    filelist = glob.glob(format_search)
    if(not(filelist)):
        print 'No hay archivos con esta extension en este directorio\n'
        sys.exit()

    try:
        nreduce = float(raw_input('Porcentaje de compresion: (0.75,0.50,0.25 ...) o ampliacion (1 a 5)\n'))
        if(not(interprete_compression(nreduce))):
            print ('Valor fuera de rango')
            sys.exit(0)
    except ValueError:
        print 'Valor no numerico\n'
        sys.exit(0)

    for names in filelist:
        reduceImages(names,format_file, nreduce)

    print 'Reduccion completa\n'



if __name__ == "__main__":
    main()
