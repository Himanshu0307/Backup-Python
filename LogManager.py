import logging
import os
class LogManager:
    Errorlogger=None
    SuccessLogger=None

    def __init__(self) -> None:
        formatter=logging.Formatter('%(asctime)s %(message)s')
        if(not os.path.exists("logs\\")):
            path=os.path.join(os.getcwd(),"logs\\")
            # print(path)
            os.mkdir(path)
            
        self.Errorlogger=logging.getLogger("Errorlogger")
        self.Errorlogger.manager
        self.Errorlogger.setLevel(logging.ERROR)
        fileHandError=logging.FileHandler(filename="logs\\logError.log",mode="a+")
        fileHandError.setFormatter(formatter)
        self.Errorlogger.addHandler(fileHandError)

        #Success
        self.SuccessLogger=logging.getLogger("Successlogger")
        self.SuccessLogger.setLevel(logging.INFO)
        fileHandSuccess=logging.FileHandler(filename="logs\\logSuccess.log",mode="a+")
        fileHandSuccess.setFormatter(formatter)
        self.SuccessLogger.addHandler(fileHandSuccess)

    def viewError(self):
       with open("logs/logError.log") as file:
           return file.readlines()[:50]

    def viewInfo(self):
       with open("logs/logSuccess.log") as file:
           return file.readlines()[:50]