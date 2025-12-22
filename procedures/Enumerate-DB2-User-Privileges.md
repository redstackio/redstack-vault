---
id: 576ef785-2ab8-4a3f-8693-34b073c1dac9
name: Enumerate-DB2-User-Privileges
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.661596+00:00'
updated_at: '2023-04-10T20:22:04.091905+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - >-
    [[techniques/Permission Groups Discovery|T1069 - Permission Groups
    Discovery]]
sub_techniques: []
tags:
  - db2
  - privilege-enumeration
  - database
  - list-privileges
commands:
  - '[[commands/db2-list-system-privileges]]'
  - '[[commands/db2-show-current-user-table-privileges]]'
  - '[[commands/db2-show-current-user-database-privileges]]'
  - '[[commands/db2-list-table-privileges]]'
platforms:
  - Linux
  - Windows
tools: []
validated: true
---

# Enumerate-DB2-User-Privileges

## Summary

This procedure enumerates user privileges in an IBM DB2 database, including system-level, database-level, and table-level permissions. It helps attackers identify potential escalation paths by revealing which users have elevated access, such as SYSADM or DBADM roles, and what objects they can access. This is a key discovery step before attempting privilege escalation via trusted relationships or injection attacks.

## Description

In DB2 environments, privileges are managed through system authorities, database authorities, and schema object permissions. Attackers with initial low-privilege access to the database can query system catalogs like SYSCAT.TABAUTH, SYSCAT.DBAUTH, and SYSIBM.SYSUSERAUTH to map out the permission landscape. This enumeration reveals over-privileged accounts or misconfigurations that can be exploited for escalation, such as using a service account with higher privileges or injecting code to impersonate users. The technique assumes SQL injection or direct query access and targets on-premises or cloud-hosted DB2 instances. Expected outcomes include a list of users with sensitive permissions, enabling targeted attacks like credential dumping or unauthorized data access.

## Requirements

1. Valid DB2 user credentials with at least CONNECT privilege to the target database.
2. Access to a DB2 client or direct SQL execution interface (e.g., db2 command-line tool or JDBC).
3. Knowledge of basic SQL syntax and DB2 system catalog structure.
4. Network connectivity to the DB2 server port (default 50000).

## Defense

- Enforce principle of least privilege by granting minimal authorities to users and regularly auditing with db2audit.
- Enable query logging and monitor for anomalous SELECT statements on system catalogs using DB2's audit facilities or external SIEM integration.
- Use role-based access control (RBAC) and avoid granting SYSADM or DBADM to application accounts.
- Implement input validation to prevent SQL injection vectors that could enable these queries.

## Objectives

1. Identify users with elevated system or database authorities for potential impersonation or escalation.
2. Map table and schema permissions to locate sensitive data accessible with current credentials.
3. Discover misconfigurations in privilege assignments to support further exploitation.
4. Validate current user's permissions to assess initial access level.

## Instructions

### Step 1: List All Table Privileges

**Context**: This step queries the SYSCAT.TABAUTH catalog to enumerate privileges on all tables across schemas, helping identify broadly accessible objects or over-privileged users. It requires sufficient authority to query the catalog; if denied, it indicates limited access.

**Command** ([[commands/db2-list-table-privileges]]):
```sql
select * from syscat.tabauth;
```

> This command retrieves columns like GRANTEE, TABSCHEMA, TABNAME, and privilege types (e.g., SELECT, INSERT). Use it to spot users with CONTROL or ALTER on critical tables.

### Step 2: Show Current User's Table Privileges

**Context**: Focus on the connected user's specific table permissions to understand immediate access boundaries and potential escalation if higher privileges are found on owned objects.

**Command** ([[commands/db2-show-current-user-table-privileges]]):
```sql
select * from syscat.tabauth where grantee = current user;
```

> Output includes the current user's granted privileges on tables. Look for unexpected grants like DELETE or INDEX on sensitive schemas, which could enable data manipulation.

### Step 3: Show Current User's Database Privileges

**Context**: Query SYSCAT.DBAUTH to reveal the current user's database-level authorities, such as CREATETAB or BINDADD, which are prerequisites for broader escalation.

**Command** ([[commands/db2-show-current-user-database-privileges]]):
```sql
select * from syscat.dbauth where grantee = current user;
```

> Results show authorities like DATAACCESS or DBADM. If DBADM is present, escalation to full control is possible; otherwise, note paths to request or abuse these.

### Step 4: List System Privileges

**Context**: Examine SYSIBM.SYSUSERAUTH for system-wide authorities like SYSADM or SECADM, identifying high-privilege users for targeted attacks via trust exploitation.

**Command** ([[commands/db2-list-system-privileges]]):
```sql
select * from SYSIBM.SYSUSERAUTH;
```

> This lists all users' system authorities (e.g., SYSCTRL, SYSMAINT). Filter for GRANTEETYPE='G' (group) or specific users to find escalation vectors like group membership abuse.
