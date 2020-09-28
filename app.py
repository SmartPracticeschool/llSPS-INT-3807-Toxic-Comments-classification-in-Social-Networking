import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow import keras
app = Flask(__name__)
model = keras.models.load_model('newmodel.h5')
tks = load('newtokens.save')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/index1.html')
def index():
    return render_template('index1.html')

@app.route('/index1.html/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    comment = [[x for x in request.form.values()]]
    print(comment)
    comment_seq = tks.texts_to_sequences(comment[0])
    req = pad_sequences(comment_seq, maxlen=200)
    p = model.predict(req)
    new_p = [i*100 for i in p]
    new_p = list(new_p[0])
    print(new_p)
    output=new_p
    
    #return render_template('index.html', prediction_text='Toxic : {}\nSevere toxic : {}\nObscene : {}\nThreat : {}\nInsult : {}\nIndentity hate : {}'.format("{:.2f}%".format(output[0]), "{:.2f}%".format(output[1]), "{:.2f}%".format(output[2]), "{:.2f}%".format(output[3]), "{:.2f}%".format(output[4]), "{:.2f}%".format(output[5])))
    return render_template('index1.html', pred_text1 = 'Toxic : {}'.format("{:.2f}%".format(output[0])),
                           pred_text2 = 'Severe toxic : {}'.format("{:.2f}%".format(output[1])),
                           pred_text3 = 'Obscene : {}'.format("{:.2f}%".format(output[2])),
                           pred_text4 = 'Threat : {}'.format("{:.2f}%".format(output[3])),
                           pred_text5 = 'Insult: {}'.format("{:.2f}%".format(output[4])),
                           pred_text6 = 'Identity hate : {}'.format("{:.2f}%".format(output[5])))

'''@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    #For direct API calls trought request
    
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)'''

if __name__ == "__main__":
    app.run(debug=True)
