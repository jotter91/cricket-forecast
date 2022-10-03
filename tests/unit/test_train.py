from pycricforecast import train
import os
import numpy as np 
def test_train_plot_loss(tmp_path):
    #create mock history class for plotting
    class temp_history:
        def __init__(self,loss,val_loss):
            self.history={}
            self.history['loss']=loss
            self.history['val_loss']=val_loss

    loss = [i for i in range(100)],
    val_loss = [i*0.5 for i in range(100)],
    history=temp_history(loss,val_loss)
    fig,ax = train.plot_loss(history,tmp_path)

    assert os.path.isfile(os.path.join(tmp_path,'loss.png'))
    x_plot, y_plot = ax.lines[0].get_xydata().T
    x_plot, y_plot = ax.lines[1].get_xydata().T
    #np.testing.assert_array_equal(y_plot, loss)
