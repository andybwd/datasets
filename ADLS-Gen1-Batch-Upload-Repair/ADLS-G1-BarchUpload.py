import os
import sys
import time
import requests
from azure.datalake.store import core, lib
import config

####################################################
####            Configure Me
####################################################
image_Source_Directory = "C:\\Users\\abawa\\Downloads\\cars_test\\"
Batchsize = 100
#LDP Repair Settings
LDP_Zones = [{'Host': 'abarb01-vm0.bdfrem.wandisco.com', 'SRC-Zone': 'ABA-LDP-ADLS-G1-001','Path': '/cars'}, \
{'Host': 'abarb01-vm4.bdfrem.wandisco.com', 'SRC-Zone': 'ABA-LDP-ADLS-G1-003','Path': '/cars'}]

## ADLS Settings Stored in config.py
ADLS_Path = config.ADLS_Path
ADLS_Azure_TenentID = config.ADLS_Azure_TenentID
ADLS_cleint_id = config.ADLS_cleint_id
ADSL_Store = config.ADSL_Store
ADLS_cleint_Secret = config.ADLS_cleint_Secret

#################################################################


# Connect to ADLS using service principal authentication
# Store tenant_id, client_id and client_secret in a separate confguration file. Below values are dummy.
token = lib.auth(tenant_id = ADLS_Azure_TenentID,
                 client_id = ADLS_cleint_id,
                 client_secret = ADLS_cleint_Secret)

# Get file system like object from ADLS
adl = core.AzureDLFileSystem(token, store_name=config.ADSL_Store)

ProcessedCount = 0

for filename in os.listdir(image_Source_Directory):

    if ProcessedCount == Batchsize:
                 
        for zone in LDP_Zones:
            print('#### Calling LDP Repair for ' + zone['SRC-Zone'] + ' from host ' + zone['Host'])
            url = "http://"+ zone['Host'] + ":8082/fusion/fs/repair?path=" + zone['Path'] + "&recursive=true&src=" + zone['SRC-Zone'] + "&preserve=true&replace=true&repair=true&type=cc&nonBlocking=true"
            payload={}
            headers = {}
            response = requests.request("PUT", url, headers=headers, data=payload)
            print("Status: " + str(response.status_code))
            print(response.text)
        
        time.sleep(60)
        ProcessedCount = 0

    elif ProcessedCount < Batchsize:
        print('=====================================================================================')
        print('==== Uploading Data to ADLS Batch Size: ' + str(Batchsize) + ' FILE: ' + filename)
        print('=====================================================================================')   
        print('')  
        image_Source_Directory + filename
        img_full = image_Source_Directory + filename
        adl.put(img_full,ADLS_Path + filename)
        ProcessedCount = ProcessedCount + 1






