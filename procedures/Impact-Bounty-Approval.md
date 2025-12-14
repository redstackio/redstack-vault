---
tags:
  - impact
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Resource Hijacking]]'
updated_at: '2025-12-14T17:32:58.220Z'
skill_level: low
impact_level: critical
detection_risk: high
sub_techniques: []
id: fcd9060d-9ee7-456a-991e-21db12d988fc
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Resource Hijacking]]'
---
# Impact-Bounty-Approval

## Summary

This final procedure uses the taken-over CEO account to enter the exfiltrated 2FA code and approve all pending bounties, demonstrating full compromise impact.

## Description

With CEO control, submit the 2FA code to authorize payments, resulting in unauthorized approvals.

## Requirements

1. Full CEO session with 2FA code
2. Access to approval interface

## Defense

- Implement approval workflows with multi-admin checks
- Log and alert on high-value approvals
- Use anomaly detection for unusual activity

## Objectives

1. Demonstrate compromise
2. Achieve business impact

## Instructions

### Step 1: Enter 2FA and Approve

**Context**: Submit code in 2FA form.

Enter h1ctf{736c635d8842751b8aafa556154eb9f3} in the CEO dashboard approval form.

> All pending bounties approved.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Resource Hijacking]] Resource Hijacking (adapted for approval abuse)

### Sub-Techniques

- None

## Commands Used

None

## Tools Used

None

## Tags

- [[Impact]]
- [[account-takeover]]
