---
id: 00317fcc-f274-42bd-b277-24a545a3c7e4
name: Trigger-and-Observe-XSS-Execution
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.732Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
tags:
  - xss
  - execution
  - observation
  - web
platforms:
  - Web
commands: []
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Trigger-and-Observe-XSS-Execution

## Summary

This procedure triggers the reflected XSS by visiting the malicious URL in a browser with an established session, observing JavaScript execution to confirm the vulnerability and potential impacts like cookie theft.

## Description

After injecting the payload, visiting the crafted URL causes the browser to load the response with the unescaped JS, executing the injected code. In a real attack, this could steal cookies via alert(document.cookie) or perform open redirects. The target is the teavana.com web app on Demandware, and outcomes include arbitrary JS in the victim's context.

## Requirements

1. Browser with developer tools
2. Malicious URL from previous injection step
3. Active session from site access

## Defense

Defensive measures and detection strategies:

- Enable XSS protection headers (X-XSS-Protection)
- Use strict CSP to block inline scripts
- Monitor for alert() or unusual JS execution in client-side logs
- Rate-limit locale change requests

## Objectives

1. Execute injected JavaScript
2. Observe payload impact (e.g., alert, cookie access)
3. Validate vulnerability for further exploitation

## Instructions

### Step 1: Visit Malicious URL

**Context**: Load the full URL in the browser to trigger the response and JS execution.

Navigate to: https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Locale-Change?LocaleID=eas%27;alert(1);//dasdsan_CA

> The page loads, and the alert(1) should pop up immediately, confirming execution.

### Step 2: Inspect Execution

**Context**: Use developer tools to verify code run and access to sensitive data.

Open console (F12) and check for errors or executed code.

> Success if alert triggers; for impact, replace alert(1) with alert(document.cookie) to see cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[observation]]
- [[web]]
