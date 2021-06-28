#pip install opencv-contrib-python
#pip install opencv-python
#pip install csv
#pip install urllib

################INPUT SEGMENT###################
print("Welcome to intrgreated MAP ANALYSIS FOR GREENERY")
lat = float(input('Your Lat: '))
lon = float(input('Your Lon: '))
zoom = 18        #max zoom 22
size = '1280x1280'
################END SEGMENT#####################


#####################GET STARTED################


###########TEST DATA IMAGE ANALYSIS##############
###########tzkhan2003@gmail.com##################
#####IMPORT###############
import cv2
import numpy as np
from csv import writer 
import urllib.request

lat = str(lat)
lon = str(lon)
zoom = str(zoom)


imgurl = 'https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/' + lon + ',' + lat+ ',' + zoom + '/'+size+'?attribution=false&logo=false&access_token=pk.eyJ1IjoidHpraGFuMjAwMyIsImEiOiJja2pvaG5ydnMyeDI1MnlsbzZvYzNhcGhhIn0.dLrxWf3VGj027tdtgCoruQ'
urllib.request.urlretrieve(imgurl,lat + ','+lon+".jpg")


def mouseRGB(event,x,y,flags,param):
  if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
    colorsB = image[y,x,0]
    colorsG = image[y,x,1]
    colorsR = image[y,x,2]
    colors = image[y,x]
    color=[0,0,0]
    color[0] = colors[1]
    color[1] = colors[2]
    color[2] = colors[0]
    with open('data.csv','a',newline='') as f:
      writer_object = writer(f)
      writer_object.writerow(color)
      f.close()
    #cv2.circle(image,(x,y),2,(0,0,0),-1)
    cv2.circle(image1,(x,y),2,(0,0,0),-1)
    print("HSV Format: ",color)
    #print("Coordinates of pixel: X: ",x,"Y: ",y)

# Read an image, a window and bind the function to window
image1 = cv2.imread(lat + ','+lon+".jpg", cv2.IMREAD_UNCHANGED)

image = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)

mask = cv2.inRange(image, (36, 25, 25), (70, 255,79))
#mask = cv2.inRange(image, (29, 62, 0), (70, 255,88))

cv2.imwrite(lat + ','+lon+"final.jpg", mask)


imask = mask>0
green = np.zeros_like(image1, np.uint8)
green[imask] = image1[imask]
cv2.imwrite(lat + ','+lon+"mid.jpg", green)


cv2.imwrite(lat + ','+lon+"temp.jpg",image)
cv2.destroyAllWindows()

img = cv2.imread(lat + ','+lon+"final.jpg")
img2 = cv2.imread(lat + ','+lon+".jpg")
number_of_white_pix = np.sum(img == 255) 
number_of_black_pix = np.sum(img == 0)

rate = str("%.2f" % ((number_of_white_pix/(number_of_black_pix + number_of_white_pix))*100)) + '%'

font = cv2.FONT_HERSHEY_SIMPLEX  
org = (75, 75) 
fontScale = 2
color = (255, 255, 255) 
thickness = 3

imagee = cv2.putText(img2, rate, org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite(lat + ','+lon+".jpg", imagee)

#Do until esc pressed
while(1):
    cv2.imshow('Result',imagee)
    #cv2.imshow('mask', mask)
    #cv2.imshow('green', green)
    if cv2.waitKey(20) & 0xFF == 27:
        break
#if esc pressed, finish.