---
tags:
  - csrf
  - drive-by
  - web-exploit
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
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:35.805Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4ff0b4c5-8e0d-4407-a116-e657c8698c43
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-CSRF-via-Browser-Submission

## Summary

This procedure delivers the malicious HTML to an authenticated victim, triggering the CSRF request to delete their profile upon page load or interaction.

## Description

With the victim logged in, loading the attacker's HTML sends a forged GET request using the browser's session cookies, exploiting the lack of CSRF protection. This is a drive-by style attack where visiting the page (e.g., via phishing link) executes the deletion. Target: Browsers with active sessions; outcomes: Immediate account deactivation. Prerequisites: Victim authentication and access to the HTML.

## Requirements

1. Hosted malicious HTML (local or remote)
2. Luring mechanism (e.g., email link to the page)
3. Victim's browser with target site session active

## Defense

Defensive measures and detection strategies:

- Convert sensitive actions to POST and require CSRF tokens
- Educate users on phishing and unexpected page behaviors
- Log and alert on anomalous deletion requests

## Objectives

1. Execute the forged request in victim's context
2. Achieve account deletion without direct interaction
3. Confirm exploit success via application response

## Instructions

### Step 1: Deliver HTML to Victim

**Context**: Host the HTML or send via link to trick the victim into opening it while authenticated.

No command; use a phishing email or direct link to csrf.html.

> Victim clicks and loads the page in their browser.

### Step 2: Submit Form

**Context**: The HTML auto-submits or prompts click, sending the GET request.

Observe in browser dev tools:

```http
GET /account/delete?action=delete_profile HTTP/1.1
Host: target.com
Cookie: session=valid_token
```

> Expected: Server processes deletion; account is deactivated. Check target site for confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[drive-by]]
- [[web-exploit]]
