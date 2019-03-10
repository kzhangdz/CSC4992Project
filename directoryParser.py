#import imghdr
#from os import listdir
#from os.path import isfile, join, realpath, dirname
import os
import csv
import operator

class DirectoryParser:
    '''used to retrieve images for cards'''

    #imageExtensions = ['jpeg', 'jpg', 'gif', 'png']

    @staticmethod
    def retrieveCardImages(theme, face):
        '''get all images in a directory'''
        '''theme: theme1, theme2, or theme3'''
        '''face: back or front'''
        #get current directory
        mainDirectory = os.path.abspath(os.curdir)

        #get image directory
        imgDirectory = os.path.join(mainDirectory, "images", "card", theme, face)

        imageList = []
        for file in os.listdir(imgDirectory):
            fileFullPath = os.path.join(imgDirectory, file)
            imageList.append(fileFullPath)
        
        return imageList

    @staticmethod
    def saveScore(userName, score):
        '''save passed user and score to score.csv'''
        #FIXME: pass in mode (10, 20 cards). use a different csv for each mode

        #get current directory
        mainDirectory = os.path.abspath(os.curdir)

        #get data directory
        dataDirectory = os.path.join(mainDirectory, "data")

        row = [userName, score.score]

        csvDirectory = os.path.join(dataDirectory, "score10.csv")

        #open score.csv
        DirectoryParser.openCSV(csvDirectory, row)
        '''with open("score10.csv", "a+", newline="") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(row)'''
            
        #sort score.csv
        sortedList = DirectoryParser.sortCSV(csvDirectory)
        '''with open("score10.csv", "r") as readFile:
            reader = csv.reader(readFile)
            sortedList = sorted(reader, key=operator.itemgetter(1))'''

        #write sortedList to csv
        DirectoryParser.writeCSV(csvDirectory, sortedList)
        '''with open("score10.csv", "a+", newline="") as writeFile:
            writer = csv.writer(writeFile)
            for row in sortedList:
                writer.writerow(row)'''

    @staticmethod
    def openCSV(csvName, row):
        with open(csvName, "a+", newline="") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(row)

    #operator.itemgetter(1)

    @staticmethod
    def sortCSV(csvName):
        with open(csvName, "r") as readFile:
            reader = csv.reader(readFile)
            sortedList = sorted(reader, key=lambda row: int(row[1]), reverse=True)
            print(sortedList)
            return sortedList

    @staticmethod
    def writeCSV(csvName, sortedList):
        with open(csvName, "w+", newline="") as writeFile:
            #rewrite data
            writer = csv.writer(writeFile)
            for row in sortedList:
                writer.writerow(row)

if __name__ == "__main__":
    print(DirectoryParser.retrieveCardImages("theme1", "back"))
    print(DirectoryParser.retrieveCardImages("theme1", "front"))
    
    


