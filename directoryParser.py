#import imghdr
#from os import listdir
#from os.path import isfile, join, realpath, dirname
import os

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
    
    '''@staticmethod
    def retrieveImages(directory):
        #get all images in a directory
        #imageList = [f for f in listdir(directory) if (isfile(join(directory, f)) and imghdr.what(join("images", f)) in DirectoryParser.imageExtensions)]
        imageList = []
        for file in listdir(directory):
            currentExtension = imghdr.what(join("images", file)) #get file extensions
            if currentExtension in DirectoryParser.imageExtensions: #guarantee image is chosen
                imageList.append(file)    
        
        return imageList'''

if __name__ == "__main__":
    print(DirectoryParser.retrieveCardImages("theme1", "back"))
    print(DirectoryParser.retrieveCardImages("theme1", "front"))
    
    


