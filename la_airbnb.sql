SAVEPOINT "RESTOREPOINT";

/* identify which neighborhoods in neighbourhoods table are not a city in regions table */
SELECT COUNT(*) FROM (SELECT * FROM neighbourhoods
LEFT JOIN regions on neighbourhoods.neighbourhood = regions.City
WHERE Region is NULL);
SELECT * FROM neighbourhoods
LEFT JOIN regions on neighbourhoods.neighbourhood = regions.City
WHERE Region is NULL LIMIT 0, 49999;

ROLLBACK TO SAVEPOINT "RESTOREPOINT";
PRAGMA database_list;

/* found two neighbourhoods not in the regions table: East Whittier and La Canada Flintridge. In 2012, East Whittier was changed from East La Mirada (which is in the regions table). La Canada Flintridge was not joined due to spelling differences in the neighbourhoods and regions table (one N had a tilde and other did not). */


/* added East Whittier in the regions table with the region of "Southeast". changed the spelling of the La Canada Flintridge in the regions table to not have a tilde to match the spelling in the neighbourhoods table */
SELECT type,name,sql,tbl_name FROM "main".sqlite_master;
RELEASE "RESTOREPOINT";
PRAGMA database_list;
SELECT type,name,sql,tbl_name FROM "main".sqlite_master;
SELECT COUNT(*) FROM "main"."calendar"
SELECT "_rowid_",* FROM "main"."calendar" LIMIT 0, 49999;
PRAGMA database_list;
SELECT type,name,sql,tbl_name FROM "main".sqlite_master;
SELECT COUNT(*) FROM "main"."regions"
SELECT "_rowid_",* FROM "main"."regions" LIMIT 0, 49999;
SAVEPOINT "RESTOREPOINT";
UPDATE "main"."regions" SET "City"=? WHERE "_rowid_"='115'
INSERT INTO "main"."regions"("City","Region") VALUES (NULL,NULL);
UPDATE "main"."regions" SET "City"=? WHERE "_rowid_"='273'
UPDATE "main"."regions" SET "Region"=? WHERE "_rowid_"='273'


/* repeated to query to re-check that all the neighbourhoods in neighbourhoods table is also in the regions table */
SELECT COUNT(*) FROM (SELECT * FROM neighbourhoods
LEFT JOIN regions on neighbourhoods.neighbourhood = regions.City
WHERE Region is NULL);
SELECT * FROM neighbourhoods
LEFT JOIN regions on neighbourhoods.neighbourhood = regions.City
WHERE Region is NULL LIMIT 0, 49999;
