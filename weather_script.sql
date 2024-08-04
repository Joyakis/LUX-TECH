-- Select all records where the weather is clear
select * from weather_data wd 
where Weather_Condition = 'clear';
-- Select occurences where wind speed was exactly 4km/hr
select * from weather_data wd 
where `Wind Speed_km/h` ='4km/hr';
# select records of specific wind speeed and visibility values
SELECT COUNT(*) AS NumberOfRecords
FROM weather_data wd
WHERE `Wind Speed_km/h` > '24km/hr' AND Visibility_km = '25km';
#grouping by weather condition then finding the mean of numerical columns
SELECT Weather_Condition,
       AVG(Temp_C) AS Avg_Temperature,
       AVG(`Wind Speed_km/h`) AS Avg_Wind_Speed,
       AVG(`Rel Hum_%`) as avg_hum,
       AVG(Visibility_km) AS Avg_Visibility,
       AVG(Press_kPa) as Avg_Press,
       AVG (`Dew Point Temp_C`) as Avg_dew
       
FROM weather_data
GROUP BY Weather_Condition;

