import pickle
from flask import Flask, request, jsonify
#from model_files.ml_model import predict_mpg


app = Flask('mpg_prediction')

@app.route('/test', methods=['GET'])
def test():
    return 'Pinging Model Application!!'

if __name__ == ‘__main__’:
    app.run(debug=True, host=’0.0.0.0', port=9696)