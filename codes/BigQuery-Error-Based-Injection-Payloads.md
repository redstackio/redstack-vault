---
id: a4111df8-0398-4605-b506-04d286b810a6
name: BigQuery-Error-Based-Injection-Payloads
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:32.398527+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - GCP
  - Cloud
tags:
  - sqli
  - error-based
  - payload
  - bigquery
validated: true
---

# BigQuery-Error-Based-Injection-Payloads

## Code

```sql
# Error based - division by zero
' OR if(1/(length((select('a')))-1)=1,true,false) OR '

# Error based - casting: select CAST(@@project_id AS INT64)
dataset_name.column_name` union all select CAST(@@project_id AS INT64) ORDER BY 1 DESC#
```

## Description

These SQL payloads are designed for error-based injection in Google BigQuery. The first uses a conditional division by zero to infer string lengths (e.g., adjust the subtracted value to probe database elements). The second forces a type casting error on the project ID variable (@@project_id), leaking the current GCP project context in the error message. They exploit BigQuery's error reporting to disclose schema or configuration without direct data dumps.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `dataset_name` | Target dataset to reference (replace with known or guessed name) | `prod_data` |
| `column_name` | Target column to inject into (e.g., in a UNION) | `user_id` |
| Length offset (e.g., -1) | Adjust for probing different lengths in division payload | `-2` for length 2 |

## Usage

Inject these into vulnerable parameters of a BigQuery query, such as a web app's search field or API POST body. For CLI testing, append to a base SELECT via the `bq` tool: `bq query "SELECT * FROM table WHERE cond=$_PAYLOAD"`. Start with the division payload for length enumeration, then use casting for direct leaks. Ideal for initial reconnaissance in GCP environments with exposed query interfaces.

## Detection

- BigQuery audit logs showing queries with functions like `CAST`, `length`, or division operations in user inputs.
- Error rates spiking with invalid type conversions or zero divisions.
- Anomalous access to @@project_id or system variables in query history.
- WAF alerts on SQL keywords (IF, SELECT, UNION) in API payloads.

## Related

- [[procedures/Google-BigQuery-Error-Based-SQL-Injection]]
- [[bq-BigQuery-CLI]]
