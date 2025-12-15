---
tags:
  - rce
  - xss
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Python]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d5e73454-4233-4014-a54d-c58fc1a193b6
created_at: '2025-12-14T17:23:24.042Z'
updated_at: '2025-12-14T17:23:24.042Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Python]]'
  - '[[JavaScript]]'
---
# Execute-Malicious-Code-and-Observe-Impact

## Summary

This procedure runs commands via the RCE payload and tests XSS by accessing uploaded HTML, demonstrating data theft, server takeover, or script execution.

## Description

Post-direct access, interact with the PHP shell for actions like cat config.php or rm -rf /; for XSS, upload HTML with <script>alert('XSS')</script> and access directly. Targets misconfigs on HTTP/HTTPS; outcomes include full compromise or session hijacking.

## Requirements

1. Active RCE via direct PHP access
2. XSS payload (HTML file with JavaScript)
3. Victim browser for XSS testing

## Defense

Defensive measures and detection strategies:

- Regularly audit admin settings for .htaccess checks on all ports
- Implement Content Security Policy (CSP) to mitigate XSS
- Log and alert on anomalous file executions or JS injections

## Objectives

1. Achieve server-side code execution for persistence
2. Trigger client-side XSS for further attacks
3. Validate impact like data exfiltration

## Instructions

### Step 1: Run RCE Commands

**Context**: Use the PHP shell to execute system commands.

Append ?cmd=ls / to the direct URL and reload.

> Output lists directory contents; extend to steal data or modify files.

### Step 2: Test XSS with HTML Upload

**Context**: Upload and access HTML for JavaScript execution.

Upload 'xss.html' with <script>alert(document.cookie)</script>, then access /data/attacker/files/xss.html.

> Alert pops with cookies, enabling phishing or hijacking.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Python]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[xss]]
- [[exploitation]]
