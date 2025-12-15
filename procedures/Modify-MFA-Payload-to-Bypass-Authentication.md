---
tags:
  - payload-modification
  - mfa-bypass
  - cookie-theft
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:24:48.280Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: c5846b5d-af69-4557-9546-ac0d3ba77254
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
  - '[[Steal Application Access Token]]'
---
# Modify-MFA-Payload-to-Bypass-Authentication

## Summary

Alter the intercepted JSON payload in the login request to switch MFA mode from 'sms' to 'email' and set 'secureLogin' to false, while including the stolen 'tdi' cookie and matching User-Agent, to bypass validation within the 15-minute device trust window.

## Description

In Burp Suite's Repeater or Proxy, edit the request body: Change the 'mode' field to 'email' (assuming original is 'sms'), set 'secureLogin': false. Ensure headers include the victim's 'tdi' (HTTP-only secure cookie) and exact User-Agent. The server trusts the device via cookie without re-validating mode or flags during the short window post-victim login, allowing bypass if timed correctly. Prerequisites: Stolen cookie/UA and recent victim activity.

## Requirements

1. Intercepted request in Burp
2. Victim's 'tdi' cookie and User-Agent
3. Timing within 15 minutes of victim login

## Defense

Defensive measures and detection strategies:

- Server-side validation of MFA mode and secureLogin flag
- Expire device trust cookies immediately or add mode-specific binding
- Monitor for payload discrepancies in logs

## Objectives

1. Exploit lack of validation on mode switching
2. Leverage device trust for unauthorized progression
3. Achieve MFA bypass without valid code

## Instructions

### Step 1: Edit JSON Payload

**Context**: Modify body to alter authentication parameters.

In request body, update {"mode": "sms", "secureLogin": true} to {"mode": "email", "secureLogin": false}.

> Expected: No syntax errors; payload valid JSON.

### Step 2: Update Headers

**Context**: Include session artifacts for trust.

Set Cookie: tdi=VICTIM_TDI_VALUE; User-Agent: Victim's UA string.

> Expected: Headers match victim's session.

### Step 3: Time and Verify

**Context**: Ensure within trust window.

Send only after victim's recent login; check for mode acceptance.

> Expected: Server processes without MFA re-challenge.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Modify Authentication Process]] Modify Authentication Process
- [[Steal Application Access Token]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[payload-modification]]
- [[mfa-bypass]]
- [[cookie-theft]]
