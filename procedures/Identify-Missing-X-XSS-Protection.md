---
id: proc-identify-missing-xss-protection
tags:
  - xss
  - security-header
  - vulnerability-scanning
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-fetch-headers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:15:26.929Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify-Missing-X-XSS-Protection

## Summary

This procedure specifically checks for the absence of the X-XSS-Protection HTTP header, which mitigates reflected XSS in legacy browsers. Identifying its absence highlights a configuration flaw that could allow attackers to execute malicious scripts without browser sanitization.

## Description

The X-XSS-Protection header enables built-in XSS filters in browsers like Internet Explorer, Chrome, and Safari. Without it (e.g., on https://doc.owncloud.org/), servers like those using Nginx, Apache, or IIS fail to instruct browsers to block or sanitize XSS payloads, increasing the risk of arbitrary code execution in user sessions. This procedure builds on header inspection to pinpoint this exact vulnerability, aiding in reports like the HackerOne disclosure for ownCloud.

## Requirements

1. Prior header fetch from the target (e.g., via curl)
2. Knowledge of expected header values (1 or 1; mode=block)
3. Access to the web endpoint

## Defense

Defensive measures and detection strategies:

- Configure servers to include X-XSS-Protection: 1; mode=block
- Use tools like securityheaders.com for automated scanning
- Monitor for reconnaissance scans targeting headers

## Objectives

1. Confirm absence of X-XSS-Protection header
2. Evaluate impact on XSS protection
3. Recommend remediation for affected sites

## Instructions

### Step 1: Search for X-XSS-Protection in Headers

**Context**: Grep the header output to check specifically for the XSS protection header.

**Command** ([[commands/curl-fetch-headers]] with grep):
```bash
curl -s -I https://doc.owncloud.org/ | grep -i 'x-xss-protection'
```

> If no output, the header is missing, confirming the vulnerability. Expected successful output for protected sites: X-XSS-Protection: 1; mode=block.

### Step 2: Assess Impact and Document

**Context**: If missing, document the root cause (e.g., server config omission) and potential exploitation (reflected XSS leading to session hijacking).

**Command** (No command; manual analysis):

> Review browser compatibility: Affects IE8+, Chrome <78, Safari <12. Note increased susceptibility to attacks injecting <script> tags via URL parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-headers]]

## Tools Used


## Tags

- xss
- security-header
- web-vulnerability
