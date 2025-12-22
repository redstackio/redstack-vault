---
tags:
  - csrf
  - exploitation
  - malicious-webpage
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.373Z'
sub_techniques: []
id: 876041c8-ac27-44bc-8b45-e180baaed13c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-CSRF-via-Malicious-Webpage

## Summary

This procedure demonstrates exploiting a CSRF vulnerability by crafting a malicious webpage that automatically submits forged requests to a vulnerable endpoint when visited by an authenticated user, enabling unauthorized actions like data modification.

## Description

Targeted at web applications lacking CSRF protections, such as a DoD website, this involves creating HTML/JavaScript to mimic legitimate requests. The scenario assumes the victim is authenticated and tricked into visiting the attacker's page (e.g., via email link). Outcomes include successful execution of state changes, like posting confidential info or redirecting data, highlighting the vulnerability's impact.

## Requirements

1. Identified vulnerable endpoint from prior reconnaissance
2. Ability to host a webpage (local server or external hosting)
3. Victim with active session on target site

## Defense

Defensive measures and detection strategies:

- Enforce CSRF token validation on all POST/PUT/DELETE requests
- Educate users on phishing risks and avoiding untrusted links
- Log and alert on state changes from suspicious user agents or referers

## Objectives

1. Forge and submit requests mimicking legitimate actions
2. Trick authenticated users into executing the exploit
3. Verify impact through observed changes on the target

## Instructions

### Step 1: Craft Malicious HTML

**Context**: Build a webpage with a hidden form or auto-submitting JavaScript targeting the vulnerable endpoint.

Create an HTML file with a form that posts to the target's URL, including necessary parameters for the unauthorized action (e.g., data update fields).

Example structure:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf-form" action="https://target-dod-site.com/vulnerable-endpoint" method="POST">
<input type="hidden" name="confidential_field" value="malicious_value">
</form>
<script>document.getElementById('csrf-form').submit();</script>
</body>
</html>
```

### Step 2: Host and Lure Victim

**Context**: Serve the page and direct the authenticated user to it.

Host the HTML on a web server (e.g., Python's SimpleHTTPServer) and send a phishing link to the victim.

**Expected Output**: Page loads and form submits automatically in victim's browser.

### Step 3: Verify Exploitation

**Context**: Confirm the forged request altered the target's state.

Access the target site as the victim or monitor logs to check for the unauthorized change.

**Expected Output**: Confidential information posted or modified as intended by attacker.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploitation]]
