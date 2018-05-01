# Applying Deep Learning

## 1.Introduction

In this lesson, we're going to go over a few really cool applications of deep learning using pre-trained models that 
others have generously provided on Github. Don't worry if you don't understand what's going on! The goal is just for 
you to see the power of deep learning in a few different contexts and play around with these models. You'll get to dive 
deep into such models later on in the program. For now just have fun and plug in your own examples where possible!

## 2.Style Transfer

As an example of the kind of things you'll be building with deep learning models, here is a really fun project, 
[fast style transfer](https://github.com/lengstrom/fast-style-transfer). Style transfer allows you to take famous 
paintings, and recreate your own images in their styles! The network learns the underlying techniques of those paintings 
and figures out how to apply them on its own. This model was trained on the styles of famous paintings and is able to 
transfer those styles to other images and [even videos](https://www.youtube.com/watch?v=xVJwwWQlQ1o)!

I used it to style my cat Chihiro in the style of [Hokusai](https://en.wikipedia.org/wiki/Hokusai)'s 
[The Great Wave Off Kanagawa](https://en.wikipedia.org/wiki/The_Great_Wave_off_Kanagawa).

![part2-1](readme/part2-1.png)

To try it out yourself, you can find the code in the [fast-style-transfer GitHub repo](https://github.com/lengstrom/fast-style-transfer). 
Either use `git` to clone the repository, or you can download the whole thing as a Zip archive and extract it.

The network has been trained on a few different styles ([here](https://github.com/lengstrom/fast-style-transfer/tree/master/examples/style)) 
and saved into [checkpoint files](https://drive.google.com/drive/folders/0B9jhaT37ydSyRk9UX0wwX3BpMzQ). Checkpoint 
files contain all the information about the trained network to apply styles to new images.

### Dependencies

The easiest way to install all the packages needed to run this code is with [Miniconda](http://conda.pydata.org/miniconda.html), 
a smaller version of [Anaconda](https://www.continuum.io/downloads). Miniconda comes with Conda, a package and 
environment manager built specifically for data science. Install the Python 3 version of Miniconda appropriate for your 
operating system.

If you haven't used Conda before, please quickly run through the Anaconda lesson (Lesson 3 on this part).

### Windows

For Windows, you'll need to install TensorFlow 0.12.1, Python 3.5, Pillow 3.4.2, scipy 0.18.1, and numpy 1.11.2. After 
installing Miniconda, open your command prompt. In there, enter these commands line by line:

```bash
conda create -n style-transfer python=3.5
activate style-transfer
pip install tensorflow
conda install scipy pillow
```

The first line creates a new environment that will hold the packages needed for the style transfer code. The next line 
(`activate style-transfer`) enters the environment, you should see the environment name in the prompt at the beginning 
of the line. The next two install TensorFlow, Scipy, and Pillow (an image processing library).

### OS X and Linux

For OS X and Linux, you'll need to install TensorFlow 0.11.0, Python 2.7.9, Pillow 3.4.2, scipy 0.18.1, and numpy 1.11.2.

In your terminal, enter this commands line by line:

```bash
conda create -n style-transfer python=2.7.9
source activate style-transfer
pip install tensorflow
conda install scipy pillow
```

The first line creates a new environment that will hold the packages needed for the style transfer code. The next line 
(`source activate style-transfer`) enters the environment, , you should see the environment name in the prompt at the 
beginning of the line. The next two install TensorFlow, Scipy, and Pillow (an image processing library).

### Transferring styles
 1. Download the Zip archive from the fast-style-transfer repository and extract it. You can download it by clicking on 
 the bright green button on the right.
 1. Download the Rain Princess checkpoint from here. Put it in the fast-style-transfer folder. A checkpoint file is a 
 model that already has tuned parameters. By using this checkpoint file, we won't need to train the model and can get 
 straight to applying it.
 1. Copy the image you want to style into the fast-style-transfer folder.
 1. Enter the Conda environment you created above, if you aren't still in it.
 1. In your terminal, navigate to the fast-style-transfer folder and enter

```bash
python evaluate.py --checkpoint ./rain-princess.ckpt --in-path <path_to_input_file> --out-path ./output_image.jpg
```

**Note:** Your checkpoint file might be named rain_princess.ckpt, notice the underscore, it's not the dash from above.

You can get more checkpoint files at the bottom of this page. Try them all!

Share what you create in the forums or on the Slack channel #neural-networks. We'd love to see what you come up with. 
Also, feel free to train the network on your own images, you can find instructions in the repository (although it does 
take some powerful hardware).

**Note:** Be careful with the size of the input image. The style transfer can take quite a while to run on larger 
images.

## 3.DeepTraffic

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F1.Introduction%2F2.Applying-Deep-Learning%2Freadme&filename=1%20-%20Traffic%20Navigation%20with%20Deep%20Reinforcement%20Learning.mp4&fid=0MZqBkd&open=normal)
 
Another great application of deep learning is in simulating traffic and making driving decisions. You can find the 
DeepTraffic simulator [here](https://selfdrivingcars.mit.edu/deeptraffic/). The network here is attempting to learn a 
driving strategy such that the car is moving as fast as possible using [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning). 
The network is rewarded when the car chooses actions that result in it moving fast. It's this feedback that allows the 
network to find a strategy of actions for optimal speed.

To learn more about setting the parameters and training the network, read the [overview here](https://selfdrivingcars.mit.edu/deeptraffic/).

Discuss how you built your network and your results with your fellow students in the #deeptraffic channel on Slack.

## 4.Flappy Bird

In this example, you'll get to see a deep learning agent playing Flappy Bird! You have the option to train the agent 
yourself, but for now let's just start with the pre-trained network given by the author. Note that the following agent 
is able to play without being told any information about the structure of the game or its rules. It automatically 
discovers the rules of the game by finding out how it did on each iteration.

We will be following [this repository](https://github.com/yenchenlin/DeepLearningFlappyBird) by Yenchen Lin.


![part4-1](readme/part4-1.jpg)

### Instructions
 1. Install miniconda or anaconda if you have not already. You can follow [our tutorial](https://classroom.udacity.com/nanodegrees/nd101/parts/2a9dba0b-28eb-4b0e-acfa-bdcf35680d90/modules/329a736b-1700-43d4-9bf0-753cc461bebc/lessons/9e9ed61d-20c3-4431-95aa-a1099f28d601/concepts/4cdc5a26-1e54-4a69-8eb4-f15e37aaab7b) 
 for help.
 1. Create an environment for flappybird
    * Mac/Linux: conda create --name=flappybird python=2.7
    * Windows: conda create --name=flappybird python=3.5
 1. Enter your conda environment
    * Mac/Linux: source activate flappybird
    * Windows: activate flappybird
 1. conda install -c menpo opencv3
 1. pip install pygame
 1. pip install tensorflow
 1. git clone https://github.com/yenchenlin/DeepLearningFlappyBird.git
 1. cd DeepLearningFlappyBird
 1. python deep_q_network.py
 
If all went correctly, you should be seeing a deep learning based agent play Flappy Bird! The repository contains 
instructions for training your own agent if you're interested!

## 5.Books to read

We believe that you learn best when you are exposed to multiple perspectives on the same idea. As such, we recommend 
checking out a few of the books below to get an added perspective on Deep Learning.

 * [Grokking Deep Learning](https://www.manning.com/books/grokking-deep-learning) by Andrew Trask. Use our exclusive 
 discount code traskud17 for 40% off. This provides a very gentle introduction to Deep Learning and covers the intuition 
 more than the theory.
 * [Neural Networks And Deep Learning](http://neuralnetworksanddeeplearning.com/) by Michael Nielsen. This book is more 
 rigorous than Grokking Deep Learning and includes a lot of fun, interactive visualizations to play with.
 * [The Deep Learning Textbook](http://www.deeplearningbook.org/) from Ian Goodfellow, Yoshua Bengio, and Aaron 
 Courville. This online book contains a lot of material and is the most rigorous of the three books suggested.
