import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

# load dataset
dataframe = pandas.read_csv("Scraped-Data/df_pivoted.csv", header=0, usecols=lambda x: x not in ['sno', 'Source'])
dataset = dataframe.values
X = dataset[:,1:].astype(int)
Y = dataset[:,0]
#print(dataframe)

#outline of the model
def diag_model():
    model = Sequential()
    model.add(Dense(300, input_dim=403, activation='relu'))
    model.add(Dense(200, activation='relu'))
    model.add(Dense(149, activation='softmax'))
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    #print(model.summary())
    return model

#printing the model summary
m=diag_model()
print(m.summary())

estimator = KerasClassifier(build_fn=diag_model, epochs=30, batch_size=8, verbose=1)

kfold = KFold(n_splits=10, shuffle=True, random_state=seed)

results = cross_val_score(estimator, X, Y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
