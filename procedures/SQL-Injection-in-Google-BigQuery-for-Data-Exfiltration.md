---
type: procedure
description: >-
  Exploit SQL injection vulnerabilities in applications backed by Google
  BigQuery to discover project details, enumerate datasets, and exfiltrate data
  from tables.
verified: true
submitted: false
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
  - '[[techniques/Data-from-Cloud-Storage|T1530 - Data from Cloud Storage]]'
sub_techniques: []
tags:
  - sql-injection
  - google-bigquery
  - data-exfiltration
  - discovery
  - gcp
commands:
  - '[[commands/bigquery-discover-project-id]]'
  - '[[commands/bigquery-enumerate-datasets]]'
  - '[[commands/bigquery-exfiltrate-table-data]]'
platforms:
  - GCP
  - Cloud
tools: []
validated: true
---

# SQL-Injection-in-Google-BigQuery-for-Data-Exfiltration

## Summary

This procedure demonstrates how to exploit SQL injection (SQLi) vulnerabilities in web applications that use Google BigQuery as the backend database. By injecting malicious SQL payloads into user inputs, an attacker can execute arbitrary queries to discover the project ID, enumerate available datasets, and exfiltrate sensitive data from specific tables. This is particularly useful in scenarios where the application fails to use parameterized queries or proper input sanitization, allowing attackers to append or modify SQL statements for reconnaissance and data theft.

## Description

Google BigQuery is a serverless data warehouse for running SQL queries against large datasets in Google Cloud Platform (GCP). Applications often integrate BigQuery for analytics or search features, passing user inputs directly into SQL queries without validation. An SQLi vulnerability enables attackers to terminate the intended query (e.g., using a single quote and semicolon) and append their own queries. This procedure covers injecting payloads to first identify the project context, list datasets for further targeting, and then dump table contents. Success depends on the injection point (e.g., a search field in a 'SELECT * FROM table WHERE column = 'user_input'') and the attacker's ability to observe query results in the application's response. Potential outcomes include unauthorized access to customer data, financial records, or other sensitive information stored in BigQuery. This technique maps to real-world attacks where misconfigured cloud apps expose petabyte-scale data.

## Requirements

1. A vulnerable web application with SQLi in a BigQuery-integrated input field (e.g., search, login, or filter).
2. Knowledge of basic SQL and BigQuery syntax.
3. Network access to the target application (e.g., via browser or proxy like Burp Suite).
4. Ability to observe application responses for query results (e.g., error messages or rendered data).
5. Optional: Access to GCP console or bq CLI for testing payloads in a lab environment.

## Defense

- Implement parameterized queries and prepared statements in application code to separate user input from SQL logic.
- Use Google Cloud's Identity and Access Management (IAM) to enforce least privilege, limiting query scopes to specific datasets.
- Enable BigQuery audit logging and monitor for anomalous queries (e.g., via Cloud Logging or Security Command Center) looking for unexpected SELECTs on INFORMATION_SCHEMA or broad table dumps.
- Apply Web Application Firewall (WAF) rules to detect and block common SQLi patterns like quote termination or union-based payloads.
- Regularly scan for vulnerabilities using tools like SQLMap adapted for cloud environments.

## Objectives

1. Identify the BigQuery project ID to understand the GCP environment scope.
2. Enumerate datasets to map the data warehouse structure and identify high-value targets.
3. Exfiltrate data from targeted tables to achieve collection of sensitive information.
4. Maintain stealth by limiting query results (e.g., using LIMIT) to avoid detection.

## Instructions

### Step 1: Discover Project ID

**Context**: Begin by injecting a payload to retrieve the current BigQuery project ID. This establishes the GCP project context, which is necessary for subsequent queries targeting specific datasets and tables. Without the project ID, INFORMATION_SCHEMA queries may fail or return incomplete results. Inject this at a point where user input is concatenated into a SQL string, such as a search parameter.

**Command** ([[commands/bigquery-discover-project-id]]):
```sql
SELECT CURRENT_PROJECT();
```

> This query returns the project ID associated with the BigQuery job. In an injection scenario, craft a payload like: `'; SELECT CURRENT_PROJECT(); --` appended to the input. Observe the response for the project ID (e.g., in JSON output or error details). If the injection point supports multiple statements, this executes after the original query.

### Step 2: Enumerate Datasets

**Context**: Using the project ID from Step 1, inject a query to list all datasets in the project. Datasets act as namespaces for tables, so enumerating them reveals the structure of available data stores. This step aids in discovery of sensitive areas like 'customer_data' or 'logs'. Specify the region (e.g., 'region-us') if known; otherwise, test common regions like 'region-us' or 'US'.

**Command** ([[commands/bigquery-enumerate-datasets]]):
```sql
SELECT dataset_id FROM `$_PROJECT_ID.INFORMATION_SCHEMA.SCHEMATA`;
```

> Replace $_PROJECT_ID with the actual project ID from Step 1. Injection payload example: `'; SELECT dataset_id FROM 'my-project.INFORMATION_SCHEMA.SCHEMATA'; --`. The result lists dataset names, helping prioritize targets for exfiltration. If no results, try specifying a region: `region-us.$_PROJECT_ID.INFORMATION_SCHEMA.SCHEMATA`.

### Step 3: Exfiltrate Table Data

**Context**: Target a specific table within an enumerated dataset to dump its contents. This achieves the objective of data collection, potentially exfiltrating sensitive records. Use LIMIT to retrieve small batches and avoid triggering rate limits or alerts. Decision point: If the table schema is unknown, first inject a DESCRIBE query; otherwise, proceed to SELECT *.

**Command** ([[commands/bigquery-exfiltrate-table-data]]):
```sql
SELECT * FROM `$_PROJECT_ID.$_DATASET_ID.$_TABLE_ID` LIMIT 10;
```

> Substitute $_PROJECT_ID, $_DATASET_ID, and $_TABLE_ID with values from previous steps (e.g., `my-project.customer_data.users LIMIT 10`). Injection example: `'; SELECT * FROM 'my-project.customer_data.users' LIMIT 10; --`. Results appear in the application response, such as rendered table data or exported CSV. If access denied, the dataset lacks permissions—pivot to another.
