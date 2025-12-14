---
id: proc-637840-002
tags:
  - path-traversal
  - mariadb
  - exploit-craft
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Dynamic Linker Hijacking]]'
updated_at: '2025-12-14T17:26:06.600Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Dynamic Linker Hijacking]]'
---
# Craft-Malicious-Plugin-Path-for-Traversal

## Summary

This procedure crafts a malicious plugin path exploiting path traversal and string padding in MariaDB client to force dlopen of an arbitrary file, bypassing the '.so' extension requirement.

## Description

By padding the path with multiple '/' characters, strxnmov truncates the string to drop the '.so' extension. Combined with '../' sequences, the path traverses to a controlled location like /Users/shinnok/Downloads/h1/init.elf. This targets the client's lack of validation, allowing server control over loaded libraries for code execution via init/fini. Requires knowledge of victim file paths.

## Requirements

1. Knowledge of target installation path (e.g., /lib/x86_64-linux-gnu/mariadb19/plugin)
2. Access to a controlled file with init/fini functions
3. Server-side capability to specify plugin paths

## Defense

Defensive measures and detection strategies:

- Validate and canonicalize all plugin paths on client
- Reject paths containing '../' or excessive '/'
- Log and alert on anomalous dlopen attempts

## Objectives

1. Bypass extension check via padding
2. Traverse to arbitrary file location
3. Prepare path for server transmission

## Instructions

### Step 1: Calculate Traversal Depth

**Context**: Determine number of '../' based on plugin directory depth.

No specific command; compute manually:

> For /lib/x86_64-linux-gnu/mariadb19/plugin, use ~10 '../' to reach root, then navigate to target.

### Step 2: Pad and Assemble Path

**Context**: Add '/' padding to manipulate strxnmov and drop '.so'.

No specific command; construct string:

> Example: "plugin_name////////////../../../../../Users/shinnok/Downloads/h1/init.elf.so" – padding causes truncation to load init.elf.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Dynamic Linker Hijacking]] Dynamic-linker Hijacking

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- path-traversal
- mariadb
- path-crafting
