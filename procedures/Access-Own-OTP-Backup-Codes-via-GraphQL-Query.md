---
tags:
  - graphql
  - information-disclosure
  - self-access
type: procedure
tools:
  - '[[tools/graphql-ruby]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/graphql-safe-query-edges]]'
  - '[[commands/graphql-vulnerable-query-nodes]]'
  - '[[commands/graphql-user-data-leak-query]]'
  - '[[commands/graphql-self-otp-query]]'
platforms:
  - Web
techniques:
  - '[[Data from Information Repositories]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: e8849bc2-8e48-44d8-abb5-50dc17edc61c
created_at: '2025-12-11T06:10:40.225Z'
updated_at: '2025-12-11T06:10:40.225Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1213]]'
---
# Access Own OTP Backup Codes via GraphQL Query

## Summary

This procedure queries a user's own data via GraphQL to retrieve hashed OTP backup codes, potentially highlighting an unintended exposure.

## Description

Using the 'me' object in GraphQL, a user can access their own sensitive attributes like OTP backup codes. This was reported as a related issue to the main vulnerability, to confirm if such access is intended or requires restriction.

## Requirements

1. Authenticated access to the GraphQL endpoint
2. Knowledge of own user ID
3. GraphQL client

## Defense

Defensive measures and detection strategies:

- Restrict sensitive fields even for self-queries if not necessary
- Audit self-access permissions

## Objectives

1. Retrieve own OTP codes
2. Assess if access is a vulnerability
3. Report findings

## Instructions

### Step 1: Query Own User Data

**Context**: Send a GraphQL query targeting the 'me' object to fetch OTP backup codes.

**Command** ([[commands/graphql-self-otp-query]]):
```graphql
{
  me{
    _id #388246
    id #gid://hackerone/User/388246
    otp_backup_codes
    username
  }
}
```

> The response should include hashed OTP codes if access is allowed.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used

- [[commands/graphql-self-otp-query]]

## Tools Used

- [[tools/graphql-ruby]]

## Tags

- [[tools/graphql-ruby]]
- [[information-disclosure]]
