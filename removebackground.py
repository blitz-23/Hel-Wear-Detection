import numpy as np
import cv2


def removebg(imagepath):
	#Load the Image
	imgo = cv2.imread(imagepath)
	height, width = imgo.shape[:2]

	#Create a mask holder
	mask = np.zeros(imgo.shape[:2],np.uint8)

	#Grab Cut the object
	bgdModel = np.zeros((1,65),np.float64)
	fgdModel = np.zeros((1,65),np.float64)


	rect = (10,10,width-30,height-30)
	cv2.grabCut(imgo,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
	mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
	img1 = imgo*mask[:,:,np.newaxis]
	background = imgo-img1


	background[np.where((background > [0,0,0]).all(axis = 2))] = [255,255,255]
	
	#Add the background and the image
	final = background + img1

	cv2.imwrite("bgremoved.jpg",final)
