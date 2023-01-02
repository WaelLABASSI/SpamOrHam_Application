# Deploy_ML_Model_into_cloud

In this project, we build a spam detector using machine learning and launch it as a serverless API into AWS virtual servers.\
We use basic machine learning methods to build the spam detector and the Flask python framework to create the API.\


1. Build a Logistic Regression model to detect spams in sms messages
    - SpamDetector.ipynb
    - Use Pickle to serialize and deserialize the trained model and the vectorizer function
      => spam_ham_model.pkl & vectorizer.pkl

2. Create a Flask application with a RESTful API - GET/POST Method
    - application.py  

3. Launch an AWS EC2 instance(Virtual Server) using AWS Elastic Beanstalk

4. Deploy Spam Detector API Flask application into AWS virtual servers
    - Prepare the deployment file: Archive version_1 into .zip file

5. Perform additional AWS Elastic Beanstalk actions: Application versioning, Server logs, Server performance monitoring & Terminate the server.

To connect to the application and create requests we use POSTMAN as API testor.

## Installation
git clone https://github.com/WaelLABASSI/Deploy_ML_Model_into_cloud.git

conda create -n py369 python=3.6.9\
conda activate py39\
cd Deploy_ML_Model_into_cloud\
pip install -r requirements_ML.txt

## Run in Notebook
SpamDetector.ipynb

## Datasets
spam_train.csv: data used to train the model
spam_test.csv: data used to test the model


## Credits
COURSERA Project Network: Deploy Machine Learning Model into AWS Cloud Servers
