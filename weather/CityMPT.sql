select * from Airport;

select distinct(cityname) from Airport;


# LONDON 2643743

select * from Country;
select * from City;

select * from City where citycode = 2643743;

select c.* from Airport a inner join City c 
on a.cityname = c.cityname and a.countrycode = c.countrycode;


select min(mpt_citycode) ,max(mpt_cityname),max(mpt_countrycode), count(*) from CityMPT 
group by mpt_countrycode, mpt_cityname having count(*) > 1;



select * from CityMPT;


insert into CityMPT(mpt_citycode, mpt_cityname, mpt_countrycode) 
select c.* from Airport a inner join City c 
on a.cityname = c.cityname and a.countrycode = c.countrycode
on duplicate key update mpt_citycode = mpt_citycode;

select * from CityMPT order by mpt_countrycode;

select * from Airport;


CREATE TABLE `Temp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mpt_citycode` int(11) DEFAULT NULL,
  `mpt_cityname` varchar(45) DEFAULT NULL,
  `mpt_countrycode` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mpt_citycode_UNIQUE` (`mpt_citycode`)
) ENGINE=InnoDB AUTO_INCREMENT=1042 DEFAULT CHARSET=utf8;


select * from Temp; # 134

select min(mpt_citycode) ,max(mpt_cityname),max(mpt_countrycode) from CityMPT 
group by mpt_countrycode, mpt_cityname having count(*) > 1;


insert into Temp(mpt_citycode, mpt_cityname, mpt_countrycode) 
select min(mpt_citycode) ,max(mpt_cityname),max(mpt_countrycode) from CityMPT 
group by mpt_countrycode, mpt_cityname having count(*) > 1
on duplicate key update mpt_citycode = mpt_citycode;

select * from Temp;

select sum(cnt) from (
select mpt_countrycode, mpt_cityname, count(*) cnt from CityMPT 
group by mpt_countrycode, mpt_cityname having count(*) > 1) s; #count sum = 425

select mpt_countrycode, mpt_cityname from CityMPT 
group by mpt_countrycode, mpt_cityname having count(*) > 1; #134

select mpt_countrycode, mpt_cityname from Temp
group by mpt_countrycode, mpt_cityname;

delete from CityMPT where (mpt_countrycode, mpt_cityname) in
(select mpt_countrycode, mpt_cityname from Temp
group by mpt_countrycode, mpt_cityname); # 425 row affected = success


select * from CityMPT;
select * from Temp;











