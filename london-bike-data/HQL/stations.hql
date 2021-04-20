CREATE EXTERNAL TABLE IF NOT EXISTS lbd.stations
(StationID INT, Capacity INT, Latitude FLOAT,Longitude FLOAT, StationName STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 'hdfs:///user/vagrant/dataroot/lbs/data/stations';