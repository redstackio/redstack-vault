---
id: 236eb80f-8708-4902-afa6-0f3c58fda08b
name: mysql-connect-to-rds-instance
type: command
executor: bash
data: >-
  mysql -h $_RDS_ENDPOINT -u $_USERNAME -P $_PORT --enable-cleartext-plugin
  -p$_PASSWORD
output: null
created_at: '2023-04-06T03:56:14.073876+00:00'
updated_at: '2023-04-10T20:20:55.168825+00:00'
platforms:
  - Linux
tags:
  - database-access
  - exfiltration
verified: true
validated: true
---

# mysql-connect-to-rds-instance

## Command

```bash
mysql -h $_RDS_ENDPOINT -u $_USERNAME -P $_PORT --enable-cleartext-plugin -p$_PASSWORD
```

## Description

This command connects to an AWS RDS MySQL instance using the mysql client over TCP. It authenticates with a username and password, enabling interactive SQL execution for data access or exfiltration. The --enable-cleartext-plugin flag ensures compatibility with RDS auth plugins that require cleartext password handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -h $_RDS_ENDPOINT | RDS instance endpoint (e.g., mydb.123456789012.us-east-1.rds.amazonaws.com) | Yes |
| -u $_USERNAME | Database username with SELECT privileges | Yes |
| -P $_PORT | Connection port (default 3306 for MySQL) | Yes |
| --enable-cleartext-plugin | Enables cleartext password plugin for RDS compatibility | Yes (for certain auth setups) |
| -p$_PASSWORD | Password for the user (prompted if omitted, but use for scripting) | Yes |

## Examples

### Basic Usage

```bash
mysql -h mydb.us-east-1.rds.amazonaws.com -u dbuser -P 3306 --enable-cleartext-plugin -pMySecurePass
```

### Advanced Usage (with SSL, if enabled on RDS)

```bash
mysql -h $_RDS_ENDPOINT -u $_USERNAME -P $_PORT --enable-cleartext-plugin --ssl-mode=REQUIRED -p$_PASSWORD
```

## Expected Output

Upon success:
```
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 12345
Server version: 8.0.32

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```

Failure (invalid creds): "ERROR 1045 (28000): Access denied for user '$_USERNAME'@'$_CLIENT_IP' (using password: YES)".

## Related

- [[procedures/Exfiltrate-Data-from-AWS-RDS-via-Password-Authentication]]
