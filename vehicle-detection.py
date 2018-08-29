import cv2
filename = 'traffic.avi'
cap = cv2.VideoCapture(filename)
reference_frame =None 
image_area = None
while True:
	ret,frame = cap.read()


	if ret is False:
		break
	else:
		if reference_frame is None:
			reference_frame = frame
			# covert gray scale
			reference_frame = cv2.cvtColor(reference_frame,cv2.COLOR_BGR2GRAY)
			# declare area of contours and the portion of frame
			image_area = reference_frame.shape[0] * reference_frame.shape[1]
			continue
         # convert gray scale
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # calculate difference between new frame with old one
		difference = cv2.absdiff(reference_frame,gray)
		# use median filter to remove noise
		blur = cv2.medianBlur(difference,31)

		f, threshold = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
		# find the contours
		(_,contours,_) = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		for i in contours:
			contour_area = cv2.contourArea(i)
			# declare area of contours in the portion of frame to avoid false contour
			if (contour_area > 0.001*image_area)and( contour_area <0.03 *image_area):
            # draw bounding box around contours
				(x,y,w,h)=cv2.boundingRect(i)
				cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

		cv2.imshow("frames",frame)
		if cv2.waitKey(1) == ord('q'):
			break