import validateInputFile as viF
commandInput = ['copy', 'select', 'delete', 'help', '1', '2', '3']
exitInput = ['exit', '0']
loopFlag = True
defEmptySpace = '         '

def getUserInput() :
    return input('Enter Input : ').lower()

def validateUserInput(userInput) :
    if userInput in exitInput :
        global loopFlag
        loopFlag = False #exits the current 
    elif userInput in commandInput :
        viF.validateInputClass().initValidate(userInput)
    else :
        print(defEmptySpace+userInput+' is Not a Valid Command...')   

def programMain() :
    while loopFlag :
        userInput = getUserInput()
        validateUserInput(userInput)

programMain()
print(defEmptySpace+'PROCESS TERMINATED')
