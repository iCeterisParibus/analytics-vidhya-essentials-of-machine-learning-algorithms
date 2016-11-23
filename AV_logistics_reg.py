# Python code for logistics regression provided by Analytics Vidhya

print '-' * 85
print """
Logistics Regression

The log odds of the outcome is modeled as a linear combination of the predictor
variables.

odds = p/(1-p) = probability of event occurrence / probability of not event occurrence
ln(odds) = ln(p/(1-p))
logit(p) = ln(p/(1-p)) = b0+b1X1+b2X2+b3X3....+bkXk

Above, p is the probability of presence of the characteristic of interest. It
chooses parameters that maximize the likelihood of observing the sample values
rather than that minimize the sum of squared errors (like in ordinary regression).
"""
print '-' * 85

print """
Code provided by Analytics Vidhya article:

    #Import Library
    from sklearn.linear_model import LogisticRegression

    #Assumed you have, X (predictor) and Y (target) for training data set and
    # x_test(predictor) of test_dataset

    # Create logistic regression object
    model = LogisticRegression()

    # Train the model using the training sets and check score
    model.fit(X, y)
    model.score(X, y)

    #Equation coefficient and Intercept
    print('Coefficient: \\n', model.coef_)
    print('Intercept: \\n', model.intercept_)

    #Predict Output
    predicted= model.predict(x_test)
"""

print '-' * 85
print """
Furthermore..

There are many different steps that could be tried in order to improve the model:

+ including interaction terms
+ removing features
+ regularization techniques
+ using a non-linear model
"""
print '-' * 85
