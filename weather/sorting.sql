select * from Weather order by id desc ;

select DISTINCT cityname, citycode from Weather where  cityname in ('Moscow', 'Johannesburg', 'Phuket',
 'Shanghai', 'Hong Kong', 'Seoul', 'Tokyo', 'Osaka', 'Singapore', 
 'Sydney', 'London', 'Brussels', 'Dublin', 'Budapest', 'Cape Town', 
 'Mexico City', 'Cancun', 'Chicago', 'Los Angeles', 'Ottawa', 'Toronto',
 'Marrakech', 'New York');
 
