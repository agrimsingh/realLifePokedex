# realLifePokedex
A stupidly quick implementation of an automatic image recognition system. 

# Instructions
## To Run:
Dependencies - keras, pillow, numpy and (maybe) opencv2 if you wish to use some of the native options. No external API calls.

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
The app is rather basic with really one route defined i.e. upload. It uses the file uploaded as part of a subprocess that executes a command line operation and returns the output on the next screen i.e. what the program thinks the photo is. 

## TODO:
Most design decisions i.e. use of a pre-trained model, the barebone functionality, the unified Python stack were made in light of little time and ease of completion. They were also made keeping in mind that there's little use to other features if the recognition fails. 

**There are tons of potential directions/options available**. 
- Showing user probability values of decisions made (already possible, perhaps useful for research)
- Showing user a log of photos tested (either a photo gallery or grouped photos based on tags)
- Allowing users to test photos by batches instead of individually.
- Allowing users to test over video feed/webcam
- Give a natural language response to prediction as opposed to a single keyword descriptor such as [this](https://github.com/karpathy/neuraltalk2) or perhaps an implementation of [YOLO](http://pjreddie.com/darknet/yolo/) over the web to do multiple object recognition in pictures/video. This could further be used to take frames of interest/screenshots based on objects/scenes of relevance.
- Implementing SqueezeNet over a raspberryPi for a lightweight CNN.
- Allowing users to get a higher-level description of photo (so 'pullover' instead of 'cardigan', 'dog' instead of 'greyhound') by freezing the lower layers of the network and then training the upper layers through finetuning.
