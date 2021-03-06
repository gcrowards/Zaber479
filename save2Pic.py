import cv2


saveLocation = 'CalibrationPhotos/MinoruCalibration10x12/'

def rescale(image, ratio): # Resize an image using linear interpolation
	if ratio == 1:
		return image
	dim = (int(image.shape[1] * ratio), int(image.shape[0] * ratio))
	rescaled = cv2.resize(image, dim, interpolation = cv2.INTER_LINEAR)
	return rescaled

exposure = -5
fps = 15
Lcam = cv2.VideoCapture(1)
Rcam = cv2.VideoCapture(2)
for camera in [Lcam, Rcam]:
	camera.set(15,exposure)
	camera.set(cv2.CAP_PROP_FPS,fps)
	camera.set(cv2.CAP_PROP_FRAME_HEIGHT,2*240)
	camera.set(cv2.CAP_PROP_FRAME_WIDTH,2*320)
	print(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
	print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
	print(camera.get(cv2.CAP_PROP_FPS))


# Logi1exposure = 0

# Lcam.set(15,Logi1exposure)
# Rcam.set(15,exposure)
# Lcam.set(5,fps)
# Rcam.set(5,fps)

#photo number
i = 0

# number of photos
p = 20

L = True
done = False

while True:
	retL, capL = Lcam.read()
	retR, capR = Rcam.read()

	cv2.imshow('imgL',capL)
	cv2.imshow('imgR',capR)

	key = cv2.waitKey(1)

	if key == ord('p'):
		# This fucked with everything.
		# LcapL = rescale(capL, 4)
		# LcapR = rescale(capR, 4)
		cv2.imwrite(saveLocation+'Stereo%d_L.png'%i, capL)
		cv2.imwrite(saveLocation+'Stereo%d_R.png'%i, capR)
		i = i + 1
		if i == p:
			done = True
	elif key == ord('q'):
		done = True

	if done:
		break

Lcam.release()
Rcam.release()
cv2.destroyAllWindows()
