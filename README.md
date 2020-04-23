# AB-testing-and-Machine-Learning

This project is based on a series of articles I ve been reading and courses I ve been taking about testing. But I based specially on the article written by Matt Dancho of Business Science - A/B Testing with Machine Learning - A Step-by-Step (https://www.business-science.io/). I will try to develop the same exercise on Python and also provide more depth about A/B testing and why machine learning shouldn’t replace A/B testing, it should complement it.
We are going to use the example published by Udacity, which are online experiments used to test potential improvements to a website or mobile app.

Main topics

•	The idea is to provide an initial understanding about A/B testing and their main benefits

•	Understand how Machine Learning approach can complement A/B Testing 


### A/B testing
A/B Testing is a method of comparing two versions of a product / feature against each other to determine which one performs better. AB testing is essentially an experiment where two or more variants are shown to users at random, and statistical analysis is used to determine which variation performs better for a given outcome.
1)	Treatment Group (Group A) - This group is exposed to the new web page, popup form, etc.
2)	Control Group (Group B) - This group experiences no change from the current setup.

The goal of the A/B is then to compare the outcomes of the two groups using statistical inference to determine if there is a significant change. 

Testing enables data-informed decisions that shift business conversations from “we think” to “we know.” By measuring the impact that changes have on your metrics, you can ensure that every change produces positive results and try to figure causal relations between variables.

NOTE: To learn more about A/B testing, the process, how to design an experiment and to evaluate results, I recommend taking Udacity A/B testing course (https://www.udacity.com/course/ab-testing--ud257) and to read this article where is explained the Udacity’s AB testing example  https://www.kaggle.com/tammyrotem/ab-tests-with-python/notebook.


### A/B testing using Machine Learning

Let's first see the conclusions of the A/B test example done for Udacity.
Once performed the A/B test you would have figured that the feature A is not significantly better than B, and that’s all. But what can happen is that the test that you had done based on your hypothesis, is not the first driver behind your outcome. Here is where Machine Learning is important. 
Most machine learning algorithms have a method for calculating their feature importance — that is, how big a role did each feature play in predicting the target/dependent feature. This is very important because we can know exactly which features are contributing enrollments and determine if there is an impact on enrollments from the new “Setting Expectations” form.

## Applying Machine Learning
