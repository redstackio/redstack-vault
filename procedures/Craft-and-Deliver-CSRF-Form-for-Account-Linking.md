---
tags:
  - csrf
  - form-craft
  - account-linking
  - weblate
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:33:06.237Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e47c1098-e268-4ccc-a4cf-01bd1eb887fd
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft and Deliver CSRF Form for Account Linking

## Summary

This procedure constructs an HTML form using the intercepted OpenID parameters to exploit the CSRF vulnerability, forcing the victim's browser to submit the data and link the attacker's Ubuntu One account to their Weblate profile.

## Description

Exploiting the Python Social Auth library's failure to validate CSRF in the Ubuntu One completion endpoint, this step creates a malicious HTML page that auto-posts the captured parameters (e.g., identity, email, nonce, signature) to /accounts/complete/ubuntu/. When loaded in the victim's logged-in session, it completes the association without user interaction. Delivery can be via phishing email, malicious site, or social engineering. Prerequisites: Intercepted parameters from prior step and victim's Weblate session. Outcome: Silent account linking, setting up takeover.

## Requirements

1. Captured OpenID parameters from interception (e.g., openid.identity=..., janrain_nonce=...)
2. Basic HTML knowledge to build the form
3. Method to deliver HTML to victim (e.g., hosted URL, email attachment)
4. Victim must be logged into Weblate during form submission

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to all auth completion endpoints and validate on server-side
- Use nonce or state parameters tied to the user's session for third-party auth
- Log and alert on unexpected third-party associations or cross-origin POSTs

## Objectives

1. Replay OpenID response cross-site under victim session
2. Complete unauthorized account linking
3. Avoid detection by mimicking legitimate auth flow

## Instructions

### Step 1: Extract Parameters from Intercepted Request

**Context**: Parse the dropped Burp request to gather all POST data.

In Burp Suite, copy parameters like openid.mode, openid.identity, openid.ax.value.email.1, janrain_nonce, openid.sig.

> List of key-value pairs ready for form inputs.

### Step 2: Build the CSRF HTML Form

**Context**: Create a self-submitting form targeting the vulnerable endpoint.

Write HTML: <form action="https://demo.weblate.org/accounts/complete/ubuntu/" method="POST"><input type="hidden" name="openid.identity" value="..."> (repeat for all params) <input type="submit"> <script>document.forms[0].submit();</script></form>.

> Form auto-submits on load, posting data without user action.

### Step 3: Host and Deliver the Form to Victim

**Context**: Ensure victim loads it while authenticated to Weblate.

Host on a server (e.g., GitHub Pages, ngrok) or embed in email; trick victim into clicking/opening (e.g., 'Check this translation update').

> Victim's browser executes the POST in their session context.

### Step 4: Verify Linking

**Context**: Confirm the association occurred.

Check attacker's Ubuntu One or Weblate profile for new links; attempt login as victim.

> Success if Ubuntu auth now grants victim's access.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- csrf-payload
- html-form
- session-hijack
