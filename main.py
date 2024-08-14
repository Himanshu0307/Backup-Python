from Company import Company
from FTPServices import FTPServices
from BackupSQL import BackupSQL
from time import sleep




def main():
    sql = BackupSQL()
    sql.BackupNow()
    




if __name__ == "__main__":
    main()
