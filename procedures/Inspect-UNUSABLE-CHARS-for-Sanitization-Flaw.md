---
tags:
  - analysis
  - sanitization
  - ruby
type: procedure
tools:
  - '[[tools/IRB]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/define-unusable-chars]]'
platforms:
  - Windows
  - Ruby
techniques:
  - '[[System Information Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f02992c0-509f-4265-9611-7ca378f0fc0b
created_at: '2025-12-14T17:26:22.901Z'
updated_at: '2025-12-14T17:26:22.901Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Inspect UNUSABLE_CHARS for Sanitization Flaw

## Summary

This procedure defines and examines the UNUSABLE_CHARS constant used in Tempfile sanitization to reveal why backslashes are not properly removed on Windows.

## Description

UNUSABLE_CHARS is defined as [File::SEPARATOR, File::ALT_SEPARATOR, File::PATH_SEPARATOR, ":"].uniq.join("").freeze, resulting in "/\\;:" on Windows where ALT_SEPARATOR is \\. This inspection shows the constant includes the backslash, but the delete method fails on escaped versions, enabling the traversal.

## Requirements

1. IRB environment on Windows Ruby
2. Knowledge of File constants

## Defense

Defensive measures and detection strategies:

- Patch Ruby or override Tempfile sanitization with stricter regex-based cleaning
- Code review for String.delete usage in path handling
- Static analysis tools to detect unsanitized path inputs

## Objectives

1. Understand the sanitization mechanism
2. Identify inclusion of Windows-specific separators
3. Link to root cause of traversal vulnerability

## Instructions

### Step 1: Define and Print UNUSABLE_CHARS

**Context**: Replicate the constant definition in IRB to inspect its value and confirm separator handling.

**Command** ([[commands/define-unusable-chars]]):
```ruby
UNUSABLE_CHARS = [File::SEPARATOR, File::ALT_SEPARATOR, File::PATH_SEPARATOR, ":"].uniq.join("").freeze
puts UNUSABLE_CHARS
```

> Defines the constant and prints it. Expected output: "/\\;:"

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/define-unusable-chars]]

## Tools Used

- [[tools/IRB]]

## Tags

- analysis
- sanitization
- ruby
