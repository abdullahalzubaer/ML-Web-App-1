# A machine learning web app for salary prediction using random forest regressor.

---


## 1 To run in a docker container:

List of required file to create the image:
```
Dockerfile
main.py
saved_steps.pkl
environment.yml
```
### Building the image locally


Step 1: Download the docker file and build an image using the following command 

```
docker build -t salary .
```

Step 2: Once the image has been build, use the docker-compose.yml file for executing the application Read more about docker compose file [here](https://docs.docker.com/compose/) - in short its a composition of all necessary things ("Define the services that make up your app in `docker-compose.yml` so they can be run together in an isolated environment.")required to run the application

 ```
 docker-compose up
 ```
 
Step 2 (alternative): Or we can just run this command (it is equivalent to what is written inside the docker-compose.yml file)
 
```
docker run --name=salary_new_container --rm -p 8501:8501 salary
```
```
--name=salary_new_container -> This is the name of the container that you see when you do "docker-container ls", we can leave it empty then just docker will give some strange names. 

--rm ->automatically cleans up the container and removes the file system when the container exits  [Reference](https://github.com/abdullahalzubaer/knote-js/blob/master/01_writing_a_note_taking_app.md)

-p 8501:8501 ->  publishes port 8501 of the container to port 8501 of our local machine. That means, if we now access port 3000 on our computer, the request is forwarded to port 3000 of the salary container. We can use the forwarding to access the app from your local machine. [Reference](https://github.com/abdullahalzubaer/knote-js/blob/master/01_writing_a_note_taking_app.md)
```
And then go to 

```
http://localhost:8501/
```
for the running app :)

### Pulling the image from Docker hub



## 2 To run locally

Tested on Python 3.7.4

--- 

In this project I will build an Machine Learning app utilize the "The Public 2020 Stack Overflow Developer Survey Results" for predicting the salary of a developer based on chosen attributes.

A short overview:

Step 1: Preprocessing of the dataset and make it suitable for training the ML model.

Step 2: Adopt Random Forest Regressor as the ML algorithm and select the hyper-parameter using Grid Search CV.

Step 3: Create and launch locally the web application using Streamlit.


To run the web app :

Please create an conda environment first using the environment.yml file 

NOTE: Latest sklearn will not be working with the code I have provided (the saved model was done using old sklearn library) that is why this conda env file I have created.

```
conda env create -f environment.yml
```

Then execute the following line from terminal (inside the same conda Environment) where the project is saved (the trained model is also present in this repository) and execute the following command:

```
streamlit run main.py
```

--- 

Dataset:

The Public 2020 Stack Overflow Developer Survey Results

https://insights.stackoverflow.com/survey

---


Reference: https://www.youtube.com/watch?v=xl0N7tHiwlw
