---
type: procedure
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/Query SQL Server|T1083.002 - Query SQL Server]]'
sub_techniques: []
tags:
  - bigquery
  - sql-injection
  - boolean-based
  - gcp
  - cloud
commands: []
tools: []
platforms:
  - GCP
  - Cloud
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# BigQuery-Boolean-Based-SQL-Injection

## Summary

This procedure outlines a Boolean-based blind SQL injection attack targeting Google BigQuery, allowing attackers to infer and extract sensitive database schema information, such as column names, by crafting queries that return true or false responses based on conditional logic. It is particularly useful when direct error-based or union-based injections are not feasible due to limited feedback from the application.

## Description

Google BigQuery is a serverless data warehouse that processes SQL queries on large datasets in the cloud. A SQL injection vulnerability occurs when user input is improperly sanitized and concatenated into SQL queries executed against BigQuery, often through web applications or APIs that query the service. In a Boolean-based blind SQL injection, the attacker injects conditions that alter the query's behavior subtly—such as changing the number of results returned or triggering different application responses—based on whether a subquery evaluates to true or false. By iteratively testing conditions (e.g., checking if the first character of a column name is 'A'), the attacker can reconstruct data character by character without seeing the full database dump. This technique targets the discovery of schema elements like table structures and can extend to data exfiltration. The attack assumes the injection point is in a WHERE clause of a SELECT query, common in search or filtering features of applications backed by BigQuery.

## Requirements

1. Access to a web application, API, or interface that accepts user input and dynamically constructs SQL queries for BigQuery execution.
2. Partial knowledge of the target BigQuery project (e.g., project_id) or ability to enumerate it via other means.
3. Tools or a browser to send and observe HTTP requests/responses, noting differences in output (e.g., page load time, result count, or content changes) for true/false conditions.
4. Understanding of BigQuery SQL syntax, including functions like SUBSTRING and backtick-quoted identifiers for datasets and tables.

## Defense

- Always use parameterized queries or prepared statements when constructing SQL for BigQuery to separate user input from code.
- Implement a web application firewall (WAF) or API gateway with rules to detect common SQL injection patterns, including Boolean conditions and substring extractions.
- Enforce least-privilege IAM roles for service accounts interacting with BigQuery, limiting query scopes to necessary datasets.
- Enable BigQuery audit logging and monitor for anomalous queries, such as those with conditional logic or excessive SUBSTRING usage; integrate with SIEM for alerts.
- Sanitize and validate all user inputs, rejecting or escaping special characters like single quotes and backticks.

## Objectives

1. Confirm the presence of a SQL injection vulnerability in the BigQuery-backed application.
2. Extract database schema details, such as column names from target tables, to map the data structure.
3. Lay groundwork for further attacks, like full data exfiltration or privilege escalation via extracted credentials.
4. Demonstrate the impact of poor query parameterization on cloud data confidentiality.

## Instructions

### Step 1: Identify and Test the Injection Point

**Context**: Locate a user input field (e.g., search box or filter parameter) that influences a SQL query's WHERE clause. Test for basic SQL injection by appending a single quote or comment to see if it alters the response, indicating unsanitized input.

Inject a simple payload like `' OR 1=1 --` into the input field and submit the query. Observe if the application returns all records (true condition) instead of filtered results, confirming injection feasibility. If successful, proceed to Boolean testing; if not, try variations like `') OR 1=1 --` for subquery contexts.

**Expected Output**: The application returns an unfiltered dataset or errors out, differing from a normal query response.

### Step 2: Enumerate Basic Schema Elements

**Context**: With injection confirmed, use Boolean conditions to guess or extract known elements like database names or table counts. This step verifies the technique before targeting specifics like column names.

Craft a payload to check if a table exists, e.g., `' AND EXISTS(SELECT 1 FROM `project_id.dataset_name.table_name`) --`. Submit and compare responses: a true response (e.g., normal results) indicates existence; false (e.g., no results or error) does not. Iterate over guessed project_id, dataset_name, and table_name values.

**Expected Output**: Consistent response patterns allowing inference of schema existence (e.g., true for valid tables, false for invalid).

### Step 3: Extract Column Name Using Boolean Substring

**Context**: Once a target table is identified, extract column names character by character using substring functions and Boolean comparisons. This leverages BigQuery's INFORMATION_SCHEMA views or direct table metadata queries to pull column details.

Use the following code snippet to extract the first character of the first column name:

**Code** ([[codes/BigQuery-SQL-Injection-Payload-Extract-First-Column-Char]]):

```sql
' WHERE SUBSTRING((select column_name from `project_id.dataset_name.table_name` limit 1),1,1)='A'#
```

Replace `project_id`, `dataset_name`, and `table_name` with known or enumerated values. Inject into the vulnerable parameter and submit. If the response indicates true (e.g., results returned), the first character is 'A'; otherwise, test 'B', 'C', etc., up to 'Z'. Repeat for subsequent positions by changing the substring start index (e.g., position 2 for second character). For INFORMATION_SCHEMA, adjust the subquery to `INFORMATION_SCHEMA.COLUMNS` where appropriate.

**Expected Output**: Boolean response (e.g., presence/absence of results) allowing character inference; after iteration, a full column name like 'user_id' reconstructed.

### Step 4: Iterate and Expand Extraction

**Context**: Build on extracted column names to fetch more data, such as row counts or actual values, using similar Boolean logic on SELECT queries from the table.

Extend the payload to check data existence, e.g., `' AND SUBSTRING((SELECT column_value FROM `project_id.dataset_name.table_name` LIMIT 1),1,1)='A' --`. Automate iterations if possible via scripting, but manually verify each step. If credentials or sensitive data is found, note for escalation.

**Expected Output**: Progressive reconstruction of data elements, confirming successful information disclosure.

### Step 5: Verify and Clean Up

**Context**: Validate extracted information by crafting a non-malicious query if possible, or cross-reference with known schema. Avoid leaving audit trails by minimizing requests.

Review logs or responses for any detection triggers. If the attack succeeds, document the full schema for further exploitation chains.

**Expected Output**: Accurate schema map or data sample, with no immediate application errors post-testing.
