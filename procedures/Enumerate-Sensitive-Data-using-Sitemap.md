---
tags:
  - enumeration
  - sitemap
  - data-leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/enumerate-with-sitemap]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:53.613Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7a242553-546a-447b-84c1-bbe01e48a6f0
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate-Sensitive-Data-using-Sitemap

## Summary

This procedure scales the timing attack by iterating over public usernames and team handles from the sitemap to enumerate payment counts, private program existence, tax form types, and payout preferences via inferred backend responses.

## Description

Using publicly available sitemap data, craft targeted queries to probe for correlations in the Payments backend. Timing differences reveal non-public info like private bug bounty programs (high counts) or specific tax/payout configs, exploiting the injection and oracle in a web GraphQL environment.

## Requirements

1. Public sitemap access (e.g., /sitemap.xml)
2. Script to automate query iteration and timing
3. List of target usernames/handles

## Defense

Defensive measures and detection strategies:

- Restrict sitemap to non-sensitive data
- Implement query rate limiting per user
- Audit backend for timing leaks and add caching

## Objectives

1. Map sensitive attributes to public entities
2. Disclose private program and financial details
3. Aggregate for broader intelligence

## Instructions

### Step 1: Extract Sitemap Data

**Context**: Parse sitemap for usernames/handles to use as filter values.

**Instructions**: Manually or script extraction of user/team paths from https://hackerone.com/sitemap.xml.

### Step 2: Iterate Timing Queries

**Context**: For each combination, run timing attack to infer data.

**Command** ([[commands/enumerate-with-sitemap]]):
```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3d[username]%26core_team_handle%3d[handle]%26") { ... on User { id } } }
```

> Vary [username]/[handle]; long delays indicate private programs or specific prefs.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/enumerate-with-sitemap]]

## Tools Used


## Tags

- account-discovery
- financial-leak
- program-enumeration
