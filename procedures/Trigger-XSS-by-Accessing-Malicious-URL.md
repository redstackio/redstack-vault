---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - execution
  - data-theft
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:06.104Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS by Accessing Malicious URL

## Summary

This procedure executes the crafted XSS payload by visiting the malicious URL, demonstrating arbitrary JavaScript execution and potential for stealing session data on smarthistory.khanacademy.org.

## Description

Accessing the injected URL causes the browser to parse and run the script in the victim's context, allowing actions like alerting, cookie theft, or phishing. The vulnerability enables injection of JavaScript, VBScript, ActiveX, HTML, or Flash, with impacts including deception and credential theft.

## Requirements

1. Web browser with JavaScript enabled
2. The crafted malicious URL from prior procedure
3. Optional: Victim simulation via different browser sessions

## Defense

Defensive measures and detection strategies:

- Deploy browser extensions like NoScript to block XSS
- Implement HTTP-only cookies to prevent theft
- Use web application firewalls (WAF) to detect and block injected scripts

## Objectives

1. Confirm JavaScript execution in browser
2. Simulate data exfiltration
3. Assess impact on user sessions

## Instructions

### Step 1: Load the Malicious URL

**Context**: Direct browser access triggers the reflection and execution.

Enter or paste http://smarthistory.khanacademy.org/Campin"><script>alert(/BigBear/)</script>.html into the address bar and press Enter.

> The page loads, and the alert popup appears, confirming success.

### Step 2: Verify Execution and Impact

**Context**: Inspect for data access capabilities.

Open browser console (F12) and replace alert with document.cookie to test theft.

> Expected output: Cookies or session data logged, proving exfiltration potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]

