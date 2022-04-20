# A machine learning web app for salary prediction using random forest regressor.

Tested on Python 3.7.4

--- 

In this project I will build an Machine Learning app utilize the "The Public 2020 Stack Overflow Developer Survey Results" for predicting the salary of a developer based on chosen attributes.

A short overview:

Step 1: Preprocessing of the dataset and make it suitable for training the ML model.

Step 2: Adopt Random Forest Regressor as the ML algorithm and select the hyper-parameter using Grid Search CV.

Step 3: Create and launch locally the web application using Streamlit.


# To run the web app 

Please create an conda environment first using the environment.yml file 

NOTE: Latest sklearn will not be working with the code I have provided (the saved model was done using old sklearn library) that is why this conda env file I have created.

```
conda env create -f environment.yml
```

Then execute the following line from terminal (inside the same conda Environment) where you have saved this project (the trained model is also present in this repository) and execute the following command:

```
streamlit run main.py
```

--- 

Dataset:

The Public 2020 Stack Overflow Developer Survey Results

https://insights.stackoverflow.com/survey

---


Reference: https://www.youtube.com/watch?v=xl0N7tHiwlw
