# Deep Convolutional GANs

## 1. Deep Convolutional GANs

In this lesson you'll implement the Deep Convolutional GAN model to generate full color images. The additional 
complexity of these images requires using convolutional layers in the generator and discriminator. You'll also need to 
use a technique called batch normalization to get the GAN to train appropriately.

![part1-1](readme/part1_1.png)

You'll be training your GAN on the Street View House Numbers dataset, a small example is shown above. After training, 
the generator will be able to create images that are nearly identical to these images.

**Note:** This lesson will eventually cover semi-supervised learning with GANs. We'll release more content in a few weeks 
with Ian Goodfellow on this.

## 2. DCGAN Architecture

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F5.Generative-Adversial-Networks%2F2.Deep-Convolutional-Gan%2Freadme&filename=1_-_Deconvolution.mp4&fid=0MZqBkd&open=normal)

## 3. Batch Normalization

Batch normalization is a technique for improving the performance and stability of neural networks. The idea is to 
normalize the layer inputs such that they have a mean of zero and variance of one, much like how we standardize the 
inputs to networks. Batch normalization is necessary to make DCGANs work.

We've prepared a few notebooks for you to work through that will teach you about batch normalization and how to 
implement it in TensorFlow. As usual, you can find the notebooks on our [GitHub repository](https://github.com/udacity/deep-learning) in the `batch-norm` folder. 
If you have already cloned the repo, do a `git pull` to get the new files. Otherwise, clone the repository:

```bash
git clone https://github.com/udacity/deep-learning.git
```

Or, you can get the notebooks [here](https://github.com/udacity/deep-learning/tree/master/batch-norm).

You'll find three notebooks:

 * `Batch_Normalization_Lesson.ipynb` - A notebook showing you how batch normalization works
 * `Batch_Normalization_Exercises.ipynb` - Exercises for you to implement batch normalization
 * `Batch_Normalization_Solutions.ipynb` - Solutions to those exercises

## 4. DCGAN Implementation

We've prepared some notebooks for you to work through where you'll implement a DCGAN on the [Street View House Numbers](http://ufldl.stanford.edu/housenumbers/) 
(SVHN) dataset. I made a short video of generated images while the GAN is being trained. If you get everything in your 
implementation right, it should look a lot like [this](https://youtu.be/TjGs2fQvCDU).

As usual, you can find the notebooks on our [GitHub repository](https://github.com/udacity/deep-learning) in the 
`dcgan-svhn` folder. If you have already cloned the repo, do a `git pull` to get the new files. Otherwise, clone the 
repository:

```bash
git clone https://github.com/udacity/deep-learning.git
```

Or, you can get the notebooks [here](https://github.com/udacity/deep-learning/tree/master/dcgan-svhn).

## 5. DCGAN and the Generator

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F5.Generative-Adversial-Networks%2F2.Deep-Convolutional-Gan%2Freadme&filename=2_-_DCGAN_And_The_Generator.mp4&fid=0MZqBkd&open=normal)

## 6. Generator Solution

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F5.Generative-Adversial-Networks%2F2.Deep-Convolutional-Gan%2Freadme&filename=3_-_Generator_Solution.mp4&fid=0MZqBkd&open=normal)

## 7. Discriminator

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F5.Generative-Adversial-Networks%2F2.Deep-Convolutional-Gan%2Freadme&filename=4_-_Discriminator.mp4&fid=0MZqBkd&open=normal)

## 8. Discriminator Solution

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F5.Generative-Adversial-Networks%2F2.Deep-Convolutional-Gan%2Freadme&filename=5_-_Discriminator_Solution.mp4&fid=0MZqBkd&open=normal)

## 9. Building and Training the Network

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F5.Generative-Adversial-Networks%2F2.Deep-Convolutional-Gan%2Freadme&filename=6_-_Building_And_Training_The_Network.mp4&fid=0MZqBkd&open=normal)

## 10. Hyperparameters Solution

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F5.Generative-Adversial-Networks%2F2.Deep-Convolutional-Gan%2Freadme&filename=7_-_Hyperparameters_Solution.mp4&fid=0MZqBkd&open=normal)
