# Python code for Dimensionality Reduction Algorithms provided by Analytics Vidhya

print '-' * 85
print """
Dimensionality Reduction Algorithms

In the last 4-5 years, there has been an exponential increase in data capturing
at every possible stages. Corporates/ Government Agencies/ Research organisations
are not only coming with new sources but also they are capturing data in great
detail.

For example: E-commerce companies are capturing more details about customer like
their demographics, web crawling history, what they like or dislike, purchase
history, feedback and many others to give them personalized attention more than
your nearest grocery shopkeeper.

As a data scientist, the data we are offered also consist of many features, this
sounds good for building good robust model but there is a challenge. How'd you
identify highly significant variable(s) out 1000 or 2000? In such cases,
dimensionality reduction algorithm helps us along with various other algorithms
like Decision Tree, Random Forest, PCA, Factor Analysis, Identify based on
correlation matrix, missing value ratio and others.
"""

print '-' * 85
print """
Code provided by Anlytics Vidhya article:

    #Import Library
    from sklearn import decomposition

    #Assumed you have training and test data set as train and test

    # Create PCA obeject pca= decomposition.PCA(n_components=k)
        #default value of k = min(n_sample, n_features)

    # For Factor analysis

    #fa = decomposition.FactorAnalysis()

    # Reduced the dimension of training dataset using PCA
    train_reduced = pca.fit_transform(train)

    #Reduced the dimension of test dataset
    test_reduced = pca.transform(test)
"""
print '-' * 85
