# Project: Generate Faces

## 1. One Project Away!

[![Video](readme/video1.png)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F5.Generative-Adversial-Networks%2F3.Project-Generate-Faces%2Freadme&filename=1_-_Last_Project_-_Congrats.mp4&fid=0MZqBkd&open=normal)

## 2. Project Introduction

[![Video](readme/video2.png)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F5.Generative-Adversial-Networks%2F3.Project-Generate-Faces%2Freadme&filename=2_-_P5_Intro.mp4&fid=0MZqBkd&open=normal)

## 3. Project: Generate Faces

### Introduction

In this project, you'll use generative adversarial networks to generate new images of faces.

### Getting the project files

The project files can be found in our [public GitHub repo](https://github.com/udacity/deep-learning/tree/master/), in the `face_generation` folder. You can download the files 
from there, but it's better to clone the repository to your computer

This way you can stay up to date with any changes we make by pulling the changes to your local repository with `git pull`.

### Submission

 1. Ensure you've passed all the unit tests in the notebook.
 1. Ensure you pass all points on [the rubric](https://review.udacity.com/#!/rubrics/891/view).
 1. When you're done with the project, please save the notebook as an HTML file. You can do this by going to the 
 **File** menu in the notebook and choosing "Download as" > HTML. **Ensure you submit both the Jupyter Notebook and it's 
 HTML version together**.
 1. Package the "dlnd_face_generation.ipynb", "helper.py", "problem_unittests.py", and the HTML file into a zip 
 archive, or push the files from your GitHub repo.
 1. Hit Submit Project below!
 
 ### Results
 
gen impl | disc impl | alpha | batch size | z dim | learning rate | beta 1 | Number Output | Celeb Output
-------- | --------- | ----- | ---------- | ----- | ------------- | ------ | ------------- | ------------
1 | 1 | 0.2 | 128 | 100 | 0.0005 | 0.5 | ![](readme/number0.jpg) | ![](readme/celeb0.jpg)
1 | 1 | 0.1 | 128 | 100 | 0.0001 | 0.5 | ![](readme/number1.jpg) | ![](readme/celeb1.jpg)
1 | 1 | 0.05 | 128 | 100 | 0.00005 | 0.5 | ![](readme/number2.jpg) | ![](readme/celeb2.jpg)
1 | 1 | 0.05 | 128 | 100 | 0.00005 | 0.8 | ![](readme/number3.jpg) | ![](readme/celeb3.jpg)
1 | 1 | 0.05 | 128 | 100 | 0.00001 | 0.8 | ![](readme/number4.jpg) | ![](readme/celeb4.jpg)
1 | 1 | 0.05 | 128 | 100 | 0.00001 | 0.5 | ![](readme/number5.jpg) | ![](readme/celeb5.jpg)
1 | 1 | 0.05 | 128 | 200 | 0.00005 | 0.5 | ![](readme/number6.jpg) | ![](readme/celeb6.jpg)
1 | 1 | 0.05 | 128 | 400 | 0.00005 | 0.5 | ![](readme/number7.jpg) | ![](readme/celeb7.jpg)
1 | 1 | 0.05 | 128 | 400 | 0.00005 | 0.9 | ![](readme/number8.jpg) | ![](readme/celeb8.jpg)
1 | 1 | 0.05 | 128 | 400 | 0.00005 | 0.7 | ![](readme/number9.jpg) | ![](readme/celeb9.jpg)
1 | 1 | 0.05 | 128 | 400 | 0.00005 | 0.3 | ![](readme/number10.jpg) | ![](readme/celeb10.jpg)
2 | 1 | 0.05 | 128 | 400 | 0.00005 | 0.5 | ![](readme/number11.jpg) | ![](readme/celeb11.jpg)
2 | 2 | 0.05 | 128 | 400 | 0.00005 | 0.5 | ![](readme/number12.jpg) | ![](readme/celeb12.jpg)
2 | 2 | 0.05 | 256 | 400 | 0.0001 | 0.5 | ![](readme/number13.jpg) | ![](readme/celeb13.jpg)
2 | 2 | 0.05 | 128 | 400 | 0.0001 | 0.5 | ![](readme/number14.jpg) | ![](readme/celeb14.jpg)
2 | 2 | 0.05 | 128 | 400 | 0.00001 | 0.5 | ![](readme/number15.jpg) | ![](readme/celeb15.jpg)
3 | 2 | 0.05 | 128 | 400 | 0.00005 | 0.5 | ![](readme/number16.jpg) | ![](readme/celeb16.jpg)
3 | 2 | 0.05 | 128 | 400 | 0.0005 | 0.8 | ![](readme/number17.jpg) | ![](readme/celeb17.jpg)
3 | 2 | 0.05 | 128 | 400 | 0.0005 | 0.2 | ![](readme/number18.jpg) | ![](readme/celeb18.jpg)
3 | 2 | 0.05 | 128 | 400 | 0.0001 | 0.5 | ![](readme/number19.jpg) | ![](readme/celeb19.jpg)
4 | 2 | 0.05 | 128 | 400 | 0.00005 | 0.5 | ![](readme/number20.jpg) | ![](readme/celeb20.jpg)

Feels now that the discrimnator is too strong. Trying with adding dropout to the discriminator to drop the learning rate.

gen impl | disc impl | gen drop | disc drop | alpha | batch size | z dim | learning rate | beta 1 | Number Output | Celeb Output
-------- | --------- | -------- | --------- | ----- | ---------- | ----- | ------------- | ------ | ------------- | ------------
4 | 3 | 0.5 | 0.25 | 0.05 | 128 | 400 | 0.00005 | 0.5 | ![](readme/number21.jpg) | ![](readme/celeb21.jpg)
4 | 3 | 0.5 | 0.5 | 0.05 | 128 | 100 | 0.00025 | 0.5 | ![](readme/number22.jpg) | ![](readme/celeb22.jpg)
4 | 3 | 0.5 | 0.5 | 0.1 | 128 | 100 | 0.0025 | 0.5 | ![](readme/number23.jpg) | ![](readme/celeb23.jpg)
4 | 3 | 0.5 | 0.5 | 0.05 | 256 | 100 | 0.0005 | 0.5 | ![](readme/number24.jpg) | ![](readme/celeb24.jpg)
4 | 3 | 0.5 | 0.5 | 0.05 | 64 | 100 | 0.000075 | 0.5 | ![](readme/number25.jpg) | ![](readme/celeb25.jpg)

add smooth factor to model_loss method

gen impl | disc impl | gen/disc drop | smooth facttor | alpha | batch size | z dim | learning rate | beta 1 | Number Output | Celeb Output
-------- | --------- | ------------- | -------------- | ----- | ---------- | ----- | ------------- | ------ | ------------- | ------------
4 | 3 | 0.5 / 0.5 | 0.1 | 0.2 | 64 | 100 | 0.00025 | 0.45 | ![](readme/number26.jpg) | ![](readme/celeb26.jpg)
4 | 3 | 0.5 / 0.5 | 0.1 | 0.2 | 128 | 100 | 0.0001 | 0.5 | ![](readme/number27.jpg) | ![](readme/celeb27.jpg)
4 | 3 | 0.5 / 0.5 | 0.1 | 0.2 | 128 | 400 | 0.0001 | 0.5 | ![](readme/number28.jpg) | ![](readme/celeb28.jpg)
4 | 3 | 0.5 / 0.5 | 0.1 | 0.2 | 128 | 400 | 0.00001 | 0.5 | ![](readme/number29.jpg) | ![](readme/celeb29.jpg)
4 | 3 | 0.5 / 0.5 | 0.1 | 0.2 | 128 | 400 | 0.001 | 0.5 | ![](readme/number30.jpg) | ![](readme/celeb30.jpg)
4 | 3 | 0.5 / 0.5 | 0.1 | 0.2 | 64 | 400 | 0.001 | 0.5 | ![](readme/number31.jpg) | ![](readme/celeb31.jpg)
4 | 3 | 0.5 / 0.5 | 0.1 | 0.2 | 64 | 400 | 0.0001 | 0.5 | ![](readme/number32.jpg) | ![](readme/celeb32.jpg)
4 | 3 | 0.5 / 0.5 | 0.1 | 0.1 | 64 | 400 | 0.0001 | 0.5 | ![](readme/number33.jpg) | ![](readme/celeb33.jpg)
1 | 1 | n/a / n/a | 0.1 | 0.1 | 128 | 400 | 0.0001 | 0.5 | ![](readme/number34.jpg) | ![](readme/celeb34.jpg)
1 | 1 | n/a / n/a | 0.1 | 0.1 | 64 | 400 | 0.0001 | 0.5 | ![](readme/number35.jpg) | ![](readme/celeb35.jpg)
1 | 1 | n/a / n/a | 0.1 | 0.1 | 64 | 400 | 0.0001 | 0.4 | ![](readme/number36.jpg) | ![](readme/celeb36.jpg)
1 | 1 | n/a / n/a | 0.1 | 0.1 | 64 | 400 | 0.0001 | 0.6 | ![](readme/number37.jpg) | ![](readme/celeb37.jpg)
1 | 1 | n/a / n/a | 0.2 | 0.1 | 64 | 400 | 0.0001 | 0.6 | ![](readme/number38.jpg) | ![](readme/celeb38.jpg)

