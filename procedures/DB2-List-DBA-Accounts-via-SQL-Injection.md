---
id: c81c8d10-d4ab-4d06-82a0-cc6a8a9e1351
name: DB2-List-DBA-Accounts-via-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.695800+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account-Discovery|T1087 - Account Discovery]]'
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - DB2
  - SQL-Injection
  - Account-Enumeration
  - Database
commands:
  - '[[commands/db2-query-controlauth-users]]'
  - '[[commands/db2-query-sysadmauth-users]]'
platforms:
  - Linux
  - Windows
tools: []
validated: true
---

# DB2-List-DBA-Accounts-via-SQL-Injection

## Summary

This procedure exploits a SQL injection vulnerability in a web application connected to a DB2 database to enumerate DBA-level accounts by querying system authorization tables. It identifies users with CONTROL authority over tables and those with SYSADM authority, providing attackers with potential high-privilege targets for further exploitation.

## Description

In a typical attack scenario, an attacker targets a web application with unsanitized input fields that interact with a DB2 backend. By injecting SQL payloads, the attacker can execute arbitrary queries against system catalogs like SYSTABAUTH and SYSUSERAUTH to discover administrative users. This technique is useful during reconnaissance or lateral movement phases to map privileged accounts without direct database access. Success depends on the injection point allowing read access to system views, and outcomes include lists of usernames that can be used for password spraying or privilege escalation attempts. The procedure assumes a blind or error-based SQL injection vector where query results can be extracted via response differences or direct output.

## Requirements

1. Access to a vulnerable web application with a DB2 backend and SQL injection entry point (e.g., login form, search field).
2. Ability to craft and submit HTTP requests with injected SQL payloads (e.g., via browser, curl, or Burp Suite).
3. Basic knowledge of the application's query structure to close the injection properly (e.g., appending ' OR 1=1 --).
4. Tools for sending requests and observing responses, such as a proxy like Burp Suite.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and parameterized queries or prepared statements to prevent SQL injection.
- Enforce least privilege by restricting application database users to minimal permissions, denying access to system catalogs.
- Monitor database logs for anomalous queries accessing SYSIBM schema tables and alert on unusual SELECT patterns from SYSTABAUTH or SYSUSERAUTH.
- Use web application firewalls (WAFs) to detect and block common SQL injection payloads.

## Objectives

1. Identify users with CONTROL authority over database tables for targeted enumeration.
2. Discover SYSADM users with full administrative privileges.
3. Extract account names for subsequent attacks like credential guessing or lateral movement.

## Instructions

### Step 1: Identify Injection Point and Test Basic SQLi

**Context**: Confirm the SQL injection vulnerability exists and can execute arbitrary SELECT queries. This step ensures the payload can be injected without breaking the application flow.

Use a tool like Burp Suite to intercept and modify requests. Append a test payload such as ' OR 1=1 -- to the vulnerable parameter and observe if the response changes (e.g., returns all records or errors revealing DB2 specifics).

> If the injection works, proceed to craft payloads for system queries. If not, the point may not be exploitable for reads.

### Step 2: Inject Query for CONTROL Authority Users

**Context**: This step enumerates users granted CONTROL privileges on tables, which often include DBAs. CONTROL allows operations like ALTER, DROP, and GRANT, making these users high-value targets.

**Command** ([[commands/db2-query-controlauth-users]]):

To inject, modify the vulnerable parameter in the HTTP request to include the query closed properly, e.g., '); [injected query] ; --. Submit via POST or GET depending on the app.

```sql
select distinct(grantee) from sysibm.systabauth where CONTROLAUTH='Y'
```

> This query returns unique grantees (users or groups) with CONTROL on any table. Expected output in the app response or error: a list of usernames like DB2ADMIN, SYSADM1. In blind SQLi, infer results via boolean conditions or time delays.

### Step 3: Inject Query for SYSADM Authority Users

**Context**: SYSADM provides instance-level admin rights, including user management and full data access. This identifies top-tier DBAs for escalation.

**Command** ([[commands/db2-query-sysadmauth-users]]):

Inject similarly, ensuring the payload fits the query context: '); [injected query] ; --.

```sql
select name from SYSIBM.SYSUSERAUTH where SYSADMAUTH = 'Y' or SYSADMAUTH = 'G'
```

> Returns names of users with SYSADM='Y' (yes) or 'G' (grantable). Expected output: usernames like INSTANCE_OWNER. Verify by checking if results overlap with CONTROL users for confirmation.

### Step 4: Extract and Validate Results

**Context**: Compile the enumerated accounts and test their validity if possible (e.g., via subsequent injections or app features). This confirms actionable intelligence.

Manually note the usernames from responses. If the app has a login or user lookup, attempt to probe these accounts without credentials to validate existence.

> Success if at least one DBA-level account is identified. Cross-reference with known app users to prioritize.
