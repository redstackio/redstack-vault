---
tags:
  - mysql
  - protocol-analysis
  - tcpdump
type: procedure
tools:
  - '[[tools/tcpdump]]'
  - '[[tools/mysql-client]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/load-data-local-infile-query]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:28:20.389Z'
sub_techniques: []
id: fa82de93-79f2-4002-88aa-44e487cb0024
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze MySQL LOAD DATA LOCAL INFILE Protocol with tcpdump

## Summary

This procedure sets up a controlled environment to test and analyze the normal behavior of MySQL's LOAD DATA LOCAL INFILE function, capturing network traffic to reveal the protocol's response mechanism.

## Description

In a testing setup, a local MySQL server is started, and traffic is captured using tcpdump while executing a LOAD DATA LOCAL INFILE query via the native mysql client. This reveals the server's 'FB' packet response echoing the filename, which is the root of the vulnerability. The procedure is essential for understanding how the client is tricked into local file reads during exploitation.

## Requirements

1. Local MySQL or MariaDB server installed and running
2. tcpdump installed for packet capture
3. mysql client available
4. A test table 'pwn' created in the database

## Defense

Defensive measures and detection strategies:

- Disable LOAD DATA LOCAL INFILE in client configurations (e.g., --local-infile=0)
- Monitor unusual MySQL connections and protocol anomalies with network IDS like Snort
- Use WAF to block arbitrary server connections in admin interfaces

## Objectives

1. Capture baseline traffic for LOAD DATA LOCAL INFILE
2. Identify server response patterns
3. Validate protocol behavior for exploitation planning

## Instructions

### Step 1: Start MySQL Server and Capture Traffic

**Context**: Launch the local MySQL server and begin packet capture on the relevant interface.

**Command** ([[commands/load-data-local-infile-query]]):
```bash
mysql -u root -p -e "CREATE TABLE IF NOT EXISTS pwn (data TEXT);"
```

> This creates the target table. Then run tcpdump: `tcpdump -i lo -w mysql_traffic.pcap port 3306` to capture on localhost.

### Step 2: Execute LOAD DATA Query

**Context**: Connect with mysql client and run the query to trigger the protocol response.

**Command** ([[commands/load-data-local-infile-query]]):
```sql
LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE pwn FIELDS TERMINATED BY '\n'
```

> Expected output: File contents inserted into 'pwn' table. Stop tcpdump after execution.

### Step 3: Verify Capture

**Context**: Ensure traffic was captured successfully.

**Command**:
```bash
tcpdump -r mysql_traffic.pcap -X | grep -i load
```

> Confirms query and response packets are present.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/load-data-local-infile-query]]

## Tools Used

- [[tools/tcpdump]]
- [[tools/mysql-client]]

## Tags

- mysql
- protocol-analysis
- tcpdump
