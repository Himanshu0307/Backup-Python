from flask import Flask, jsonify,request;
from json import dumps
from main import getAllCompanyInfo as Com;
from BackupSQL import BackupSQL;




app=Flask(__name__)

backupService=BackupSQL()


# Schedule New JOB
@app.route("/Jobs/ScheduleJob",methods=["POST"])
def ScheduleJob():
    if(request.method=="POST"):
        time=request.get_json()["time"]
    
    print("hours",time[:2])
    print("minute",time[3:5])
    res=backupService.scheduleBackup(time[:2],time[3:5])
    if res:
        return "Successfully Created",200
    else:
        return 'Job Creation Failure',500
    


# GetAllJObs of a company
@app.route("/Jobs/GetCompanyJob",methods=["POST"])
def GetCompanyJob():
    return backupService.scheduledjob

#Delete a JOb
@app.route("/Jobs/DeleteJob",methods=["DELETE"])
def DeleteJob():
    if(request.method=="DELETE"):
        time=request.get_json()["id"]
    if backupService.DeleteJob(id):
        return "Successfully Deleted Job",200
    else:
        return "Failed to Deleted Job",500
    

# Delete All Jobs
@app.route("/Jobs/DeleteAllJob",methods=["DELETE"])
def DeleteAllJob():
    
    if backupService.cancelAllJob():
        return "Successfully Deleted Jobs",200
    else:
        return "Failed to Deleted Jobs",500


#Backup Now
@app.route("/Jobs/BackupNow",methods=["POST"])
def BackupNow():
    if(request.method=="POST"):
        backupService.BackupNow()
    return {"msg":"Please Check Log files after some Time"}, 200, {"Access-Control-Allow-Origin": "*"}

#View Error
@app.route("/Logs/ViewError",methods=["POST"])
def ViewError():
    return backupService.log.viewError()

#View Info
@app.route("/Logs/ViewInfo",methods=["POST"])
def ViewInfo():
    return backupService.log.viewInfo()
        # return "Success", 200, {"Access-Control-Allow-Origin": "*"}


#Config
@app.route("/Server/Config",methods=["POST"])
def ConfigServer():
    pass