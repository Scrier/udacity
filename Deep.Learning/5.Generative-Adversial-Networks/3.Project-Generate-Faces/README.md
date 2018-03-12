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
 
| gen impl | disc impl | alpha | batch size | z dim | learning rate | beta 1 | Number Output | Celeb Output |
| -------- | --------- | ----- | ---------- | ----- | ------------- | ------ | ------------- | ------------ |
| 1        | 1         | 0.2   | 128        | 100   | 0.0005        | 0.5    | ![](readme/number0.png) | ![](readme/celeb0.png) |
| 1        | 1         | 0.1   | 128        | 100   | 0.0001        | 0.5    | ![](readme/number1.png) | ![](readme/celeb1.png) |
| 1        | 1         | 0.05  | 128        | 100   | 0.00005       | 0.5    | ![](readme/number2.png) | ![](readme/celeb2.png) |
| 1        | 1         | 0.05  | 128        | 100   | 0.00005       | 0.8    | ![](readme/number3.png) | ![](readme/celeb3.png) |
| 1        | 1         | 0.05  | 128        | 100   | 0.00001       | 0.8    | ![](readme/number4.png) | ![](readme/celeb4.png) |
| 1        | 1         | 0.05  | 128        | 100   | 0.00001       | 0.5    | ![](readme/number5.png) | ![](readme/celeb5.png) |
| 1        | 1         | 0.05  | 128        | 200   | 0.00005       | 0.5    | ![](readme/number6.png) | ![](readme/celeb6.png) |
| 1        | 1         | 0.05  | 128        | 400   | 0.00005       | 0.5    | ![](readme/number7.png) | ![](readme/celeb7.png) |
| 1        | 1         | 0.05  | 128        | 400   | 0.00005       | 0.9    | ![](readme/number8.png) | ![](readme/celeb8.png) |
| 1        | 1         | 0.05  | 128        | 400   | 0.00005       | 0.7    | ![](readme/number9.png) | ![](readme/celeb9.png) |
| 1        | 1         | 0.05  | 128        | 400   | 0.00005       | 0.3    | ![](readme/number10.png) | ![](readme/celeb10.png) |
| 2        | 1         | 0.05  | 128        | 400   | 0.00005       | 0.5    | ![](readme/number11.png) | ![](readme/celeb11.png) |
| 2        | 2         | 0.05  | 128        | 400   | 0.00005       | 0.5    | ![](readme/number12.png) | ![](readme/celeb12.png) |
| 2        | 2         | 0.05  | 256        | 400   | 0.0001        | 0.5    | ![](readme/number13.png) | ![](readme/celeb13.png) |
| 2        | 2         | 0.05  | 128        | 400   | 0.0001        | 0.5    | ![](readme/number14.png) | ![](readme/celeb14.png) |
| 2        | 2         | 0.05  | 128        | 400   | 0.00001       | 0.5    | ![](readme/number15.png) | ![](readme/celeb15.png) |
| 3        | 2         | 0.05  | 128        | 400   | 0.00005       | 0.5    | ![](readme/number16.png) | ![](readme/celeb16.png) |
| 3        | 2         | 0.05  | 128        | 400   | 0.0005        | 0.8    | ![](readme/number17.png) | ![](readme/celeb17.png) |
| 3        | 2         | 0.05  | 128        | 400   | 0.0005        | 0.2    | ![](readme/number18.png) | ![](readme/celeb18.png) |
| 3        | 2         | 0.05  | 128        | 400   | 0.0001        | 0.5    | ![](readme/number19.png) | ![](readme/celeb19.png) |
| 4        | 2         | 0.05  | 128        | 400   | 0.00005       | 0.5    | ![](readme/number20.png) | ![](readme/celeb20.png) |

Feels now that the discrimnator is too strong. Trying with adding dropout to the discriminator to drop the learning rate.

