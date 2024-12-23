import os
os.system("adb start-server")
os.system("adb devices > devicess.txt")
deviceFile = open("devicess.txt","r")
deviceList = deviceFile.readlines()
deviceFile.close()
os.system("del devicess.txt")
deviceDSN = []
cwd=os.getcwd()
urDirectory=cwd.replace('\\','\\\\')
urDirectory=urDirectory+"\\" 

for device in deviceList:
	deviceDSN.append(device.split('\t')[0])
del deviceDSN[0] # list of devices attached element
del deviceDSN[-1] # last \n element

#print len(deviceDSN)
#print deviceDSN

if(len(deviceDSN)==0):
        print "No devices attached"
	os.system("PAUSE")

else:

        print deviceDSN



for i in range(0,len(deviceDSN),1):
	deviceDSN[i]=deviceDSN[i].split(':')[0]
 	print "loading logs for device "+str(i)+" saved as "+"logs_"+deviceDSN[i]+".txt"
 	os.system("start cmd /k "+urDirectory+"savelog.bat "+deviceDSN[i])
 	os.system("start cmd /k "+urDirectory+"runninglog.bat "+deviceDSN[i])
	os.system("start cmd /k "+urDirectory+"disablelogchatty.bat "+deviceDSN[i])
			
# this takes logs for all connected devices....
