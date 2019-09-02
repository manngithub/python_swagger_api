# Deployment of Machine Learning Model as a REST API with Swagger interface

This template provides a basic structure of components for deploying a machine learning model as a REST API. A regression model is trained on publicly available dataset https://raw.githubusercontent.com/vyashemang/flask-salary-predictor/master/Salary_Data.csv that is salary earned as per years of work experience. This model is serialized as pickle file and made available for future use. A web server is instantiated that accepts input data (years of experience) and provides prediction of salary using the trained model pickle file. Further, the deployment framework is extended to generate interactive documentation using Swagger. 

Keywords: Machine Learning, Python, Web API, Swagger

### Package Directory

- app/model.py: optional file to understand the data and associated regression model. 
- app/server.py: execution of this file (starting the web server) 
- app/swagger.yaml: swagger specifications that describe endpoint, parameters etc...
- model/model.pkl: serialized machine learning model that was saved after running app/model.py file
- requirements.txt: package requirements that can be be used to setup the environment

### Environment Setup

(Note that these steps are tested only on Mac Device)
1. Run this command on the terminal to check if conda is available
```sh
$ conda
```
If conda is not available, then follow this link https://docs.anaconda.com/anaconda/install/. 

2. Setup a new Conda Environment for your package:
```sh
$ conda create --name python_swagger python=3.4
```
3. Activate the environment:
```sh
$ conda activate python_swagger
```
4. Install the dependencies
```sh
$ conda install --yes --file requirements.txt
```
5. Execute the server script
```sh
$ python app/server.py
```
This will instantiate the web api and user can interactively input the json payload from swagger ui. In the web browser, type: http://localhost:5000/ui

6. User can input the data in the Parameters section and obtain the results in Response Body. Here is screen shot that shows swagger user interface with Parameter window to input the value in json format. 

![Swagger Input](Swagger_Input.png)

Next, results can be obtained at the same interface in Response Body section -

![Swagger Response](Swagger_Response.png)


7. It is not necessary to interact with swagger ui to use the model api. You can use postman as well as curl to interact with the model api. Postman: This is optional. curl using terminal can also do the job. Refer this https://www.getpostman.com/downloads/ to install postman. Once installed, start Postman and use the following url and body json payload 
- URL: http://localhost:5000/predictions
- Body: [{"Experience":1.8}] 

8. If not using Postman, then open a new window in terminal
```sh
$ curl --header "Content-Type: application/json" --request POST --data '[{"Experience":1.8}]' http://localhost:5000/predictions
```