---
tags:
  - mutation
  - query-modification
  - replay-attack
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/graphql-sessions-query]]'
  - '[[commands/create-paypal-preference-mutation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.401Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 2f7b94a4-77c8-4087-aa1a-29f5014e2580
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-and-Replay-GraphQL-Queries

## Summary

Edit intercepted GraphQL requests in a repeater tool to execute custom queries or mutations, bypassing UI restrictions on disabled accounts.

## Description

Replace JSON bodies with targeted GraphQL operations (e.g., fetch sessions or add payments) while preserving auth headers. This exploits lack of status checks in the API.

## Requirements

1. Intercepted request in Burp Repeater
2. Knowledge of GraphQL schema (queries like Sessions_page)
3. Valid session token

## Defense

Defensive measures and detection strategies:

- Add user status validation in GraphQL resolvers
- Log all mutations and alert on sensitive changes
- Use query whitelisting for disabled users

## Objectives

1. Craft and send custom GraphQL operations
2. Retrieve or modify data silently
3. Confirm bypass success

## Instructions

### Step 1: Send to Repeater

**Context**: Prepare for editing.

No command; Right-click request in History, "Send to Repeater".

> Tab opens with raw request.

### Step 2: Edit and Execute Query

**Context**: Modify payload for data retrieval.

Execute [[commands/graphql-sessions-query]] by pasting into body and clicking Send.

```http
POST /graphql? HTTP/1.1
Host: hackerone.com
...
{"query":"query Sessions_page($first_0:Int!) {me {id,...F1}} ...","variables":{"first_0":10}}
```

> Response: JSON with session data.

### Step 3: Perform Mutation

**Context**: Test data modification.

Execute [[commands/create-paypal-preference-mutation]] similarly.

```http
POST /graphql? HTTP/1.1
Host: hackerone.com
...
{"query":"mutation Create_paypal_preference_mutation ...","variables":{"input_0":{"paypal_email":"test@example.com",...}}}
```

> Response: Success with updated prefs.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/graphql-sessions-query]]
- [[commands/create-paypal-preference-mutation]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- graphql-replay
- payload-modification
