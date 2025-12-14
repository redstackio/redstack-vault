---
id: proc-885539-brute-force-attempt
tags:
  - brute-force
  - enumeration
  - graphql
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - GraphQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:26:00.370Z'
skill_level: intermediate
impact_level: low
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Attempt Brute-Force of List IDs via GraphQL

## Summary

This procedure scripts the brute-forcing of Twitter snowflake list IDs using the ListMembers GraphQL query, revealing rate limits that block high-volume attempts.

## Description

Snowflake IDs (64-bit: timestamp + sequence + worker ID) are generated and queried via ListMembers to enumerate private lists. Scripting in Ruby or similar handles ID generation, but GraphQL's rate limits (e.g., after 100 requests) halt progress, necessitating bypasses. This step confirms the feasibility of enumeration but highlights enforcement gaps.

## Requirements

1. Script for snowflake ID generation (e.g., Ruby).
2. Authenticated API access.
3. Basic programming for request looping.

## Defense

Defensive measures and detection strategies:

- Enforce strict rate limits on ID-based queries.
- Implement CAPTCHA or anomaly detection for brute-force patterns.
- Randomize or obscure ID formats.

## Objectives

1. Test brute-force viability.
2. Identify rate limit thresholds.
3. Prepare for alternative scaling methods.

## Instructions

### Step 1: Generate Snowflake IDs

**Context**: Create a range of potential list IDs based on Twitter's snowflake structure.

Implement a function to compute IDs from timestamps (e.g., current epoch shifted).

**Expected Output**: Array of candidate IDs (e.g., 1,000+).

### Step 2: Query ListMembers in Loop

**Context**: Send sequential POST requests with varying listId variables.

Loop: POST to /graphql/iUmNRKLdkKVH4WyBNw9x2A/ListMembers {"listId": id, "count":20}.

**Expected Output**: Rate limit error after ~100 requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- None

## Tags

- [[brute-force]]
- [[enumeration]]
