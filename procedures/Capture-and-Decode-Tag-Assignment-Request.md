---
tags:
  - request-capture
  - graphql
  - base64-decode
  - recon
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/base64-decode]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:48.108Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c41cac12-d188-4f85-9fe5-eaddcc1ec930
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Capture-and-Decode-Tag-Assignment-Request

## Summary

This procedure intercepts a legitimate GraphQL request for adding tags to assets on HackerOne, analyzes the tagId parameter, and decodes its base64 format to uncover the predictable internal ID structure for IDOR exploitation.

## Description

Targeted at HackerOne's GraphQL API, this step involves assigning a tag in the attacker's account while capturing the network request. The tagId is base64-encoded in a global ID format (gid://hackerone/AsmTag/XXXX), revealing sequential numeric IDs that can be bruteforced. This reconnaissance enables tampering with unauthorized tags. Prerequisites include an active attacker account with a scope asset.

## Requirements

1. Web browser with network interception (DevTools) or proxy tool
2. Logged-in attacker session with a scope asset
3. Basic knowledge of base64 decoding

## Defense

Defensive measures and detection strategies:

- Obfuscate internal IDs with non-sequential or hashed formats
- Log and monitor GraphQL requests for unusual tagId patterns
- Implement client-side request validation before API submission

## Objectives

1. Capture the AddTagToAssets mutation request
2. Extract and decode the tagId parameter
3. Identify the AsmTag ID pattern for bruteforcing

## Instructions

### Step 1: Assign Tag and Intercept Request

**Context**: Perform a normal tag assignment to trigger the GraphQL mutation while capturing traffic.

Log in to the attacker account, select a scope asset, assign an existing tag, and monitor network tab in DevTools for the POST to https://hackerone.com/graphql with operationName: AddTagToAssets.

**Expected Output**: Request payload including tagId like "Z2lkOi8vaGFja2Vyb25lL0FzbVRhZy80OTc5XXXX".

### Step 2: Decode tagId

**Context**: Reveal the internal format to understand the ID structure.

Copy the tagId value and decode it using a base64 decoder.

Execute [[commands/base64-decode]] to process the tagId:

```bash
echo 'Z2lkOi8vaGFja2Vyb25lL0FzbVRhZy80OTc5XXXX' | base64 -d
```

> This outputs "gid://hackerone/AsmTag/4979XXXX", showing the predictable AsmTag numeric ID.

**Expected Output**: Decoded string exposing the ID pattern.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/base64-decode]]

## Tools Used


## Tags

- request-capture
- graphql
