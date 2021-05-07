import os
import sys
import time
import requests
from azure.datalake.store import core, lib
import config

####################################################
####            Configure Me
####################################################
#Sorce Files (could be anuting just as long as its a flat stucture no sub folders)
image_Source_Directory = "D:\\tmp\\cars_test\\"

#Number Of Files Per Directory 
Batchsize = 10
#Total Number Of Files To Upload
maxProcessCount = 40

#Data Root Inside ADLS Root
dataRoot = 'cars'
#Batch Folder Name
batchName = 'Batch'
#fusion API Host
wDFusionAPIHost = 'abarb01-vm0.bdfrem.wandisco.com'

## ADLS Settings Stored in config.py
ADLS_Path = config.ADLS_Path
ADLS_Azure_TenentID = config.ADLS_Azure_TenentID
ADLS_cleint_id = config.ADLS_cleint_id
ADSL_Store = config.ADSL_Store
ADLS_cleint_Secret = config.ADLS_cleint_Secret

#################################################################
# Connect to ADLS using service principal authentication
# Store tenant_id, client_id and client_secret in a separate confguration file. 

token = lib.auth(tenant_id = ADLS_Azure_TenentID,
                 client_id = ADLS_cleint_id,
                 client_secret = ADLS_cleint_Secret)

# Get file system like object from ADLS
adl = core.AzureDLFileSystem(token, store_name=config.ADSL_Store)

targetDir = ADLS_Path + '/cars'
dirs = adl.ls(targetDir)

url = 'http://' + wDFusionAPIHost +':8082/fusion/fs/deployReplicatedRule'

for dir in dirs:
    shortPath = dir.replace(ADLS_Path,'/',1)

    print(shortPath)

    pName = shortPath.replace('/', ' ')
    pName.strip()
    pSrcPath = shortPath
    pTarPath = shortPath
    
    payload = '''<deployReplicatedDirectory>\n  
                    <replicatedPathName>{0}</replicatedPathName>\n
                        <mappings>\n    
                            <mapping>\n
                                <zoneId>ABA-LDP-ADLS-G1-002</zoneId>\n      
                                <location>{1}</location>\n   
                            </mapping>\n   
                            <mapping>\n     
                                <zoneId>ABA-LDP-ADLS-G1-001</zoneId>\n      
                                <location>{2}</location>\n   
                            </mapping>\n  
                        </mappings>\n  
                    <preferredZone>ABA-LDP-ADLS-G1-001</preferredZone>\n
                </deployReplicatedDirectory>
    '''    
    headers = {
    'Content-Type': 'application/xml'
    }   
    #print()
    response = requests.request("POST", url, headers=headers, data=payload.format(pName,pSrcPath,pTarPath))

    print(response.status_code)


