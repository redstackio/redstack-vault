---
tags:
  - decoding
  - base64
  - analysis
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:48.278Z'
skill_level: beginner
impact_level: low
detection_risk: none
sub_techniques: []
id: 14dabbe0-48a7-43eb-b012-45c8a09b95ad
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Decode-Base64-Campaign-ID

## Summary

Decode the base64-encoded campaign_id from the captured GraphQL request to expose the internal GlobalID format used by HackerOne's Ruby on Rails backend.

## Description

HackerOne uses GlobalIDs (gid://hackerone/Campaign/XXX) encoded in base64 for object references in GraphQL. Decoding reveals the structure, enabling ID manipulation for IDOR. This step is non-intrusive and prepares for targeting other campaigns.

## Requirements

1. Captured request with campaign_id value
2. Base64 decoding tool (e.g., online decoder, Python base64 module, or command-line)
3. Understanding of string encoding

## Defense

Defensive measures and detection strategies:

- Obfuscate internal IDs beyond simple base64 to prevent easy decoding
- Log decoding attempts if client-side, though typically server-side

## Objectives

1. Extract numeric campaign ID
2. Confirm GlobalID format
3. Identify modifiable components

## Instructions

### Step 1: Extract campaign_id

**Context**: From the JSON variables.input.campaign_id.

No command; copy value like 'Z2lkOi8vaGFja2Vyb25lL0NhbXBhaWduLzI0NA=='.

### Step 2: Decode Using Command Line

**Context**: Use built-in tools to decode.

**Command** (base64 decode):
```bash
echo 'Z2lkOi8vaGFja2Vyb25lL0NhbXBhaWduLzI0NA==' | base64 -d
```

> Output: gid://hackerone/Campaign/244. Success if format matches expected GlobalID.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- decoding
- analysis
