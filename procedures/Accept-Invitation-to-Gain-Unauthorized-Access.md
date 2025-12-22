---
tags:
  - auth-bypass
  - access-gain
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0e5e1b41-ff4c-4289-ba69-7c26afb1ea5b
created_at: '2025-12-14T17:24:45.523Z'
updated_at: '2025-12-14T17:24:45.523Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Accept-Invitation-to-Gain-Unauthorized-Access

## Summary

This procedure allows a non-2FA account to accept a collaborator invitation to a report in a 2FA-required HackerOne program, resulting in unauthorized access to sensitive content without multi-factor verification.

## Description

Building on the invitation step, this procedure demonstrates the final bypass by having the non-2FA account log in and accept the invite. The platform's failure to re-validate 2FA during acceptance grants full report access, including vulnerability details and program information. This occurs in the web interface of HackerOne and highlights a policy enforcement gap.

## Requirements

1. Pending invitation in the non-2FA account's notifications or email.
2. Login credentials for the non-2FA account.
3. No 2FA configured on the accepting account.

## Defense

Defensive measures and detection strategies:

- Require 2FA re-authentication upon invitation acceptance for secure programs.
- Monitor access logs for non-2FA logins to 2FA-required resources.
- Use anomaly detection for unusual collaborator additions.

## Objectives

1. Accept the invitation without 2FA prompts.
2. Verify access to the protected report.
3. Confirm the bypass by viewing sensitive data.

## Instructions

### Step 1: Log In to Non-2FA Account

**Context**: Access the HackerOne platform with the secondary account to check for the invitation.

Go to hackerone.com, log in with the non-2FA account credentials. No 2FA challenge should appear.

> Expected output: Successful login to the dashboard.

### Step 2: Accept the Invitation

**Context**: Locate and accept the collaborator invite to join the report.

Check notifications or email for the invitation link, click it, and confirm acceptance in the UI.

> Expected output: Access granted to the report; sensitive content (e.g., vulnerability description) visible without further authentication.

### Step 3: Validate Access

**Context**: Confirm unauthorized access by reviewing report details.

Navigate to the report in the shared programs section and inspect contents.

> Expected output: Full read access confirmed, proving 2FA bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[hackerone]]
