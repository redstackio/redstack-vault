---
id: proc-decode-hackerone-node-id
tags:
  - idor
  - graphql
  - decoding
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/base64-decode-node-id]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:53.649Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Decode-HackerOne-GraphQL-Node-ID

## Summary

This procedure decodes a base64-encoded GraphQL node ID from HackerOne to reveal the underlying auto-incremental primary key of an EmbeddedSubmissionForm object, setting the stage for IDOR-based enumeration.

## Description

In HackerOne's GraphQL interface, node IDs are base64-encoded strings representing global IDs (GIDs) like `gid://hackerone/EmbeddedSubmissionForm/9`. Decoding exposes the predictable integer primary key (e.g., 9), which can be incremented for enumeration. This is the initial step in exploiting the IDOR vulnerability to access unauthorized forms without authentication. Prerequisites include a known valid node ID, obtainable from public sources or initial unauthenticated queries.

## Requirements

1. Access to a base64 decoder tool or command-line utility (e.g., base64 command in Linux).
2. A sample node ID such as `Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==`.
3. No network access or credentials required.

## Defense

Defensive measures and detection strategies:

- Use secure, random UUIDs for object references instead of auto-incremental IDs.
- Implement rate limiting on GraphQL queries to detect enumeration attempts.
- Monitor for unusual patterns in node ID decoding or sequential queries.

## Objectives

1. Extract the integer primary key from the encoded node ID.
2. Confirm the predictable structure for subsequent modification.
3. Enable enumeration of additional forms.

## Instructions

### Step 1: Decode the Base64 Node ID

**Context**: Take a known encoded node ID and decode it to understand the GID format.

**Command** ([[commands/base64-decode-node-id]]):
```bash
echo 'Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==' | base64 -d
```

> This command decodes the base64 string, outputting `gid://hackerone/EmbeddedSubmissionForm/9`. The integer `9` is the auto-incremental primary key, indicating vulnerability to enumeration by incrementing this value.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/base64-decode-node-id]]

## Tools Used

- None

## Tags

- [[idor]]
- [[graphql]]
- [[decoding]]
