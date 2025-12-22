---
id: proc-trigger-xss-clickjacking
tags:
  - xss
  - clickjacking
  - data-exfiltration
type: procedure
tools:
  - '[[tools/Microsoft-Edge]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Microsoft Edge
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:55.180Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Trigger-XSS-via-Clickjacking-Interaction

## Summary

This procedure uses clickjacking on the PoC page to trick the user into clicking a link in the URL Advisor frame, executing the injected javascript: URL in the context of the spoofed domain like google.com.

## Description

After loading the PoC, the page overlays a transparent iframe or element to clickjack the URL Advisor balloon. Clicking sets the link target to a malicious javascript: URL, executing JS such as alert('Hi, this JavaScript code is running on ' + document.domain). This runs in any domain's context due to first-party serving, enabling exfiltration. Prerequisites: PoC loaded; outcome: arbitrary JS execution.

## Requirements

1. PoC page loaded in Edge with URL Advisor active
2. User interaction (mouse movement and click)
3. No clickjacking protections enabled in browser

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options or CSP frame-ancestors in security UIs
- Educate users on suspicious popups and alerts
- Detect anomalous JS execution in security software logs

## Objectives

1. Force click to inject and execute javascript: URL
2. Achieve universal XSS in target domain context
3. Demonstrate exfiltration capability

## Instructions

### Step 1: Initiate Interaction

**Context**: Move mouse over the page to align the clickjacking element with the balloon link.

**Command** (User action):
```bash
# No CLI; hover and position mouse as guided by PoC visuals
```

> The PoC implements clickjacking; expected: invisible overlay positions click over the vulnerable link.

### Step 2: Execute Click

**Context**: Click to trigger the unsanitized link target assignment and execution.

**Command** (User action):
```bash
# Click the overlaid element
```

> Click executes javascript:alert('Hi, this JavaScript code is running on ' + document.domain); alert confirms context like www.google.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Microsoft-Edge]]

## Tags

- xss
- clickjacking
- data-exfiltration
