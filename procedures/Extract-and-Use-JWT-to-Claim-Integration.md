---
id: proc-uuid-003
tags:
  - jwt-extraction
  - integration-claim
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:30:58.159Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Extract-and-Use-JWT-to-Claim-Integration

## Summary

Extract the leaked JWT token from the config page link and use it to claim the HackerOne-Jira integration on an unauthorized account, effectively escalating privileges.

## Description

The JWT, generated without user permission validation, allows any possessor to link their HackerOne account to the Jira instance. Post-claim, actions route through a system user ('comh') with admin rights, bypassing Jira's role checks.

## Requirements

1. Exposed JWT from config page
2. Attacker's HackerOne account credentials
3. Browser session

## Defense

Defensive measures and detection strategies:

- Embed user-specific claims in JWT and validate on HackerOne server
- Revoke or expire JWTs quickly after generation
- Monitor HackerOne for unexpected integration claims

## Objectives

1. Steal and decode JWT for claiming
2. Link unauthorized account to instance
3. Enable over-privileged access via system user

## Instructions

### Step 1: Extract JWT

**Context**: Copy the token from the link.

Right-click the setup link on config page, copy href, extract jwt=<TOKEN> portion using [[tools/Browser-Developer-Tools]].

> Expected: Valid JWT string, e.g., eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

### Step 2: Claim Integration

**Context**: Use JWT to link accounts.

Log into HackerOne, paste full link https://hackerone.com/apps/atlassian/claim-app?jwt=<TOKEN> into browser.

> Expected: Success message confirming integration linked to your HackerOne account.

### Step 3: Verify Claim

**Context**: Test linkage.

In HackerOne, check connected apps or attempt to create a test report linked to Jira.

> Expected: No errors; integration active.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- jwt-extraction
- integration-claim