| gen impl | disc impl | gen drop | disc drop | alpha | batch size | z dim | learning rate | beta 1 | Number Output | Celeb Output |
| -------- | --------- | -------- | --------- | ----- | ---------- | ----- | ------------- | ------ | ------------- | ------------ |
| 4        | 3         | 0.5      | 0.25      | 0.05  | 128        | 400   | 0.00005       | 0.5    | ![](readme/number21.png) | ![](readme/celeb21.png) |
| 4        | 3         | 0.5      | 0.5       | 0.05  | 128        | 100   | 0.00025       | 0.5    | ![](readme/number22.png) | ![](readme/celeb22.png) |
| 4        | 3         | 0.5      | 0.5       | 0.1   | 128        | 100   | 0.0025        | 0.5    | ![](readme/number23.png) | ![](readme/celeb23.png) |
| 4        | 3         | 0.5      | 0.5       | 0.05  | 256        | 100   | 0.0005        | 0.5    | ![](readme/number24.png) | ![](readme/celeb24.png) |
| 4        | 3         | 0.5      | 0.5       | 0.05  | 64         | 100   | 0.000075      | 0.5    | ![](readme/number25.png) | ![](readme/celeb25.png) |

add smooth factor to model_loss method

| gen impl | disc impl | gen/disc drop | smooth facttor | alpha | batch size | z dim | learning rate | beta 1 | Number Output | Celeb Output |
| -------- | --------- | ------------- | -------------- | ----- | ---------- | ----- | ------------- | ------ | ------------- | ------------ |
| 4        | 3         | 0.5 / 0.5     | 0.1            | 0.2   | 64         | 100   | 0.00025       | 0.45   | ![](readme/number26.png) | ![](readme/celeb26.png) |
| 4        | 3         | 0.5 / 0.5     | 0.1            | 0.2   | 128        | 100   | 0.0001        | 0.5   | ![](readme/number27.png) | ![](readme/celeb27.png) |
| 4        | 3         | 0.5 / 0.5     | 0.1            | 0.2   | 128        | 400   | 0.0001        | 0.5   | ![](readme/number28.png) | ![](readme/celeb28.png) |
| 4        | 3         | 0.5 / 0.5     | 0.1            | 0.2   | 128        | 400   | 0.00001       | 0.5   | ![](readme/number29.png) | ![](readme/celeb29.png) |
| 4        | 3         | 0.5 / 0.5     | 0.1            | 0.2   | 128        | 400   | 0.001         | 0.5   | ![](readme/number30.png) | ![](readme/celeb30.png) |
| 4        | 3         | 0.5 / 0.5     | 0.1            | 0.2   | 64         | 400   | 0.001         | 0.5   | ![](readme/number31.png) | ![](readme/celeb31.png) |
| 4        | 3         | 0.5 / 0.5     | 0.1            | 0.2   | 64         | 400   | 0.0001        | 0.5   | ![](readme/number32.png) | ![](readme/celeb32.png) |
| 4        | 3         | 0.5 / 0.5     | 0.1            | 0.1   | 64         | 400   | 0.0001        | 0.5   | ![](readme/number33.png) | ![](readme/celeb33.png) |
| 1        | 1         | n/a / n/a     | 0.1            | 0.1   | 128        | 400   | 0.0001        | 0.5   | ![](readme/number34.png) | ![](readme/celeb34.png) |
| 1        | 1         | n/a / n/a     | 0.1            | 0.1   | 64         | 400   | 0.0001        | 0.5   | ![](readme/number35.png) | ![](readme/celeb35.png) |
| 1        | 1         | n/a / n/a     | 0.1            | 0.1   | 64         | 400   | 0.0001        | 0.4   | ![](readme/number36.png) | ![](readme/celeb36.png) |
| 1        | 1         | n/a / n/a     | 0.1            | 0.1   | 64         | 400   | 0.0001        | 0.6   | ![](readme/number37.png) | ![](readme/celeb37.png) |
| 1        | 1         | n/a / n/a     | 0.2            | 0.1   | 64         | 400   | 0.0001        | 0.6   | ![](readme/number38.png) | ![](readme/celeb38.png) |

