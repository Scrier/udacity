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
| 1        | 1         | 0.2   | 128        | 100   | 0.0005        | 0.5    | ![n0](readme/number0.png) | ![c0](readme/celeb0.png) |
| 1        | 1         | 0.1   | 128        | 100   | 0.0001        | 0.5    | ![n1](readme/number1.png) | ![c1](readme/celeb1.png) |
| 1        | 1         | 0.05  | 128        | 100   | 0.00005       | 0.5    | ![n2](readme/number2.png) | ![c2](readme/celeb2.png) |
| 1        | 1         | 0.05  | 128        | 100   | 0.00005       | 0.8    | ![n3](readme/number3.png) | ![c3](readme/celeb3.png) |
| 1        | 1         | 0.05  | 128        | 100   | 0.00001       | 0.8    | ![n4](readme/number4.png) | ![c4](readme/celeb4.png) |
| 1        | 1         | 0.05  | 128        | 100   | 0.00001       | 0.5    | ![n5](readme/number5.png) | ![c5](readme/celeb5.png) |
| 1        | 1         | 0.05  | 128        | 200   | 0.00005       | 0.5    | ![n6](readme/number6.png) | ![c6](readme/celeb6.png) |
| 1        | 1         | 0.05  | 128        | 400   | 0.00005       | 0.5    | ![n7](readme/number7.png) | ![c7](readme/celeb7.png) |
| 1        | 1         | 0.05  | 128        | 400   | 0.00005       | 0.9    | ![n8](readme/number8.png) | ![c8](readme/celeb8.png) |
| 1        | 1         | 0.05  | 128        | 400   | 0.00005       | 0.7    | ![n9](readme/number9.png) | ![c9](readme/celeb9.png) |
| 1        | 1         | 0.05  | 128        | 400   | 0.00005       | 0.3    | ![n10](readme/number10.png) | ![c10](readme/celeb10.png) |
| 2        | 1         | 0.05  | 128        | 400   | 0.00005       | 0.5    | ![n11](readme/number11.png) | ![c11](readme/celeb11.png) |
| 2        | 2         | 0.05  | 128        | 400   | 0.00005       | 0.5    | ![n12](readme/number12.png) | ![c12](readme/celeb12.png) |
| 2        | 2         | 0.05  | 256        | 400   | 0.0001        | 0.5    | ![n13](readme/number13.png) | ![c13](readme/celeb13.png) |
| 2        | 2         | 0.05  | 128        | 400   | 0.0001        | 0.5    | ![n14](readme/number14.png) | ![c14](readme/celeb14.png) |
| 2        | 2         | 0.05  | 128        | 400   | 0.00001       | 0.5    | ![n15](readme/number15.png) | ![c15](readme/celeb15.png) |
| 3        | 2         | 0.05  | 128        | 400   | 0.00005       | 0.5    | ![n16](readme/number16.png) | ![c16](readme/celeb16.png) |
| 3        | 2         | 0.05  | 128        | 400   | 0.0005        | 0.8    | ![n17](readme/number17.png) | ![c17](readme/celeb17.png) |
| 3        | 2         | 0.05  | 128        | 400   | 0.0005        | 0.2    | ![n18](readme/number18.png) | ![c18](readme/celeb18.png) |
| 3        | 2         | 0.05  | 128        | 400   | 0.0001        | 0.5    | ![n19](readme/number19.png) | ![c19](readme/celeb19.png) |
