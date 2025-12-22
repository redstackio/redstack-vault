---
tags:
  - xss
  - easypay
  - multiple-triggers
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.716Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ee9797b6-26f2-47fa-b9e1-a767e8df96f8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Victim-Views-Easypay-Section-Triggering-XSS

## Summary

This procedure triggers multiple XSS instances by viewing the easypay section of the requests page, where both username and easy payment name fields reflect the unsanitized payload.

## Description

The easypay anchor on the requests page displays user names without encoding, executing the stored script upon load or interaction. This expands the attack surface with repeated firings. Prerequisites: Requests page access; outcomes: Enhanced execution opportunities.

## Requirements

1. Victim on requests page
2. Easypay feature enabled
3. Payload in username and payment name

## Defense

Defensive measures and detection strategies:

- Sanitize all fields in payment-related displays
- Segment easypay rendering with isolated encoding
- Monitor for XSS in payment contexts via anomaly detection

## Objectives

1. Load easypay section
2. Reflect multiple fields
3. Fire XSS repeatedly

## Instructions

### Step 1: Access Requests with Anchor

**Context**: Target the vulnerable section.

Navigate to https://mobilevikings.be/en/account/requests/#easypay.

### Step 2: View Displays

**Context**: Render the name fields.

The section loads, showing username and easy payment name with payload.

> Unsanitized output parses the script tags.

### Step 3: Observe Multiple Executions

**Context**: Confirm broadened impact.

Payload fires in username display and payment name areas.

**Expected Output**: Dual or chained XSS alerts/executions.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[easypay]]
- [[web]]
