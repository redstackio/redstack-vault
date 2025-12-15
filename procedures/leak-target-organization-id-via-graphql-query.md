---
id: proc-graphql-leak-org-id
tags:
  - graphql
  - discovery
  - idor
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/graphql-query-organizations]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:20.909Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Leak Target Organization ID via GraphQL Query

## Summary

This procedure uses a legitimate GraphQL query on the Helium Console to enumerate organizations the authenticated user is a member of, leaking the UUID of the target organization for subsequent IDOR exploitation.

## Description

In the Helium Console, low-privileged users (readers) can query their memberships via /graphql, which returns organization details including UUIDs. This information enables attackers to target specific organizations in IDOR attacks without direct access. The procedure assumes an authenticated session with reader access to the target org and focuses on paginated results to identify the target.

## Requirements

1. Valid JWT token for a reader member of the target organization
2. Network access to https://console.helium.com/graphql
3. Tool like curl for sending POST requests

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls on GraphQL queries to limit organization visibility
- Monitor GraphQL queries for unusual pagination or enumeration patterns
- Use query whitelisting to restrict fields like organization IDs

## Objectives

1. Discover UUID of target organization
2. Confirm attacker's membership in target org
3. Prepare for IDOR exploitation

## Instructions

### Step 1: Send GraphQL Query for Organizations

**Context**: Authenticate and query the PaginatedOrganizationsQuery to fetch organization entries, revealing IDs.

**Command** ([[commands/graphql-query-organizations]]):
```bash
curl -X POST https://console.helium.com/graphql \
  -H "Authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjb25zb2xlIiwiZXhwIjoxNTg1NzAyODgzLCJpYXQiOjE1ODU2MTY0ODMsImlzcyI6ImNvbnNvbGUiLCJqdGkiOiIwNjUwMGRiOS1kNjNlLTRiYTQtYWJiYy0xYmQ0YTViMzUxY2YiLCJuYmYiOjE1ODU2MTY0ODIsIm9yZ2FuaXphdGlvbiI6Ijg4M2IwYTQ2LWU0Y2YtNDMxNS1hZjRmLTQyMjZkMWFkYTU2MSIsIm9yZ2FuaXphdGlvbl9uYW1lIjoibG9sIiwic3ViIjoiOGY1YWJlMTktMDAwMS00MWI1LWE5NjktZmUwYjcxZGNjZjFmIiwidHlwIjoiYWNjZXNzIiwidXNlciI6IjhmNWFiZTE5LTAwMDEtNDFiNS1hOTY5LWZlMGI3MWRjY2YxZiJ9.VMAi-07cZkCJg-dffHdR1wwJbi9JNSzpaQSRSQGDX-_vDrcTOPEfgJU_LCZ8H5tYiwsexyD-ogLFakGY1bFy-A" \
  -H "Content-Type: application/json" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" \
  -d '{"operationName":"PaginatedOrganizationsQuery","variables":{"page":1,"pageSize":10},"query":"query PaginatedOrganizationsQuery($page: Int, $pageSize: Int) {\n organizations(page: $page, pageSize: $pageSize) {\n entries {\n ...OrganizationFragment\n __typename\n }\n totalEntries\n totalPages\n pageSize\n pageNumber\n __typename\n }\n}\n\nfragment OrganizationFragment on Organization {\n id\n name\n inserted_at\n __typename\n}"}'
```

> This command sends a POST to /graphql with the query, using the provided JWT. Expected output includes organization IDs like "cb23000e-65b3-4628-9ede-656ffa0d5aa8" for the target.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-query-organizations]]

## Tools Used


## Tags

- graphql
- discovery
- idor
