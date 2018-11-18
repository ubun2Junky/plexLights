import argparse
import urllib2
import json

#Gather arguments
parser=argparse.ArgumentParser(description="Plex home theatre light controller script.")
parser.add_argument('--loglvl', '-l', type=int, help="log detail (10 info, 20 debug)", metavar="10", choices=[10, 20])
parser.add_argument('homeController', choices=['vera','smartthings'], help="Select between vera or smartthings controller")
parser.add_argument('controllerIP', help="IP of the controller.")
parser.add_argument('controllerPort', default=3480, type=int, help="Port the controller is connected to.")
parser.add_argument('daynightID', help="Object ID on controller")
parser.add_argument('sceneID', help="Scene ID on controller")

args = parser.parse_args()

#Assign arguments to local variables
loglvl = args.loglvl
homeController = args.homeController
daynightID = args.daynightID
sceneID = args.sceneID

#General Vera request function
def veraRequest(URL):
	response = urllib2.urlopen(URL)
	content = response.read()

	data = json.loads(content.decode("utf8"))

	return data

#Get Day/Night status from Vera controller
def veraDayNight(URL):
	dayNightDevice = 'Device_Num_' + daynightID
	data = veraRequest(URL)
	dayNightStatus = (data[dayNightDevice]['states'][0]['value'])

	return dayNightStatus

#Trigger scene on Vera controller
def veraScene(URL):
	data = veraRequest(URL)
	veraStatus = (data['u:RunSceneResponse']['OK'])

	return veraStatus


#MAIN
if homeController == "vera":
	veraIP = args.controllerIP
	veraPort = args.controllerPort
	DayNightStatusURL = 'http://' + str(veraIP) + ':' + str(veraPort) + '/data_request?id=status&output_format=json&DeviceNum=' + str(daynightID)
	sceneRequestURL = 'http://' + str(veraIP) + ':' + str(veraPort) + '/data_request?id=lu_action&output_format=json&serviceId=urn:micasaverde-com:serviceId:HomeAutomationGateway1&action=RunScene&SceneNum=' + str(sceneID)

	if veraDayNight(DayNightStatusURL) == '0':
		veraScene(sceneRequestURL)