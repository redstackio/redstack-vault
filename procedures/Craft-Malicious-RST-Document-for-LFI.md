---
tags:
  - payload-crafting
  - rst
  - lfi
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:17.107Z'
sub_techniques: []
id: 56cd7619-f2fb-4ec6-9638-d7ee33807104
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-RST-Document-for-LFI

## Summary

This procedure creates a malicious reStructuredText (RST) document embedding a path traversal payload in the include directive to exploit LFI in the Gregwar/RST parser.

## Description

Attackers craft RST content that appears benign but includes a directive to pull in sensitive files via traversal (e.g., multiple '../' to reach /etc/hosts). This targets RST-enabled web apps like Airship CMS, where user uploads lead to parsing. The outcome is a payload ready for injection, demonstrating info disclosure without direct code execution.

## Requirements

1. Text editor for RST file creation
2. Knowledge of RST syntax and path traversal techniques
3. Target file path (e.g., /etc/hosts on Linux)

## Defense

Defensive measures and detection strategies:

- Sanitize RST input to remove or whitelist directives
- Validate file paths against a safe directory
- Use content security policies to block unexpected file renders

## Objectives

1. Embed functional include payload in valid RST
2. Ensure traversal reaches target file
3. Maintain parsable syntax for evasion

## Instructions

### Step 1: Write Base RST

**Context**: Start with neutral RST elements to mask the payload.

Create malicious.rst:

```rst
*Test* .. include:: /./../../../../../../../../../../../../../../../../../../etc/hosts ``test``
```

> The '*Test*' italicizes text, while the include pulls /etc/hosts. Adjust '../' count based on working directory depth.

### Step 2: Validate Syntax

**Context**: Ensure the RST is syntactically correct before use.

Manually check or use an RST linter.

> Expected: No syntax errors; include directive recognized.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- payload-crafting
- rst
- lfi
