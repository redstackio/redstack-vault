---
id: proc-003
tags:
  - csrf-execution
  - account-takeover
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:32:58.121Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Execute-CSRF-Attack-via-Malicious-HTML

## Summary

This procedure delivers and triggers a CSRF PoC HTML page to an authenticated victim, forging a profile update request that modifies sensitive account details for takeover.

## Description

Once the CSRF PoC is generated, this step involves saving or hosting the HTML and using social engineering to lure the victim to load it while their session is active on the target site. The malicious page contains a form that auto-posts to the unprotected endpoint (e.g., POST https://█████ with action=save_info), updating username, email, and password without user consent. The attack relies on the victim's browser sending the session cookie with the forged request, exploiting the lack of CSRF tokens.

## Requirements

1. Generated CSRF PoC HTML file
2. Attacker-controlled hosting (optional; local file for testing)
3. Victim authenticated to target and visitable via link

## Defense

Defensive measures and detection strategies:

- Require user confirmation for sensitive actions (e.g., password changes)
- Log and alert on rapid profile modifications from unexpected referers
- Educate users on phishing and suspicious links

## Objectives

1. Trick victim into loading the PoC while authenticated
2. Forge and submit the state-changing request
3. Achieve account control via updated credentials

## Instructions

### Step 1: Prepare Delivery

**Context**: Make the PoC accessible to the victim.

Save the HTML as csrf-poc.html or host on a server (e.g., via Python http.server).

> For testing, open locally; for attack, send link via email/phishing. Expected output: Page loads with form visible or auto-submitting.

### Step 2: Trigger the Attack

**Context**: Ensure victim visits while session is valid.

Victim clicks link; browser loads HTML and submits form to target endpoint.

> The POST includes session cookie, updating profile (e.g., new email/password). Expected output: No errors; changes apply silently.

### Step 3: Verify Takeover

**Context**: Confirm control over the account.

Log in with new credentials provided in PoC.

> Success if access granted with modified details. Check app logs if available.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Credential Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-execution]]
- [[account-takeover]]
- [[web]]
