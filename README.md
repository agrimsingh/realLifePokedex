# realLifePokedex
automatic image recognition over a (functional, barebone) web app.

# Instructions
## To Run:
Dependencies - keras, numpy and (maybe) opencv2 if you wish to use some of the native options.

Once installed, run:
```bash
python app_basic.py
```h
This will serve the Flask app  (default @ 127.0.0.1:5000).

## How it works:
Upload a picture of your choice on the form. The model _should_ then respond with a guess of what it thinks it is. 

### Under the hood:You may 
Thanks to François Chollet's python implementation of VGG16, VGG19, ResNet50 as well as Keras itself, the models, pre-trained on ImageNet could be directly used. 
Ya
