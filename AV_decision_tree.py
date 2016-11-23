# Python code for decision trees provided by Analytics Vidhya

print '-' * 85
print """
Decision Trees

Decision Trees are a type of supervised learning algorithm that is mostly used
for classification problems. Surprisingly, it works for both categorical and
continuous dependent variables. In this algorithm, we split the population into
two or more homogeneous sets. This is done based on most significant
attributes/independent variables to make as distinct groups as possible.
"""

print '-' * 85
print """
Code provided by Analytics Vidhya article:

    #Import Library

    #Import other necessary libraries like pandas, numpy...
    from sklearn import tree

    #Assumed you have, X (predictor) and Y (target) for training data set and
    # x_test(predictor) of test_dataset

    # Create tree object
    model = tree.DecisionTreeClassifier(criterion='gini')
        # for classification, here you can change the algorithm as gini or
        # entropy (information gain) by default it is gini

    # model = tree.DecisionTreeRegressor() for regression

    # Train the model using the training sets and check score
    model.fit(X, y)
    model.score(X, y)

    #Predict Output
    predicted= model.predict(x_test)
"""
print '-' * 85
