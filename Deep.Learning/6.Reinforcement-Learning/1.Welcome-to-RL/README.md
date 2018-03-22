# Welcome to RL!

## 1. Introduction

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F1.Welcome-to-RL%2Freadme&filename=1_-_Introduction.mp4&fid=0MZqBkd&open=normal)

## 2. Applications

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F1.Welcome-to-RL%2Freadme&filename=2_-_Applications.mp4&fid=0MZqBkd&open=normal)

### Optional Resources

 * Read about [TD-Gammon](https://courses.cs.washington.edu/courses/cse590hk/01sp/Readings/tesauro95cacm.pdf), one of the first successful applications of neural networks to reinforcement learning.
 * Read about [AlphaGo Zero](https://deepmind.com/blog/alphago-zero-learning-scratch/), the state-of-the-art computer program that defeats professional human Go players.
 * Learn about how reinforcement learning (RL) is used to play [Atari games](https://deepmind.com/research/dqn/).
 * Read about [OpenAI's bot](https://blog.openai.com/dota-2/) that beat the world’s top players of [Dota 2](http://www.dota2.com/play/).
 * Read about [research](https://classroom.udacity.com/nanodegrees/nd101/parts/7d0218b1-1a81-4d49-95f7-14b015020851/modules/38c16ab9-91e8-44ce-a0ce-ae1b9ba12146/lessons/2942b8b9-76c1-451d-879c-3d31d3ac00c8/concepts/(https://deepmind.com/blog/producing-flexible-behaviours-simulated-environments/) used to teach humanoid bodies to walk.
 * Learn about RL for [self-driving cars](http://selfdrivingcars.mit.edu/).
 * To see an example of RL applied to finance, check out this [final project](https://github.com/ucaiado/QLearning_Trading) 
 from a student who graduated from the [Machine Learning Engineer Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009). 
 * Learn about RL for [telecommunication](https://papers.nips.cc/paper/1740-low-power-wireless-communication-via-reinforcement-learning.pdf).
 * Read [this paper](https://goo.gl/e3gaM2) that introduces RL for inventory management.

## 3. The Setting

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F1.Welcome-to-RL%2Freadme&filename=3_-_The_Setting.mp4&fid=0MZqBkd&open=normal)

## 4. OpenAI Gym

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F1.Welcome-to-RL%2Freadme&filename=4_-_OpenAI_Gym.mp4&fid=0MZqBkd&open=normal)

You are **not** required to install OpenAI Gym on your computer, and you will have the option to do all of your coding 
implementations within the classroom. You can learn more about OpenAI Gym by perusing the [GitHub repository](https://github.com/openai/gym.git).

You're encouraged to take the time to check out the [leaderboard](https://github.com/openai/gym/wiki/Leaderboard), which contains the best solutions to each task.

Check out this [blog post](https://blog.openai.com/openai-gym-beta/) to read more about how OpenAI Gym is used to accelerate reinforcement learning (RL) research.

### (Optional) Installation Instructions

If you'd like to install OpenAI Gym on your machine, you are encouraged to perform a minimal install:

```bash
git clone https://github.com/openai/gym.git
cd gym
pip install -e .
```

Once you have installed OpenAI Gym, obtain the code for the classic control tasks (such as `'CartPole-v0'`):

pip install -e '.[classic_control]'
Finally, check your installation by running the [simple random agent](https://github.com/openai/gym/blob/master/examples/agents/random_agent.py) provided in the `examples` directory.

```bash
cd examples/agents
python random_agent.py
```

(These instructions are derived from the README in the [GitHub repository](https://github.com/openai/gym).)

## 5. Resources

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F1.Welcome-to-RL%2Freadme&filename=5_-_Resources.mp4&fid=0MZqBkd&open=normal)

As part of this course, we will recommend excerpts from this [classic textbook on reinforcement learning](http://go.udacity.com/rl-textbook).

**Note that all of the suggested readings are optional!**

Check out this [GitHub repository](https://github.com/ShangtongZhang/reinforcement-learning-an-introduction) to see Python implementations of most of the figures in the book.

Before transitioning to the next lesson, you are encouraged to read Chapter 1 (especially 1.1-1.4) of the [textbook](http://go.udacity.com/rl-textbook) 
to get a nice introduction to the field of reinforcement learning.

## 6. Reference Guide

You are encouraged to download [this sheet](https://github.com/udacity/rl-cheatsheet/blob/master/cheatsheet.pdf), which contains all of the notation and algorithms that we will use in this 
course. Please only use this sheet as a supplement to your own notes! :)

Another useful notation guide can be found in the pages immediately preceding Chapter 1 of the [textbook](http://go.udacity.com/rl-textbook).

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/cheatsheet.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F1.Welcome-to-RL%2Freadme&filename=cheatsheet.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/cheatsheet.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F1.Welcome-to-RL%2Freadme&filename=cheatsheet.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/cheatsheet.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F1.Welcome-to-RL%2Freadme&filename=cheatsheet.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>
