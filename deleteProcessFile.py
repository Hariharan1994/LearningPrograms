import shutil
import os
import time
import datetime

delFileCount = 0
defEmptySpace = '         '

class deleteProcessClass :
    
    def initDeleteProcess(self) :
        global delFileCount
        srcPath = input(defEmptySpace+'Enter Source Path to be Deleted : ')
        lastModifyDate = input(defEmptySpace+'Enter the Last Modified Date to be DELETEd (YYYY/MM/DD): ')
        errorInput = self.checkDeleteDate(lastModifyDate)
        if errorInput == '' :
            delFileCount = 0
            self.startDeleteProcess(srcPath, lastModifyDate)
            print('Totally, ',delFileCount,' Files Deleted which has the Last Modiifed Date on "',lastModifyDate,'"')
        else :
            print(defEmptySpace+errorInput)

    def startDeleteProcess(self, srcPath, lastModifyDate) :
        if os.path.isdir(srcPath) :
            self.deleteFolder(srcPath, lastModifyDate)
            #self.deleteFullFolder(srcPath)
        elif os.path.isfile(srcPath) :
            self.deleteSingleFile(srcPath, lastModifyDate)
        else :
            print(defEmptySpace+srcPath + ' is NOT a Valid File/ Directory to be DELETEd')
            
    def deleteFolder(self, srcPath, lastModifyDate) :
        for(dirPath, dirNames, fileNameList) in os.walk(srcPath) :
            for fileName in fileNameList :
                filePath = dirPath +'\\'+ fileName
                self.deleteSingleFile(filePath, lastModifyDate)

    def deleteFullFolder(self, srcPath) :
        print(defEmptySpace+'#_Deleting the given Source Directory...')
        shutil.rmtree(srcPath)

    def deleteSingleFile(self, filePath, lastModifyDate) :
        fileName = os.path.basename(filePath)
        modified = os.path.getmtime(filePath)
        year,month,day,hour,minute,second=time.localtime(modified)[:-3]
        #print("Date modified:",datetime.datetime.fromtimestamp(modified))
        print(defEmptySpace + fileName+" --> %d/%02d/%02d %02d:%02d:%02d"%(year,month,day,hour,minute,second))
        fileModifiedDate = "%d/%02d/%02d"%(year,month,day)
        if lastModifyDate == fileModifiedDate :
            global delFileCount
            delFileCount = delFileCount + 1
            print(defEmptySpace+'#_Deleting the file, '+fileName)
            os.remove(filePath)

    def checkDeleteDate(self, deleteDate) :
        errorInput = ''
        try :
            datetime.datetime.strptime(deleteDate, '%Y/%m/%d') #import datetime
        except :
            errorInput = 'Not a Valid Last Modified Date (DD/MM/YYYY)'
            #dateSplit = deleteDate.split('/')
            #if int(dateSplit[0]) > 31 :
            #    errorInput = 'Not a Valid Date (DD)'
            #elif int(dateSplit[1]) > 12 :
            #    errorInput = 'Not a Valid Month (MM)'
            #elif len(dateSplit[2]) != 4 :
            #    errorInput = 'Not a Valid Year (YYYY)'
        return errorInput
