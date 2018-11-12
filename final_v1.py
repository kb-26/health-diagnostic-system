import numpy
import pandas
from keras.models import Sequential,load_model,model_from_json
from keras.layers import Dense,Dropout,Reshape
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import os

le = LabelEncoder()                                 #to convert labels to integers
enc = OneHotEncoder(sparse=False)                   #to convert integers to one-hot-vectors

def encodeXY(dataframe):
    dataset = dataframe.values
    X = dataset[:,:132].astype(int)
    Y = dataset[:,132]

    Y_encoded = le.fit_transform(Y).astype(int)
    Y_encoded = Y_encoded.reshape(len(Y_encoded), 1)

    Y_oneHot = enc.fit_transform(Y_encoded)

    return X,Y_oneHot


dataframe = pandas.read_csv("Manual-Data/Training.csv", header=0)
X_train,Y_train = encodeXY(dataframe)

dataframe = pandas.read_csv("Manual-Data/Testing.csv", header=0)
X_test,Y_test = encodeXY(dataframe)


x_predict = [0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x_predict = numpy.array([x_predict])
print(x_predict)
print(x_predict.shape)

# print("printing X_train\n",X_train[0])
# print(X_train[0].shape)
# print("encoded Y_train\n",Y_train[0])
# print(Y_train[0].shape)



#================== Making and saving the model ================================
# use only once to same the model onto the disk, rest of the time read the model from the disk to do the computations
#
#
# def diag_model():
#     model = Sequential()
#     model.add(Dense(3000, input_shape=(132,), activation='relu'))
#     model.add(Dropout(0.5))
#     model.add(Dense(1000, activation='relu'))
#     model.add(Dropout(0.5))
#     model.add(Dense(100, activation='relu'))
#     model.add(Dense(41, activation='softmax'))
#     model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#     return model
#
# m=diag_model()
#
# #printing the model summary
# print(m.summary())
#
# m.fit(X_train,Y_train,batch_size=128, epochs=5, verbose=1, shuffle=True)
#
# print("evaluating the model on test set")
# scores = m.evaluate(x=X_test, y=Y_test, batch_size=8, verbose=1)
# print("%s: %.2f%%" % (m.metrics_names[1], scores[1]*100))
#
# # serialize model to JSON
# model_json = m.to_json()
# with open("model.json", "w") as json_file:
#     json_file.write(model_json)
# # serialize weights to HDF5
# m.save_weights("model.h5")
# print("Saved model to disk")
#===============================================================================

#========================= Loadig the model ====================================
#loading the model from the disk, use this always if you have saved model.
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
m = model_from_json(loaded_model_json)
# load weights into new model
m.load_weights("model.h5")
print("Loaded model from disk")
#===============================================================================

def predict_diagnosis(x_predict):
    x_predict = numpy.array([x_predict])
    y_predict = m.predict_classes(x_predict)
    print("Predicted=%s" % (y_predict[0]), le.inverse_transform(y_predict[0]))
    return y_predict[0], le.inverse_transform(y_predict[0])
