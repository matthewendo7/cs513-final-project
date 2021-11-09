

/*  The following SQL statements were utilized in the Jupyter Notebook */

/* count the records in the listing table.  note that the listing table was created using df.to_sql from the pandas dataframe */
select count(*) from listings;

/* create regions table and count the records*/
CREATE TABLE  IF NOT EXISTS  regions (City, Region);
select count() from regions;

/* Check for null records in listings table */
select count() from listings where neighbourhood is null;
select count(*) from listings where neighbourhood_cleansed is null;

/* Examine some of the data */
select neighbourhood, neighbourhood_cleansed from listings limit 20;
select * from neighbourhoods limit 5;
select * from regions limit 3;

/* check for unmatched values in listings and regions */
SELECT COUNT(*) FROM (SELECT * FROM listings
LEFT JOIN regions on listings.neighbourhood_cleansed = regions.City
WHERE Region is NULL);

/* Evaluate the unmatched values */
SELECT distinct listings.neighbourhood_cleansed, regions.city FROM listings
LEFT JOIN regions on listings.neighbourhood_cleansed = regions.City
WHERE Region is NULL LIMIT 0, 49999;
select city from regions where city like '%Flintridge';

/*  Add one missing value and update the other value */
INSERT into regions values ('East Whittier','Southeast');
update regions set city = 'La Canada Flintridge' where city like '%ada% Flint%';

/* Second validation */
SELECT COUNT(*) FROM (SELECT * FROM listings
LEFT JOIN regions on listings.neighbourhood_cleansed = regions.City
WHERE Region is NULL);
select * from regions where city like '%ada% Flint%';

/* convert price to a numeric field */
select count(*) from listings where price is null;
alter table listings add column price_num number;
select  cast(replace(replace(price,'$',''), ',','') as number) from listings limit 3;
update listings set price_num = cast(replace(replace(price,'$',''), ',','') as number) ;
select price, price_num from listings limit 10;
select min(price_num), max(price_num) from listings;
select count(*) from listings where price_num = 0;
select price, neighbourhood_cleansed, room_type, property_type from listings where price_num =0  limit 5
select price, neighbourhood_cleansed, room_type, property_type from listings order by price_num desc limit 5
select price_num from listings;


/* Check for missing data in the columns we are interested in */
select count(*) from listings where review_scores_value is  null;
select review_scores_value from listings where review_scores_value is not null;
select count(*) from listings where review_scores_value =0;
select count(*) from listings where room_type is  null;
select count(), room_type from listings group by room_type;
select distinct neighbourhood_cleansed from listings ;
select count(), neighbourhood_cleansed from listings group by neighbourhood_cleansed;
select count() from (select distinct region from regions);
select count(), neighbourhood_cleansed from listings group by neighbourhood_cleansed;

/* U1 analysis */
SELECT  round(avg(price_num),2) as avg_price, round(avg(review_scores_value),2) as avg_review_score, room_type ,region FROM listings
LEFT JOIN regions on listings.neighbourhood_cleansed = regions.City  where review_scores_value is not null and price_num > 0
group by room_type ,regions.region order by 1  desc
;
SELECT  round(avg(price_num),2) as avg_price, round(avg(review_scores_value),2) as avg_review_score, room_type ,region FROM listings
LEFT JOIN regions on listings.neighbourhood_cleansed = regions.City  where review_scores_value is not null and price_num > 0
group by room_type ,regions.region order by 2  desc
;

%%sql
SELECT  round(avg(price_num),2) as avg_price, round(avg(review_scores_value),2) as avg_review_score, region FROM listings
LEFT JOIN regions on listings.neighbourhood_cleansed = regions.City  where review_scores_value is not null and price_num > 0
group by regions.region order by 2 desc
;
SELECT  round(avg(price_num),2) as avg_price, round(avg(review_scores_value),2) as avg_review_score, region FROM listings
LEFT JOIN regions on listings.neighbourhood_cleansed = regions.City  where review_scores_value is not null and price_num > 0
group by regions.region order by 1  desc   
;
