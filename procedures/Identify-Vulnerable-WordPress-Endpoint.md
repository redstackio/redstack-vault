---
id: proc-uuid-1
tags:
  - dos
  - wordpress
  - recon
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:30.151Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable WordPress Endpoint

## Summary

This procedure locates the /wp-admin/load-scripts.php endpoint in a WordPress installation, confirming it is accessible without authentication as required for CVE-2018-6389 exploitation.

## Description

The load-scripts.php script is part of WordPress core and handles concatenation of JavaScript files based on the 'load' parameter. Due to lack of authentication and no resource limits, it can be abused for DoS. This step involves reconnaissance to identify if the endpoint is exposed on the target site, typically by direct URL access or directory browsing.

## Requirements

1. Network access to the target WordPress site
2. Basic web browser or HTTP client
3. Knowledge of WordPress directory structure

## Defense

Defensive measures and detection strategies:

- Implement authentication on admin endpoints
- Use web application firewall (WAF) to block anomalous requests to /wp-admin/
- Monitor access logs for unauthenticated hits to load-scripts.php

## Objectives

1. Confirm endpoint exposure
2. Verify no auth barriers
3. Prepare for exploitation

## Instructions

### Step 1: Access the Endpoint

**Context**: Directly request the endpoint to check accessibility.

No specific command; use a browser to visit https://target.com/wp-admin/load-scripts.php or send a simple GET request.

**Expected Output**: HTTP 200 response with script loader content or minimal error.

### Step 2: Validate Vulnerability

**Context**: Check if the endpoint processes parameters without auth.

Append a basic 'load' parameter like ?load=common and observe response.

**Expected Output**: Concatenated JS output without login prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- wordpress
- recon
