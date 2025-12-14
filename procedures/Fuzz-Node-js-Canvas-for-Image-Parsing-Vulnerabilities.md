---
id: proc-fuzz-canvas-001
name: Fuzz Node.js Canvas for Image Parsing Vulnerabilities
tags:
  - fuzzing
  - dos
  - node-js
  - canvas
type: procedure
tools:
  - '[[tools/AFL]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.079Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Fuzz Node.js Canvas for Image Parsing Vulnerabilities

## Summary

This procedure uses AFL fuzzing to identify buffer overflows and invalid memory reads in the Node.js canvas module's PNG, JPG, and GIF parsing functions, enabling discovery of denial-of-service vulnerabilities.

## Description

The canvas module, a popular Node.js library for image manipulation using Cairo, contains flaws in its media parsing code. By fuzzing the parsing routines with malformed inputs, attackers can uncover crashes that lead to segfaults in Node.js processes. This is particularly relevant for services that process user-supplied images, such as image conversion tools. The procedure targets canvas version 1.6.9 and requires compiling the module with fuzzing instrumentation. Expected outcomes include crash dumps that reveal exploitable issues like buffer overflows.

## Requirements

1. AFL fuzzer installed and configured
2. Node.js and NPM environment with canvas 1.6.9
3. Cairo graphics library for canvas backend
4. Local machine with sufficient CPU for fuzzing sessions

## Defense

Defensive measures and detection strategies:

- Input validation and sanitization for image uploads
- Use updated versions of canvas module (post-1.6.9 patches)
- Monitor Node.js processes for unexpected segfaults and crashes
- Implement rate limiting on image processing endpoints

## Objectives

1. Discover parsing vulnerabilities causing DoS
2. Generate crash data for exploitability analysis
3. Validate impacts on dependent services

## Instructions

### Step 1: Setup AFL and Canvas

**Context**: Instrument the canvas module for fuzzing by compiling with AFL support.

Install canvas via NPM and prepare the build environment:

```bash
npm install canvas@1.6.9
```

Configure AFL to target the parsing functions, such as those handling PNG/JPG/GIF headers.

### Step 2: Run Fuzzing Session

**Context**: Launch AFL to generate and test malformed image inputs against parsing code.

Start the fuzzer on the canvas image loading interface:

```bash
afl-fuzz -i input_seeds -o findings -- /path/to/node /path/to/test_script.js @@
```

Where input_seeds contains sample PNG/JPG/GIF files, and test_script.js loads the fuzzed input via canvas.

> AFL will mutate inputs and report crashes when segfaults occur in parsing.

### Step 3: Analyze Crashes

**Context**: Examine crash logs to identify vulnerability types.

Use GDB with [[tools/Exploitable]] on core dumps:

```bash
gdb --core=crash.core /path/to/node
(exploitable)
```

> Output indicates buffer overflow or invalid read exploitability.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AFL]]

## Tags

- fuzzing
- dos
- node-js
