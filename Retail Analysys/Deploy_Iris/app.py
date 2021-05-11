import numpy as np
from flask import Flask,request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	int_features = [float(x) for x in request.form.values()]
	print(int_features)
	final_features = [np.array(int_features)]
	print(type(final_features))
	prediction = model.predict(final_features)
	print(type(prediction))
	print(prediction.shape)
	if prediction.item(0) == 0:
		pred_final = "Iris-setosa"
	elif prediction.item(0) == 1:
		pred_final = "Iris-versicolor"
	else:
		pred_final = "Iris-virginica"
	return render_template('index.html', prediction_text=pred_final)

if __name__ == "__main__":
    app.run(debug=True)