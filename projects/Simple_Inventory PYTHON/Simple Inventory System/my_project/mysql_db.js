drop database if exists inventory;
create database wpb_db CHARACTER SET utf8 COLLATE utf8_general_ci;
grant all on wpb_db.* to 'root'@'localhost' identified by 'root';
