---
id: proc-code-review-xss-revive
tags:
  - code-review
  - xss
  - php
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:47:18.229Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Code-Review-to-Identify-XSS-in-Revive-Adserver

## Summary

This procedure involves manually reviewing the source code of Revive Adserver to identify a reflected XSS vulnerability in the afr.php file, where the untrusted QUERY_STRING is concatenated without encoding and inserted into HTML output.

## Description

In a code review scenario, examine the PHP files of Revive Adserver, particularly www/delivery/afr.php. The vulnerability stems from line 4381, where $dest = MAX_commonGetDeliveryUrl($conf['file']['frame']).'?'.$_SERVER['QUERY_STRING']; occurs without URL encoding. This $dest is then output into an HTML script tag at lines 4386-4387, allowing injected JavaScript to execute in the victim's browser. A similar issue exists in www/delivery_dev/afr.php. This procedure is the initial step in vulnerability discovery, enabling subsequent exploitation for attacks like session hijacking or CSRF.

## Requirements

1. Access to Revive Adserver source code (e.g., via GitHub or download)
2. Text editor or IDE for code analysis (e.g., VS Code)
3. Basic knowledge of PHP and web security

## Defense

Defensive measures and detection strategies:

- Implement static code analysis tools like SonarQube to flag unsanitized inputs
- Enforce URL encoding (e.g., urlencode()) for query strings before HTML insertion
- Use Content Security Policy (CSP) to mitigate XSS execution

## Objectives

1. Locate the exact lines of vulnerable code
2. Understand the root cause: lack of sanitization on $_SERVER['QUERY_STRING']
3. Confirm potential for arbitrary JavaScript execution

## Instructions

### Step 1: Download and Open Source Code

**Context**: Obtain the Revive Adserver codebase to begin static analysis.

Download the source from the official repository and open afr.php in your editor.

### Step 2: Search for QUERY_STRING Usage

**Context**: Identify assignments involving untrusted server variables.

Search for $_SERVER['QUERY_STRING'] and trace its usage. Note the concatenation at line 4381 without encoding.

### Step 3: Check HTML Output

**Context**: Verify insertion points in the response.

Examine lines 4386-4387 for direct output of $dest into a <script> tag, confirming XSS risk.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- code-review
- xss-discovery
