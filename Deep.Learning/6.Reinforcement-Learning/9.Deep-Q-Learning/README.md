# Deep Q Learning

## 1. Intro to Deep Q-Learning

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F9.Deep-Q-Learning%2Freadme&filename=1_-_Intro_to_Deep_Q-Learning.mp4&fid=0MZqBkd&open=normal)

## 2. Neural Nets as Value Functions

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F9.Deep-Q-Learning%2Freadme&filename=2_-_Neural_Nets_as_Value_Functions.mp4&fid=0MZqBkd&open=normal)

## 3. Monte Carlo Learning

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F9.Deep-Q-Learning%2Freadme&filename=3_-_Monte_Carlo_Learning.mp4&fid=0MZqBkd&open=normal)

**Note:** MC is guaranteed to converge on a local optimum in general; in case of a linear function approximation, it 
will converge on the global optimum.

## 4. Temporal Diggerence Learning

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F9.Deep-Q-Learning%2Freadme&filename=4_-_Temporal_Difference_Learning.mp4&fid=0MZqBkd&open=normal)

## 5. Q-Learning

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F9.Deep-Q-Learning%2Freadme&filename=5_-_Q-Learning.mp4&fid=0MZqBkd&open=normal)

**Note:** One drawback of both SARSA & Q-Learning, since they are TD approaches, is that they may not converge on the 
global optimum when using non-linear function approximation.

### Readings

 * Rahimi & Recht, 2007. [Random Features for Large-Scale Kernel Machines](https://classroom.udacity.com/nanodegrees/nd101/parts/7d0218b1-1a81-4d49-95f7-14b015020851/modules/691b7845-f7d8-413d-90c7-971cd5016b5c/lessons/2faec296-1a78-4393-9aea-2b91310713ed/concepts/www.robots.ox.ac.uk/~vgg/rg/papers/randomfeatures.pdf). Presents an efficient approximation to 
 RBF-like kernel transforms.
 
## 6. Deep Q Network

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F9.Deep-Q-Learning%2Freadme&filename=6_-_Deep_Q_Network.mp4&fid=0MZqBkd&open=normal)

### Readings

Mnih et al., 2015. [Human-level control through deep reinforcement learning](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf).

## 7. Experience Replay

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F9.Deep-Q-Learning%2Freadme&filename=7_-_Experience_Replay.mp4&fid=0MZqBkd&open=normal)

### Readings

Long-Ji Lin, 1993. [Reinforcement learning for robots using neural networks](https://pdfs.semanticscholar.org/54c4/cf3a8168c1b70f91cf78a3dc98b671935492.pdf).

## 8. Fixed Q Targets

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F9.Deep-Q-Learning%2Freadme&filename=8_-_Fixed_Q_Targets.mp4&fid=0MZqBkd&open=normal)

Ever wondered how this would look in real life? See: [Carrot Stick Riding](https://www.youtube.com/watch?v=-PVFBGN_zoM).

## 9. Deep Q-Learning Algorithm

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F9.Deep-Q-Learning%2Freadme&filename=9_-_Deep_Q-Learning_Algorithm.mp4&fid=0MZqBkd&open=normal)

### Readings

 * Mnih et al., 2015. [Human-level control through deep reinforcement learning](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf). (DQN paper)
 * He et al., 2015. [Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification](https://arxiv.org/abs/1502.01852). 
 (weight initialization)

## 10. DQN Improvements

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F9.Deep-Q-Learning%2Freadme&filename=10_-_DQN_Improvements.mp4&fid=0MZqBkd&open=normal)

### Readings

 * Thrun & Schwartz, 1993. [Issues in Using Function Approximation for Reinforcement Learning](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.73.3097). (overestimation of 
 Q-values)
 * van Hasselt et al., 2015. [Deep Reinforcement Learning with Double Q-Learning](https://arxiv.org/abs/1509.06461).
 * Schaul et al., 2016. [Prioritized Experience Replay](https://arxiv.org/abs/1511.05952).
 * Wang et al., 2015. [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581).
 * Hausknecht & Stone, 2015. [Deep Recurrent Q-Learning for Partially Observable MDPs](https://arxiv.org/abs/1507.06527).

## 11. implementing Deep Q-Learning

![part6-9-11-1](readme/part6-9-11-1.png)

### Implementing Deep Q-Learning

In the **next concept**, you will explore a Jupyter notebook with a TensorFlow implementation of the deep Q-learning 
algorithm.

To run the code on GPU, select "**YES**" in the pop-up window. This will allow you to run the notebook on GPU.

![part6-9-11-2](readme/part6-9-11-2.png)

If you would like to learn how to write an implementation in another Python framework, check out:

 * (Keras) [https://keon.io/deep-q-learning/](https://keon.io/deep-q-learning/)
 * (PyTorch) [http://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html](http://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html)

## 13. Wrap Up

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F9.Deep-Q-Learning%2Freadme&filename=11_-_Wrap_Up.mp4&fid=0MZqBkd&open=normal)
