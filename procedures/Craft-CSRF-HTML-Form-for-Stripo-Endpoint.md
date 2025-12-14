---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
name: Craft-CSRF-HTML-Form-for-Stripo-Endpoint
tags:
  - csrf
  - exploit
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
updated_at: '2025-12-14T17:27:35.758Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-CSRF-HTML-Form-for-Stripo-Endpoint

## Summary

This procedure creates a malicious HTML page with an auto-submitting form that forges a POST request to Stripo's resend confirmation endpoint, exploiting the lack of CSRF protection to trigger unwanted email resends.

## Description

Based on the intercepted request, the attacker crafts a simple HTML document containing a form targeted at https://my.stripo.email/cabinet/stripeapi/v1/resendEmailConfirmation. The form uses method='POST' and auto-submits via onload event, ensuring no user interaction is needed. When loaded in a victim's browser (while authenticated to Stripo), it leverages the existing session cookies to send the request cross-origin, bypassing protections due to the endpoint's acceptance of empty bodies without token validation or content-type requirements.

## Requirements

1. Text editor to create the HTML file
2. Knowledge of the vulnerable endpoint from prior interception
3. Victim must be authenticated to Stripo in their browser

## Defense

Defensive measures and detection strategies:

- Require unique CSRF tokens in all forms and validate them server-side
- Restrict POST requests to same-origin only via CORS policies
- Log and alert on resend requests from suspicious user-agents or referers

## Objectives

1. Forge the resend request without user knowledge
2. Exploit session-based authentication
3. Trigger email delivery to victim's inbox

## Instructions

### Step 1: Create HTML Structure

**Context**: Build the basic form targeting the endpoint.

Open a text editor and write the HTML with a form element:

```html
<form name="form" method="POST" action="https://my.stripo.email/cabinet/stripeapi/v1/resendEmailConfirmation">
</form>
```

### Step 2: Add Auto-Submit Functionality

**Context**: Ensure the form submits immediately upon page load.

Add a body with onload attribute to trigger submission:

```html
<body onload="document.form.submit()"><form name="form" method="POST" action="https://my.stripo.email/cabinet/stripeapi/v1/resendEmailConfirmation"></form></body>
```

Save as resendEmail.html.

**Expected Output**: A minimal HTML file ready for hosting; when opened in a browser with Stripo session, it auto-submits the POST.

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
- [[web]]
- [[exploit]]
