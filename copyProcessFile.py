import shutil
import os

defEmptySpace = '         '

class copyProcessClass :

    def initCopyProcess(self) :
        srcPath = input(defEmptySpace+'Enter Source Path : ')
        destPath = input(defEmptySpace+'Enter Destination Path : ')
        self.startCopyProcess(srcPath, destPath)
        
    def startCopyProcess(self, srcPath, destPath) :
        if os.path.isdir(srcPath) :
            self.copyFullFolder(srcPath, destPath)
        elif os.path.isfile(srcPath) :
            self.copySingleFile(srcPath, destPath)
        else :
            print(defEmptySpace+srcPath + 'is NOT a Valid Source File/ Directory')

    def copyFullFolder(self, srcPath, destPath) :
        if os.path.isdir(destPath) :
            print(defEmptySpace+'#_Deleting the existing Destination Directory...')
            shutil.rmtree(destPath)
            
        print(defEmptySpace+'#_Copying entire Source Directory...')
        shutil.copytree(srcPath, destPath, False, None)

    def copySingleFile(self, srcPath, destPath) :
        destDirPath = os.path.dirname(destPath)
        if not os.path.isdir(destDirPath) :
            print(defEmptySpace+'#_Creating new Destination Folder...')
            os.makedirs(destDirPath)
            
        print(defEmptySpace+'#_Copying Single Source File...')
        shutil.copyfile(srcPath, destPath)

    
            
