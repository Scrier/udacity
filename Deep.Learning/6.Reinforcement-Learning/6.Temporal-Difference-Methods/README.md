# Temporal-Difference Methods

## 1. Introduction

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=1_-_Introduction.mp4&fid=0MZqBkd&open=normal)

This lesson covers material in **Chapter 6** (especially 6.1-6.6) of the [textbook](http://go.udacity.com/rl-textbook).

## 2. OpenAI Gym: CliffWalkingEnv

In this lesson, you will write your own Python implementations of all of the algorithms that we discuss. While your 
algorithms will be designed to work with any OpenAI Gym environment, you will test your code with the CliffWalking 
environment.

![Source: Wikipedia](readme/part2-1.jpg)

In the CliffWalking environment, the agent navigates a 4x12 gridworld. Please read about the cliff-walking task in 
Example 6.6 of the [textbook](http://go.udacity.com/rl-textbook). When you have finished, you can learn more about the environment in its corresponding 
[GitHub file](https://github.com/openai/gym/blob/master/gym/envs/toy_text/cliffwalking.py), by reading the commented block in the CliffWalkingEnv class. For clarity, we have also pasted the 
description of the environment below (note that the link below to the Sutton and Barto textbook may not work, and 
you're encouraged to use [this link](http://go.udacity.com/rl-textbook) to access the textbook):

    """
    This is a simple implementation of the Gridworld Cliff
    reinforcement learning task.
    Adapted from Example 6.6 (page 145) from Reinforcement Learning: An Introduction
    by Sutton and Barto:
    http://people.inf.elte.hu/lorincz/Files/RL_2006/SuttonBook.pdf

    With inspiration from:
    https://github.com/dennybritz/reinforcement-learning/blob/master/lib/envs/cliff_walking.py
    The board is a 4x12 matrix, with (using Numpy matrix indexing):
        [3, 0] as the start at bottom-left
        [3, 11] as the goal at bottom-right
        [3, 1..10] as the cliff at bottom-center
    Each time step incurs -1 reward, and stepping into the cliff incurs -100 reward 
    and a reset to the start. An episode terminates when the agent reaches the goal.
    """

## 3. TD Prediction: TD(0)

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=2_-_TD_Prediction:_TD(0).mp4&fid=0MZqBkd&open=normal)

## 4. Implementation

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-4.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-4.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-4.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-4.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-4.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-4.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 6. TD Prediction: Action Values

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=3_-_TD_Prediction:_Action_Values.mp4&fid=0MZqBkd&open=normal)

Similar to TD(0), this method for estimating the action values is guaranteed to converge to the true action-value 
function, as long as the step-size parameter α is sufficiently small.

## 7. TD Control: Sarsa(0)

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=4_-_TD_Control:_Sarsa(0).mp4&fid=0MZqBkd&open=normal)

## 8. Implementation

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-8.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-8.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-8.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-8.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-8.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-8.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 10. TD Control: Sarsamax

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=5_-_TD_Control:_Sarsamax.mp4&fid=0MZqBkd&open=normal)

Check out this (optional) [research paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.80.7501&rep=rep1&type=pdf) to read the proof that Sarsamax (or Q-learning) converges.

## 11. Implementation

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-11.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-11.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-11.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-11.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-11.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-11.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 13. TD Control: Expected Sarsa

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=6_-_TD_Control:_Expected_Sarsa.mp4&fid=0MZqBkd&open=normal)

Check out this [research paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.216.4144&rep=rep1&type=pdf) to learn more about Expected Sarsa.

## 14. Implementation

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-14.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-14.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-14.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-14.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-14.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-14.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 16. Analyzing Performance

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-16.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-16.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-16.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-16.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-16.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-16.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 17. Summary

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-17.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-17.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-17.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-17.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part6-6-17.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F6.Temporal-Difference-Methods%2Freadme&filename=part6-6-17.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>
