---
tags:
  - rce
  - deserialization
  - execution
type: procedure
tools:
  - '[[tools/rdoc]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/rdoc-execute]]'
platforms:
  - Ruby
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d7f356fc-f1b1-470e-8b08-8925b67e01b4
created_at: '2025-12-14T17:23:42.449Z'
updated_at: '2025-12-14T17:23:42.449Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Command-Line Interface]]'
---
# Execute-RDoc-to-Trigger-Deserialization

## Summary

This procedure runs the RDoc command to parse the malicious `.rdoc_options` file, triggering YAML deserialization and executing the embedded gadget chain for RCE.

## Description

When RDoc starts, it calls `YAML.load_file('.rdoc_options')` at lib/rdoc/rdoc.rb#L165, deserializing without restrictions and activating the gadget chain. This leads to `Kernel.system` invocation, executing arbitrary commands like `date`. Applicable in scenarios where RDoc processes untrusted repos, such as in IDEs or build scripts.

## Requirements

1. Malicious `.rdoc_options` in current directory
2. Vulnerable RDoc installation
3. Shell access to run rdoc

## Defense

Defensive measures and detection strategies:

- Disable or sandbox RDoc for untrusted inputs
- Log and alert on deserialization errors
- Patch to use safe YAML parsing

## Objectives

1. Trigger YAML load for gadget activation
2. Achieve RCE via system call
3. Validate exploitation success

## Instructions

### Step 1: Invoke RDoc in Malicious Directory

**Context**: Change to the directory with `.rdoc_options` and run RDoc to force parsing and deserialization.

**Command** ([[commands/rdoc-execute]]):
```bash
rdoc
```

> RDoc attempts documentation generation, loads the YAML, deserializes the object, and executes the command. Expected output includes date/time from `date` and RDoc errors like "no implicit conversion of nil into String".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]
- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/rdoc-execute]]

## Tools Used

- [[tools/rdoc]]

## Tags

- rce
- execution
