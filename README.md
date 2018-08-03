# IBM Code Model Asset Exchange: Show and Tell Image Caption Generator

This repository contains code to instantiate and deploy an image caption generation model. This model generates captions from a fixed vocabulary that describe the contents of images in the [COCO Dataset](http://cocodataset.org/#home). The model consists of an _encoder_ model - a deep convolutional net using the Inception-v3 architecture trained on [ImageNet-2012 data](http://www.image-net.org/challenges/LSVRC/2012/) - and a _decoder_ model - an LSTM network that is trained conditioned on the encoding from the image _encoder_ model. The input to the model is an image, and the output is a sentence describing the image content.

The model is based on the [Show and Tell Image Caption Generator Model](https://github.com/tensorflow/models/tree/master/research/im2txt). The checkpoint files are hosted on [IBM Cloud Object Storage](http://max-assets.s3-api.us-geo.objectstorage.softlayer.net/tf/im2txt/im2txt_ckpt.tar.gz). The code in this repository deploys the model as a web service in a Docker container. This repository was developed as part of the [IBM Code Model Asset Exchange](https://developer.ibm.com/code/exchanges/models/).

## Model Metadata
| Domain | Application | Industry  | Framework | Training Data | Input Data Format |
| ------------- | --------  | -------- | --------- | --------- | -------------- | 
| Vision | Image Caption Generator | General | TensorFlow | [COCO](http://cocodataset.org/#home) | Images | 

## References
* _O. Vinyals, A. Toshev, S. Bengio, D. Erhan._, ["Show and Tell: Lessons learned from the 2015 MSCOCO Image Captioning Challenge"](https://arxiv.org/abs/1609.06647), IEEE transactions on Pattern Analysis and Machine Intelligence, 2016.
* [im2txt TensorFlow Model GitHub Page](https://github.com/tensorflow/models/tree/master/research/im2txt)
* [COCO Dataset Project Page](http://cocodataset.org/#home)

## Licenses

| Component | License | Link  |
| ------------- | --------  | -------- |
| This repository | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](LICENSE) |
| Model Weights | [MIT](https://opensource.org/licenses/MIT) | [Pretrained Show and Tell Model](https://github.com/KranthiGV/Pretrained-Show-and-Tell-model) |
| Model Code (3rd party) | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [im2txt](https://github.com/tensorflow/models/tree/master/research/im2txt) |
| Test assets | Various | [Asset README](assets/README.md) |

## Pre-requisites:

* `docker`: The [Docker](https://www.docker.com/) command-line interface. Follow the [installation instructions](https://docs.docker.com/install/) for your system.
* The minimum recommended resources for this model is 2GB Memory and 2 CPUs.

## Steps

1. [Build the Model](#1-build-the-model)
2. [Deploy the Model](#2-deploy-the-model)
3. [Use the Model](#3-use-the-model)
4. [Development](#4-development)
5. [Clean Up](#5-clean-up)

## 1. Build the Model

Clone this repository locally. In a terminal, run the following command:

```
$ git clone https://github.com/IBM/MAX-Image-Caption-Generator.git
```

Change directory into the repository base folder:

```
$ cd MAX-Image-Caption-Generator
```

To build the docker image locally, run: 

```
$ docker build -t max-im2txt .
```

All required model assets will be downloaded during the build process. _Note_ that currently this docker image is CPU only (we will add support for GPU images later).

## 2. Deploy the Model

To run the docker image, which automatically starts the model serving API, run:

```
$ docker run -it -p 5000:5000 max-im2txt
```

## 3. Use the Model

The API server automatically generates an interactive Swagger documentation page. Go to `http://localhost:5000` to load it. From there you can explore the API and also create test requests.

Use the `model/predict` endpoint to load a test file and get captions for the image from the API.

![pic](/docs/swagger-screenshot.png "Swagger Screenshot")

You can also test it on the command line, for example:

```
$ curl -F "image=@assets/surfing.jpg" -X POST http://127.0.0.1:5000/model/predict
```

```json
{
  "status": "ok",
  "predictions": [
    {
      "index": "0",
      "caption": "a man riding a wave on top of a surfboard .",
      "probability": 0.038827644239537
    },
    {
      "index": "1",
      "caption": "a person riding a surf board on a wave",
      "probability": 0.017933410519265
    },
    {
      "index": "2",
      "caption": "a man riding a wave on a surfboard in the ocean .",
      "probability": 0.0056628732021868
    }
  ]
}
```

## 4. Development

To run the Flask API app in debug mode, edit `config.py` to set `DEBUG = True` under the application settings. You will then need to rebuild the docker image (see [step 1](#1-build-the-model)).

## 5. Clean Up

To stop the Docker container, type `CTRL` + `C` in your terminal.

## Links

* [Image Caption Generator Web App](http://developer.ibm.com/code/patterns/create-web-app-interact-machine-learning-generated-image-captions): A reference application created by the IBM CODAIT team that uses the Image Caption Generator
