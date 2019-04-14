'''
Created on Apr 14, 2019

@author: PIKU
'''


class TextPySplitter:
    '''
    classdocs
    '''
    
    @classmethod
    def splitString(self, textToSplit, splitSeparator):
        splittedString = []
        if (textToSplit is not None and len(textToSplit) != 0):
            splittedValues = textToSplit.split(splitSeparator)
            
            for val in splittedValues:
                splittedString.append(val)
#                 print("Splitted Value : ", val)
            return splittedString
