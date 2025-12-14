---
id: proc-graphql-fix-verification
tags:
  - graphql
  - vulnerability-verification
  - fix-testing
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-verify-graphql-fix]]'
verified: false
platforms:
  - Web
  - GraphQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:00.123Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-GraphQL-Fix-for-Whitelisted-Hackers

## Summary

This procedure verifies the resolution of the GraphQL information disclosure vulnerability by re-testing queries post-fix, confirming restricted access to whitelisted_hackers total_count for non-members.

## Description

After implementing authorization fixes, the API returns 0 for unauthorized users and accurate counts (e.g., 1) only for whitelisted hackers in soft-launched teams. This step uses curl to send queries and validate the patch, useful for red teaming or bug bounty verification.

## Requirements

1. Knowledge of a soft-launched team handle for testing.
2. Curl or equivalent HTTP tool.
3. Awareness of pre-fix behavior for comparison.

## Defense

Defensive measures and detection strategies:

- Audit GraphQL schema for post-fix leaks in similar fields.
- Use introspection queries to validate field restrictions.
- Monitor for repeated verification attempts as potential probing.

## Objectives

1. Confirm vulnerability remediation.
2. Ensure no residual disclosure for non-members.
3. Document fix efficacy for reporting.

## Instructions

### Step 1: Send Post-Fix Query

**Context**: Execute the original query style on a soft-launched team to check restricted output.

**Command** ([[commands/curl-verify-graphql-fix]]):
```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query {team(handle:\"example-soft-launch\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

> Expected output: For non-members, {"data":{"team":{..."whitelisted_hackers":{"total_count":0}}}}; for whitelisted, total_count:1. This indicates successful fix.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-verify-graphql-fix]]

## Tools Used


## Tags

- graphql
- fix-verification
- api-testing
