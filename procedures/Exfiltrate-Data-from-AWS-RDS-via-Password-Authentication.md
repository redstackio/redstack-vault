---
id: cbc9a144-243d-4a29-8761-2c557cda1c30
name: Exfiltrate-Data-from-AWS-RDS-via-Password-Authentication
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.017071+00:00'
updated_at: '2023-04-10T20:20:30.249176+00:00'
tactics:
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
sub_techniques:
  - >-
    [[sub-techniques/Exfiltration Over Unencrypted Non-C2 Protocol|T1048.003 -
    Exfiltration Over Unencrypted Non-C2 Protocol]]
tags:
  - '[[tags/data-exfiltration]]'
  - '[[tags/password-based-authentication]]'
  - '[[tags/aws-rds]]'
commands:
  - '[[commands/mysql-connect-to-rds-instance]]'
platforms:
  - AWS
  - Linux
tools: []
validated: true
---

# Exfiltrate-Data-from-AWS-RDS-via-Password-Authentication

## Summary

This procedure demonstrates how an attacker with valid credentials can connect to an AWS RDS MySQL instance using password-based authentication and exfiltrate sensitive data via SQL queries. It covers establishing a connection and executing queries to dump database contents, such as user tables or configuration data, over the unencrypted MySQL protocol.

## Description

AWS RDS (Relational Database Service) is a managed database offering that supports MySQL, PostgreSQL, and other engines. In scenarios where password-based authentication is enabled without additional controls like IAM database authentication or network restrictions, an attacker with stolen or weak credentials can directly connect to the RDS endpoint. Once connected, the attacker executes SELECT queries to retrieve data, which can be piped to files for offline analysis or exfiltrated via other channels. This technique leverages the MySQL client for remote access and is particularly effective in environments with exposed RDS instances or compromised AWS credentials granting DB access. The procedure assumes TCP access to the RDS port (default 3306) and focuses on MySQL as the engine, though adaptable to others.

## Requirements

1. Valid RDS database username and password (password-based authentication enabled on the instance).
2. Network access to the RDS endpoint (e.g., public subnet or VPC peering; port 3306 open).
3. MySQL client installed on the attacker's machine (e.g., via apt on Linux).
4. Knowledge of the target database schema to craft effective queries (e.g., table names like 'users' or 'secrets').

## Defense

- Enable IAM database authentication instead of password-based to reduce credential exposure.
- Encrypt data at rest and in transit using TLS for RDS connections to prevent cleartext exfiltration.
- Implement network-level controls like security groups, NACLs, or VPC endpoints to restrict access to trusted IPs.
- Monitor RDS logs for unusual queries (e.g., large SELECT statements) and enable CloudTrail for credential usage auditing.
- Use database firewalls or tools like AWS GuardDuty to detect anomalous access patterns.

## Objectives

1. Establish a secure connection to the RDS MySQL instance using provided credentials.
2. Execute SQL queries to identify and extract sensitive data from target tables.
3. Exfiltrate the retrieved data without triggering immediate alerts, maintaining stealth.

## Instructions

### Step 1: Connect to the RDS MySQL Instance

**Context**: Begin by using the MySQL client to authenticate and establish a session with the RDS instance. This step verifies credential validity and grants interactive access to the database. Replace placeholders with actual RDS endpoint, port, username, and password. For RDS with certain auth plugins, include the --enable-cleartext-plugin flag to handle password transmission.

**Command** ([[commands/mysql-connect-to-rds-instance]]):
```bash
mysql -h $_RDS_ENDPOINT -u $_USERNAME -P $_PORT --enable-cleartext-plugin -p$_PASSWORD
```

> This command initiates a TCP connection to the RDS MySQL server. Upon success, you enter the MySQL prompt (mysql>). If credentials are invalid, it returns an access denied error. At the prompt, you can now run SQL commands.

### Step 2: Enumerate Database Schema

**Context**: Once connected, query the information_schema to discover available databases, tables, and columns. This reconnaissance helps identify targets for exfiltration without prior knowledge of the schema, reducing trial-and-error that might trigger logging.

**Command**:
```sql
SHOW DATABASES;
USE information_schema;
SELECT TABLE_NAME, COLUMN_NAME FROM COLUMNS WHERE TABLE_SCHEMA = '$_TARGET_DB';
```

> Expected output includes a list of databases (e.g., 'mydb', 'users_db') and table details (e.g., 'users' table with 'username', 'password_hash' columns). Note the target database name for the next step. Exit with errors if insufficient privileges.

### Step 3: Exfiltrate Sensitive Data

**Context**: Switch to the target database and execute SELECT queries to dump data. For large datasets, use LIMIT or INTO OUTFILE (if file privileges allow) to export to a file on the RDS instance, then retrieve it separately. Pipe output to a local file for immediate exfiltration.

**Command**:
```sql
USE $_TARGET_DB;
SELECT * FROM users LIMIT 100;
-- Or for export: SELECT * FROM secrets INTO OUTFILE '/tmp/secrets.txt';
```

> Successful queries return rows of data (e.g., usernames, emails, or API keys). For INTO OUTFILE, confirm file creation with SHOW VARIABLES LIKE 'secure_file_priv'; to ensure the path is allowed. Redirect MySQL output to a file on your machine: mysql ... > exfil_data.txt. Look for complete rows without truncation.
