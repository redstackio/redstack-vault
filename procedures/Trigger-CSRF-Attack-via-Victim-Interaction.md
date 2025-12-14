---
tags:
  - csrf
  - execution
  - deletion
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:23.503Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1c8202a2-4bd1-44aa-867e-8ef52531d603
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Trigger-CSRF-Attack-via-Victim-Interaction

## Summary

This procedure executes the CSRF attack by having the victim interact with the malicious HTML, sending forged POST requests to m.badoo.com for permanent account deletion or contact erasure.

## Description

Once opened, the HTML form submits using the victim's cookies, exploiting the session for unauthorized actions. The attack succeeds if the victim is logged in, leading to irreversible data loss. Monitoring involves checking victim feedback or site changes.

## Requirements

1. Victim has opened HTML in browser with active m.badoo.com session
2. HTML includes auto-submit or clear instructions
3. No direct attacker access; relies on victim action
4. Awareness of expected server responses

## Defense

Defensive measures and detection strategies:

- Require user confirmation for destructive actions
- Implement referrer checks in CSRF defenses
- Alert on sudden account deletions

## Objectives

1. Forge and send POST request from victim's browser
2. Achieve deletion or erasure without additional auth
3. Confirm impact on victim's account

## Instructions

### Step 1: Guide Victim Interaction

**Context**: Ensure submission occurs.

Instruct victim to click submit if not auto-submitting, or confirm file loads with session active.

### Step 2: Execute the Forged Request

**Context**: The browser handles submission.

Upon click/load, the form POSTs to e.g., https://m.badoo.com/api/account/delete with hidden fields and dummy param. Cookies authenticate it as legitimate.

### Step 3: Validate Attack Success

**Context**: Check outcomes.

Ask victim to log in; account should be gone, or contacts empty. Server may return JSON success without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Execution]]
- [[deletion]]
