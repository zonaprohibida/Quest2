'''
Created on Jun 12, 2018

@author: torky
'''
numStrings = 0
with open('pytestFile1.txt', 'r') as fileReader:
    fileContent = fileReader.read()
    print(fileContent)
    print(len(fileContent))
    print(type(fileContent))