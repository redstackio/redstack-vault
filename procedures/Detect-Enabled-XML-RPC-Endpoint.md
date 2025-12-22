---
id: proc-detect-xmlrpc
name: Detect Enabled XML-RPC Endpoint
tags:
  - wordpress
  - xmlrpc
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-check-xmlrpc]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:26:48.203Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Detect Enabled XML-RPC Endpoint

## Summary

This procedure checks for the presence and accessibility of the xmlrpc.php file in a WordPress installation, which if enabled, exposes the site to brute force and DoS risks.

## Description

WordPress XML-RPC is a feature that allows remote procedure calls, but when left enabled, it provides an unrestricted endpoint for methods like system.multicall (for brute forcing logins) and pingback.ping (for DoS via resource-intensive operations). This procedure involves sending an HTTP request to /xmlrpc.php to verify if it returns a successful response, indicating the service is active. The target is any public-facing WordPress site; no authentication is needed for detection. Successful detection confirms the vulnerability, rated critical due to potential for unauthorized access or service disruption.

## Requirements

1. Network access to the target website (HTTP/HTTPS)
2. curl or similar HTTP client installed
3. Knowledge of the target domain

## Defense

Defensive measures and detection strategies:

- Disable XML-RPC by adding code to functions.php or using plugins like Disable XML-RPC
- Monitor access logs for repeated requests to /xmlrpc.php
- Implement rate limiting on the endpoint

## Objectives

1. Verify XML-RPC endpoint accessibility
2. Identify WordPress sites vulnerable to related attacks
3. Assess initial attack surface for further exploitation

## Instructions

### Step 1: Send HEAD Request to Endpoint

**Context**: Use a lightweight HEAD request to check if the endpoint exists and is enabled without downloading the full body.

**Command** ([[commands/curl-check-xmlrpc]]):
```bash
curl -I https://target.com/xmlrpc.php
```

> This command sends a HEAD request to the XML-RPC endpoint. A 200 OK response indicates the service is enabled and accessible. Look for headers like Server: Apache or content indicating XML-RPC methods.

### Step 2: Validate Response

**Context**: Inspect the response for confirmation of XML-RPC activity.

**Command** ([[commands/curl-check-xmlrpc]] with verbose):
```bash
curl -v https://target.com/xmlrpc.php
```

> If the response includes XML like <methodName>system.listMethods</methodName> or a 200 status, the endpoint is active. Errors like 404 mean it's disabled or protected.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-check-xmlrpc]]

## Tools Used

- None

## Tags

- [[wordpress]]
- [[xmlrpc]]
- [[recon]]
