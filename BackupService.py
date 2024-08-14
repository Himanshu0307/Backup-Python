import main
import time
from BackupSQL import BackupSQL
from PythonService import PythonService
class BackupService(PythonService):
    # Define the class variables
    _svc_name_ = "BackupServiceSQL"
    _svc_display_name_ = "Backup Service SQL - Finnaux Tech Solution"
    _svc_description_ = "Automatic Backup Service"
    _exe_name_ = "D:\BackupService\env\Scripts\pythonservice.exe"
    # Override the method to set the running condition
    def start(self):
        self.isrunning =True
        self.sqlSer = BackupSQL()
        self.sqlSer.BackupNow()
        
    # Override the method to invalidate the running condition
    # When the service is requested to be stopped.
    def stop(self):
        self.sqlSer.closeScheduler()
        self.isrunning =False
        
    # Override the method to perform the service function
    def main(self):
        while self.isrunning:
            self.sqlSer.BackupNow()
            time.sleep(60)
# Use this condition to determine the execution context.
if __name__ == '__main__':
    # Handle the command line when run as a script
    BackupService.parse_command_line()