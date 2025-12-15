---
id: proc-uuid-4
tags:
  - csrf
  - exploitation
  - account-compromise
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
updated_at: '2025-12-14T17:27:29.889Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute CSRF to Reset Victim's Security Key

## Summary

This procedure finalizes the attack by processing the forged request on the server, resulting in the unauthorized reset of the victim's personal security key and potential account recovery disruption.

## Description

On secure.login.gov, the vulnerable endpoint processes the GET request using the victim's session cookies, bypassing origin checks. Scenario: Victim loads POC, request sent, server acts. Prerequisites: Active POC and victim session. Outcomes: Key reset, possible lockout.

## Requirements

1. Functional POC hosted
2. Victim authentication active
3. Monitoring for server response

## Defense

Defensive measures and detection strategies:

- Audit logs for unexpected key resets
- Rate-limit sensitive actions
- Require multi-factor confirmation for key changes

## Objectives

1. Trigger server-side action
2. Confirm unauthorized change
3. Assess impact on victim account

## Instructions

### Step 1: Monitor POC Access

**Context**: Watch for victim interaction.

Check hosting logs for page loads from victim's IP.

**Expected Output**: Access log entry.

### Step 2: Verify Reset Execution

**Context**: Confirm server processes the request.

Victim should receive reset notification; attacker can infer success via follow-up social engineering or public indicators.

**Expected Output**: Key resent/reset without victim intent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[key-reset]]
- [[exploitation]]
