select * from City ct inner join Country co 
on ct.countrycode = co.countrycode
where cityname in ('Moscow', 'Johannesburg', 'Phuket',
 'Shanghai', 'Hong Kong', 'Seoul', 'Tokyo', 'Osaka', 'Singapore', 
 'Sydney', 'London', 'Brussels', 'Dublin', 'Budapest', 'Cape Town', 
 'Mexico City', 'Cancun', 'Chicago', 'Los Angeles', 'Ottawa', 'Toronto',
 'Marrakech', 'New York');
 
 select * from Temp1 group by countryname, where count(countryname) > 1;

 
insert into Temp1(cityname, countryname) 
select ct.cityname, co.countryname from City ct inner join Country co 
on ct.countrycode = co.countrycode
where cityname in ('Moscow', 'Johannesburg', 'Phuket',
 'Shanghai', 'Hong Kong', 'Seoul', 'Tokyo', 'Osaka', 'Singapore', 
 'Sydney', 'London', 'Brussels', 'Dublin', 'Budapest', 'Cape Town', 
 'Mexico City', 'Cancun', 'Chicago', 'Los Angeles', 'Ottawa', 'Toronto',
 'Marrakech', 'New York');
 

select * from Country;

 select * from Temp1 group by countryname, where count(countryname) > 1;


