---
id: 236eb80f-8708-4902-afa6-0f3c58fda08b
name: Connect-to-RDS-MySQL-with-IAM-Token
type: command
executor: bash
data: >-
  mysql -h $_RDS_HOSTNAME -u $_DB_USERNAME -P $_RDS_PORT
  --enable-cleartext-plugin --password=$TOKEN
output: null
created_at: '2023-04-06T03:56:14.073876+00:00'
updated_at: '2023-04-10T20:20:55.168825+00:00'
platforms:
  - AWS
  - Linux
tags:
  - mysql
  - rds
  - connection
verified: true
validated: true
---

# Connect-to-RDS-MySQL-with-IAM-Token

## Command

```bash
mysql -h $_RDS_HOSTNAME -u $_DB_USERNAME -P $_RDS_PORT --enable-cleartext-plugin --password=$TOKEN
```

## Description

This command establishes a connection to an RDS MySQL database using an IAM-generated authentication token as the password. It enables interactive access for querying or modifying data without static credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_RDS_HOSTNAME | The DB instance endpoint | Yes |
| $_DB_USERNAME | The database username | Yes |
| $_RDS_PORT | The connection port (default 3306) | Yes |
| $TOKEN | The IAM authentication token from generate-db-auth-token | Yes |
| -h | Specifies the hostname | Built-in |
| -u | Specifies the username | Built-in |
| -P | Specifies the port | Built-in |
| --enable-cleartext-plugin | Enables cleartext password transmission for token auth | Built-in |
| --password | Uses the token as password (no --user flag needed, as -u sets it) | Built-in |

## Examples

### Basic Usage

Assuming $TOKEN is set:
```bash
mysql -h mydb.abc123.us-east-1.rds.amazonaws.com -u dbuser -P 3306 --enable-cleartext-plugin --password=$TOKEN
```

### Advanced Usage

Connect and run a query inline:
```bash
mysql -h $_RDS_HOSTNAME -u $_DB_USERNAME -P $_RDS_PORT --enable-cleartext-plugin --password=$TOKEN -e "SHOW DATABASES;"
```

## Expected Output

Successful connection shows the MySQL prompt:
```
mysql> 
```
Followed by query results if executed. Errors include "ERROR 1045 (28000): Access denied" for invalid tokens or "ERROR 2026 (HY000): SSL connection error" for network/SSL issues.

## Related

- [[procedures/IAM-Authentication-for-RDS-MySQL-Database]]
- [[commands/Generate-RDS-DB-Auth-Token]]
