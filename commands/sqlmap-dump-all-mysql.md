---
id: 0b432b09-c424-4a72-a0bb-34e97a643b80
name: sqlmap-dump-all-mysql
type: command
executor: bash
data: 'sqlmap.py -d "mysql://user:pass@ip/database" --dump-all --batch'
output: null
created_at: '2023-04-06T03:56:36.526980+00:00'
updated_at: '2023-04-10T20:24:27.086249+00:00'
platforms:
  - Linux
tags:
  - sqlmap
  - database-dump
  - mysql
verified: true
validated: true
---

# sqlmap-dump-all-mysql

## Command

```bash
sqlmap.py -d "mysql://user:pass@ip/database" --dump-all --batch
```

## Description

This command uses SQLmap to directly connect to a MySQL database via a connection string and dump all tables and data to CSV files. It is ideal for post-credential scenarios where direct access is available, automating the extraction of database contents without web-based injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d "mysql://user:pass@ip/database" | Direct connection string specifying MySQL URI with credentials, host IP, and database name | Yes |
| --dump-all | Instructs SQLmap to retrieve and save all database tables' data | Yes |
| --batch | Runs in non-interactive mode, auto-accepting defaults to avoid prompts | No (recommended for automation) |
| user | Database username (e.g., root) | Yes |
| pass | Database password | Yes |
| ip | Target MySQL server IP or hostname | Yes |
| database | Name of the target database | Yes |

## Examples

### Basic Usage

```bash
sqlmap.py -d "mysql://root:admin123@192.168.1.100/webapp_db" --dump-all --batch
```

### Advanced Usage

```bash
sqlmap.py -d "mysql://root:admin123@192.168.1.100/webapp_db" --dump-all --batch --threads=5 --dbms=mysql
```

(Adds multi-threading for speed and explicit DBMS specification.)

## Expected Output

The command outputs progress logs to the terminal, such as:

```
[INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
[INFO] fetching database names
available databases [2]:
[*] information_schema
[*] webapp_db
[INFO] fetching tables for database: 'webapp_db'
Database: webapp_db (5 tables)
+------------+
| users      |
| products   |
| orders     |
| sessions   |
| logs       |
+------------+
[INFO] table 'users' dumped to CSV file '/root/.sqlmap/output/192.168.1.100/dump/webapp_db/users.csv'
[INFO] finished in X seconds
```

Success is indicated by CSV files in the output directory containing table data, e.g., users.csv with rows like:

```
id,username,password,email
1,jdoe,hashedpass,jdoe@example.com
```

## Related

- [[procedures/Dump-MySQL-Database-Using-SQLmap]]
- [[tools/sqlmap]]
