# realLifePokedex
automatic image recognition over a (functional, barebone) web app.

# Instructions
## To Run:
Dependencies - keras, pillow, numpy and (maybe) opencv2 if you wish to use some of the native options.

Once installed, run:
```bash
python app_basic.py
```

This will serve the Flask app  (default @ 127.0.0.1:5000).

## How it works:
Upload a picture of your choice on the form. The model _should_ then respond with a guess of what it thinks it is. 

### Under the hood: 
Thanks to François Chollet's python implementation of VGG16, VGG19, ResNet50 as well as Keras itself, the models, pre-trained on ImageNet could be directly used. 
You could choose to implement your own models too. I didn't have time to train one. Usually, the model weights are not python-friendly. Mostly available on Caffe. The imagenet_utils.py file and the model files (vgg16.py) contains some dope helper functions for the same such as model download and other stuff. 

The first time you run the code, it will download the VGG16 model weights (~500 mb). Subsequent testing will be much faster since models are onboard. 

#### Flask App:
T

The a
