---
tags:
  - vulnerability-verification
  - post-exploitation
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/graphql-team-policy-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:26:00.155Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3e2c15ce-5c30-4046-a55e-228b7b200f12
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Verify-Fix-Post-Patch

## Summary

This procedure re-tests the GraphQL API after the June 26, 2020 patch to confirm that private policies are no longer disclosed via the 'policy_markdown_html' field.

## Description

Post-remediation validation involves repeating original queries on affected teams to ensure access controls prevent information leakage. This confirms resolution of the disclosure vulnerability. Target: Patched HackerOne API. Prerequisites: Knowledge of fix date and prior vulnerable responses. Outcomes: Verification of security improvements.

## Requirements

1. Access post-patch date
2. List of previously tested team handles
3. Comparison baseline from pre-patch queries

## Defense

Defensive measures and detection strategies:

- Conduct post-patch testing in staging
- Automate regression tests for API fields
- Monitor for re-introduced exposures in updates

## Objectives

1. Re-execute queries on patched endpoint
2. Confirm no private policy disclosure
3. Document resolution effectiveness

## Instructions

### Step 1: Re-Query Affected Teams

**Context**: Send original queries after patch deployment.

**Command** ([[commands/graphql-team-policy-query]]):
```graphql
query { team(handle:"example") { name policy_markdown_html } }
```

> Expected output: Null or public-only content, no private HTML.

### Step 2: Compare Pre- and Post-Patch

**Context**: Diff responses to validate changes.

**Command** (Manual Comparison):
Parse and compare JSON/HTML.

> Expected: Absence of differing private policies.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/graphql-team-policy-query]]

## Tools Used

- None

## Tags

- [[vulnerability-verification]]
- [[post-exploitation]]
