---
tags:
  - organization-query
  - github
type: procedure
tools:
  - '[[tools/npx]]'
  - '[[tools/asar]]'
  - '[[tools/curl]]'
  - '[[tools/git]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/npx-asar-extract]]'
  - '[[commands/asar-extract]]'
  - '[[commands/curl-github-user-auth]]'
platforms:
  - macOS
techniques:
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: ffe6b2fa-dbcc-491e-9f50-2de729d77671
created_at: '2025-12-11T06:10:40.487Z'
updated_at: '2025-12-11T06:10:40.487Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1087]]'
---
# Query User and Organization Details

## Summary

This procedure queries GitHub API for user organizations to identify affiliations, such as with Shopify, using a validated token.

## Description

Building on token validation, hit the /user/orgs endpoint with curl to list organizations associated with the token's user. This confirms membership in targets like Shopify, revealing potential access scopes. Requires a valid token and API access. Outcomes include a list of organizations, enabling targeted repo queries.

## Requirements

1. Validated GH_TOKEN
2. Curl tool
3. Internet connectivity

## Defense

Defensive measures and detection strategies:

- Use fine-grained tokens with minimal scopes
- Log and alert on organization query attempts

## Objectives

1. Identify organizational affiliations
2. Confirm Shopify membership
3. Prepare for repo access verification

## Instructions

### Step 1: Query Organizations

**Context**: List user organizations.

Use curl to access /user/orgs endpoint with the authenticated token.

> Expected output: JSON list including Shopify.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques

## Commands Used

## Tools Used

- [[tools/curl]]

## Tags

- [[organization-query]]
- [[commands/curl-github-user-auth]]
