# Computer-vision-Vehicle-Detection-from-Videos
## The steps are:

a.covert gray scale of every frame

b.declare area of contours and the portion of frame

c.calculate difference between new frame with old one

d.use median filter to remove noise

e.find the contours using declared area in the image/frame

f.declare area of contours in the portion of frame to avoid false contour

g.draw bounding box around contours

## To run

python vehicle-detection.py
