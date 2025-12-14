---
tags:
  - oob-read
  - irssi
  - fuzzing
  - irc
type: procedure
tools:
  - '[[tools/AFL-Fuzz]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/afl-fuzz-irssi-output]]'
  - '[[commands/afl-fuzz-irssi-commands]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:24:31.095Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 0130dc09-6688-49d6-8f0d-f7d74423d26a
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Fuzzing Irssi for Out-of-Bounds Reads

## Summary

This procedure uses AFL via Perl scripts to fuzz Irssi's output parsing and command handling, triggering OOB reads on sequences like %[, causing crashes (CVE-2017-5196).

## Description

Irssi mishandles script output with %[ for color codes, leading to invalid memory reads. Fuzz piped input and commands. Targets IRC clients on Linux.

## Requirements

1. Irssi compiled
2. AFL and Perl
3. Input dirs for fuzzp.txt/fuzzc.txt
4. No memory limit (-m none)

## Defense

Defensive measures and detection strategies:

- Sanitize script outputs
- Bounds check format strings
- Patch CVE-2017-5196

## Objectives

1. Trigger OOB in parsing
2. Crash client
3. Potential info leak

## Instructions

### Step 1: Fuzz Output Parsing

**Context**: Target %[ sequences.

**Command** ([[commands/afl-fuzz-irssi-output]]):
```bash
afl-fuzz -i in -o out -m none -f fuzzp.txt Irssi
```

> Crashes on invalid reads.

### Step 2: Fuzz Commands

**Context**: Test command execution.

**Command** ([[commands/afl-fuzz-irssi-commands]]):
```bash
afl-fuzz -i in -o out -m none -f fuzzc.txt Irssi
```

> Finds handling bugs.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- None

## Commands Used

- [[commands/afl-fuzz-irssi-output]]
- [[commands/afl-fuzz-irssi-commands]]

## Tools Used

- [[tools/AFL-Fuzz]]

## Tags

- oob-read
- irc-client
