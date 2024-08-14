
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, date, time
from LogManager import LogManager
from Company import Company
from FTPServices import FTPServices
import pyodbc
import os
import json


class BackupSQL():
    scheduledjob = {}
    def __init__(self) -> None:
        
        # Create folder For Backup Folder
        path = "BackupFolder"
        parentdir = os.getcwd()
        path = os.path.join(parentdir, path)
        if not (os.path.exists(path)):
            os.mkdir(path=path)

        # Log
        BackupSQL.log = LogManager()
        
        
        # Scheduler
        BackupSQL.scheduler = BackgroundScheduler()
        BackupSQL.scheduler.start()


        # config Company
        BackupSQL.company = Company()
        with open("config.json") as file:
            js=json.load(file)
            if js["scheduled"]!=None:
                self.scheduleBackup(js["scheduled"][:2],js["scheduled"][3:5])

    def Backup(self):
        try:
            # Make Directory for Current Date
            path = "BackupFolder\\{0}\\".format(datetime.now().date())
            parentdir = os.getcwd()
            path = os.path.join(parentdir, path)
            if not (os.path.exists(path)):
                os.mkdir(path=path)

            server = BackupSQL.company.dbServer
            database = BackupSQL.company.database
            dbusername = BackupSQL.company.dbusername
            dbpassword = BackupSQL.company.dbpassword

            # Create a connection object
            conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' +
                                  database+';Trusted_Connection=yes'+';Uid='+dbusername+';Pwd='+dbpassword)
            conn.autocommit = 'false'

            # Create a cursor object
            cursor = conn.cursor()
            # Backup file name
            backup_file = 'backup' + \
                str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '.bak'
            # Backup command
            backup_command = 'BACKUP DATABASE %s TO DISK =\'' % (
                database) + os.path.join(path, backup_file) + '\''
            # Execute the backup command
            print(backup_command)
            cursor.execute(backup_command)
            BackupSQL.log.SuccessLogger.info("Successfully Created Backup")
            ftpService = FTPServices(BackupSQL.log,BackupSQL.company)
            print("Path for Backup:"+path+backup_file)
            ftpService.transfer(path+backup_file)

        except Exception as e:
            BackupSQL.log.Errorlogger.error(e)

    def configService(self):
        print("Enter ID")
        id = int(input())
        print("Enter Company Name")
        name = input()
        print("Enter Database Server Name")
        dbServer = input()
        print("Enter Server IP")
        serverip = input()
        print("Enter Database Name")
        database = input()
        return {"id": id, "name": name, "dbServer": dbServer, "serverip": serverip, "database": database}

    def scheduleBackup(self, hours: str, minute: str):
        try:
            job = BackupSQL.scheduler.add_job(self.Backup, trigger='cron', hour=int(
                hours), minute=int(minute))
            self.scheduledjob[job.id] = hours+":"+minute
            print(self.scheduledjob)
        except Exception as e:
            BackupSQL.log.Errorlogger.error(e)
            return False
        else:
            return True

    def cancelAllJob(self):
        try:
            BackupSQL.scheduler.remove_all_jobs()
            self.scheduledjob = {}
        except Exception as e:
            BackupSQL.log.Errorlogger.error(e)
            return False
        else:
            return True

    def closeScheduler(self):
        BackupSQL.scheduler.shutdown()

    def BackupNow(self):
        self.Backup()

    def DeleteJob(self, id):
        try:
            BackupSQL.scheduler.remove_job(id)
        except Exception as e:
            BackupSQL.log.Errorlogger.error(e)
            return False
        else:
            return True
