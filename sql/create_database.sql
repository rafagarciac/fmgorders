/*
This file is used to bootstrap development database.

Note: ONLY development database;
*/

CREATE USER 'fmgorders'@'localhost' IDENTIFIED BY 'fmgorders_pass';
CREATE DATABASE fmgorders;
GRANT ALL PRIVILEGES ON fmgorders.* TO 'fmgorders'@'localhost' WITH GRANT OPTION;
