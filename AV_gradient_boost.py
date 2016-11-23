# Python code for Gradient Boosting & AdaBoost provided by Analytics Vidhya

print '-' * 85
print """
Gradient Boosting & AdaBoost

GBM & AdaBoost are boosting algorithms used when we deal with plenty of data to
make a prediction with high prediction power. Boosting is an ensemble learning
algorithm which combines the prediction of several base estimators in order to
improve robustness over a single estimator. It combines multiple weak or average
predictors to a build strong predictor. These boosting algorithms always work
well in data science competitions like Kaggle, AV Hackathon, CrowdAnalytix.
"""

print '-' * 85
print """
Code provided by Analytics Vidhya article:

    #Import Library
    from sklearn.ensemble import GradientBoostingClassifier

    #Assumed you have, X (predictor) and Y (target) for training data set and
    # x_test(predictor) of test_dataset

    # Create Gradient Boosting Classifier object
    model= GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,
                                      max_depth=1, random_state=0)

    # Train the model using the training sets and check score
    model.fit(X, y)

    #Predict Output
    predicted= model.predict(x_test)
"""
print '-' * 85
