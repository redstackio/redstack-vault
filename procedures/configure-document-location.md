---
tags:
  - xss
  - document-config
type: procedure
tools:
  - '[[tools/mozilla-firefox]]'
  - '[[tools/google-chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 6da8487f-62e1-4756-927b-10ced89f64a4
created_at: '2025-12-14T03:16:30.849Z'
updated_at: '2025-12-14T03:16:30.849Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure Document Location

## Summary

This procedure sets the storage location for the new document in the Informatica Marketplace, ensuring it is published under the attacker's control for later exploitation.

## Description

During document creation, selecting 'Your Documents' as the location stores the content in the user's personal space, making it publicly viewable after publishing. This step is crucial for persistence in the XSS attack, as it allows the malicious title to be rendered on the /docs/ page without additional permissions.

## Requirements

1. Active session in document creation form
2. Web browser for UI interaction
3. No special privileges needed

## Defense

Defensive measures and detection strategies:

- Validate location selections server-side
- Log all document configurations for anomaly detection
- Restrict publication to approved locations

## Objectives

1. Assign document to personal storage
2. Advance to content fields
3. Maintain exploit setup

## Instructions

### Step 1: Select Location

**Context**: Choose where to save the document to enable publishing.

In the creation form, locate the location dropdown and select 'Your Documents'.

> Expected output: Location field updates, unlocking title and body inputs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/mozilla-firefox]]
- [[tools/google-chrome]]

## Tags

- [[xss]]
- [[document-config]]
