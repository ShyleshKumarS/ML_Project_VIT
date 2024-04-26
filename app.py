from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder




app = Flask(__name__)

# Load the pre-trained model
with open('Card.pkl', 'rb') as f:
    model = pickle.load(f)

credit_data = pd.read_excel('credit_rating.xls')

df_encoded = credit_data.copy()


label_encoder = LabelEncoder()

for column in df_encoded.columns:
    if df_encoded[column].dtype == 'object':
        df_encoded[column] = label_encoder.fit_transform(df_encoded[column])


label_encoders = {
    'CHK_ACCT': LabelEncoder(),
    'Purpose of credit': LabelEncoder(),
    'Balance in Savings A/C': LabelEncoder(),
    'Marital status': LabelEncoder()
}


for feature, encoder in label_encoders.items():
    encoder.fit(credit_data[feature])



@app.route('/')
def index():
    
    return render_template('index.html')



# Your Flask application code
@app.route('/form')
def form():
    # Get the URL parameters passed from index.html
    purpose_options = sorted(credit_data['Purpose of credit'].unique())
    CHK_ACCT_options = sorted(credit_data['CHK_ACCT'].unique())
    Balance_acc_options = sorted(credit_data['Balance in Savings A/C'].unique())
    martial_op = sorted(credit_data['Marital status'].unique())
    
    # Render form.html and pass the URL parameters
    return render_template('form.html', purpose_options=purpose_options, CHK_ACCT_options=CHK_ACCT_options, Balance_acc_options=Balance_acc_options, martial_op=martial_op)



@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the form data
        duration = float(request.form['duration'])
        creditAmount = float(request.form['creditAmount'])
        age = float(request.form['age'])
        purpose = request.form['purpose']
        CHK_ACCT = request.form['CHK_ACCT']
        Balance_acc = request.form['Balance_acc']
        martial = request.form['martial']
        
        # Transform categorical features
        CHK_ACCT_encoded = label_encoders['CHK_ACCT'].transform([CHK_ACCT])[0]
        purpose_encoded = label_encoders['Purpose of credit'].transform([purpose])[0]
        Balance_acc_encoded = label_encoders['Balance in Savings A/C'].transform([Balance_acc])[0]
        martial_encoded = label_encoders['Marital status'].transform([martial])[0]
        
        input_data = [[CHK_ACCT_encoded, duration, purpose_encoded, creditAmount, 
                       Balance_acc_encoded, martial_encoded, age]]
        
        
    
        prediction = model.predict(input_data)[0]
        
        label = "good" if prediction == 1 else "bad"
        
        return jsonify({'prediction': label})
    
    except ValueError:
        return jsonify({'error': 'Invalid form data'})

if __name__ == '__main__':
    app.run(debug=True)
