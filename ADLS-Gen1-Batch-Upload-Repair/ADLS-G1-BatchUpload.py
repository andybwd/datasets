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


ProcessedCount = 0
batchCount = 0
tgtPath = ADLS_Path + '/' + dataRoot +'/'
totalFileProcessCount = 0

for filename in os.listdir(image_Source_Directory):
    
    
    if batchCount == 0:
        batchCount = batchCount + 1
        batchPath = tgtPath + batchName + '-' + str(batchCount)   
        adl.mkdir(batchPath)

    if ProcessedCount == Batchsize:
                 
        time.sleep(5)
        ProcessedCount = 0
        batchCount = batchCount + 1
        batchPath = tgtPath + batchName + '-' + str(batchCount)   
        adl.mkdir(batchPath)

        image_Source_Directory + filename
        img_full = image_Source_Directory + filename
        adl.put(img_full,batchPath + '/' + filename)
        
        ProcessedCount = ProcessedCount + 1

    elif ProcessedCount < Batchsize:
        batchTotal = maxProcessCount / Batchsize
        print('===================================================================================================================')
        print('==== Uploading Data to ADLS Batch Size: ' + str(Batchsize) + ' FILE: ' + filename + ' Total Files: ' + str(maxProcessCount) + ' in ' + str(batchTotal) + ' Batchs')
        print('===================================================================================================================')   
        print('')  
     
        image_Source_Directory + filename
        img_full = image_Source_Directory + filename
        adl.put(img_full,batchPath + '/' + filename)
        
        ProcessedCount = ProcessedCount + 1

    totalFileProcessCount = totalFileProcessCount + 1

    if totalFileProcessCount == maxProcessCount:
        break




