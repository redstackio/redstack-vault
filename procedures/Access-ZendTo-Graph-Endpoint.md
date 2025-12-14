---
id: proc-access-graph-endpoint
tags:
  - web-access
  - endpoint-testing
  - zendto
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-graph]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:05.833Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-ZendTo-Graph-Endpoint

## Summary

This procedure accesses the graph.php endpoint in ZendTo with an authenticated session to confirm functionality and prepare for parameter manipulation in LFI exploitation.

## Description

The graph.php file in ZendTo 5.11 handles RRD graph rendering but is vulnerable to parameter tampering. This step verifies access using the 'p' parameter, ensuring the session is valid in a PHP/Apache web environment before attempting traversal.

## Requirements

1. Active session cookie from prior login
2. Network access to https://████/graph.php
3. Basic understanding of HTTP GET requests

## Defense

Defensive measures and detection strategies:

- Rate-limit requests to sensitive endpoints like graph.php
- Log all parameter values and scan for traversal patterns (e.g., ../)
- Enforce authentication checks and session validation on all endpoints

## Objectives

1. Load the endpoint without errors
2. Observe normal RRD data handling
3. Set stage for vulnerability testing

## Instructions

### Step 1: Send Authenticated Request to Endpoint

**Context**: Visit graph.php with a benign parameter to test access.

**Command** ([[commands/curl-access-graph]]):
```bash
curl -b cookies.txt 'https://████/graph.php?p=7' -o response.html
```

> Saves the response to response.html; expect RRD graph content or image data.

### Step 2: Inspect Response

**Context**: Review output for successful loading.

**Command** ([[commands/cat-response]]):
```bash
cat response.html
```

> Look for graph elements or no 403/401 errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-access-graph]]
- [[commands/cat-response]]

## Tools Used


## Tags

- endpoint-access
- authentication-required
- zendto-graph
