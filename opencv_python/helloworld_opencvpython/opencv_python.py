#!/usr/bin/python
import cv2.cv as cv

cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE)
image=cv.LoadImage('lena.jpg', cv.CV_LOAD_IMAGE_COLOR) #Load the image
font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8) #Creates a font
x = 100
y = 100
cv.PutText(image,"Hello World!!!", (x,y),font, 255) #Draw the text

while(1):
    cv.ShowImage('a_window', image) #Show the image
    cv.WaitKey(10)
    if cv.WaitKey(10) == 27:
        break
    
cv.SaveImage('image.png', image) #Saves the image
print 'imagen guardada'
cv.DestroyAllWindows()

