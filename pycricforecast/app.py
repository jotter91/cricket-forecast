from flask import Flask, render_template, request
from pycricforecast.predictor.predict import rpb
from pycricforecast.predictor.first_inn_dnn import FirstInnDNN
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')

@app.route('/send', methods=['POST'])
#TODO: replace sum 
def send(sum=sum):
    if request.method == 'POST':
        #TODO :check type for inputs
        runs  = int(request.form['runs'])
        balls = int(request.form['balls'])
        wickets = int(request.form['wickets'])
        model = request.form['model']

        if model == 'rpb':
            prediction=rpb([])
            sum = int(prediction.predict_end_of_innings_score(runs,balls))
            return render_template('app.html', sum=sum)
        elif model == 'another':
            prediction=rpb([])
            sum = 1
            return render_template('app.html', sum=sum)
        elif model == 'dnn':
            #TODO: move this init outside of send?
            prediction=FirstInnDNN([])
            sum = prediction.predict_end_of_innings_score(runs,wickets,balls)
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html')

if __name__ == ' __main__':
    app.run(debug=True)
