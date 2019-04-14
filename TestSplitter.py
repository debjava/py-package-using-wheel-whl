'''
Created on Apr 14, 2019

@author: PIKU
'''
from textsplitter.TextPySplitter import TextPySplitter


def testSplitter():
    textToSplit = "Bangalore,Karnataka,Chennai,Tamilnadu"
    strSeparator = ","
    strSplitter = TextPySplitter()
    splittedValues = strSplitter.splitString(textToSplit, strSeparator)
    if len(splittedValues) != 0:
        for splittedData in splittedValues:
            print("Splitted Value : ", splittedData)

    
if __name__ == "__main__":
    testSplitter()
    
