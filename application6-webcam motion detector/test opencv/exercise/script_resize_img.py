import cv2
import glob

images=glob.glob("*.jpg")
#img1=cv2.imread("galaxy.jpg",0)
#img2=cv2.imread("kangaroos-rain-australia_71370_990x742.jpg",0)
#img3=cv2.imread("Lighthouse.jpg",0)
#img4=cv2.imread("Moon sinking, sun rising.jpg",0)

for image in images:
	img=cv2.imread(image,0)
	re=cv2.resize(img,(100,100))
	cv2.imshow("test",re)
	cv2.waitKey(500)
	cv2.destroyAllWindows()
	#cv2.imwrite("resized_"+image,re)
#cv2.imwrite("galaxy.jpg",resized_img1)
