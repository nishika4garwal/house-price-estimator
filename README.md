This is a real estate price prediction website. Firstly, I build a model using sklearn and linear regression using banglore home prices dataset from kaggle.com. It comprised of 
Data loading and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, gridsearchcv for hyperparameter tunning, k fold cross validation etc. 
Then I wrote a python flask server that uses the saved model to serve http requests. Next is the website built in html, css and javascript that allows user to enter 
home square ft area, bedrooms, bathrooms and location and it will call python flask server to retrieve the predicted price. Technology and tools used in this project are:

Numpy and Pandas for data cleaning
Matplotlib for data visualization
Sklearn for model building
visual studio code and pycharm as IDE
Python flask for http server
HTML/CSS/Javascript for UI
