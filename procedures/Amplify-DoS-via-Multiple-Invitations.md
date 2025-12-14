---
id: p5e6f7g8-h9i0-1234-efgh-5678901234
tags:
  - dos
  - amplification
  - ddos
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:56.784Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Amplify-DoS-via-Multiple-Invitations

## Summary

This procedure extends the DoS attack by inviting multiple accounts with oversized filenames to the same report, increasing the volume of junk data in GraphQL responses for a DDoS-like effect.

## Description

By adding more participants with exploited profiles to a single report, the /reports/<report-id>/participants/ endpoint returns compounded oversized data. This scales the resource exhaustion, potentially affecting organization pages and multiple users simultaneously.

## Requirements

1. Multiple HackerOne accounts prepared with oversized filename uploads
2. Access to the existing dummy report
3. Invitation permissions

## Defense

Defensive measures and detection strategies:

- Cap the number of participants per report
- Detect and block bulk invitation patterns
- Apply response compression or field selection in GraphQL to limit data

## Objectives

1. Add additional affected accounts to the report
2. Verify escalated response sizes and impacts
3. Demonstrate potential for broader platform disruption

## Instructions

### Step 1: Prepare Additional Accounts

**Context**: Ensure other accounts have the oversized payload uploaded using prior procedures.

Repeat the upload process on secondary accounts (e.g., @fossnow27).

### Step 2: Issue Multiple Invitations

**Context**: Expand the participant list to amplify data bloat.

From the report participants page, invite the additional accounts one by one.

**Expected Output**: Larger participant lists; GraphQL responses grow proportionally, worsening load times and crashes.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- dos
- amplification
- multi-account
