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
    def getCSVDirectory(numCards):
        #get current directory
        mainDirectory = os.path.abspath(os.curdir)

        #get data directory
        dataDirectory = os.path.join(mainDirectory, "data")

        csvDirectory = ""

        if numCards == 10:
            csvDirectory = os.path.join(dataDirectory, "score10.csv")
        elif numCards == 14:
            csvDirectory = os.path.join(dataDirectory, "score14.csv")
        elif numCards == 18:
            csvDirectory = os.path.join(dataDirectory, "score18.csv")

        return csvDirectory

    @staticmethod
    def saveScore(userName, score, numCards):
        '''save passed user and score to score.csv'''
        #FIXME: pass in mode (10, 20 cards). use a different csv for each mode

        csvDirectory = DirectoryParser.getCSVDirectory(numCards)

        row = [userName, score.score]

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

    @staticmethod
    def getTop10Scores(numCards):
        csvDirectory = DirectoryParser.getCSVDirectory(numCards)

        with open(csvDirectory, "r") as readFile:
            reader = csv.reader(readFile)
            lines = list(reader) #store all csv data in list

            if len(lines) < 10: #if less than 10 scores, add dummy entries
                numRows = len(lines)
                for i in range(numRows, 10):
                    lines.append(["N/A", 0])
                return lines[:10]
            else:
                return lines[:10] #return rows 0 to 9
            

if __name__ == "__main__":
    print(DirectoryParser.retrieveCardImages("theme1", "back"))
    print(DirectoryParser.retrieveCardImages("theme1", "front"))

    print(DirectoryParser.getTop10Scores(10))
    
    
    


