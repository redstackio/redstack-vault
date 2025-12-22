---
id: 6a4dc94e-a187-42e9-8dd5-25818e01b4b9
name: DB2-User-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.624480+00:00'
updated_at: '2023-04-10T20:22:05.502526+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/DB2 Cheatsheet]]'
  - '[[tags/DB2 Injection]]'
  - '[[tags/List Users]]'
  - db2
  - enumeration
  - users
  - privileges
commands:
  - '[[commands/db2-select-authorized-users]]'
  - '[[commands/db2-select-schema-owners]]'
  - '[[commands/db2-select-database-privilege-grantees]]'
  - '[[commands/db2-select-table-privilege-grantees]]'
platforms:
  - Database
  - DB2
tools: []
validated: true
---

# DB2-User-Enumeration

## Summary

The DB2 User Enumeration procedure identifies users and their associated authorization levels within a DB2 database instance. This involves querying system catalogs to retrieve lists of authorized users, schema owners, and grantees of database and table-level privileges, providing attackers with insights into the database's access structure for further exploitation planning.

## Description

In a penetration testing or red team scenario, enumerating users in a DB2 database reveals the attack surface by exposing account names, roles, and privilege distributions. This technique targets DB2's system administrative views and catalogs, such as sysibmadm.privileges and syscat.dbauth, to extract authorization data without requiring full administrative access—though some queries may need elevated privileges. The process helps map potential privilege escalation paths or identify high-value targets like schema owners. It assumes the attacker has already gained initial database access, such as through SQL injection or valid credentials, and is executed via a DB2 client or compatible SQL interface. Outcomes include lists of users that can inform targeted attacks, like credential guessing or privilege abuse.

## Requirements

1. Valid authentication credentials for the DB2 database (e.g., username and password with at least read access to system catalogs).
2. Access to a DB2 client tool or SQL interface (e.g., db2 command-line processor or a connected application like DBeaver).
3. Network connectivity to the DB2 instance if remote access is required.
4. Sufficient privileges to query system views (some commands may fail without them, indicating privilege boundaries).

## Defense

Defensive measures and detection strategies:

- Restrict access to system catalogs by granting minimal privileges to database users and auditing privilege assignments regularly.
- Enable DB2 auditing for SQL queries accessing sysibmadm, syscat, or sysibm schemas to log suspicious enumeration attempts.
- Implement database activity monitoring (DAM) tools to alert on queries targeting authorization views.
- Use role-based access control (RBAC) to limit visibility of user and privilege data, and regularly review user accounts for dormant or overly permissive ones.

## Objectives

1. Retrieve a comprehensive list of authorized users, schema owners, and privilege grantees in the DB2 instance.
2. Identify users with elevated privileges for potential targeting in subsequent attacks.
3. Assess the database's authorization structure to uncover misconfigurations or vulnerabilities.

## Instructions

### Step 1: Retrieve Authorized Users

**Context**: This step queries the privileges administrative view to list all unique authorization IDs (users) with any privileges in the DB2 instance, providing a broad overview of active accounts.

**Command** ([[commands/db2-select-authorized-users]]):
```sql
select distinct(authid) from sysibmadm.privileges;
```

> This command scans the sysibmadm.privileges table for unique authid entries, which represent users or groups authorized for various objects. It requires access to administrative views and helps identify all potentially privileged entities. If the query returns no results or errors, it may indicate insufficient privileges.

### Step 2: Retrieve Schema Owners

**Context**: Identify owners of database schemas, as these users often have significant control over objects within their schemas, making them high-value targets for escalation.

**Command** ([[commands/db2-select-schema-owners]]):
```sql
select distinct(definer) from syscat.schemata;
```

> This extracts unique definer values from the syscat.schemata catalog, listing schema creators/owners. Schemas are namespaces for database objects, so owners typically hold implicit privileges. Success confirms the list of administrative-like users.

### Step 3: Retrieve Database-Level Privilege Grantees

**Context**: Enumerate users granted privileges at the database level (e.g., CONNECT, DATAACCESS), which indicate broader access rights beyond specific objects.

**Command** ([[commands/db2-select-database-privilege-grantees]]):
```sql
select grantee from syscat.dbauth;
```

> Querying syscat.dbauth returns grantees of database authorities. Note that results may include duplicates or be incomplete without full access; cross-reference with other steps for accuracy. This reveals users with systemic privileges.

### Step 4: Retrieve Table-Level Privilege Grantees

**Context**: List users with privileges on tables, offering granular insights into data access patterns and potential weak points for lateral movement.

**Command** ([[commands/db2-select-table-privilege-grantees]]):
```sql
select distinct(grantee) from sysibm.systabauth;
```

> This command pulls unique grantees from the systabauth authorization view, focusing on table-specific privileges like SELECT or ALTER. It provides more precise results than database-level queries and is useful for identifying data-sensitive users.
