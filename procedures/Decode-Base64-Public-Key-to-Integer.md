---
id: proc-uuid-2
name: Decode-Base64-Public-Key-to-Integer
tags:
  - decoding
  - base64
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/base64-decode]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:27:15.668Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Decode-Base64-Public-Key-to-Integer

## Summary

This procedure decodes the Base64-encoded public product key extracted from the URL to reveal the underlying integer ID, which is essential for crafting manipulated private IDs in CSRF exploits.

## Description

The public keys on the target site are Base64-encoded integers without full padding. Decoding them provides the numeric core that the server validates weakly, ignoring prefixed/suffixed random characters. This step uses standard Base64 decoding, often requiring manual padding with `==`.

## Requirements

1. Extracted Base64 key from public URL
2. Access to a Base64 decoder (terminal, browser console, or online tool)
3. Basic command-line knowledge for Linux/macOS

## Defense

Defensive measures and detection strategies:

- Use non-Base64 encoding schemes or add integrity checks to keys
- Log decoding attempts if client-side, though typically server-side

## Objectives

1. Convert Base64 string to integer product ID
2. Verify the decoded value is numeric
3. Prepare integer for ID crafting

## Instructions

### Step 1: Pad and Decode Key

**Context**: Append `==` if the key length requires padding (Base64 keys are often unpadded in URLs).

**Command** ([[commands/base64-decode]]):
```bash
echo "NDgxNQ==" | base64 -d
```

> This decodes `NDgxNQ==` to `4815`. On Windows, use `certutil -decode` or PowerShell `[System.Convert]::FromBase64String()`.

### Step 2: Validate Output

**Context**: Confirm the output is a valid integer.

No command; inspect the result.

> Expected: Clean integer like `4815` with no garbage characters.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Software

### Sub-Techniques


## Commands Used

- [[commands/base64-decode]]

## Tools Used


## Tags

- [[decoding]]
- [[base64]]
- [[web]]
