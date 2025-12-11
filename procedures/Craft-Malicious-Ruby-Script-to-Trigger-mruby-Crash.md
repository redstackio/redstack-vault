---
id: 4ea152be-52cf-4063-aa2f-e260adcdedf0
name: Craft Malicious Ruby Script to Trigger mruby Crash
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:48.234Z'
updated_at: '2025-12-11T03:47:48.234Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
tags:
  - null-pointer-dereference
  - mruby
  - crash
commands:
  - '[[commands/./dev/bin/mruby-crash.rb]]'
  - '[[commands/lldb-./dev/bin/mruby-crash.rb]]'
  - '[[commands/target-create-"./dev/bin/mruby"]]'
  - '[[commands/settings-set----target.run-args-"crash.rb"]]'
  - '[[commands/register-read]]'
  - '[[commands/./bin/sandbox-crash.rb]]'
  - >-
    [[commands/diff---git-a/mrbgems/mruby-compiler/core/codegen.c-b/mrbgems/mruby-compiler/core/codegen.c]]
platforms:
  - macOS
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---

# Craft Malicious Ruby Script to Trigger mruby Crash

## Summary

This procedure involves creating a specially crafted Ruby script that exploits a null pointer dereference vulnerability in mruby's code generation, specifically in handling negation in case statements without using the value, leading to a crash.

## Description

The vulnerability occurs in mruby-compiler/core/codegen.c around line 2256 due to improper stack management when negating values not used in expressions. This results in a null pointer being dereferenced in ary_concat, causing a segmentation fault. The procedure is used in scenarios where mruby is embedded in applications like Shopify Scripts, enabling denial of service attacks.

## Requirements

1. Access to a text editor or file creation tool
2. Knowledge of basic Ruby syntax
3. Target system with mruby installed

## Defense

Defensive measures and detection strategies:

- Update mruby to a patched version that conditionally pushes to stack only if value is used
- Monitor for unexpected crashes in mruby-based applications and analyze scripts for suspicious case statements with negation

## Objectives

1. Create a script that triggers the vulnerability
2. Ensure the script causes improper stack handling
3. Achieve interpreter crash for denial of service

## Instructions

### Step 1: Create Crash File

**Context**: Write the Ruby code that includes a case statement with negation (-0) without using the value, leading to the bug in codegen.

Create a file named crash.rb with the following content:

```ruby
case -0
when 1
end
```

> This code induces the null pointer dereference when executed in mruby.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #null-pointer-dereference
- #mruby
