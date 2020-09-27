

import pandas # manipulation of data 
import numpy # Scientific computation for array usage and conversion 
import matplotlib # data visualization used in python 
import train_set_split fro sklearn model selection 
# used to split array or matrices into train and test 
import linear_discriminant_analysis from sklearn_discriminant_analysis 
# To perform linear discriminant analysis 
df=read csv file 
X=df.iloc.[:,1:] 
Class =df [“class”] 
X_train , X_test ,y_train,y_test = train_test_split(dataset test_size=0.3)
 #Instantiate the method and fit transformation the algorithm LDA 
    LDA = LinearDiscrimantAnalysis 
    Data_projected = LDA.fit_transform(x_train,y_train) 
# using markers and colors for representation 
        markers=[‘H’,’+’,’D’,’d’,’|’,’_’] 
#("H":"hexagon2","+":"plus","D":"diamond","d":"thin_diamond","|":"vline", "_":"h line”)
         colors = [‘b’,’g’,’r’,’c’,’m’,’y’] 
#( b: blue , g: green ,r: red ,c: cyan ,m: magenta ,y: yellow) 
          fig = plot .figure() 
          for l,m,c in np.unique(trainset),markers,colours 
          scatter (train,test,marker,colour) 
# generates scatter plot for the limit mentioned to the given train set. 
# Inferring the results obtained so far using plot. 








import pandas as pd
import numpy as np
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
df = pd.read_csv ('C:/Users/HP/Desktop/data.csv', sep=',',names = ['Class' , 'I0', 'PA500', 'HFS', 'DA', 'Area', 'A/DA','Max IP','DR','P'])
X = df.iloc[:,1:]
Class = df['Class']
X_train, X_test, y_train, y_test = train_test_split(X,Class,test_size=0.3,random_state=0) 
LDA = LinearDiscriminantAnalysis()
data_projected = LDA.fit_transform(X_train,y_train)
LDA.fit(X_train,y_train)
markers = ['H','+','D','d','|','_']
colors = ['b','g','r','c','m','y']
fig = plt.figure(figsize=(10,10))
ax0 = fig.add_subplot(111)
for l,m,c in zip(np.unique(y_train),markers,colors):
    ax0.scatter(data_projected[:,0][y_train==l],data_projected[:,1][y_train==l],c=c,marker=m)
print('Accuracy of LDA classifier on test set: {:.2f}'.format(LDA.score(X_test, y_test)))


