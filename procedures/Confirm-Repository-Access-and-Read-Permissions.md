---
tags:
  - repo-access
  - github
type: procedure
tools:
  - '[[tools/npx]]'
  - '[[tools/asar]]'
  - '[[tools/curl]]'
  - '[[tools/git]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npx-asar-extract]]'
  - '[[commands/asar-extract]]'
  - '[[commands/curl-github-user-auth]]'
platforms:
  - macOS
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 702fcde5-9eff-452a-973e-a4b8d911f2e6
created_at: '2025-12-11T06:10:40.483Z'
updated_at: '2025-12-11T06:10:40.483Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Confirm Repository Access and Read Permissions

## Summary

This procedure verifies read and write access to organization repositories by querying APIs and cloning repos to prove permissions without full disclosure.

## Description

Using the validated token, query /orgs/Shopify/repos to list repositories and confirm push/pull access. Then, clone a repo with git and compute a file hash to demonstrate access. This targets Shopify repos, with potential for data exfiltration or backdoors. Requires token and git. Outcomes include successful clone and hash verification.

## Requirements

1. Valid GH_TOKEN with org affiliation
2. Git and curl installed
3. Access to GitHub repos

## Defense

Defensive measures and detection strategies:

- Revoke exposed tokens immediately
- Monitor repo access logs for anomalies

## Objectives

1. List accessible repositories
2. Verify read access via cloning
3. Demonstrate impact without exploitation

## Instructions

### Step 1: Query Repositories

**Context**: List Shopify repos.

Use curl to access /orgs/Shopify/repos with token.

> Confirms push and pull permissions.

### Step 2: Clone and Verify

**Context**: Clone repo to prove access.

Use git to clone to /tmp and compute SHA512 of README.md.

> Provides proof without disclosing full content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

## Commands Used

## Tools Used

- [[tools/curl]]
- [[tools/git]]

## Tags

- [[repo-access]]
- [[commands/curl-github-user-auth]]
