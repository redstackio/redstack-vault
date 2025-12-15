---
id: proc-uuid-002
tags:
  - information-disclosure
  - reconnaissance
  - javascript
  - sprockets
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-sprockets-js]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:18.098Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
  - '[[Exploit Public-Facing Application]]'
---
# Access-Exposed-Sprockets-Js-Source-Code

## Summary

This procedure retrieves a publicly accessible sprockets.js file from a web subdomain, disclosing client-side JavaScript source code including internal scripts for prototype pollution prevention, useful for reconnaissance.

## Description

Attackers access JavaScript assets intended for public use but containing source code details on misconfigured static sites. By requesting /sprockets.js, the full code is exposed, potentially revealing application logic. This is low-impact as it's client-side and often non-sensitive, but aids in understanding the tech stack. Target environment is web servers serving static files without minification or protection.

## Requirements

1. Public web endpoint serving JavaScript files
2. Basic HTTP client (curl or browser)
3. Knowledge of asset paths from prior recon (e.g., from .htaccess)

## Defense

Defensive measures and detection strategies:

- Minify and obfuscate JavaScript files before serving
- Use content security policies (CSP) to control script loading
- Log and alert on direct requests to source code files

## Objectives

1. Download and inspect JavaScript source for internal details
2. Identify potential vulnerabilities like pollution gadgets
3. Enhance reconnaissance on client-side behaviors

## Instructions

### Step 1: Request the JavaScript File

**Context**: Directly fetch the exposed JS file to view source code.

**Command** ([[commands/curl-access-sprockets-js]]):
```bash
curl https://_domainkey.launchpad.37signals.com/sprockets.js -o sprockets.js
```

> This downloads the file. In a browser, it loads directly. Expected output is JS code with functions for prototype pollution mitigation.

### Step 2: Review Source Code

**Context**: Analyze for sensitive logic or comments.

**Command** (No specific command; use editor):

> Examine sprockets.js for scripts like Object.freeze to prevent pollution. Note any application-specific code.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Software]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-sprockets-js]]

## Tools Used


## Tags

- information-disclosure
- reconnaissance
- javascript
- sprockets
