from flask import Flask, render_template, request, current_app
from pycricforecast.predictor.predict import rpb
from pycricforecast.predictor.first_inn_dnn import FirstInnDNN
app = Flask(__name__)

@app.route('/index.html')
def index():
    return current_app.send_static_file('index.html')
@app.route('/')    
def main():
    return current_app.send_static_file('index.html')
@app.route('/about.html')
def about():
    return current_app.send_static_file('about.html')
@app.route('/about_dnn.html')
def about_dnn():
    return current_app.send_static_file('about_dnn.html') 
    
@app.route('/dnn_model/')
def dnn_model():
    return render_template('dnn_model.html')    

@app.route('/send', methods=['POST'])
#TODO: replace sum 
def send(sum=sum):
    if request.method == 'POST':
        #TODO :check type for inputs
        try:
            runs  = int(request.form['runs'])
            balls = int(request.form['balls'])
            wickets = int(request.form['wickets'])
            model = request.form['model']
        except ValueError:
            return render_template('dnn_model.html')

        if model == 'rpb':
            prediction=rpb([])
            sum = int(prediction.predict_end_of_innings_score(runs,balls))
            return render_template('dnn_model.html', sum=sum)
        elif model == 'another':
            prediction=rpb([])
            sum = 1
            return render_template('dnn_model.html', sum=sum)
        elif model == 'dnn':
            #TODO: move this init outside of send?
            prediction=FirstInnDNN([])
            sum = prediction.predict_end_of_innings_score(runs,wickets,balls)
            return render_template('dnn_model.html', sum=sum)
        else:
            return render_template('dnn_model.html')

if __name__ == ' __main__':
    app.run(debug=True)
