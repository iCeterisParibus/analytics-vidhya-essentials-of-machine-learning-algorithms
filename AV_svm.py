# Python code for SVM (Support ector Machine) provided by Analytics Vidhya

print '-' * 85
print """
SVM (Support Vector Machine)

It is a classification method. In this algorithm, we plot each data item as a
point in n-dimensional space (where n is number of features you have) with the
value of each feature being the value of a particular coordinate.

For example, if we only had two features like Height and Hair length of an
individual, we'd first plot these two variables in two dimensional space where
each point has two co-ordinates (these co-ordinates are known as Support
Vectors)

Now, we will find some line that splits the data between the two differently
classified groups of data. This will be the line such that the distances from
the closest point in each of the two groups will be farthest away.

In the example shown above, the line which splits the data into two differently
classified groups is the black line, since the two closest points are the
farthest apart from the line. This line is our classifier. Then, depending on
where the testing data lands on either side of the line, that's what class we
can classify the new data as.
"""

print '-' * 85
print """
Code provided by Analytics Vidhya article:

    #Import Library
    from sklearn import svm

    #Assumed you have, X (predictor) and Y (target) for training data set and
    # x_test(predictor) of test_dataset

    # Create SVM classification object
    model = svm.svc() # there is various option associated with it, this is
        # simple for classification.

    # Train the model using the training sets and check score
    model.fit(X, y)
    model.score(X, y)
    #Predict Output
    predicted= model.predict(x_test)
"""
print '-' * 85
