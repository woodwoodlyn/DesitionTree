import math

def createDataSet():
    dataSet = [[1,1,"yes"],
               [1,1,"yes"],
               [1,0,"no"],
               [0,1,"no"],
               [0,1,"no"]]
    label =["no surfacing","flippers"]
    return dataSet,label

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCountsDic ={}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCountsDic.keys():
            labelCountsDic[currentLabel] =0
        labelCountsDic[currentLabel] +=1
    shannonEt = 0
    for key in labelCountsDic.keys():
        prob = float(labelCountsDic[key])/numEntries
        shannonEt -= prob * math.log(prob,2)
    return shannonEt


def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0])-1
    bestEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featLst = [example[i] for example in dataSet]
        uniqueVals = set(featLst)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob*calcShannonEnt(subDataSet)
        infoGain = bestEntropy - newEntropy
        if(infoGain>bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] =0
        classCount[vote] +=1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


myDat, labels = createDataSet()
createTree(myDat, labels)