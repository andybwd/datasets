CREATE EXTERNAL TABLE IF NOT EXISTS londonbikedata.journeys
(JourneyDuration INT,JourneyID INT,EndDate INT,EndMonth INT,EndYear INT,EndHour INT,EndMinute INT,EndStationID INT,StartDate INT,StartMonth INT,StartYear INT,StartHour INT,StartMinute INT,StartStationID INT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 'hdfs://FULLPATH-TO-ROOT-OF-FOLDER/journeys';