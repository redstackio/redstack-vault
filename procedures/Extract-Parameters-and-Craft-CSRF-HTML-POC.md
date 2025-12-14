---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - csrf-poc
  - html-craft
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:42.886Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Parameters-and-Craft-CSRF-HTML-POC

## Summary

This procedure extracts authentication parameters from the Liberapay confirmation link and crafts a malicious HTML form to exploit the CSRF vulnerability.

## Description

By parsing the email link, the attacker obtains log-in.id, log-in.key, and log-in.token. These are inserted into an HTML form that POSTs to https://liberapay.com/about/ without CSRF protection. JavaScript auto-submits the form on load, mimicking user action cross-site. Burp Suite aids in extraction and testing. Outcome: A POC that forces login when loaded by the victim.

## Requirements

1. Confirmation link from previous step
2. Text editor for HTML
3. [[tools/Burp-Suite-Professional]] for parsing/testing
4. Local web server for POC hosting

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all POST endpoints
- Scan for anomalous form submissions from external sites

## Objectives

1. Extract sensitive parameters
2. Build functional CSRF POC
3. Test submission without errors

## Instructions

### Step 1: Parse Confirmation Link

**Context**: Extract id, key, token using interception or manual inspection.

Use [[tools/Burp-Suite-Professional]] to capture the link if simulating, or copy from email.

> URL example: https://liberapay.com/about/?log-in.id=123&log-in.key=abc&log-in.token=xyz. Note values.

### Step 2: Create HTML Form

**Context**: Build the POC with hidden inputs and auto-submit.

In a text editor, write the HTML as shown in the attack chain, replacing placeholders.

```html
<input type="hidden" name="log-in.id" value="123" />
<input type="hidden" name="log-in.key" value="abc" />
<input type="hidden" name="log-in.token" value="xyz" />
<script>document.getElementById('csrf-form').submit();</script>
```

> Save as .html; test in browser to ensure POST occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[csrf]]
- [[poc]]
