---
tags:
  - social-engineering
  - ownership-transfer
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
techniques: []
updated_at: '2025-12-14T03:46:31.509Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
id: e807839c-545a-49c9-94a0-50234bfe95e4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Transfer-VK-Group-Ownership-to-New-Admin

## Summary

This procedure legitimately transfers VK group ownership to a new admin after setting up a persistent XSS payload, creating conditions for the exploit to trigger in the victim's session.

## Description

VK.com allows group owners to sell or transfer control to another user, who must accept. This step ensures the malicious server remains post-transfer, positioning the new admin to unknowingly trigger the XSS during management tasks like deletion. It relies on social trust or deception to prompt the handover.

## Requirements

1. Current group ownership
2. Identified new admin candidate
3. Communication channel to coordinate transfer

## Defense

Defensive measures and detection strategies:

- Require multi-factor approval for ownership changes
- Audit group settings before accepting ownership
- Train admins to inspect server names for anomalies

## Objectives

1. Hand over control without removing injected elements
2. Position victim for payload interaction
3. Maintain persistence of the vulnerability

## Instructions

### Step 1: Initiate Transfer

**Context**: Start the official handover process.

In group settings, select "Management" > "Transfer Ownership," enter the new admin's VK ID, and confirm the action.

### Step 2: Complete Handover

**Context**: Finalize and exit the group.

Notify the new admin to accept via VK notifications. Once accepted, leave the group to relinquish all access.

### Step 3: Verify Setup

**Context**: Ensure the server persists.

Ask the new admin (externally) to confirm the server list includes the suspicious name.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ownership-transfer]]
