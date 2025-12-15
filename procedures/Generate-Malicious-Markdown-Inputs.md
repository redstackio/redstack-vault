---
id: uuid3
tags:
  - poc-generation
  - collision-craft
type: procedure
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:49.037Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Generate-Malicious-Markdown-Inputs

## Summary

This procedure crafts malicious markdown inputs exploiting Snudown's hash weaknesses, creating collisions or duplicates to force long linked lists and O(N) lookups for DoS.

## Description

For Bug 1, generate unique strings with same hash modulus for buckets; for Bug 2, repeat keys with different hashes. Format includes multiple [si]: /url definitions followed by [s1] uses. Targets markdown parsers; outcomes are PoC files slowing processing.

## Requirements

1. Knowledge of SDBM hash function
2. Scripting tool (e.g., Python) for generating colliding strings
3. Text editor for markdown formatting

## Defense

Defensive measures and detection strategies:

- Input validation limiting reference count
- Rate limiting on markdown processing
- Anomaly detection on parsing times

## Objectives

1. Create collision-based inputs for long lists
2. Generate duplicate keys for O(N) first-entry retrieval
3. Prepare inputs for Bug 3 confirmation

## Instructions

### Step 1: Craft Collision Strings

**Context**: Find strings hashing to same bucket (e.g., modulus T).

No specific command; use a script to compute SDBM hashes and select collisions like those modulo table size.

> Produces strings for same bucket; expected output is list of colliding refs.

### Step 2: Format Markdown

**Context**: Build input with definitions and uses.

No specific command; write markdown with [ref1]: url1, [ref2]: url2 (colliding), then multiple [ref] links.

> Creates PoC file; expected output is valid markdown exploiting insertion.

### Step 3: Include Equality Test

**Context**: Add colliding names like '37qpypu' and 'uvhisfu' with hash 7150400.

No specific command; append definitions with unique URLs.

> Tests wrong resolution; expected output is input confirming Bug 3.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[poc-generation]]
- [[collision-craft]]
