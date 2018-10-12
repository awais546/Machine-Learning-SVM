import pandas as pd
import pdb
from sklearn import svm
import numpy as np
import os


class TestClassName:
    def __init__(self):
        print('')


    def start_process(self):
        
        return "Data Science Testing\n[Mammals:1, Bird:2, Reptile:3, Fish:4, Amphibian:5, Bug:6, Invertebrate:7]"


def read_csv(): #read the class.xlsx file for knowing the actual class of animals
    info_df = pd.read_csv(os.getcwd()+'\\class.csv')

    type_dict = info_df.set_index('Class_Type')['Animal_Names'].to_dict()
    #reading the file from which testing and training data is obtained
    data_set_df = pd.read_csv(os.getcwd()+'\\zoo.csv')#dataframe of machine learning data
    data_set_df['Type'] = str(0) #entering a new column to enter the string values of classes
    # data_set_df['Type Number'] =  str(0)
    for index, row in data_set_df.iterrows():#iterating each row to enter the type of each class
        for each in type_dict:
            if row['animal_name'] in type_dict[each]:
                data_set_df._set_value(index, 'Type', each)

    writer = pd.ExcelWriter(os.getcwd() + '\\zoo_testing.xlsx')
    data_set_df.to_excel(writer, 'Sheet1', index=False)
    writer.save() #saving a reference file to see in future

    features_train = data_set_df.sample(frac=0.8)#shuffling the data to 80 20 ratio and creating train dataframe
    features_test = data_set_df.drop(features_train.index) #test dataframe
    features_train_label = features_train['class_type'] #train labels
    features_test_label = features_test['class_type'] #test label
    features_train = features_train.drop(['animal_name', 'Type', 'class_type'], axis=1) #removing the columns which are not needed
    features_test = features_test.drop(['animal_name', 'Type', 'class_type'], axis=1)


    return features_train,features_train_label,features_test,features_test_label


def machine_learning(features_train,features_train_label,features_test,features_test_label):

    clf = svm.SVC(gamma='scale') #initializing classifier

    clf.fit(features_train, features_train_label)

    result = clf.predict(features_test).astype(int) #result of prediction
    try:
        real_label = features_test_label.values

    except:
        real_label = features_test_label.astype(int)
    correct = result == real_label
    accuracy = correct.sum() / correct.size

    return accuracy,result

def main_start(Feathers,Eggs,Milk,Airborne,Aquatic,Predator,Toothed,Backbone,Venomous,Legs,Tail,Check_Label):

    features_train, features_train_label, features_test, features_test_label = read_csv()
    accuracy,label_test = machine_learning(features_train, features_train_label, features_test, features_test_label)
    #if (int(Feathers) == 1 or int(Feathers) == 0) and (int(Eggs) == 1 or int(Eggs) == 0) and (int(Milk) == 1 or int(Milk) == 0) and (int(Airborne) == 1 or int(Airborne) == 0) and (int(Aquatic) == 1 or int(Aquatic) == 0) and (int(Predator) == 1 or int(Predator) == 0) and (int(Toothed) == 1 or int(Toothed) == 0) and (int(Backbone) == 1 or int(Backbone) == 0) and (int(Venomous) == 1 or int(Venomous) == 0) and (int(Legs) == 1 or int(Legs) == 0) and (int(Tail) == 1 or int(Tail) == 0) and int(Check_Label) in [1,2,3,4,5,6,7]:
    try:
        check_test = [[int(Feathers),int(Eggs),int(Milk),int(Airborne),int(Aquatic),int(Predator),int(Toothed),int(Backbone),int(Venomous),int(Legs),int(Tail)]] #data coming from form
        check_test = np.asarray(check_test)#converting the testing data to numpy array
        Check_Label = np.asarray([Check_Label]) #converting the testing label to numpy array
        check_accuracy,check_label = machine_learning(features_train,features_train_label,check_test,Check_Label)
    #else:
    except: #if data is not entered correctly then this error will be shown
        check_accuracy = 'Please Enter all the values'
        check_label = 'Please Enter correct value'
    return str(Feathers) +" "+str(Eggs) +" "+str(Milk) +" "+str(Airborne) +" "+str(Aquatic) +" "+str(Predator) +" "+str(Toothed) +" "+str(Backbone) +" "+str(Venomous) +" "+str(Legs) +" "+str(Tail),accuracy,check_accuracy,str(check_label)