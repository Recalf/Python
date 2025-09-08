from flask import Flask,jsonify,request
import joblib
import pandas as pd

# setp 1
app = Flask(__name__)

# load model and its col names.
model = joblib.load('final_model.pkl')
ml_col_names = joblib.load('column_names.pkl')

# step 2, connect api post to function. Now when we go to /predict in URL, it'll activate this fuction automatically.
@app.route('/predict',methods=['POST'])
def predict():

    #step 3, take the data that was posted by the user
    data = request.json
    df = pd.DataFrame(data)
    
    # make the col names of this df the same as the ML df we saved & loaded.
    df = df.reindex(columns=ml_col_names) # This reshapes df to have exactly ml_col_names, if old df col names are more == they'll get dropped, if less, the new df col name will be with NANs

    # predict df with the model we saved & loaded. (as list, for JSON safe)
    prediction = list(model.predict(df))

    return jsonify({"prediction":prediction}) # made it dict like that to be : JSON object with a named field (common in APIs). its just better
                                               # 2- jsonify cuz in APIs its 'better' to POST a json for status codes...
                                               # 3- also we did str(prediction) in the lecture, without str is just better


if __name__ == '__main__':
    app.run(debug=True)
    # the predict() function is activated when we enter /predict in our url.
