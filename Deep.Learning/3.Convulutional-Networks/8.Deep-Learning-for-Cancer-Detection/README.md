# Deep Learning for Cancer Detection

## 1. Introduction

![Video](readme/1%20-%20Introduction.mp4)

## 2. Skin Cancer

![Video](readme/2%20-%2002%20Skin%20Cancer%20V4.mp4)

## 3. Survival Probability of Skin Cancer

![Video](readme/3%20-%20Survival%20Rate.mp4)

## 4. Medical Classification

![Video](readme/4%20-%20Medical%20Classification.mp4)

## 5. The Data

![Video](readme/5%20-%20The%20Data.mp4)

## 6. Image Challenges

![Video](readme/6%20-%2006%20Image%20Challenge%20V3.mp4)

### Challenge

Looking at the following images, could you tell the characteristics that determine if a lesion is benign (above) or 
malignant (below)?

![part6-1](readme/part6-1.png)

## 9. Training the Neural Network

![Video](readme/9%20-%20Training%20The%20Neural%20Network.mp4)

## 12. Validating the Training

![Video](readme/12%20-%20Validating%20The%20Training.mp4)

## 15. More on Sensitivity and Specificity

Although similar, sensitivity and specificity are not the same as precision and recall. Here are the definitions:

In the cancer example, sensitivity and specificity are the following:

 * Sensitivity: Of all the people **with** cancer, how many were correctly diagnosed?
 * Specificity: Of all the people **without** cancer, how many were correctly diagnosed?

And precision and recall are the following:

 * Recall: Of all the people who **have cancer**, how many did **we diagnose** as having cancer?
 * Precision: Of all the people **we diagnosed** with cancer, how many actually **partpart**?
 
From here we can see that Sensitivity is Recall, and the other two are not the same thing.

Trust me, we also have a hard time remembering which one is which, so here's a little trick. If you remember from 
Luis's Evaluation Metrics section, here is the [confusion matrix](https://classroom.udacity.com/nanodegrees/nd101/parts/73a7fe8e-4354-4362-939d-a8bf2bae870d/modules/e6a4e4a1-98a9-4afe-a744-7ae6a59c01b8/lessons/9ac722df-8191-44df-b7f5-ef1732b2d053/concepts/2034dd12-8ffc-4753-b8f4-c6042487ea5d):

![part15-1](readme/part15-1.png)

Now, sensitivity and specificity are the rows of this matrix. More specifically, if we label

 * TP: (True Positives) Sick people that we correctly diagnosed as sick.
 * TN: (True Negatives) Healthy people that we correctly diagnosed as healthy.
 * FP: (False Positives) Healthy people that we incorrectly diagnosed as sick.
 * FN: (False Negatives) Sick people that we incorrectly diagnosed as healthy.

then:

![part15-c1](readme/part15-c1.png)

and

![part15-c2](readme/part15-c2.png)

![part15-2](readme/part15-2.png)

And precision and recall are the top row and the left column of the matrix:

![part15-c3](readme/part15-c3.png)

and

![part15-c4](readme/part15-c4.png)

![part15-3](readme/part15-3.png)

## 17.Solution: Diagnosing Cancer

![Video](readme/17%20-%20Images.mp4)

The graph below is a histogram of the predictions our model gives in a set of images of lesions, as follows:

 * Each point in the horizontal axis is a value pp from 0 to 1.
 * Over each value pp, we locate all the lesions that our classifier predicted to have probability p of being malignant.

![part17-1](readme/part17-1.png)

Here we have graphed the thresholds at 0.2, 0.5, and 0.8. Notice how:

 * At 0.2, we classify every malignant lesion correctly, yet we also send a lot of benign lesions for more testing.
 * At 0.5, we miss some malignant lesions (bad), and we send a few benign lesions for more testing.
 * At 0.8, we correctly classify most of the benign lesions, but we miss many malignant lesions (very bad).

So in this case, it's arguable that 0.2 is better.

However, for this model, there may even be a better value for the threshold. What would it be?

## 18. Refresh on ROC Curves
