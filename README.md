# Test Datasets
Datasets for use with stuff 

### London Bike data


#### Content
A 36-day record of journeys made from 1 August to 13 September 2017 in London bike sharing system were recorded. During this period, there were >1.5 million journeys made among >700 bike docking stations in London.

##### Setup Instuctions

#### HIVE/HDFS

1. ###### HDFS Paths 
   Create the follwing HDFS Folder in your HDFS (replace **PATH** with your HDFS location) 

    /PATH/lbd/stations
    /PATH/lbd/journeys

2. ###### Create Database 
    Using your preferred client connect to HS2 and run the following 

    CREATE DATABASE londonbikedata;

3. ###### Create Tables 
    using your preferred client connect to HS2 and run the HQL from both stations.hql and    journeys.hql (remember to adjust the location to your HDFS paths or remove if not required)

4. ###### Station Data
    copy the staiions.csv into the HDFS Path created in step 1 /PATH/lbd/stations

5. ###### Adding journeys Data
    There are 3 csv files containing journey data journeys-1.csv containing a single row journeys-2.csv containing two additional rows and journeys-15.csv containing around 1.5Million additional rows. 
    These CSV’s can be copied into the path created in step 1     /PATH/lbd/journeys. Individually and you should be able to query using your HS2 client to see data being added.  


__Source:__ https://www.kaggle.com/edenau/london-bike-sharing-system-data
__Licence:__ CC BY-NC-SA 4.0
