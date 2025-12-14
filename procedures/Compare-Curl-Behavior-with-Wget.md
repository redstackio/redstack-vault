---
tags:
  - curl
  - wget
  - comparison
type: procedure
tools:
  - '[[tools/wget]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/wget-glob-fail]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:26:06.310Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 180c2fac-ac10-4586-affb-66b06ea1b32d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Compare-Curl-Behavior-with-Wget

## Summary

This procedure tests the same globbed URL with wget to demonstrate that it does not support URL expansion, failing to bypass filters and highlighting the curl-specific nature of the globbing exploit.

## Description

Wget treats bracketed patterns literally without globbing, unlike curl. This comparison validates the attack's tool dependency, useful in environments where multiple download tools are available, confirming no similar bypass in alternatives.

## Requirements

1. Installed wget on Linux
2. Same globbed URL as in curl test
3. Local shell access

## Defense

Defensive measures and detection strategies:

- Prefer tools without globbing in untrusted inputs
- Audit tool usage patterns
- Block or monitor download tool executions

## Objectives

1. Verify wget's lack of globbing support
2. Confirm attack specificity to curl
3. Rule out alternative tool exploits

## Instructions

### Step 1: Test Globbing URL with Wget

**Context**: Run the identical URL to show wget's failure to parse or expand, resulting in a protocol error without file access.

**Command** ([[commands/wget-glob-fail]]):
```bash
wget 'f[h-j]le:///etc/passwd'
```

> Wget interprets the URL literally, outputting an error like "f[h-j]le:///etc/passwd: Address lacks protocol type," with no expansion or file read attempt.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning: Scanning IP Blocks

### Sub-Techniques


## Commands Used

- [[commands/wget-glob-fail]]

## Tools Used

- [[tools/wget]]

## Tags

- wget
- comparison
