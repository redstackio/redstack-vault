---
id: proc-uuid-3
name: Craft-Malicious-Private-Product-ID
tags:
  - id-manipulation
  - weak-validation
  - base64
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/base64-encode]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.665Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-Private-Product-ID

## Summary

This procedure crafts a fake private product ID by wrapping the decoded integer with random prefixes and suffixes, then Base64-encoding it, exploiting the server's weak validation that only checks the numeric core.

## Description

The target endpoint validates product IDs by extracting only the numeric part from Base64-decoded strings, ignoring added noise like `AA#` and `#AA`. Attackers can thus create valid IDs from public keys, enabling CSRF payloads to target any product.

## Requirements

1. Decoded integer ID from previous step
2. Choice of prefix/suffix strings (e.g., `AA#` and `#AA` to mimic random symbols)
3. Base64 encoder tool

## Defense

Defensive measures and detection strategies:

- Implement full ID format validation including prefixes/suffixes
- Use cryptographic signing or HMAC for IDs to prevent tampering

## Objectives

1. Generate a manipulated string with the target integer
2. Encode it to Base64 without trailing padding
3. Produce a valid ID for CSRF submission

## Instructions

### Step 1: Construct Manipulated String

**Context**: Surround the integer with custom prefix and suffix.

No command; manually create string like `AA#4815#AA`.

> Use a text editor to build the string ensuring it includes the exact integer.

### Step 2: Encode to Base64

**Context**: Base64-encode the string and strip trailing `==` to match URL format.

**Command** ([[commands/base64-encode]]):
```bash
echo "AA#4815#AA" | base64 | sed 's/==$//'
```

> Output: `QUEjNDgxNSNBQQ`. This ID will decode to include the integer but pass weak checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/base64-encode]]

## Tools Used


## Tags

- [[id-manipulation]]
- [[weak-validation]]
- [[base64]]
