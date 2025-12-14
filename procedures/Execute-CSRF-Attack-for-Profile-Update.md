---
tags:
  - csrf
  - execution
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
updated_at: '2025-12-14T17:33:24.322Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a35c717e-d592-4c16-92f0-7978c6382fbe
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-CSRF-Attack-for-Profile-Update

## Summary

This procedure delivers and triggers the malicious HTML payload to the victim, causing an automatic POST request to the unprotected profile endpoint, resulting in unauthorized updates including password change.

## Description

With the victim logged in (active session), loading the HTML in their browser submits the form cross-origin to myprofile.asp?update=yes. The lack of CSRF protection allows the request to process, altering profile data and resetting the password to '████'. This achieves account takeover. Delivery can be via phishing link to the hosted HTML.

## Requirements

1. Victim's browser must have an active session to the target site
2. Hosted malicious HTML accessible via URL
3. Social engineering to get victim to load the page (e.g., email lure)

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens or stateful checks for sensitive actions like password changes
- Block or warn on auto-submitting forms from external domains
- Audit logs for profile changes without corresponding GET requests

## Objectives

1. Forge and submit the profile update request
2. Confirm silent execution without victim awareness
3. Achieve password reset for takeover

## Instructions

### Step 1: Deliver the Payload

**Context**: Get the victim to load the HTML while authenticated.

Send a phishing email or link pointing to the hosted HTML file (e.g., http://attacker.com/csrf.html).

> Expected output: Victim clicks and loads the page; no visible content due to auto-submit.

### Step 2: Trigger Submission

**Context**: The embedded JavaScript handles auto-submission upon load.

Monitor network traffic (if possible) or wait for ~1-2 seconds post-load.

The form POSTs to:

```http
POST /█████████/myprofile.asp?update=yes HTTP/1.1
Host: ████████
Content-Type: application/x-www-form-urlencoded

txtFName=VictimFirst&txtPassword=████&txtVeriPW=████
```

> Expected output: Server processes the request (200 OK), updating the profile. Victim may see a brief redirect or nothing.

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
- [[Execution]]
