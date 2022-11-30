-- grant all privileges to a new user in Mysql

CREATE USER IF NOT EXISTS'user_0d_1'@'localhost' IDENTIFIED BY 'Mypass30@..';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
