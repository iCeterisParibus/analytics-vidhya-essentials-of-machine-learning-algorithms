# Python code for Naive Bayes provided by Analytics Vidhya

print '-' * 85
print """
Naive Bayes'

It is a classification technique based on Bayes' theorem with an assumption of
independence between predictors. In simple terms, a Naive Bayes classifier
assumes that the presence of a particular feature in a class is unrelated to the
presence of any other feature. For example, a fruit may be considered to be an
apple if it is red, round, and about 3 inches in diameter. Even if these
features depend on each other or upon the existence of the other features, a
naive Bayes classifier would consider all of these properties to independently
contribute to the probability that this fruit is an apple.

Naive Bayesian model is easy to build and particularly useful for very large
data sets. Along with simplicity, Naive Bayes is known to outperform even highly
sophisticated classification methods.

Bayes theorem provides a way of calculating posterior probability P(c|x) from
P(c), P(x) and P(x|c). Look at the equation below:

P(c|x) = (P(x|c)P(c)) / P(x)

Here,

+ P(c|x) is the posterior probability of class (target)
    given predictor (attribute).
+ P(c) is the prior probability of class.
+ P(x|c) is the likelihood which is the probability of predictor given class.
+ P(x) is the prior probability of predictor.

Example: Let's understand it using an example. Below I have a training data set
of weather and corresponding target variable 'Play'. Now, we need to classify
whether players will play or not based on weather condition. Let's follow the
below steps to perform it.

Step 1: Convert the data set to frequency table

Step 2: Create Likelihood table by finding the probabilities like Overcast
probability = 0.29 and probability of playing is 0.64.

Step 3: Now, use Naive Bayesian equation to calculate the posterior probability
for each class. The class with the highest posterior probability is the outcome
of prediction.

Problem: Players will pay if weather is sunny, is this statement is correct?

We can solve it using above discussed method, so
P(Yes | Sunny) = P( Sunny | Yes) * P(Yes) / P (Sunny)

Here we have P (Sunny |Yes) = 3/9 = 0.33, P(Sunny) = 5/14 = 0.36,
P( Yes)= 9/14 = 0.64

Now, P (Yes | Sunny) = 0.33 * 0.64 / 0.36 = 0.60, which has higher probability.

Naive Bayes uses a similar method to predict the probability of different class
based on various attributes. This algorithm is mostly used in text classification
and with problems having multiple classes.
"""

print '-' * 85
print """
Code provided by Analytics Vidhya article:

    #Import Library
    from sklearn.naive_bayes import GaussianNB

    #Assumed you have, X (predictor) and Y (target) for training data set and
    # x_test(predictor) of test_dataset

    # Create SVM classification object model = GaussianNB()
        # there is other distribution for multinomial classes like Bernoulli
        # Naive Bayes

    # Train the model using the training sets and check score
    model.fit(X, y)

    #Predict Output
    predicted= model.predict(x_test)
"""
print '-' * 85
