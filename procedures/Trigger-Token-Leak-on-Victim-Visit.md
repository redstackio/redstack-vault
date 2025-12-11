---
tags:
  - xssi
  - token-leak
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Man in the Browser]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: eb079270-cbdd-412c-b02b-4116cde0f3c5
created_at: '2025-12-11T06:10:40.530Z'
updated_at: '2025-12-11T06:10:40.530Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1185]]'
---
# Trigger Token Leak on Victim Visit

## Summary

This procedure triggers the leakage of the security challenge token when a victim visits the malicious site, exploiting the lack of XSSI protection in the PayPal JS file.

## Description

Upon visiting, the victim's browser loads the included script, exposing tokens that the malicious JavaScript captures and sends to the attacker, setting up for credential exposure.

## Requirements

1. Victim must be lured to the malicious site.
2. Malicious site set up as per prior procedure.
3. Mechanism to receive leaked data (e.g., server endpoint).

## Defense

Defensive measures and detection strategies:

- Use browser extensions to block third-party scripts.
- Server-side monitoring for anomalous data exfiltration.

## Objectives

1. Capture leaked token from victim's browser.
2. Prepare token for use in challenge completion.
3. Advance to inducing victim login.

## Instructions

### Step 1: Lure Victim to Site

**Context**: Direct the victim to visit the malicious URL.

Use social engineering to have the victim navigate to the site.

> Upon visit, the script automatically leaks the token.

### Step 2: Capture Leaked Token

**Context**: Receive and store the token sent by the malicious JS.

Monitor your server logs or endpoint for the incoming token data.

> Example: Token appears in POST request to your capture endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Man in the Browser]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xssi]]
- [[token-leak]]
