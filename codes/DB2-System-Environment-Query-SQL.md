---
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:33.151304+00:00'
updated_at: '2023-04-10T20:22:02.293610+00:00'
platforms:
  - Linux
  - Windows
  - Database
tags:
  - db2
  - injection
  - discovery
validated: true
---

# DB2-System-Environment-Query-SQL

## Code

```sql
select os_name,os_version,os_release,host_name from sysibmadm.env_sys_info -- requires priv
```

## Description

This SQL code snippet queries the DB2 sysibmadm.env_sys_info administrative view to extract essential system environment details, including the operating system name, version, release, and hostname. It is designed for injection into vulnerable DB2 applications or execution within stored procedures/user-defined functions (UDFs), providing attackers with host reconnaissance data to support further exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static query with no user-defined variables; adapt for injection by wrapping in UNION or subquery contexts | N/A |

## Usage

Inject this code into a vulnerable parameter, e.g., in a web app search field: ' UNION SELECT os_name,os_version,os_release,host_name FROM sysibmadm.env_sys_info --. For procedural use, embed in a CREATE PROCEDURE statement. Requires execution privileges on the sysibmadm schema. Use tools like sqlmap for automated delivery or Burp Suite for manual testing.

## Detection

- Monitor DB2 audit logs for SELECT operations on sysibmadm.env_sys_info by non-admin users.
- Web application logs showing anomalous SQL errors or delays indicative of injection attempts.
- Intrusion detection signatures for DB2-specific payloads, including references to sysibmadm tables.
- Database firewall rules blocking unauthorized procedural executions.

## Related

- [[procedures/DB2-SQL-Injection-for-System-Information-Discovery]]
- [[techniques/System Information Discovery|T1082 - System Information Discovery]]
