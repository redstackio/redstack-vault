---
id: proc-uuid-001
name: Trigger-SQL-Injection-in-Trac-Report-Parameter
tags:
  - sqli
  - web
  - trac
  - input-validation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-test-sqli-report]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.316Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SQL-Injection-in-Trac-Report-Parameter

## Summary

This procedure exploits a SQL Injection vulnerability in the 'report' parameter of the Trac ticket query endpoint by appending a single quote to trigger syntax errors, exposing database structure and confirming lack of input sanitization for potential data extraction or manipulation.

## Description

The Trac ticket system, used by the Tor Project, processes the 'report' parameter in its query endpoint without proper validation, allowing SQL metacharacters like single quotes to alter the backend SQL query. In a typical scenario, an attacker accesses the public-facing /projects/tor/query endpoint and modifies the URL to inject payloads. Successful execution reveals error messages that may include database details, enabling further attacks like data dumping. This targets web-based Trac installations on Python backends, with outcomes including leaked ticket data if escalated.

## Requirements

1. Public access to the Trac query endpoint (e.g., https://trac.torproject.org/projects/tor/query)
2. Web browser or command-line tool like curl for URL manipulation
3. Basic knowledge of SQL syntax and URL encoding

## Defense

Defensive measures and detection strategies:

- Implement parameterized queries or prepared statements in Trac's backend to sanitize inputs
- Use web application firewalls (WAF) to block SQL metacharacters in query parameters
- Monitor server logs for SQL error patterns and anomalous query parameters

## Objectives

1. Confirm SQL Injection vulnerability by triggering errors
2. Expose database schema or error details for reconnaissance
3. Lay groundwork for advanced exploitation like data extraction

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the base Trac query URL and append a single quote to the 'report' parameter to inject a syntax-breaking payload.

**Command** ([[commands/curl-test-sqli-report]]):
```bash
curl "https://trac.torproject.org/projects/tor/query?status=closed&report=1'" -v
```

> This command sends a GET request with the injected single quote after 'report=1'. The verbose flag (-v) shows headers and response. Expected output includes a 500 Internal Server Error or similar, with the body containing a SQL syntax error like "near '1'": syntax error".

### Step 2: Analyze Response for Confirmation

**Context**: Inspect the response body for SQL error indicators to validate the vulnerability.

**Command** ([[commands/curl-test-sqli-report]]):
```bash
curl "https://trac.torproject.org/projects/tor/query?status=closed&report=1'" | grep -i "sql\|error\|syntax"
```

> Pipe the response through grep to filter for error keywords. Successful output will match SQL-related terms, confirming unsanitized input propagation to the database layer.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-sqli-report]]

## Tools Used


## Tags

- sqli
- web-vulnerability
- database-exploitation
