---
id: proc-reproduce-canvas-dos-001
name: Reproduce Canvas DoS with Crafted Images via Ascii-Art
tags:
  - dos
  - buffer-overflow
  - node-js
  - canvas
  - image-parsing
type: procedure
tools:
  - '[[tools/ascii-art]]'
  - '[[tools/Exploitable]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/ascii-art-process-image]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:30.061Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Reproduce Canvas DoS with Crafted Images via Ascii-Art

## Summary

This procedure reproduces denial-of-service vulnerabilities in the Node.js canvas module by passing specially crafted PNG, JPG, or GIF images to the ascii-art NPM package, which uses canvas for processing, resulting in Node.js segfaults and crashes.

## Description

The ascii-art package relies on the vulnerable canvas module (version 1.6.9) for image-to-ASCII conversion. By supplying malformed images discovered via fuzzing, the parsing flaws—such as buffer overflows in PNG handling—trigger invalid memory reads and process termination. This simulates an attack on any Node.js service that processes user-uploaded images, leading to DoS. Further analysis with !exploitable can reveal potential for code injection. Prerequisites include a Node.js environment and crafted test images.

## Requirements

1. Node.js and NPM installed
2. ascii-art package (depends on vulnerable canvas)
3. Crafted malicious image files (from fuzzing or manual creation)
4. GDB for crash analysis

## Defense

Defensive measures and detection strategies:

- Patch to latest canvas version
- Validate image formats and sizes before processing
- Run image parsing in sandboxed or isolated processes
- Log and alert on Node.js crashes during media handling

## Objectives

1. Trigger DoS crash in canvas-dependent services
2. Demonstrate exploitability of parsing vulnerabilities
3. Assess escalation potential via crash analysis

## Instructions

### Step 1: Install Ascii-Art Package

**Context**: Set up the environment with the vulnerable dependency.

Install via NPM:

```bash
npm install ascii-art
```

This pulls in canvas 1.6.9 with known parsing issues.

### Step 2: Process Crafted Image

**Context**: Feed a malicious image to trigger the vulnerability.

Execute [[commands/ascii-art-process-image]] with a test image path:

```bash
ascii-art image /full/path/to/test/image
```

> The command attempts ASCII conversion, but parsing fails with segfault due to buffer overflow or invalid read.

### Step 3: Analyze the Crash

**Context**: Use !exploitable to evaluate the crash for further exploitation.

Load the core dump in GDB:

```bash
gdb --core=segfault.core /usr/bin/node
(exploitable)
```

> Output shows exploitability score, indicating potential beyond DoS.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/ascii-art-process-image]]

## Tools Used

- [[tools/ascii-art]]
- [[tools/Exploitable]]

## Tags

- dos
- buffer-overflow
- exploitation
