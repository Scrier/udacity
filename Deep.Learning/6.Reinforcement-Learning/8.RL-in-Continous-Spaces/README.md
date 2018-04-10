# RL in Continous Spaces

## 1. Deep Reinforcement Learning

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=1_-_Deep_Reinforcement_Learning.mp4&fid=0MZqBkd&open=normal)

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part6-8-1.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=part6-8-1.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part6-8-1.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=part6-8-1.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part6-8-1.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=part6-8-1.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 2. Resources

### Coding: OpenAI Gym
We'll be using OpenAI Gym for coding exercises throughout this class. It is an open-source library and platform for 
developing and sharing reinforcement learning algorithms. If you haven't used it before, now is a good time to get 
familiar with it.

Read the instructions in the [OpenAI Gym documentation](https://gym.openai.com/docs/) to learn the basic syntax.

> The documentation has instructions for installing OpenAI Gym on your computer. If you’d like, you can skip this 
> step, as you will have the option to do all of your coding implementations within the classroom. But I personally 
> recommend installing it, because it’s pretty fun to tinker with!

You're also encouraged to take the time to check out the [leaderboard](https://github.com/openai/gym/wiki/Leaderboard), 
which contains the best solutions to each task.

Check out [this blog](https://blog.openai.com/openai-gym-beta/) post to read more about how OpenAI Gym is used to accelerate reinforcement learning (RL) research.

### Textbook: Sutton & Barto, 2nd Ed.
We will recommend you to read excerpts from this [classic textbook on reinforcement learning](http://go.udacity.com/rl-textbook). The topics we cover in 
Deep Reinforcement Learning are discussed in Part II: Approximate Solution Methods. In addition, we'll refer to 
important papers that provide further details about specific algorithms and techniques.

> Note that all of the suggested readings are optional! But they are highly recommended, esp. if you find a topic 
> interesting and want to know more about it, or if something is unclear and you need an alternate explanation.

Check out this [GitHub repository](https://github.com/ShangtongZhang/reinforcement-learning-an-introduction) to see Python implementations of most of the figures in the book.

## 3. Discrete vs. Continuous Space

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=2_-_Discrete_vs._Continuous_Spaces.mp4&fid=0MZqBkd&open=normal)

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part6-8-3.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=part6-8-3.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part6-8-3.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=part6-8-3.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part6-8-3.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=part6-8-3.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 4. Space Representations

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part6-8-4.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=part6-8-4.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part6-8-4.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=part6-8-4.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part6-8-4.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=part6-8-4.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 5. Discretization

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=3_-_Discretization.mp4&fid=0MZqBkd&open=normal)

## 6. Tile Coding

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=4_-_Tile_Coding.mp4&fid=0MZqBkd&open=normal)

## 7. Coarse Coding

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=5_-_Coarse_Coding.mp4&fid=0MZqBkd&open=normal)

## 8. Function Approximation

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=6_-_Function_Approximation.mp4&fid=0MZqBkd&open=normal)

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part6-8-8.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=part6-8-8.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part6-8-8.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=part6-8-8.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part6-8-8.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=part6-8-8.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 9. Linear Function Approximation

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=7_-_Linear_Function_Approximation.mp4&fid=0MZqBkd&open=normal)

## 10. Kernel Functions

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=8_-_Kernel_Functions.mp4&fid=0MZqBkd&open=normal)

## 11. Non-Linear Function Approximation

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=9_-_Non-Linear_Function_Approximation.mp4&fid=0MZqBkd&open=normal)

## 12. Summary

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F8.RL-in-Continous-Spaces%2Freadme&filename=10_-_Summary.mp4&fid=0MZqBkd&open=normal)
