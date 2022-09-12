import pycricforecast.predictor.predict as cric_predict 
from pycricforecast.predictor.predict import Predict
import numpy as np
import os 
#import pickle 

# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

class FirstInnDNN(Predict):
    
    def __init__(self,inputs):
        Predict.__init__(self,inputs)
        
        path = os.path.dirname(cric_predict.__file__)
        
        self.dnn_model = tf.keras.models.load_model(os.path.join(path,'dnn_model'))
    
    def predict_end_of_innings_score(self,n_runs,n_wickets,n_balls):
        data = np.asarray([n_runs,n_wickets,n_balls]) 
        output = self.dnn_model.predict(data).flatten()
        return int(output[0]) 
