from keras.preprocessing import image as image_utils
from imagenet_utils import decode_predictions
from imagenet_utils import preprocess_input
from vgg16 import VGG16
import numpy as np
import argparse
import cv2

# cmd argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())

# cv2 operation to load image - not needed for final product
# orig = cv2.imread(args["image"])

# convert input using keras' helper, resize image to 224x224, finally get image as np array from pil

image = image_utils.load_img(args["image"], target_size=(224, 224))
image = image_utils.img_to_array(image)

#expand array dimensions from 3 to 4 for the network + subtract rgb pixel intensity from dataset

image = np.expand_dims(image, axis=0)
image = preprocess_input(image)

# load the VGG16 network
model = VGG16(weights="imagenet")

# classify the image
preds = model.predict(image)

magic = decode_predictions(preds)
#print magic
#print magic[0][0]
(inID, label, something) = decode_predictions(preds)[0][0] 

# we only need the top prediction. the decode_predictions can be modified to give probabilities and other guesses.

# display the predictions to our screen
print("ImageNet ID: {}, Label: {}".format(inID, label))

#cv2 operations not used on web

# cv2.putText(orig, "Label: {}".format(label), (10, 30),
# 	cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
# cv2.imshow("Classification", orig)
# cv2.waitKey(0)