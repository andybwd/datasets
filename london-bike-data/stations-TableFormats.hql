
-- ### Managed Table ###  
CREATE TABLE IF NOT EXISTS lbd.stations
(StationID INT, Capacity INT, Latitude FLOAT,Longitude FLOAT, StationName STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE


-- ### Extenal Table ###  

CREATE EXTERNAL TABLE IF NOT EXISTS lbd_ext.stations
(StationID INT, Capacity INT, Latitude FLOAT,Longitude FLOAT, StationName STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 'hdfs:///user/vagrant/dataroot/lbd/data/stations';   --- placvfe a csv file in the follwing HDFS location containing some data 


-- #### ACID Table ###

CREATE TABLE IF NOT EXISTS lbd_acid.stations
(StationID INT, Capacity INT, Latitude FLOAT,Longitude FLOAT, StationName STRING)
STORED AS ORC
TBLPROPERTIES ('transactional'='true');


-- #### Single Line of data  ####

INSERT INTO stations  VALUES 
(1,19,51.529163,-0.10997,'River Street  Clerkenwell')



--- #### Some More Data ####
(2,37,51.499606,-0.197574,'Phillimore Gardens Kensington')
(3,32,51.521283,-0.084605,'Christopher Street Liverpool Street')
(4,23,51.530059,-0.120973,'St. Chad's Street King's Cross')
(5,27,51.49313,-0.156876,'Sedding Street Sloane Square')
(6,18,51.518117,-0.144228,'Broadcasting House Marylebone')
(7,16,51.5343,-0.168074,'Charlbert Street St. John's Wood')
(8,18,51.528341,-0.170134,'Lodge Road St. John's Wood')
(9,19,51.507385,-0.09644,'New Globe Walk Bankside')
(10,18,51.505974,-0.092754,'Park Street Bankside')
(11,24,51.523951,-0.122502,'Brunswick Square Bloomsbury')
(12,49,51.52168,-0.130431,'Malet Street Bloomsbury')
(13,21,51.519914,-0.136039,'Scala Street Fitzrovia')
(14,48,51.529943,-0.123616,'Belgrove Street  King's Cross')
(15,26,51.517727,-0.127854,'Great Russell Street Bloomsbury')
(16,22,51.526357,-0.125979,'Cartwright Gardens  Bloomsbury')
(17,26,51.521661,-0.109006,'Hatton Wall Holborn')
(18,27,51.51477,-0.122219,'Drury Lane Covent Garden')
(19,30,51.52505,-0.131161,'Taviton Street Bloomsbury')
(20,28,51.527736,-0.135273,'Drummond Street  Euston')
