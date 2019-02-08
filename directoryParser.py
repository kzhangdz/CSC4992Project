import imghdr
from os import listdir
from os.path import isfile, join, realpath, dirname

class DirectoryParser:
    '''used to retrieve images for cards'''

    imageExtensions = ['jpeg', 'jpg', 'gif', 'png']
    
    @staticmethod
    def retrieveImages(directory):
        '''get all images in a directory'''
        #imageList = [f for f in listdir(directory) if (isfile(join(directory, f)) and imghdr.what(join("images", f)) in DirectoryParser.imageExtensions)]
        imageList = []
        for file in listdir(directory):
            currentExtension = imghdr.what(join("images", file)) #get file extensions
            if currentExtension in DirectoryParser.imageExtensions: #guarantee image is chosen
                imageList.append(file)    
        
        return imageList

if __name__ == "__main__":
    currentPath = dirname(realpath(__file__))
    imagePath = join(currentPath, "images")
    print(imagePath)
    print(DirectoryParser.retrieveImages(imagePath))    
    
    


