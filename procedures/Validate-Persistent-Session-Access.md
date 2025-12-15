---
tags:
  - session-persistence
  - unauthorized-access
  - weblate
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:10.910Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 405fc989-1603-445f-9bee-a788fce547f8
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Validate-Persistent-Session-Access

## Summary

This procedure tests and confirms unauthorized continued access to a Weblate account via an existing session after removing all linked authentication methods, demonstrating the core vulnerability.

## Description

Post-removal of third-party auth, this step verifies session validity on the secondary device. In a secure system, access should be denied; here, the flaw allows hijacking. Targets the Weblate dashboard and requires a pre-established session. Outcome: Proof of persistent access without credentials, enabling account takeover.

## Requirements

1. Pre-existing session on secondary device from OAuth login
2. Third-party linkage removed on primary device
4. Ability to perform account actions for validation

## Defense

Defensive measures and detection strategies:

- Implement global session invalidation on auth profile changes
- Monitor for orphaned sessions without valid auth methods
- Use short session timeouts and anomaly detection on access patterns

## Objectives

1. Confirm lack of session revocation
2. Demonstrate unauthorized account access
3. Highlight risk of persistent hijacking

## Instructions

### Step 1: Reactivate Secondary Session

**Context**: Return to the second device and attempt to use the session.

Switch to Device 2 and navigate to https://hosted.weblate.org, refreshing the current page if open.

> Check for any logout or re-auth prompts; none should appear due to the vulnerability.

### Step 2: Perform Validation Actions

**Context**: Execute account-specific operations to ensure full access.

Access sensitive areas like profile settings or project dashboards, and attempt modifications if possible.

> Successful interactions without credential challenges confirm persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[session-persistence]]
- [[unauthorized-access]]
