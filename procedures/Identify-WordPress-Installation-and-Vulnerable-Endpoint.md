---
id: proc-identify-wordpress-endpoint
name: Identify WordPress Installation and Vulnerable Endpoint
tags:
  - recon
  - wordpress
  - dos
type: procedure
tools:
  - '[[tools/Apache-JMeter]]'
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:26:36.835Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify WordPress Installation and Vulnerable Endpoint

## Summary

This procedure scans a target website to confirm it runs a vulnerable WordPress installation and verifies access to the /wp-admin/load-scripts.php endpoint exploited in CVE-2018-6389 for denial-of-service attacks.

## Description

In a typical attack scenario, reconnaissance identifies WordPress sites via common indicators like /wp-content/ directories or meta tags. The vulnerable endpoint loads and concatenates JavaScript files based on a 'load' parameter without authentication, making it ideal for resource exhaustion. This step ensures the target is suitable before proceeding to exploitation, targeting public sites like https://iandunn.name/.

## Requirements

1. Network access to the target website.
2. Browser or basic HTTP client for inspection.
3. Knowledge of WordPress fingerprints (e.g., version <5.0.1 unpatched).

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) rules to block unauthenticated access to admin endpoints.
- Enable rate-limiting on /wp-admin/ paths using tools like nginx limit_req.
- Monitor for anomalous requests to load-scripts.php via logs (e.g., high data output).

## Objectives

1. Confirm WordPress presence and version.
2. Validate unauthenticated access to the endpoint.
3. Identify potential for resource exhaustion.

## Instructions

### Step 1: Inspect Site for WordPress Indicators

**Context**: Check HTML source or headers for WordPress signatures to confirm the platform.

Browse to https://target/ and view page source. Look for <meta name="generator" content="WordPress x.x"> or requests to /wp-includes/.

**Expected Output**: Confirmation of WordPress installation.

### Step 2: Test Vulnerable Endpoint Access

**Context**: Send a basic request to verify the endpoint responds without authentication.

Use a browser or curl to access https://target/wp-admin/load-scripts.php?load=common.

```bash
curl "https://iandunn.name/wp-admin/load-scripts.php?load=common" -o response.js
```

> This fetches and saves the concatenated JS files. Check file size and content for success.

**Expected Output**: JavaScript response without 401/403 errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Impact

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Apache-JMeter]]

## Tags

- [[recon]]
- [[wordpress]]
