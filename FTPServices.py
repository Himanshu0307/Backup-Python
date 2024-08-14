import ftplib
import datetime
from Company import Company

from LogManager import LogManager
class FTPServices:

    def __init__(self,logManager:LogManager,company:Company) -> None:
        self.log=logManager
        self._company=company


    def transfer(self,source=""):
        ftp=ftplib.FTP()
        try:
            con=ftp.connect(self._company.serverip,self._company.port,timeout=200)
            print(con)
            ftp.login(self._company.username,self._company.password)
            with open(source,"rb") as file:
                try:
                    ftp.cwd("/{company}/{datetime}".format(company=self._company.name,datetime=datetime.datetime.now().date()))
                except:
                    
                    ftp.mkd("/{company}/{datetime}".format(company=self._company.name,datetime=datetime.datetime.now().date()))
                    ftp.cwd("/{company}/{datetime}".format(company=self._company.name,datetime=datetime.datetime.now().date()))
             
                target="{filename}".format(filename=file.name.split("\\")[-1])
                # print("current file name","{filename}".format(filename=file.name.split("\\")[-1]))
                ftp.storbinary('STOR '+ target, file)
            ftp.quit()
           
        except Exception as e:
            self.log.Errorlogger.error(e)
        else:
            self.log.SuccessLogger.info("Successfully sent file to server")
        finally:    
            ftp.close()

        
        

