---
type: procedure
description: >-
  Exploit SQL injection vulnerabilities in applications connected to Google
  BigQuery by using SQL comment syntax to bypass input validation and execute
  arbitrary queries.
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - bigquery-comment
  - google-bigquery-sqli
commands: []
platforms:
  - GCP
  - Web
tools:
  - '[[tools/Google-Cloud-SDK]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# BigQuery-SQL-Injection-Using-Comment-Syntax

## Summary

This procedure demonstrates how to perform SQL injection attacks against applications that interface with Google BigQuery by leveraging SQL comment syntax (such as # or /* */) to bypass basic input filters and validation. This allows attackers to append or modify queries to exfiltrate data, execute unauthorized commands, or escalate access within the cloud environment.

## Description

Google BigQuery is a serverless data warehouse that uses SQL-like queries to analyze large datasets. Applications built on top of BigQuery often accept user input to construct dynamic queries, creating opportunities for SQL injection if inputs are not properly sanitized. This technique exploits comment syntax to evade filters that block certain keywords or structures, enabling the injection of malicious SQL payloads. For example, comments can terminate intended queries prematurely and append attacker-controlled code. This is particularly effective against web applications or APIs that pass unsanitized input directly to BigQuery's query execution. Successful exploitation can lead to data exfiltration, alteration of datasets, or further lateral movement in GCP environments. The procedure assumes a vulnerable application endpoint and focuses on crafting and delivering the payload.

## Requirements

1. Valid credentials or access to a Google Cloud project with BigQuery permissions (e.g., BigQuery User or Data Editor role).
2. Access to the vulnerable application or API endpoint that constructs BigQuery queries from user input.
3. Tools for testing injections, such as a browser, [[tools/Burp-Suite]], or curl for API requests.
4. Knowledge of the application's query structure (e.g., via error messages or reconnaissance).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization, using parameterized queries or prepared statements in application code.
- Employ web application firewalls (WAFs) configured to detect SQL comment patterns and injection attempts.
- Limit BigQuery IAM roles to least privilege, auditing query logs via Cloud Logging for anomalous SQL patterns.
- Use query preprocessing to strip or escape comments and special characters before execution.

## Objectives

1. Bypass input validation filters using SQL comments to inject arbitrary code into BigQuery queries.
2. Execute unauthorized SQL commands to exfiltrate or manipulate data in BigQuery datasets.
3. Confirm successful injection through response analysis or data access verification.

## Instructions

### Step 1: Identify Vulnerable Input Endpoint

**Context**: Locate an application input field, form, or API parameter that influences BigQuery query construction. This could be a search box, report generator, or dynamic query builder. Test for basic SQLi by appending single quotes (') to inputs and observing errors that reveal SQL syntax or BigQuery internals.

**Why**: Understanding the query structure helps craft effective payloads that align with the application's SQL generation.

### Step 2: Craft Injection Payload with Comment Syntax

**Context**: Use SQL comment syntax to neutralize the original query and append malicious code. Comments like # (line comment) or /* */ (block comment) can bypass filters that scan for keywords without considering comment wrappers.

**Code** ([[codes/BigQuery-SQL-Injection-Comment-Example]]):

Refer to the code snippet for example payloads demonstrating comment usage.

**Why**: Comments allow truncation of the legitimate query (e.g., after 'SELECT') and injection of UNION-based exfiltration or other payloads without triggering keyword blocks.

### Step 3: Submit and Test the Payload

**Context**: Deliver the payload via the identified endpoint, such as a POST request to an API or form submission. Monitor responses for signs of injection success, like unexpected data dumps, errors exposing table names, or altered query results.

**Example Delivery** (using a tool like curl for API testing):

```bash
curl -X POST 'https://vulnerable-app.example.com/query' \
  -d 'search=1 # malicious payload: UNION SELECT * FROM sensitive_table --'
```

**Why**: Direct submission verifies if the comment bypass works; adjust payload based on response (e.g., add /*comment*/ if # is filtered).

**Expected Output**: If successful, the response may include leaked data (e.g., "row1, sensitive_data"), BigQuery error messages revealing schema, or no errors with partial data exfiltration.

### Step 4: Verify and Escalate

**Context**: Analyze the output to confirm injection. If data is exfiltrated, use it for further attacks (e.g., credential dumping). Escalate by chaining with other payloads like time-based blinds or stacked queries if supported by BigQuery.

**Why**: Validation ensures the bypass is reliable; escalation maximizes impact, such as dumping entire datasets.

**Expected Output**: Access to unauthorized BigQuery tables or datasets, confirmed by querying known sensitive information.
