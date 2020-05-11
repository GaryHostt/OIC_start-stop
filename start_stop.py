

import requests
import oci
from oci.config import validate_config
import datetime
from datetime import date, time, datetime
import time
import sys

# OCI SDK config 

config = oci.config.from_file(
	"/Users/aamacdon/.oci/config",
"DEFAULT")
identity = oci.identity.IdentityClient(config)
user = identity.get_user(config["user"]).data
#print(user)

## Time work
today = datetime.now() 
NewText = today.strftime("%A, %d. %B %Y %I:%M%p")

## announcements test

def announcements():
	url = "https://announcements.us-ashburn-1.oraclecloud.com/20180904/announcements"
	payload  = {}
	headers = {
  	'Content-Type': 'application/json'
	}
	print(url)
	response = requests.request("GET", url, headers=headers, data = payload)
	print(response.text.encode('utf8'))

# API calls in functions

def start_input():
	#print(user)
	print("Please input the OCID of your tenancy, and then press enter.")
	ID = input("")
	print ("Instance with OCID: " + ID + " is now stopping.")
	#print (ID)
	url = "https://integration.us-ashburn-1.ocp.oraclecloud.com/20190131/integrationInstances/" + ID + "/actions/start"
	payload  = {}
	headers = {
  	'Content-Type': 'application/json'
	}
	print(url)
	response = requests.request("POST", url, headers=headers, data = payload)
	#print(url)
	print("The response from the OCI API is below:")
	print(response.text.encode('utf8'))

def stop_input():
	print("Please input the OCID of your tenancy, and then press enter.")
	ID = input("")
	print ("Instance with OCID: " + ID + " is now stopping.")
	url = "https://integration.us-ashburn-1.ocp.oraclecloud.com/20190131/integrationInstances/" + ID + "/actions/stop"

	payload  = {}
	headers = {
  	'Content-Type': 'application/json'
	}

	response = requests.request("POST", url, headers=headers, data = payload)
	print("The response from the OCI API is below:")
	print(response.status_code)
	print(response.text.encode('utf8'))

# Running the program
i = 0
while True:
	validate_config(config)
	print(config)
	count = 0
	print("Hello user, input 1 and press enter to start your OIC instance, and input 2 to stop your instance.")
	answer = input("")
	i += 1
	#print(answer)
	if answer == "1":
		print("You have choosen to start the instance.")
		start_input()
	if answer == "2":
		print("You have choosen to stop the instance.")
		stop_input()
	if answer == "3":
		announcements()
	print(i)
	if i == 1:
		print("Thank you for using the OCI API today, good bye.")
		break


	
