# Transfer Learning in Tensorflow

## 1. Transfer Learning Intro 

In this lesson you'll be learning about transfer learning. In practice, you won't typically be training your own huge networks. There are multiple models out there that have been trained for weeks on huge datasets like [ImageNet](http://www.image-net.org/). In this lesson, you'll be using one of these pretrained networks, [VGGNet](http://www.robots.ox.ac.uk/~vgg/research/very_deep/), to classify images of flowers.

### The lesson notebooks
As always, you can find the notebooks used in this lesson in our [public GitHub repository](https://github.com/udacity/deep-learning).

To get the files:

```bash
git clone https://github.com/udacity/deep-learning.git
```

The notebooks are in the `transfer-learning` directory.

We'll be using a pretrained network from [https://github.com/machrisaa/tensorflow-vgg](https://github.com/machrisaa/tensorflow-vgg). Make sure you clone this repository into the `transfer-learning` directory.

```bash
cd  transfer-learning
git clone https://github.com/machrisaa/tensorflow-vgg.git tensorflow_vgg
```

### Additional Packages
To run this code, you'll need a few packages you might not have installed in your environment. You'll need all the normal ones, plus `tqdm` and `scikit-image`. To install them, use Conda as usual:

```bash
pip install tqdm
conda install scikit-image
```
