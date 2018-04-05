# Monte Carlo Methods

## 1. Introduction

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=1_-_Introduction.mp4&fid=0MZqBkd&open=normal)

This lesson covers material in **Chapter 5** (especially 5.1-5.6) of the [textbook](http://go.udacity.com/rl-textbook).

## 2. OpenAI Gym: BlackjackEnv

In this lesson, you will write code to teach an agent to play Blackjack.

![Source: https://www.blackjackinfo.com/img/2-card-21.png](readme/part2-1.png)

Please read about the game of Blackjack in Example 5.1 of the [textbook](http://go.udacity.com/rl-textbook).

When you have finished, please review the corresponding [GitHub file](https://github.com/openai/gym/blob/master/gym/envs/toy_text/blackjack.py), 
by reading the commented block in the BlackjackEnv class. (While you do not need to understand how all of the code 
works, please read the commented block that explains the dynamics of the environment.) or clarity, we have also pasted 
the description of the environment below:

    """Simple blackjack environment

    Blackjack is a card game where the goal is to obtain cards that sum to as
    near as possible to 21 without going over.  They're playing against a fixed
    dealer.
    Face cards (Jack, Queen, King) have point value 10.
    Aces can either count as 11 or 1, and it's called 'usable' at 11.
    This game is placed with an infinite deck (or with replacement).
    The game starts with each (player and dealer) having one face up and one
    face down card.

    The player can request additional cards (hit=1) until they decide to stop
    (stick=0) or exceed 21 (bust).

    After the player sticks, the dealer reveals their facedown card, and draws
    until their sum is 17 or greater.  If the dealer goes bust the player wins.

    If neither player nor dealer busts, the outcome (win, lose, draw) is
    decided by whose sum is closer to 21.  The reward for winning is +1,
    drawing is 0, and losing is -1.

    The observation of a 3-tuple of: the players current sum,
    the dealer's one showing card (1-10 where 1 is ace),
    and whether or not the player holds a usable ace (0 or 1).

    This environment corresponds to the version of the blackjack problem
    described in Example 5.1 in Reinforcement Learning: An Introduction
    by Sutton and Barto (1998).
    http://incompleteideas.net/sutton/book/the-book.html
    """
    
## 3. MC Prediction: State Values

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=2_-_MC_Prediction:_State_Values.mp4&fid=0MZqBkd&open=normal)

## 4. Implementation

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part6-5-4.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-4.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part6-5-4.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-4.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part6-5-4.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-4.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 6. MC Prediction: Action Values

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=3_-_MC_Prediction:_Action_Values.mp4&fid=0MZqBkd&open=normal)

## 7. Implementation

<object data="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-7.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-7.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-7.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-7.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-7.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-7.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 9. Generalized Policy Iteration

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=4_-_Generalized_Policy_Iteration.mp4&fid=0MZqBkd&open=normal)

## 10. MC Control: Incremental Mean

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=5_-_MC_Control:_Incremental_Mean.mp4&fid=0MZqBkd&open=normal)

## 11. Quiz: Incremental Mean

<object data="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-11.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-11.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-11.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-11.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-11.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-11.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 12. MC Control: Policy Evaluation

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=6_-_MC_Control:_Policy_Evaluation.mp4&fid=0MZqBkd&open=normal)

## 13. MC Control: Policy Improvement

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=7_-_MC_Control:_Policy_Improvement.mp4&fid=0MZqBkd&open=normal)

## 14. Quiz: Epsilon-Greedy Policies

<object data="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-14.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-14.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-14.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-14.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-14.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-14.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 15. Exploration vs. Explotation

<object data="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-15.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-15.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-15.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-15.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-15.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-15.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 16. Implementation

<object data="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-16.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-16.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-16.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-16.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-16.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-16.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 18. MC Control: Constant-alpha, Part 1

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=8_-_MC_Control:_Constant-alpha.mp4&fid=0MZqBkd&open=normal)

## 19. MC Control: Constant-alpha, Part 2

<object data="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-19.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-19.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-19.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-19.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-19.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-19.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 20. Implementation

<object data="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-20.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-20.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-20.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-20.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-20.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-20.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 22. Summary

<object data="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-22.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-22.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-22.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-22.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="hhttp://scrier.myqnapcloud.com:8080/share.cgi/part6-5-22.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F6.Reinforcement-Learning%2F5.Monte-Carlo-Methods%2Freadme&filename=part6-5-22.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>
