---
tags:
  - recon
  - wordpress
  - vulnerability-scan
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-check-wp]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:26:30.046Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: bea8ed68-3601-4f35-b8a0-6529bb236ff8
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable WordPress Site

## Summary

This procedure scans a target website to confirm it runs a vulnerable version of WordPress (pre-4.9.5) with the SWFUpload component exposed, setting the stage for CVE-2018-6389 exploitation.

## Description

WordPress sites can be fingerprinted by checking meta tags, generator fields, or specific endpoints like /wp-admin/. CVE-2018-6389 affects the SWFUpload library used in admin-ajax.php for upload handling, allowing unauthenticated DoS. This step involves HTTP requests to detect these indicators without triggering alerts.

## Requirements

1. Network access to the target domain (e.g., https://blog.makerdao.com/)
2. curl or similar HTTP client installed
3. Basic knowledge of HTTP responses and WordPress structure

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) to block unusual /wp-admin/ probes
- Use version hiding plugins to obscure WordPress fingerprints
- Monitor access logs for repeated GET/POST to admin-ajax.php

## Objectives

1. Confirm WordPress presence and version vulnerability
2. Verify accessibility of SWFUpload endpoint
3. Avoid detection during reconnaissance

## Instructions

### Step 1: Fingerprint WordPress Installation

**Context**: Retrieve the homepage and search for WordPress indicators like the generator meta tag.

**Command** ([[commands/curl-check-wp]]):
```bash
curl -s https://blog.makerdao.com/ | grep -i generator
```

> This command fetches the page silently and greps for 'WordPress' in meta tags. Expected output: <meta name="generator" content="WordPress 4.x" /> or similar, indicating version < 4.9.5.

### Step 2: Probe Vulnerable Endpoint

**Context**: Test the SWFUpload action endpoint without authentication to confirm exposure.

**Command** ([[commands/curl-check-wp]]):
```bash
curl -s "https://blog.makerdao.com/wp-admin/admin-ajax.php?action=upload-errors"
```

> Sends a GET request to the ajax endpoint. Successful output: JSON response or empty string without 403/401 errors, confirming unauthenticated access.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-wp]]

## Tools Used


## Tags

- [[recon]]
- [[wordpress]]
