import json


class Company():
    #Configure default Server IP
    def __init__(self,id=0,name="Vagmi",dbServer="DESKTOP-BAKKVDS",serverip="192.168.29.127",database="company",port=2221,username="android",password="android") -> None:
        f=open('config.json') 
        js=json.load(f)
        print(js)
        self.id=js["id"]
        self.name=js["name"]
        self.serverip=js["serverip"]
        self.database=js["database"]
        self.dbServer=js["dbServer"]
        self.port=js["port"]
        self.username=js["username"]
        self.password=js["password"]
        self.dbusername=js["dbusername"]
        self.dbpassword=js["dbpassword"]
        f.close()
      

    
    # def __str__(self) -> str:
    #     x={"id":self.id,"name":self.name,"ip":self.ip,"serverip":self.serverip,"database":self.database}
    
 
 