import shutil
import os

defEmptySpace = '         '

class selectProcessClass :
    
    def initSelectProcess(self) :
        srcPath = input(defEmptySpace+'Enter Source Path : ')
        fileEtension = input(defEmptySpace+'Enter Required File Extension to be SELECTed: ')
        destPath = input(defEmptySpace+'Enter Destination Path : ')
        self.startSelectProcess(srcPath, destPath, fileEtension)

    def startSelectProcess(self, srcPath, destPath, fileEtension) :
        if os.path.isdir(srcPath) :
            self.selectExtensions(srcPath, destPath, fileEtension)
        elif os.path.isfile(srcPath) :
            self.selectSingleFile(srcPath, destPath, fileEtension)
        else :
            print(defEmptySpace+srcPath+' is NOT a Valid Source Directory...')

    def selectExtensions(self, srcPath, destPath, fileEtension) :
        fileExtensionCount = 0
        for(dirPath, dirNames, fileNameList) in os.walk(srcPath) :
            #print('dirPath = ', dirPath)
            #print('dirNames = ', dirNames)
            #print('fileNameList = ', fileNameList)
            for fileName in fileNameList :
                #print('fileName = ', fileName)
                if fileName.endswith(fileEtension) :
                    if fileExtensionCount == 0 :
                        self.checkDestInput(destPath)
                    fileExtensionCount = fileExtensionCount + 1
                    newSourcePath = dirPath +'\\'+ fileName
                    newDestPath = destPath +'\\'+ fileName
                    print(defEmptySpace+'#_Copying the file, '+fileName)
                    shutil.copyfile(newSourcePath, newDestPath)
        print('Totally, ',fileExtensionCount,'"',fileEtension,'" File Selected and Copied...')

    def selectSingleFile(self, srcPath, destPath, fileEtension) :
        if srcPath.endswith(fileEtension) :
            self.checkDestInput(destPath)
            fileName = os.path.basename(srcPath)
            newDestPath = destPath +'\\'+ fileName
            print(defEmptySpace+'#_Copying the file, '+fileName)
            shutil.copyfile(srcPath, newDestPath)
        else :
            print(defEmptySpace+srcPath+' is NOT a "',fileEtension,'" Source File...')
        
    def checkDestInput(self, destPath) :
        if not os.path.isdir(destPath) :
            print(defEmptySpace+'#_Creating new Destination Folder...')
            os.makedirs(destPath)
