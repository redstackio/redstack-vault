---
tags:
  - information-disclosure
  - graphql
  - email-leak
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/gitlab-users-graphql-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.084Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 66408839-fa3b-4344-a41b-1dabb08339c9
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Execute-GitLab-Users-GraphQL-Query

## Summary

This procedure demonstrates executing a GraphQL query in GitLab's Explorer to disclose private user email addresses, bypassing public profile visibility restrictions.

## Description

By running the 'users' query in the unauthenticated GraphQL Explorer, attackers can retrieve sensitive data including emails, usernames, avatars, and status info. The root cause is inadequate authorization in the GraphQL schema, allowing public access to private fields. This targets GitLab's web platform and requires no tools beyond a browser. Outcomes include a JSON list of users with emails, enabling follow-on attacks like phishing.

## Requirements

1. Access to GitLab GraphQL Explorer (from prior procedure)
2. Basic knowledge of GraphQL syntax
3. Web browser for execution

## Defense

Defensive measures and detection strategies:

- Enforce authentication and visibility checks on user queries
- Audit GraphQL schema for over-exposed fields
- Log and alert on queries accessing sensitive data like emails

## Objectives

1. Retrieve private email addresses unauthenticated
2. Collect user data for reconnaissance
3. Validate API misconfiguration

## Instructions

### Step 1: Input the Query

**Context**: Prepare the GraphQL query to fetch user details including emails.

Execute [[commands/gitlab-users-graphql-query]] in the Explorer's query editor:

```graphql
{ users { edges { node { username email avatarUrl status { emoji message messageHtml } } } } }
```

> This query targets the root 'users' field, using pagination via 'edges' and 'node' to extract fields like 'email' (private), 'username' (public), and status objects. Paste it into the left pane of the Explorer.

### Step 2: Execute and Review Response

**Context**: Run the query and analyze the output for disclosed data.

Click the 'Execute Query' button.

> Expected JSON response: {"data":{"users":{"edges":[{"node":{"username":"example","email":"user@example.com","avatarUrl":"https://...","status":{"emoji":"","message":"","messageHtml":""}}}...}]}}} . Verify emails are returned despite being private.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/gitlab-users-graphql-query]]

## Tools Used


## Tags

- graphql-query
- user-enumeration
- disclosure
