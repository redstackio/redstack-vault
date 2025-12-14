---
id: proc-cloudflare-access-zero-trust-001
tags:
  - session-hijack
  - cloudflare
  - account-takeover
  - idor
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
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:33:06.500Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1078.004]]'
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Steal Web Session Cookie]]'
---
# Access-Zero-Trust-Dashboard-Post-Logout

## Summary

This procedure demonstrates unauthorized continued access to the Zero Trust Dashboard after logging out from the Cloudflare Dashboard, exploiting the session management flaw for potential account takeover.

## Description

Following logout from the main Dashboard, the Zero Trust session persists due to unsynchronized invalidation and improper reference checks, akin to an IDOR in session handling. This allows local attackers with device access to perform sensitive actions like policy changes. Requires prior dual login. Expected outcome: Full Zero Trust functionality without re-auth, confirming the vulnerability.

## Requirements

1. Active Zero Trust session from prior login
2. Browser session intact (cookies not cleared)
3. Local device access for exploitation

## Defense

Defensive measures and detection strategies:

- Enforce session synchronization on logout across all dashboards
- Add object-level checks for session validity in Zero Trust
- Detect and log cross-service access anomalies

## Objectives

1. Regain access to Zero Trust post-Dashboard logout
2. Perform unauthorized actions to simulate takeover
3. Highlight IDOR in session references

## Instructions

### Step 1: Navigate to Zero Trust Dashboard

**Context**: Attempt access using the lingering session.

In the same browser, enter https://dash.teams.cloudflare.com or click the Zero Trust link.

> No login prompt should appear; the dashboard loads directly.

### Step 2: Perform Test Actions

**Context**: Verify full access and potential for takeover.

Interact with features like viewing access policies or gateway logs.

> Expected output: All user-specific data and controls are accessible, indicating active session.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques

- [[T1078.004]] Cloud Accounts

## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[idor]]
