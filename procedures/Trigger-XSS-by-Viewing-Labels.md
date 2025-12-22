---
tags:
  - xss-trigger
  - execution
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.968Z'
sub_techniques: []
id: 4a75ceb5-9a2c-4deb-95ea-a1b088912dcb
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Viewing-Labels

## Summary

This procedure triggers the stored XSS payload by accessing project labels or issues in GitLab, executing JavaScript in the victim's browser context for potential data theft or account takeover.

## Description

Once imported, the malicious label color injects HTML/JS that renders when viewing /labels or /issues. The payload creates a hidden form with a script in an input title, evading CSP. On load, alert(document.domain) fires, but in real attacks, it could steal tokens, access private repos, or perform DoS.

## Requirements

1. Imported project accessible to victim
2. Victim's browser session on GitLab
3. No additional tools; browser access suffices

## Defense

Defensive measures and detection strategies:

- Escape user-controlled data in label rendering (e.g., color as CSS only)
- Enable strict CSP reporting and blocking
- Monitor for anomalous script executions via browser dev tools or WAF

## Objectives

1. Execute injected JavaScript
2. Demonstrate impact like domain alert or data exfil
3. Validate persistence across views

## Instructions

### Step 1: Access Malicious Page

**Context**: Load a page rendering the infected label.

Navigate to https://gitlab.com/yvvdwf-group-a/xss-on-label-color/-/labels or https://gitlab.com/yvvdwf-group-a/xss-on-label-color/-/issues/1.

> Expected output: Page loads with alert('gitlab.com') popping up, confirming XSS. In production, replace alert with fetch to attacker server for exfil.

### Step 2: Verify Execution

**Context**: Check for payload effects.

Inspect page source for injected <form> and <script>; test in incognito to simulate victim.

> Expected output: Script runs on DOM load; no server-side errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[Execution]]
- [[gitlab]]
