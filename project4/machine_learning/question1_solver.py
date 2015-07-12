import math
import operator
import types
class Question1_Solver:
    def __init__(self):
        self.learn('train.data');
        return;

    # Add your code here.
    # Read training data and build your decision tree
    # Store the decision tree in this class
    # This function runs only once when initializing
    # Please read and only read train_data: 'train.data'

    #calculate max Information Gain and get the best feature
    def getMaxEntropy(self, data1, data2, count):
        H = 0
        total = 0
        count_d = 0
        count_r = 0
        prob_d = 0
        prob_r = 0
        count_attr1 = list(0 for i in range(count))
        count_attr2 = list(0 for i in range(count))
        count_attr3 = list(0 for i in range(count))
        count_sub_attr1 = list(0 for i in range(count))
        count_sub_attr2 = list(0 for i in range(count))
        count_sub_attr3 = list(0 for i in range(count))
        count_sub_attr4 = list(0 for i in range(count))
        count_sub_attr5 = list(0 for i in range(count))
        count_sub_attr6 = list(0 for i in range(count))
        for row in range(len(data2)):
            if data1[row] == "democrat":
                total = total+1
                count_d = count_d+1
            else:
                total = total+1
                count_r = count_r+1
            for i in range(count):
                if data2[row][i] == "y":
                    count_attr1[i] = count_attr1[i]+1
                    if data1[row] == "democrat":
                        count_sub_attr1[i] = count_sub_attr1[i]+1
                    else:
                        count_sub_attr2[i] = count_sub_attr2[i]+1
                elif data2[row][i] == "n":
                    count_attr2[i] = count_attr2[i]+1
                    if data1[row] == "democrat":
                        count_sub_attr3[i] = count_sub_attr3[i]+1
                    else:
                        count_sub_attr4[i] = count_sub_attr4[i]+1
                elif data2[row][i] == "?":
                    count_attr3[i] = count_attr3[i]+1
                    if data1[row] == "democrat":
                        count_sub_attr5[i] = count_sub_attr5[i]+1
                    else:
                        count_sub_attr6[i] = count_sub_attr6[i]+1
        prob_d =  1.0*count_d/total
        prob_r = 1.0*count_r/total
        if prob_d == 0.0 or prob_r == 0.0:
            H = 0.0
        else:
            H = H - prob_d*math.log(prob_d,2)-prob_r*math.log(prob_d,2)
        max_H = -1
        position = -1
        for i in range(len(count_attr1)):
            if count_attr1[i] == 0:
                prob1 = 0.0
            else:
                prob1 = 1.0*count_attr1[i]/total
            if count_attr2[i] == 0:
                prob2 = 0.0
            else:
                prob2 = 1.0*count_attr2[i]/total
            if count_attr3[i] == 0:
                prob3 = 0.0
            else:
                prob3 = 1.0*count_attr3[i]/total
            if count_sub_attr1[i] == 0:
                subprob1 = 0.0
            else:
                subprob1 = 1.0*count_sub_attr1[i]/count_attr1[i]
            if count_sub_attr2[i] == 0:
                subprob2 = 0.0
            else:
                subprob2 = 1.0*count_sub_attr2[i]/count_attr1[i]
            if count_sub_attr3[i] == 0:
                subprob3 = 0.0
            else:
                subprob3 = 1.0*count_sub_attr3[i]/count_attr2[i]
            if count_sub_attr4[i] == 0:
                subprob4 = 0.0
            else:
                subprob4 = 1.0*count_sub_attr4[i]/count_attr2[i]
            if count_sub_attr5[i] == 0:
                subprob5 = 0.0
            else:
                subprob5 = 1.0*count_sub_attr5[i]/count_attr3[i]
            if count_sub_attr6[i] == 0:
                subprob6 = 0.0
            else:
                subprob6 = 1.0*count_sub_attr6[i]/count_attr3[i]

            temp = 0.0
            if prob1 == 0.0:
                temp = temp+0
            else:
                if subprob1 == 0.0 or subprob2 == 0.0:
                    temp = temp+prob1*0.0
                else:
                    temp = temp+prob1*(-1.0*subprob1*math.log(subprob1,2)-1.0*subprob2*math.log(subprob2,2))

            if prob2 == 0.0:
                temp = temp+0
            else:
                if subprob3 == 0.0 or subprob4 == 0.0:
                    temp = temp+prob2*0.0
                else:
                    temp = temp+prob2*(-1.0*subprob3*math.log(subprob3,2)-1.0*subprob4*math.log(subprob4,2))

            if prob3 == 0.0:
                temp = temp+0
            else:
                if subprob5 == 0.0 or subprob6 == 0.0:
                    temp = temp+prob3*0.0
                else:
                    temp = temp+prob3*(-1.0*subprob5*math.log(subprob5,2)-1.0*subprob6*math.log(subprob6,2))
            info_Gain = H-temp
            if max_H <= info_Gain:
                max_H = info_Gain
                position = i
        return position;

    #Based on the best feature and its 3 possible value, spilt the data in into 3 subdata to construct the subtree
    def spiltData(self, data1, data2, position, value):
        retData1 = []
        retData2 = []  
        for row in range(len(data2)):  
            if data2[row][position] == value:  
                reducedObj1 = data2[row][:position]  
                reducedObj2 = data2[row][position+1:]
                reducedObj = reducedObj1+reducedObj2
                retData2.append(reducedObj)
                retData1.append(data1[row])
        return [retData1, retData2]

    #create the Decision Tree
    def createTree(self, data1, data2, labels, count):
        #if there is only one kind of label in data, return the label.
        if data1.count(data1[0]) == len(data1):  
            return data1[0]  
        
        #get the best feature position
        bestFeature = self.getMaxEntropy(data1, data2, count)
        #get the best feature label
        bestFeatureLabel = labels[bestFeature]  
        #define a empty tree
        myTree = {bestFeatureLabel:{}}    
        #delete the best feature label in the feature labels
        del(labels[bestFeature])

        count = count-1     
        #get all possible feature values
        featureValues = [example[bestFeature] for example in data2]
        uniqueVals = set(featureValues)
          
         
        for value in uniqueVals:  
              
            subLabels = labels[:]
            para = self.spiltData(data1, data2, bestFeature, value)
            newdata1 = para[0]
            newdata2 = para[1]
            #construct the decision tree with recursion
            myTree[bestFeatureLabel][value] = self.createTree(newdata1, newdata2, subLabels, count)  
          
        return myTree

    def learn(self, train_data):
        with open(train_data, "r") as f:
            data = f.read().splitlines();
        temp1 = list()
        temp2 = list()
        count = 0
        for row in data:
            instance = row.split();
            s = ""
            temp_count = 0
            for i in instance[1]:
                if i != ",":
                    s = s + i
                    temp_count = temp_count+1
            count = temp_count
            temp1.append(instance[0])
            temp2.append(s)
        labels = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
        labelsCopy = labels[:]

        decisionTree = self.createTree(temp1, temp2, labels, count)  
        print decisionTree
        self.labelsCopy = labelsCopy
        self.decisionTree = decisionTree

    # Add your code here.
    # Use the learned decision tree to predict
    # query example: 'n,y,n,y,y,y,n,n,n,y,?,y,y,y,n,y'
    # return 'republican' or 'republican'

    #classify the test data based on the decision tree
    def classify(self, decisionTree, featureLabels, testVector):  
        
        firstStr = tuple(decisionTree.keys())[0]
        
        secondDict = decisionTree[firstStr]
        
        featIndex = featureLabels.index(firstStr) 
        
        classLabel = ""
        for key in secondDict.keys():  
            if testVector[featIndex] == key:  
                if type(secondDict[key]).__name__ == 'dict':  
                    classLabel = self.classify(secondDict[key],featureLabels,testVector)  
                else:  
                    classLabel = secondDict[key]
        return classLabel

    def solve(self, query):
        temp = ""
        for i in query:
            if i != ",":
                temp = temp+i

        result = self.classify(self.decisionTree, self.labelsCopy, temp)
        return result

