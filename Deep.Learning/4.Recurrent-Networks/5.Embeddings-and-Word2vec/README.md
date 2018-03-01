# Embeddings and Word2vec

## 1. Embeddings Intro

### Word Embeddings

This week, we'll be covering embeddings. This is a deep neural network method for representing data with a huge number 
of classes more efficiently. Embeddings greatly improve the ability of networks to learn from data of this sort by 
representing the data with lower dimensional vectors.

Word embeddings in particular are interesting because the networks are able to learn semantic relationships between 
words. For example, the embeddings will know that the male equivalent of a queen is a king.

![part5-1](readme/part5-1.png)

These word embeddings are learned using a model called [Word2vec](https://en.wikipedia.org/wiki/Word2vec). In this lesson, you'll implement Word2vec yourself.

We've built a notebook with exercises and also provided our solutions. You can find the notebooks in our [GitHub repo](https://github.com/udacity/deep-learning/tree/master/embeddings) 
in the `embeddings` folder.

> **Requirements**: You'll need Numpy, Matplotlib, Scikit-learn, tqdm, and **TensorFlow 1.0** to run this code.

Next up, I'll walk you through implementing the Word2Vec model.

## 2. Implementing Word2Vec

[![Video](readme/video1.png)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F5.Embeddings-and-Word2vec%2Freadme&filename=1_-_Implementing_Word2Vec.mp4&fid=0MZqBkd&open=normal)

## 3. Subsampling Solution

[![Video](readme/video2.png)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F5.Embeddings-and-Word2vec%2Freadme&filename=2_-_Subsampling_Solution.mp4&fid=0MZqBkd&open=normal)

## 4. Making Batches

[![Video](readme/video3.png)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F5.Embeddings-and-Word2vec%2Freadme&filename=3_-_Making_Batches.mp4&fid=0MZqBkd&open=normal)

## 5. Batches Solution

[![Video](readme/video4.png)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F5.Embeddings-and-Word2vec%2Freadme&filename=4_-_Batches_Solution.mp4&fid=0MZqBkd&open=normal)

## 6. Building the Network

[![Video](readme/video5.png)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F5.Embeddings-and-Word2vec%2Freadme&filename=5_-_Building_The_Network.mp4&fid=0MZqBkd&open=normal)

## 7. Negative Sampling

[![Video](readme/video6.png)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F5.Embeddings-and-Word2vec%2Freadme&filename=6_-_Negative_Sampling.mp4&fid=0MZqBkd&open=normal)

## 8. Building the Network Solution

[![Video](readme/video7.png)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F5.Embeddings-and-Word2vec%2Freadme&filename=7_-_Building_The_Network_Solution.mp4&fid=0MZqBkd&open=normal)

## 9. Training Results

[![Video](readme/video8.png)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F4.Recurrent-Networks%2F5.Embeddings-and-Word2vec%2Freadme&filename=8_-_Training_Results.mp4&fid=0MZqBkd&open=normal)
