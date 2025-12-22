---
id: 4025ce4e-47ab-43b8-babb-434c61f8dd52
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:33.093428+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - db2
  - sqli
  - blind-sqli
  - time-delay
platforms:
  - Database
validated: true
---

# DB2-Time-Delay-Payload-for-Blind-SQL-Injection

## Code

```sql
' and (SELECT count(*) from sysibm.columns t1, sysibm.columns t2, sysibm.columns t3)>0 and (select ascii(substr(user,1,1)) from sysibm.sysdummy1)=68 
```

## Description

This SQL payload is designed for time-based blind SQL injection in IBM DB2 databases. It injects a boolean condition that, if true, triggers a resource-intensive cross-join query on the sysibm.columns table (aliased as t1, t2, t3), causing a significant delay in response time. The condition here checks if the ASCII value of the first character of the current database user is 68 ('D'). This allows attackers to infer data by observing timing differences without any visible output or errors.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| =68 | ASCII value to test against (vary for extraction) | =65 (for 'A'), =90 (for 'Z') |
| substr(user,1,1) | Target data substring (modify position and source) | substr(dbname,1,1), substr(version,2,1) |

## Usage

Inject this payload into a vulnerable parameter in a web application (e.g., via GET/POST request using a proxy like Burp Suite). Submit and measure response time: a delay indicates the condition is true. Use in conjunction with the [[procedures/DB2-Time-Based-Blind-SQL-Injection]] procedure to systematically extract strings like usernames or versions by iterating or binary-searching ASCII values.

## Detection

- Monitor DB2 logs for queries involving cross-joins on system tables like sysibm.columns or sysibm.sysdummy1.
- Detect unusual CPU spikes or long-running SELECT COUNT(*) queries.
- WAF rules for SQLi patterns including ' and (SELECT or substr(user.
- Network-level timing anomalies in application responses (>5 seconds).
