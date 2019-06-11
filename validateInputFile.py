import copyProcessFile
import selectProcessFile
import deleteProcessFile

defEmptySpace = '         '

class validateInputClass() :

    def printHelpCommand(self) :
        print(defEmptySpace+'1. copy')
        print(defEmptySpace+'2. select')
        print(defEmptySpace+'3. delete')

    def getCommandName(self, userInput) :
        commandName = {
                '1' : 'copy',
                '2' : 'select',
                '3' : 'delete'
             }
        return commandName.get(userInput, userInput)

    def processCommand(self, commandInput) :
        print(defEmptySpace+'#processCommand Input = ', commandInput)
        try :
            if commandInput == 'copy' :
                copyProcessFile.copyProcessClass().initCopyProcess()
            elif commandInput == 'select' :
                selectProcessFile.selectProcessClass().initSelectProcess()
            elif commandInput == 'delete' :
                deleteProcessFile.deleteProcessClass().initDeleteProcess()
            else :
                print(defEmptySpace+commandInput+' is NOT a Valid Command')
        except :
            print('>> #_Exception occurred while processing "'+commandInput+'" command...Try Again...!!!')
        
    def initValidate(self, userInput):
        if userInput == 'help' :
            self.printHelpCommand()
        else :
            self.processCommand(self.getCommandName(userInput))
        
