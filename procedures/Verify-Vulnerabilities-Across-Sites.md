---
id: proc-verify-vulnerabilities-across-sites
name: Verify-Vulnerabilities-Across-Sites
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.271Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - verification
  - multi-site
  - xss
  - open-redirect
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---

# Verify-Vulnerabilities-Across-Sites

## Summary

This procedure tests open redirect and XSS payloads across multiple Starbucks domains and parameters to confirm widespread exploitability, excluding main starbucks.* domains, ensuring comprehensive vulnerability assessment.

## Description

By systematically applying payloads to sites like shop.starbucks.de, teavana.com, and store.starbucks.com, this verifies injection points in root URLs and GET parameters. It highlights the vulnerability's scope for potential mass phishing or data theft.

## Requirements

1. List of target domains
2. Previously crafted payloads
3. Browser for manual testing

## Defense

Defensive measures and detection strategies:

- Conduct regular vulnerability scans across all subdomains
- Centralize input validation policies
- Monitor for anomalous traffic patterns to multiple sites

## Objectives

1. Confirm vulnerability persistence across ecosystem
2. Identify all exploitable injection points
3. Assess overall impact for reporting

## Instructions

### Step 1: Test on Primary Site

**Context**: Apply payloads to shop.starbucks.de root and parameters.

Use <>//google.com and <>javascript:alert('xss');

> Verify redirect and alert on multiple parameters.

### Step 2: Extend to Other Sites

**Context**: Repeat on teavana.com and store.starbucks.com.

Load equivalent URLs.

> Success if exploits work consistently, noting any exceptions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[multi-site]]
