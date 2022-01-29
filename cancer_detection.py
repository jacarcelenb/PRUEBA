
from sklearn import preprocessing
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import r2_score


def predict_cancer(neuronas , epocas , optimizador):
    admissions = pd.read_excel('Datos_Cancer.xlsx')
    datos = admissions.values
    datos_robust_scaler = preprocessing.RobustScaler().fit_transform(datos)
    datos_robust_scaler
    entrada = datos_robust_scaler[:, 1:31]
    salida = datos_robust_scaler[:, 0]
    training_data = np.array(entrada, "float32")
    target_data = np.array(salida, "float32")

    model = Sequential()
    model.add(Dense(int(neuronas), activation='relu', input_dim=30))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy',
                  optimizer=optimizador,
                  metrics=['accuracy'])
    model.fit(training_data, target_data, epochs=int(epocas))
    scores = model.evaluate(training_data, target_data)
    print("\%s: %.4f" % (model.metrics_names[0], scores[0]))  # loss
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))  # accuracy
    # full metrics
    y_pred = model.predict(training_data).round()
    y_true = target_data
    cm = confusion_matrix(y_true, y_pred)
    acc = round( accuracy_score(y_true, y_pred),2)
    rec = round(recall_score(y_true, y_pred), 2)
    prec = round(precision_score(y_true, y_pred),2)
    f1 = round(f1_score(y_true, y_pred),2)
    auc = roc_auc_score(y_true, y_pred)
    r2 = round(r2_score(y_true, y_pred),2)

    return acc , rec , prec , f1 , r2
    
def calcular_exactitud(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    return acc
   
