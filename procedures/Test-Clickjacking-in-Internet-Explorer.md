---
id: proc-test-clickjacking-ie
tags:
  - clickjacking
  - testing
  - internet-explorer
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
updated_at: '2025-12-14T17:28:05.050Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Test-Clickjacking-in-Internet-Explorer

## Summary

This procedure validates a clickjacking PoC in Internet Explorer, confirming exploit success for actions like account deletion, as modern browsers block via CSP.

## Description

IE lacks strict CSP enforcement, allowing full iframe exploitation. Testing involves loading the PoC while authenticated to Zomato, simulating victim clicks, and verifying impacts such as DoS (account deletion) or integrity changes (ratings). This confirms the attack's viability in legacy environments.

## Requirements

1. Internet Explorer browser
2. Active Zomato session
3. Hosted PoC with overlays

## Defense

Defensive measures and detection strategies:

- Deprecate IE usage and enforce modern browser policies
- Implement server-side frame detection
- Monitor for legacy browser access to sensitive pages

## Objectives

1. Execute PoC in vulnerable browser
2. Verify action completion
3. Document browser-specific behaviors

## Instructions

### Step 1: Prepare Authenticated Session

**Context**: Log in to Zomato in IE to ensure cookies are available.

Open IE, navigate to Zomato, authenticate, then access the hosted PoC.

**Expected Output**: PoC loads with Zomato session active.

### Step 2: Simulate Victim Interaction

**Context**: Click overlaid elements to trigger actions.

Follow div guides: e.g., 3 clicks for deletion (confirmations hidden in iframe).

**Expected Output**: Zomato actions execute (e.g., deletion request sent).

### Step 3: Validate Impacts

**Context**: Check Zomato for changes post-clicks.

Refresh Zomato profile or business page to confirm effects.

**Expected Output**: Account deleted, settings changed, or rating applied.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[browser-testing]]
- [[legacy-exploit]]
