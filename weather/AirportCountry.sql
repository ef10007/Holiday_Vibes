
select * from Country where countryname = 'Cape Verde';

update Country set countrycode = 'GB' where countrycode = 'UK';

insert into Country(countryname, countrycode) values('Cape Verde', 'CV');

insert into Country(countryname, countrycode) values('Mayotte', 'YT');

insert into Country(countryname, countrycode) values('Libya', 'LY');

insert into Country(countryname, countrycode) values('Monaco', 'MC');

insert into Country(countryname, countrycode) values('Samoa', 'WS');

select * from Country;


select * from Airport; # 577

select  a.*, c.countryname from Airport a left outer join Country c
on a.countrycode = c.countrycode; # 577


