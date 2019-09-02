import numpy as np
import connexion
import pickle

# Load the trained model
model = pickle.load(open('model/model.pkl','rb'))

def salary_prediction(data):
	predictions = []
	for item in data:
		value = item["Experience"]
		prediction = model.predict([[np.array(value)]])[0]
		predictions.append({"Salary":prediction,"Experience":value})
	return predictions
	
app = connexion.App(__name__)
app.add_api('swagger.yaml')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
