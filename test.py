import math
import numpy as np
import pandas as pd

def creatDataSet():
    dataSet = [[1, 1, "yes"],
               [1, 1, "yes"],
               [1, 0, "no"],
               [0, 1, "no"],
               [0, 1, "no"]]
    label = ["no surfacing", "flippers","labels"]
    return pd.DataFrame(dataSet,columns=label)


def calcEnt(dataSet):
    dataEnt = 0
    countre = pd.value_counts(dataSet.iloc[:,-1])/dataSet.shape[0]
    for item in countre:
        dataEnt -= item*math.log(item,2)
    return dataEnt

def calcConEnt(dataSet,colname):
    dataConEnt = 0
    for value in np.unique(dataSet[colname]):
        cashData = dataSet[dataSet[colname]==value]
        dataConEnt += calcEnt(cashData)*cashData.shape[0]/dataSet.shape[0]
    return dataConEnt


def voteMostlabel(dataSet):
    countre = pd.value_counts(dataSet.iloc[:, -1])
    return countre.index[np.where(max(countre)==countre)][0]

def chooseBestFeatureID3(dataSet):
    featureLst = dataSet.columns[:-1]
    dataEnt = calcEnt(dataSet)
    bestFeature = -1
    bestConEnt = dataEnt
    bestConEntGain = 0
    for feature in  featureLst:
        conEnt = calcConEnt(dataSet,feature)
        if conEnt < bestConEnt:
            bestFeature = feature
            bestConEnt = conEnt
    bestConEntGain = dataEnt-bestConEnt
    return bestFeature,bestConEnt,bestConEntGain



def chooseBestFeatureC45(dataSet):
    featureLst = dataSet.columns[:-1]
    dataEnt = calcEnt(dataSet)
    bestFeature = -1
    bestConEnt = dataEnt
    bestConEntGain = 0
    for feature in  featureLst:
        conEnt = calcConEnt(dataSet,feature)
        entGain =(dataEnt - conEnt)/calcEnt(dataSet[feature])
        if entGain > bestConEntGain:
            bestFeature = feature
            bestConEntGain = entGain
            bestConEnt = conEnt
    return bestFeature,bestConEnt,bestConEntGain

def CreatTree(dataSet):
    if len(np.unique(dataSet.iloc[:,-1]))==1:
        return dataSet.iloc[0,-1]
    if len(dataSet.columns)==1:
        return voteMostlabel(dataSet)
    bestFeature, bestConEnt, bestConEntGain = chooseBestFeatureID3(dataSet)
    treeDic = {bestFeature:{}}
    for value in np.unique(dataSet[bestFeature]):
        cashDataSet = dataSet[dataSet[bestFeature] == value]
        treeDic[bestFeature][value] = CreatTree(cashDataSet.drop(bestFeature, 1))
    return treeDic


if __name__ == "__main__":
    dataSet = creatDataSet()
    CreatTree(dataSet)