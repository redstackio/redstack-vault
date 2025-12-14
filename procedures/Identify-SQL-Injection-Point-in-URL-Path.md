---
tags:
  - sqli
  - injection-point
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.357Z'
sub_techniques: []
id: fa73aae8-2f6f-44ea-a770-5115567389ab
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify SQL Injection Point in URL Path

## Summary

This procedure identifies a SQL injection vulnerability in the URL path processing of a web application by injecting a single quote to disrupt SQL syntax and observe error responses.

## Description

In the context of www.ibm.com, the URL path after the leading slash is directly incorporated into SQL queries without proper sanitization. Injecting a single quote (') immediately after the slash causes a SQL syntax error, confirming the vulnerability. This step is foundational for blind SQLi exploitation where no direct error messages are returned.

## Requirements

1. Access to a tool like curl or a browser for sending HTTP requests
2. Internet connectivity to reach the target (www.ibm.com)
3. Basic understanding of HTTP requests and SQL syntax

## Defense

Defensive measures and detection strategies:

- Implement URL path sanitization and parameterized queries
- Use web application firewalls (WAF) to block anomalous path injections
- Monitor server logs for 500 errors correlated with path manipulations

## Objectives

1. Confirm SQL injection vulnerability in URL path
2. Establish the exact injection point (after leading slash)
3. Prepare for response-based exploitation

## Instructions

### Step 1: Send Basic Injection Payload

**Context**: Test the injection point by appending a single quote to the URL path to break SQL syntax.

**Command** ([[commands/curl-send-request]]):
```bash
curl -i "https://www.ibm.com/'"
```

> This sends a GET request to the malformed URL. A successful injection triggers a 500 error due to unclosed SQL string.

### Step 2: Validate Normal vs. Injected Response

**Context**: Compare with a normal request to confirm the error is injection-induced.

**Command** ([[commands/curl-send-request]]):
```bash
curl -i "https://www.ibm.com/"
```

> Normal requests return a 200 OK with page content; injected ones return 500, indicating vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-request]]

## Tools Used


## Tags

- [[sqli]]
- [[web]]
