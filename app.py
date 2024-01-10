from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load your trained model
with open('phishing.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ''
    probability = ''
    if request.method == 'POST':
        url = request.form['url']
        # Get the prediction class and probability
        prediction_class = model.predict([url])[0]
        prediction_probability = model.predict_proba([url])
        
        # Assuming 'bad' is the first class and 'good' is the second class
        if prediction_class == 'bad':
            probability = prediction_probability[0][0] * 100  # Probability of being 'bad'
        else:
            probability = prediction_probability[0][1] * 100  # Probability of being 'good'

        prediction = f'{prediction_class} (Probability: {probability:.2f}%)'

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
