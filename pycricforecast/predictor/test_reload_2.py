import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import seaborn as sns
#from read_json import Match
import os 
#import pickle 

# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers


reloaded = tf.keras.models.load_model('dnn_model')


print(reloaded.predict(np.asarray([100,4,70]).flatten()))