# Python code for Random Forests provided by Analytics Vidhya

print '-' * 85
print """
Random Forests

Random Forest is a trademark term for an ensemble of decision trees. In Random
Forest, we've collection of decision trees (so known as \"Forest\"). To classify a
new object based on attributes, each tree gives a classification and we say the
tree \"votes\" for that class. The forest chooses the classification having the
most votes (over all the trees in the forest).

Each tree is planted & grown as follows:

1. If the number of cases in the training set is N, then sample of N cases is
taken at random but with replacement. This sample will be the training set for
growing the tree.
2. If there are M input variables, a number m<<M is specified such that at each
node, m variables are selected at random out of the M and the best split on
these m is used to split the node. The value of m is held constant during the
forest growing.
3. Each tree is grown to the largest extent possible. There is no pruning.

For more details on this algorithm, comparing with decision tree and tuning
model parameters, I would suggest you to read these articles:

+ https://www.analyticsvidhya.com/blog/2014/06/introduction-random-forest-simplified/
+ https://www.analyticsvidhya.com/blog/2014/06/comparing-cart-random-forest-1/
+ https://www.analyticsvidhya.com/blog/2014/06/comparing-random-forest-simple-cart-model/
+ https://www.analyticsvidhya.com/blog/2015/06/tuning-random-forest-model/
"""

print '-' * 85
print """
Code provided by Analytics Vidhya article:

    #Import Library
    from sklearn.ensemble import RandomForestClassifier

    #Assumed you have, X (predictor) and Y (target) for training data set and
    # x_test(predictor) of test_dataset

    # Create Random Forest object
    model= RandomForestClassifier()

    # Train the model using the training sets and check score
    model.fit(X, y)

    #Predict Output
    predicted= model.predict(x_test)
"""
print '-' * 85
