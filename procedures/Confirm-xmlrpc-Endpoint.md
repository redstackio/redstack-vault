---
id: proc-confirm-xmlrpc-endpoint
tags:
  - recon
  - wordpress
  - xmlrpc
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-basic-get]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T04:08:46.018Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Confirm-xmlrpc-Endpoint

## Summary

This procedure verifies the presence and accessibility of the xmlrpc.php endpoint in a WordPress installation, confirming it accepts POST requests without authentication, as a precursor to SSRF exploitation.

## Description

WordPress sites often expose xmlrpc.php for remote procedures, which can be vulnerable to SSRF if unvalidated. This step involves sending a simple GET request to elicit the characteristic response, identifying the endpoint for further testing. It applies to public-facing web apps and requires no special access.

## Requirements

1. Target URL accessible via HTTP/HTTPS
2. Basic HTTP client like curl
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Block or remove xmlrpc.php if not needed
- Log access to xmlrpc.php and alert on anomalous patterns
- Use WAF rules to restrict methods on XML-RPC endpoints

## Objectives

1. Confirm endpoint existence and POST requirement
2. Identify unauthenticated access
3. Prepare for payload crafting

## Instructions

### Step 1: Send GET Request to Endpoint

**Context**: Probe the endpoint to observe its behavior.

**Command** ([[commands/curl-basic-get]]):
```bash
curl -X GET https://target/xmlrpc.php
```

> This command sends a GET request and returns the response body, expecting "XML-RPC server accepts POST requests only."

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-basic-get]]

## Tools Used


## Tags

- [[recon]]
- [[wordpress]]
