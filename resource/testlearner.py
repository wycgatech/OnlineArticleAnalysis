import numpy as np
import math
import sys
import matplotlib.pyplot as plt
import random
import json


def whole_query(data, num, tree):
        # data = np.array(points)
        queryResult = []

        for l in range(num):
            queryResult.append(one_query(data, l, tree))

        toArray = np.array(queryResult)

        mean = toArray.mean(axis=0)

        if mean < 1.8:
            return 1
        elif mean >= 2.2:
            return 3
        else:
            return 2

def one_query(record, i, tree):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """

        # print points

        index = 0
        tree_now = tree[i]
        curr_Node = tree_now[index, :]
        leafFlag = curr_Node[0]
        while leafFlag != -1:
            feature = curr_Node[0]
            if record[feature] <= curr_Node[1]:
                index = index + curr_Node[2]
                curr_Node = tree_now[index, :]
                leafFlag = curr_Node[0]
            else:
                index = index + curr_Node[3]
                curr_Node = tree_now[index, :]
                leafFlag = curr_Node[0]
        return curr_Node[1]

        # print queryResult



if __name__=="__main__":

    data = [0]*17
    input = json.loads((sys.argv[1]))
    #input = ["Monday",'1000','Business',"3",'2','5']
    if input[0]== 'Monday':
         data[0] = 1

    elif input[0] == 'Tuesday':
         data[1] = 1
    elif input[0] == 'Wednesday':
         data[2] = 1
    elif input[0] == 'Thursday':
         data[3] = 1
    elif input[0] == 'Friday':
         data[4] = 1
    elif input[1] == 'Saturday':
         data[5] = 1
    else :
         data[6] = 1

    data[7] = int(input[1])

    if input[2]== 'Lifestyle':
         data[8] = 1
    elif input[2] == 'Entertainment':
         data[9] = 1
    elif input[2] == 'Business':
         data[10] = 1
    elif input[2] == 'Social Media':
         data[11] = 1
    elif input[2] == 'Tech':
         data[12] = 1
    elif input[2] == 'World':
         data[13] = 1
    else :
         data[13] = 0

    data[14] = int(input[3])
    data[15] = int(input[4])
    data[16] = int(input[5])
    testX = np.array(data)


    # create a learner and train it

    tree= np.load('learnedTree.npy')

    # evaluate in sample

    predY = whole_query(testX,10,tree) # get the predictions


    if predY == 1:
        comment = "1"
    elif predY == 2:
        comment = "2"
    else:
        comment = "3"
    rank = [""]*5;
    rank[0] = "No human wants to read or share!"
    rank[1] = "not popular"
    rank[2] = "popular"
    rank[3] = "very popular"
    rank[4] = "Extremely popular"

    if data[7] < 0 or data[14] < 0 or data[15] < 0:
        comment = "invalid input: input has to be positive"
    elif (data[7] > 0 and data[7] < 50) or data[7] > 3000:
        if data[14] < 5:
            comment = rank[0]
        else:
            comment = rank[1]
    elif (data[7] >= 50 and data[7] < 110) or (data[7] >= 2400 and data[7] < 3000):
        if data[14] == 0:
            comment = rank[1]
        else:
            comment = rank[2]
    elif (data[7] >= 110 and data[7] < 500) or (data[7] >= 1800 and data[7] < 2400):
        comment = rank[2]
    elif (data[7] >= 500 and data[7] <= 1100):
        if data[13] == 1:
            comment = rank[2]
        else:
            comment = rank[3]
    elif (data[7] > 1100 and data[7] < 1800):
        if data[13] == 1:
            comment = rank[1]
        else:
            comment = rank[4]

    # word count: data[7]
    # number of picture:  data[14]
    # number of reference: data[15]
    # title words count: data[16]


    print json.dumps({'result': comment})

