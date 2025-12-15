---
tags:
  - credential-association
  - silent-takeover
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
detection_risk: low
sub_techniques: []
id: d26bd327-a334-46f3-8cf5-f1c1965453dc
created_at: '2025-12-14T17:33:34.474Z'
updated_at: '2025-12-14T17:33:34.474Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Associate-Attacker-Phone-with-Victim-Account

## Summary

Exploit the accepted postMessage to have the Digits SDK resolve and associate the attacker's phone number and tokens with the victim's account session.

## Description

In the SDK's onReceiveMessage function, the origin is validated via this.config.get('sdk_host').search(t.origin), which treats the fake origin as a matching regex. The function then processes the fake data, updating the session to use the attacker's phone without prompting the user.

## Requirements

1. PostMessage event successfully received by SDK
2. Victim's browser executing the site's JS
3. No additional auth checks in the integration

## Defense

Defensive measures and detection strategies:

- Add explicit origin whitelisting
- Require user confirmation for phone changes
- Audit SDK for regex vulnerabilities

## Objectives

1. Bypass validation and process fake sign-in
2. Update account association silently
3. Prepare for takeover

## Instructions

### Step 1: Monitor SDK Processing

**Context**: Ensure the search() returns a match.

**Instructions**: In dev tools, the SDK logs or network shows data resolution.

### Step 2: Confirm Association

**Context**: Verify phone linkage.

**Instructions**: Check site API calls post-event; phone should now be attacker's.

### Step 3: Handle Any Edge Cases

**Context**: If partial failure, retry interaction.

**Instructions**: Reload page or re-trigger if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-linkage]]
- [[validation-bypass]]
