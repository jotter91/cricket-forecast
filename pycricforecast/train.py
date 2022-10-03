import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os 
import pickle 

# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

def plot_loss(history,out_dir):
    """ plot loss and val_loss as function of epoch
    Parameters
    -----------
    history, History class
        histroy class from a tensorflow fit
    out_dir, str
        a string for the output dir to save png 
    Returns
    ---------
    fig, matplotlib fig object
    ax , matplotlib axes object
    """

    fig,ax = plt.subplots()
  
    ax.plot(history.history['loss'], label='loss')
    ax.plot(history.history['val_loss'], label='val_loss')
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Error [runs]')
    plt.legend()
    ax.grid(True)

    plt.savefig(os.path.join(out_dir,'loss.png')) 
    
    return fig,ax

def plot_predictions(test_labels,test_predictions):    
    plt.figure()
    a = plt.axes(aspect='equal')
    plt.scatter(test_labels, test_predictions)
    plt.xlabel('True Values [runs]')
    plt.ylabel('Predictions [runs]')
    plt.savefig('predictions.png')
def plot_error(error) :   
    plt.figure()
    plt.hist(error, bins=25)
    plt.xlabel('Prediction Error [runs]')
    _ = plt.ylabel('Count')
    plt.savefig('error.png') 
def build_and_compile_model(norm):
  model = keras.Sequential([
      norm,
      layers.Dense(64, activation='relu'),
      layers.Dense(64, activation='relu'),
      layers.Dense(1)
  ])

  model.compile(loss='mean_absolute_error',
                optimizer=tf.keras.optimizers.Adam(0.001))
  return model  


def split_into_train_and_test(data_set,train_fac=0.8):
    
    data = pd.DataFrame(data_set)
    
    train_dataset = data.sample(frac=train_fac, random_state=1)
    test_dataset = data.drop(train_dataset.index)
    return train_dataset,test_dataset        

def train_DNN(data_set,objective_func,output_name):
    """ Train a DNN model 
    
    Parameters
    -----------

    Returns
    -----------

    """
    train_dataset,test_dataset =  split_into_train_and_test(data_set,train_fac=0.8)   
        
       
                
    train_features = train_dataset.copy()
    test_features = test_dataset.copy()

    train_labels = train_features.pop(objective_func)
    test_labels = test_features.pop(objective_func)

        
    normalizer = tf.keras.layers.Normalization(axis=-1)
    normalizer.adapt(np.array(train_features))

    
    dnn_model = build_and_compile_model(normalizer)
    dnn_model.summary()
    
    history = dnn_model.fit(
    train_features,
    train_labels,
    validation_split=0.2,
    verbose=0, epochs=500)
    
    plot_loss(history,'')
    test_results={}
    test_results[output_name] = dnn_model.evaluate(test_features, test_labels, verbose=0)
    
    dnn_model.save(output_name)
    test_predictions = dnn_model.predict(test_features).flatten()
    plot_predictions(test_labels,test_predictions)
   
    error = test_predictions - test_labels
    summary = (dnn_model.evaluate(test_features,test_labels,verbose=0))
    plot_error(error)

if __name__=="__main__":
    from  pycricforecast import tools
    for_fit = tools.collate_from_dir(r'C:\JohnData\software\misc\t20s_json')
    train_DNN(for_fit,'final_score','testing')
