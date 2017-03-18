"""
A simple wrapper for linear regression.  (c) 2015 Tucker Balch
"""
import RTLearner as rt
import numpy as np

class BagLearner(object):

    def __init__(learner = rt.RTLearner, kwargs = {"leaf_size":1}, bags = 20, boost = False, verbose = False):   
        self.learners = []
        # kwargs = {"k":10}
        for i in range(0,bags):
            self.learners.append(learner(**kwargs))
    
    def addEvidence(self,dataX,dataY):
        newdataX = np.ones([dataX.shape[0], dataX.shape[1] + 1])
        newdataX[:, 0:dataX.shape[1]] = dataX
        newdataX[:, dataX.shape[1]] = dataY

        for t in self.learners:
            t.addEvidence(newdataX, dataY)
        
    def query(self,points):
        list = []
        for t in self.learners:
            list.append(t.query(points))
        result = np.array(list).mean(axis=0)
        print result
        return result

if __name__=="__main__":
    print "the secret clue is 'zzyzx'"
