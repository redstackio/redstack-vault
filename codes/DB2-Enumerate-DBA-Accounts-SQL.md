---
id: 66d26c03-dd43-40af-9119-035d964a1edc
name: DB2-Enumerate-DBA-Accounts-SQL
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:32.690028+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - DB2
  - SQL-Injection
  - Account-Enumeration
validated: true
---

# DB2-Enumerate-DBA-Accounts-SQL

## Code

```sql
select distinct(grantee) from sysibm.systabauth where CONTROLAUTH='Y'
select name from SYSIBM.SYSUSERAUTH where SYSADMAUTH = ‘Y’ or SYSADMAUTH = ‘G’
```

## Description

This SQL code snippet contains two queries to enumerate DBA-level accounts in a DB2 database. The first identifies users with table CONTROL authority, while the second lists those with SYSADM instance authority. Designed for injection into vulnerable applications to extract privilege information without native DB2 access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; static queries for direct injection or execution. | N/A |

## Usage

Inject these queries via SQL injection in web app parameters, e.g., in a search field: '); [query1]; -- for the first, repeating for the second. In a direct DB2 session, run sequentially. Use in reconnaissance to map admin users for targeted attacks like credential dumping.

## Detection

- Database audit logs showing SELECT from SYSIBM.SYSUSERAUTH or SYSTABAUTH by non-admin users.
- WAF alerts on SQL keywords like 'SYSADMAUTH' or 'CONTROLAUTH' in payloads.
- Anomalous response times or error messages indicating system table access.

## Related

- [[procedures/DB2-List-DBA-Accounts-via-SQL-Injection]]
