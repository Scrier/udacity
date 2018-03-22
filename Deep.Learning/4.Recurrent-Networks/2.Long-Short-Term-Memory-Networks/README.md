# Long Short-Term Memory Networks

## 1. Intro to LSTM

Hi! It's Luis again!

Now that you've gone through the **Recurrent Neural Network lesson**, I'll be teaching you what an **LSTM** is. This stands for 
**Long Short Term Memory Networks**, and are quite useful when our neural network needs to switch between remembering 
recent things, and things from long time ago. But first, I want to give you some great references to study this further. 
There are many posts out there about LSTMs, here are a few of my favorites:

 * [Chris Olah's LSTM post](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
 * [Edwin Chen's LSTM post](http://blog.echen.me/2017/05/30/exploring-lstms/)
 * [Andrej Karpathy's lecture](https://www.youtube.com/watch?v=iX5V1WpxxkY) on RNNs and LSTMs from CS231n

So, let's dig in!

## 2. RNN vs LSTM

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=1_-_RNN_Vs_LSTM.mp4&fid=0MZqBkd&open=normal)

## 3. Basics of LSTM

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=2_-_LSTM_Basics.mp4&fid=0MZqBkd&open=normal)

## 4. Architecture of LSTM

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=3_-_LSTM_Architecture.mp4&fid=0MZqBkd&open=normal)

## 5. The Learn Gate

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=4_-_Learn_Gate.mp4&fid=0MZqBkd&open=normal)

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part4-2-5.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=part4-2-5.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part4-2-5.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=part4-2-5.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part4-2-5.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=part4-2-5.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 6. The Forget Gate

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=5_-_Forget_Gate.mp4&fid=0MZqBkd&open=normal)

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part4-2-6.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=part4-2-6.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part4-2-6.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=part4-2-6.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part4-2-6.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=part4-2-6.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 7. The Remember Gate

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=6_-_Remember_Gate.mp4&fid=0MZqBkd&open=normal)

## 8. The Use Gate

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=7_-_LSTM_7_Use_Gate.mp4&fid=0MZqBkd&open=normal)

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part4-2-8.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=part4-2-8.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part4-2-8.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=part4-2-8.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part4-2-8.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=part4-2-8.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 9. Putting it All Togheter

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=8_-_Putting_It_All_Together.mp4&fid=0MZqBkd&open=normal)

## 10. Quiz

<object data="http://scrier.myqnapcloud.com:8080/share.cgi/part4-2-10.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=part4-2-10.pdf&openfolder=normal&ep=" type="application/pdf" width="700px" height="700px">
    <embed src="http://scrier.myqnapcloud.com:8080/share.cgi/part4-2-10.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=part4-2-10.pdf&openfolder=normal&ep=">
        This browser does not support PDFs. Please download the PDF to view it: <a href="http://scrier.myqnapcloud.com:8080/share.cgi/part4-2-10.pdf?ssid=0MZqBkd&fid=0MZqBkd&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=part4-2-10.pdf&openfolder=normal&ep=">Download PDF</a>.</p>
    </embed>
</object>

## 11. Other Architectures

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F2.Long-Short-Term-Memory-Networks%2Freadme&filename=9_-_Other_Architectures.mp4&fid=0MZqBkd&open=normal)
