---
tags:
  - discovery
  - data-access
type: procedure
tools:
  - '[[tools/cURL]]'
  - '[[tools/Browser-Console]]'
  - '[[tools/Browser]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: low
impact_level: high
detection_risk: high
sub_techniques: []
id: bfa5df1c-4ebc-4165-89f4-0e9289b612f7
created_at: '2025-12-10T05:55:44.978Z'
updated_at: '2025-12-10T05:55:44.978Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1087]]'
---
# Access Sensitive Inboxes and Reports

## Summary

This procedure involves navigating a hijacked account to view sensitive data in various inboxes and reports.

## Description

Once in control, attackers browse inboxes like HAS and Triage, loading metadata and contents via GraphQL queries to assess and demonstrate impact.

## Requirements

1. Hijacked session access.
2. Knowledge of platform navigation.
3. Tool: [[tools/Browser]].

## Defense

Defensive measures and detection strategies:

- Log and alert on unusual inbox access patterns.
- Implement role-based access controls and auditing.

## Objectives

1. View sensitive report data.
2. Document accessed information for proof.
3. Maximize demonstrated impact.

## Instructions

### Step 1: Navigate to Inboxes

**Context**: Use the platform menu to access inboxes.

No command; click through interfaces.

> Load up to 100 reports in Triage Inbox.

### Step 2: View Report Details

**Context**: Open individual reports to load contents.

Browse to report views.

> GraphQL queries fetch data automatically.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Browser]]

## Tags

- [[Discovery]]
- #data-access
