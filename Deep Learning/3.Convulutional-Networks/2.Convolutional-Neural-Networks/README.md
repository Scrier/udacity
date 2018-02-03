# Convulutional Neural Networks

## 2. Applications of CNN's

 * Read about the [WaveNet](https://deepmind.com/blog/wavenet-generative-model-raw-audio/) model.
   * Why train an A.I. to talk, when you can train it to sing ;)? In April 2017, researchers used a variant of the WaveNet model to generate songs. The original paper and demo can be found here.
 * Learn about CNNs [for text classification](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/).
   * You might like to sign up for the author's [Deep Learning Newsletter](https://www.getrevue.co/profile/wildml)!
 * Read about [Facebook's novel CNN](https://code.facebook.com/posts/1978007565818999/a-novel-approach-to-neural-machine-translation/) approach for language translation that achieves state-of-the-art accuracy at nine times the speed of RNN models.
 * Play [Atari games](https://deepmind.com/research/dqn/) with a CNN and reinforcement learning. You can [download](https://sites.google.com/a/deepmind.com/dqn/) the code that comes with this paper.
  * If you would like to play around with some beginner code (for deep reinforcement learning), you're encouraged to check out Andrej Karpathy's [post](http://karpathy.github.io/2016/05/31/rl/).
 * Play [pictionary](https://quickdraw.withgoogle.com/#) with a CNN!
  * Also check out all of the other cool implementations on the [A.I. Experiments](https://aiexperiments.withgoogle.com/) website. Be sure not to miss [AutoDraw](https://www.autodraw.com/)!
 * Read more about [AlphaGo](https://deepmind.com/research/alphago/).
  * Check out [this article](https://www.technologyreview.com/s/604273/finding-solace-in-defeat-by-artificial-intelligence/?set=604287), which asks the question: If mastering Go “requires human intuition,” what is it like to have a piece of one’s humanity challenged?
 * Check out these really cool videos with drones that are powered by CNNs.
  * Here's an interview with a startup - [Intelligent Flying Machines (IFM)](https://www.youtube.com/watch?v=AMDiR61f86Y).
  * Outdoor autonomous navigation is typically accomplished through the use of the [global positioning system (GPS)](http://www.droneomega.com/gps-drone-navigation-works/), but here's a demo with a CNN-powered autonomous drone.
 * If you're excited about using CNNs in self-driving cars, you're encouraged to check out:
  * our [Self-Driving Car Engineer Nanodegree](https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013), where we classify signs in the [German Traffic Sign](http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset) dataset in [this project](https://github.com/udacity/CarND-Traffic-Sign-Classifier-Project).
  * our [Machine Learning Engineer Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009), where we classify house numbers from the [Street View House Numbers](http://ufldl.stanford.edu/housenumbers/) dataset in [this project](https://github.com/udacity/machine-learning/tree/master/projects/digit_recognition).
  * this [series of blog posts](https://pythonprogramming.net/game-frames-open-cv-python-plays-gta-v/) that details how to train a CNN in Python to produce a self-driving A.I. to play Grand Theft Auto V.
 * Check out some additional applications not mentioned in the video.
  * Some of the world's most famous paintings have been [turned into 3D](http://www.businessinsider.com/3d-printed-works-of-art-for-the-blind-2016-1) for the visually impaired. Although the article does not mention how this was done, we note that it is possible to use a CNN to [predict depth](https://www.cs.nyu.edu/~deigen/depth/) from a single image.
  * Check out [this research](https://research.googleblog.com/2017/03/assisting-pathologists-in-detecting.html) that uses CNNs to localize breast cancer.
  * CNNs are used to [save endangered species](https://blogs.nvidia.com/blog/2016/11/04/saving-endangered-species/?adbsc=social_20170303_70517416)!
  * An app called [FaceApp](http://www.digitaltrends.com/photography/faceapp-neural-net-image-editing/) uses a CNN to make you smile in a picture or change genders.
  
## 5. MLPs for Image Classification

 * Check out the [first research paper](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf) to propose dropout as a technique for overfitting.
 * Here's the Keras [documentation](https://keras.io/layers/core/#flatten) for the Flatten layer.
 * If you'd like more information on activation functions, check out this [website](http://cs231n.github.io/neural-networks-1/#actfun).

## 6. Categorical Cross-Entropy

 * If you'd like more details about fully connected layers in Keras, check out the [documentation](https://keras.io/layers/core/) for the Dense layer. You can change the way the weights are initialized through supplying values for the kernel_initializer and bias_initializer parameters. Note that the default values are 'glorot_uniform', and 'zeros', respectively. You can read more about how each of these initializers work in the corresponding Keras documentation.
 * There are many different [loss functions](https://keras.io/losses/) in Keras. For this lesson, we will only use categorical_crossentropy.
 * Check out the [list of available optimizers](https://keras.io/optimizers/) in Keras. The optimizer is specified when you compile the model (in Step 7 of the notebook).
  * 'sgd' : SGD
  * 'rmsprop' : RMSprop
  * 'adagrad' : Adagrad
  * 'adadelta' : Adadelta
  * 'adam' : Adam
  * 'adamax' : Adamax
  * 'nadam' : Nadam
  * 'tfoptimizer' : TFOptimizer

```python
# compile the model
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', 
              metrics=['accuracy'])
```

## 7. Model Validation in Keras

There are many callbacks (such as ModelCheckpoint) that you can use to monitor your model during the training process. If you'd like, check out the [details](https://keras.io/callbacks/#modelcheckpoint) here. You're encouraged to begin with learning more about the EarlyStopping callback. If you'd like to see another code example of ModelCheckpoint, check out [this blog](http://machinelearningmastery.com/check-point-deep-learning-models-keras/).
```python
from keras.callbacks import ModelCheckpoint   

# train the model
checkpointer = ModelCheckpoint(filepath='mnist.model.best.hdf5', 
                               verbose=1, save_best_only=True)
hist = model.fit(X_train, y_train, batch_size=128, epochs=10,
          validation_split=0.2, callbacks=[checkpointer],
          verbose=1, shuffle=True)
```

