---
type: code
language: sql
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - GCP
tags:
  - sql-injection
  - boolean-based
  - payload
  - bigquery
validated: true
---

# BigQuery-SQL-Injection-Payload-Extract-First-Column-Char

## Code

```sql
' WHERE SUBSTRING((select column_name from `project_id.dataset_name.table_name` limit 1),1,1)='A'#
```

## Description

This SQL injection payload is designed for Boolean-based blind SQL injection in Google BigQuery. It injects into a WHERE clause to extract the first character of the first column name from a specified table by comparing it to 'A' using the SUBSTRING function. If the condition evaluates to true, the query returns results (or alters behavior observably); otherwise, it returns false. The '#' comments out the rest of the original query, and single quotes close the string context. This allows character-by-character inference of schema details without direct output of sensitive data.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| project_id | Google Cloud project ID containing the BigQuery dataset | my-project-123 |
| dataset_name | Name of the BigQuery dataset | my_dataset |
| table_name | Name of the target table | users_table |
| 'A' | Character to test against (iterate A-Z for guessing) | 'B' (for next test) |

## Usage

Inject this payload into a vulnerable user input field in a web application or API that constructs SQL queries for BigQuery (e.g., a search parameter). Observe the application's response: a difference in result count, page content, or timing indicates true/false. Iterate the character ('A' to 'Z') and position (1,2,3...) in SUBSTRING to reconstruct the full column name. Use in conjunction with tools like Burp Suite for request manipulation. This is typically part of a larger procedure for schema discovery in blind SQLi scenarios.

## Detection

- BigQuery audit logs showing queries with SUBSTRING, conditional WHERE clauses, or comments like '#'; alert on high-frequency character tests.
- Application logs for unusual response patterns or increased query volume from single IPs.
- WAF rules matching SQL injection signatures, including backticks (`) for BigQuery identifiers and LIMIT 1 in subqueries.
- Network monitoring for repeated similar requests to BigQuery APIs.

## Related

- [[procedures/BigQuery-Boolean-Based-SQL-Injection]] (procedure that uses this payload for schema extraction)
