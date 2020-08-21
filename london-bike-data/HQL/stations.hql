CREATE EXTERNAL TABLE IF NOT EXISTS londonBikedata.stations
(StationID INT, Capacity INT, Latitude FLOAT,Longitude FLOAT, StationName STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 'hdfs://FULLPATH-TO-ROOT-OF-FOLDER/stations';