

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
