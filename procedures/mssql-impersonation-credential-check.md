---
id: 175a4922-2470-4c4c-91df-1caf4ee8f1f8
name: mssql-impersonation-credential-check
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.044509+00:00'
updated_at: '2023-04-10T20:36:37.172560+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - >-
    [[techniques/Permission Groups Discovery|T1069 - Permission Groups
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Exploiting Impersonation]]'
  - '[[tags/Manual SQL Server Queries]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/mssql-select-system-user]]'
  - '[[commands/mssql-select-is-srvrolemember-sysadmin]]'
  - '[[commands/mssql-execute-as-login]]'
  - '[[commands/mssql-select-original-login]]'
platforms:
  - Windows
tools: []
validated: true
---

# mssql-impersonation-credential-check

## Summary

The MSSQL Impersonation Credential Check procedure exploits SQL Server's EXECUTE AS LOGIN feature to impersonate a target login, verify current and impersonated system user identities, check membership in the sysadmin server role, and retrieve the original login context. This allows attackers with initial SQL access to discover account details, assess privilege levels, and potentially identify paths for privilege escalation without directly dumping credentials.

## Description

In Microsoft SQL Server environments, the EXECUTE AS LOGIN statement enables context switching to another login's security context, provided the current user has IMPERSONATE permissions on the target login. This procedure demonstrates how to use a series of SQL queries to inspect the current authentication context before and after impersonation, including role membership checks via IS_SRVROLEMEMBER. It is typically used in post-exploitation scenarios where an attacker has low-privileged SQL access and seeks to map out administrative accounts or confirm elevated privileges. The target environment is a Windows-based SQL Server instance (e.g., on-premises or Azure SQL). Success reveals whether the impersonated login has sysadmin rights, aiding in lateral movement or persistence planning. Note that this does not extract plaintext credentials but provides discovery of user and role information.

## Requirements

1. Valid SQL Server login credentials with execute permissions on the database.
2. IMPERSONATE permission on the target login (e.g., 'adminuser').
3. Access to a SQL Server Management Studio (SSMS) or sqlcmd tool for query execution.
4. Target SQL Server instance running on Windows with domain-integrated or SQL authentication enabled.

## Defense

Defensive measures and detection strategies:

- Enforce principle of least privilege by revoking unnecessary IMPERSONATE permissions from non-administrative logins.
- Enable SQL Server Audit for EXECUTE AS events and monitor for anomalous impersonation attempts via SQL logs or Extended Events.
- Implement multi-factor authentication (MFA) for SQL logins and regularly audit server role memberships.
- Use database activity monitoring (DAM) tools to alert on queries involving SYSTEM_USER, IS_SRVROLEMEMBER, or ORIGINAL_LOGIN.

## Objectives

1. Identify the current system user and sysadmin role membership.
2. Impersonate a target login to assess its privileges.
3. Verify the original login context post-impersonation to maintain awareness of the security boundary.
4. Detect potential privilege escalation opportunities through role discovery.

## Instructions

Execute the following steps in sequence within a SQL Server query window (e.g., SSMS) or via sqlcmd. Replace placeholders like the target login name as needed. For the full scripted version, refer to [[codes/mssql-impersonation-credential-check-script]].

### Step 1: Query Current System User

**Context**: This step retrieves the current system user under which the SQL session is running, providing baseline authentication context. This helps confirm initial access level before attempting impersonation.

**Command** ([[commands/mssql-select-system-user]]):
```sql
SELECT SYSTEM_USER;
```

> The SYSTEM_USER function returns the login name used to connect to the instance. If successful, it displays the current login without errors.

### Step 2: Check Current Sysadmin Role Membership

**Context**: Verify if the current user belongs to the sysadmin server role, which grants full control over the SQL instance. This informs whether initial access already provides elevated privileges.

**Command** ([[commands/mssql-select-is-srvrolemember-sysadmin]]):
```sql
SELECT IS_SRVROLEMEMBER('sysadmin');
```

> IS_SRVROLEMEMBER returns 1 if the user is a member, 0 if not, or NULL if unknown. Expect a numeric result indicating membership status.

### Step 3: Impersonate Target Login

**Context**: Switch the execution context to the specified login (e.g., 'adminuser') to simulate actions under its privileges. This requires IMPERSONATE permission; failure indicates insufficient rights.

**Command** ([[commands/mssql-execute-as-login]]):
```sql
EXECUTE AS LOGIN = '$_TARGET_LOGIN';
```

> The EXECUTE AS LOGIN statement changes the context for subsequent queries. On success, no output is returned, but errors like 'The impersonate permission was denied' will appear if permissions are lacking.

### Step 4: Query System User After Impersonation

**Context**: After switching context, re-query the system user to confirm the impersonation took effect and identify the assumed identity.

**Command** ([[commands/mssql-select-system-user]]):
```sql
SELECT SYSTEM_USER;
```

> Expect the output to show the target login (e.g., 'adminuser') instead of the original user, confirming successful context switch.

### Step 5: Check Sysadmin Role Membership After Impersonation

**Context**: Assess if the impersonated login has sysadmin privileges, revealing potential escalation value.

**Command** ([[commands/mssql-select-is-srvrolemember-sysadmin]]):
```sql
SELECT IS_SRVROLEMEMBER('sysadmin');
```

> Returns 1 if the impersonated user is sysadmin, indicating high privileges available under this context.

### Step 6: Retrieve Original Login and Revert Context

**Context**: Query the original login to track the session's root identity, then implicitly revert (or explicitly use REVERT if needed) to return to the original context. This prevents lingering impersonation.

**Command** ([[commands/mssql-select-original-login]]):
```sql
SELECT ORIGINAL_LOGIN();
```

> ORIGINAL_LOGIN returns the login used to initially connect. After this, execute `REVERT;` (not shown in base script) to end impersonation. Success shows the initial login name.
