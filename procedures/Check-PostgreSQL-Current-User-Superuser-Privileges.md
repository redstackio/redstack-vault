---
id: 522e4e4a-1179-4c9a-b378-ddfe0ce73e86
name: Check-PostgreSQL-Current-User-Superuser-Privileges
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.603271+00:00'
updated_at: '2023-04-10T20:23:22.107218+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Permission Groups Discovery|T1069 - Permission Groups
    Discovery]]
sub_techniques: []
tags:
  - postgresql
  - superuser
  - privileges
  - database-discovery
commands:
  - '[[commands/show-is-superuser]]'
  - '[[commands/select-current-setting-is-superuser]]'
  - '[[commands/select-usesuper-from-pg-user-current-user]]'
platforms:
  - Linux
  - Database
tools: []
validated: true
---

# Check-PostgreSQL-Current-User-Superuser-Privileges

## Summary

This procedure determines if the current user in a PostgreSQL database has superuser privileges by executing specific SQL queries. Superuser status grants full administrative control, allowing operations like creating databases, modifying system settings, and bypassing restrictions, which is critical for assessing privilege escalation potential in penetration testing or post-exploitation scenarios.

## Description

In a PostgreSQL environment, verifying superuser privileges is a key discovery step after gaining initial database access, such as through SQL injection or valid credentials. This procedure uses built-in PostgreSQL functions and system tables to query the current user's permissions without requiring additional tools. It is particularly useful in scenarios where an attacker has limited shell access but can execute SQL commands, helping to identify if escalation to full database control is possible. The technique relies on direct queries to pg_user and configuration settings, assuming the attacker is already authenticated to the database session. Success enables further actions like data exfiltration or lateral movement within the database server.

## Requirements

1. Valid database connection to the PostgreSQL instance (e.g., via psql client or application-level access).
2. Ability to execute SELECT queries and SHOW commands in the current session.
3. Network access to the PostgreSQL port (default 5432) if connecting remotely.

## Defense

Defensive measures and detection strategies:

- Implement least privilege principles by avoiding superuser assignments to application accounts.
- Enable query logging in PostgreSQL (log_statement = 'all') to monitor privilege checks.
- Use database firewalls or row-level security to restrict access to system tables like pg_user.
- Regularly audit user roles and revoke unnecessary superuser grants.

## Objectives

1. Confirm if the current PostgreSQL user has superuser capabilities.
2. Identify potential for privilege escalation if superuser status is present.
3. Gather intelligence on database permissions for further exploitation planning.

## Instructions

### Step 1: Query Superuser Status Using SHOW Command

**Context**: This step uses the built-in SHOW command to directly display the is_superuser setting for the current session, providing a quick boolean indicator of superuser privileges.

**Command** ([[commands/show-is-superuser]]):
```sql
SHOW is_superuser;
```

> This command queries the session's superuser configuration. It is the simplest method and requires no additional permissions beyond basic connectivity. Run it first to get an immediate yes/no response.

### Step 2: Check Superuser Setting via Current Configuration

**Context**: If the SHOW command is insufficient or for verification, this step retrieves the is_superuser value from the runtime configuration, confirming the privilege level programmatically.

**Command** ([[commands/select-current-setting-is-superuser]]):
```sql
SELECT current_setting('is_superuser');
```

> This SELECT statement accesses the current session's GUC (Grand Unified Configuration) settings. It returns a string value, allowing for scripting or integration into larger queries. Use this if you need the output in a format suitable for parsing.

### Step 3: Verify Superuser Attribute in System Catalog

**Context**: For a deeper check, query the pg_user system table to examine the usesuper attribute of the current user, providing insight into role-based permissions.

**Command** ([[commands/select-usesuper-from-pg-user-current-user]]):
```sql
SELECT usesuper FROM pg_user WHERE usename = CURRENT_USER;
```

> This query directly inspects the PostgreSQL catalog for the current user's superuser flag. It requires SELECT access to pg_user (typically granted to all users) and confirms role membership. Cross-reference this with the previous steps for consistency; a value of 't' indicates superuser status.
