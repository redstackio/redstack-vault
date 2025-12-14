---
id: uuid4
tags:
  - local-testing
  - performance-measure
type: procedure
tools:
  - '[[tools/Snudown]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:49.035Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Test-Locally-with-Proof-of-Concept

## Summary

This procedure builds the Snudown parser locally and tests malicious inputs to measure parsing time degradation, confirming O(N) complexity for DoS impact.

## Description

Using snudown_proof_of_concept.zip, compile the C parser and run it on random vs. malicious markdown with increasing N references. Plots show linear growth for attacks. Targets local dev environments; outcomes validate exploit efficacy.

## Requirements

1. C compiler (gcc)
2. Snudown source and PoC zip
3. Timing tool or script for measurement

## Defense

Defensive measures and detection strategies:

- Resource limits on parser threads
- Monitoring CPU usage during markdown rendering
- Fuzz testing for complexity attacks

## Objectives

1. Build and execute the parser
2. Compare parsing times for benign vs. malicious inputs
3. Visualize O(N) impact

## Instructions

### Step 1: Build Parser

**Context**: Compile Snudown using provided files.

No specific command; follow zip instructions, typically gcc markdown.c -o snudown.

> Builds executable; expected output is runnable parser binary.

### Step 2: Run Tests

**Context**: Parse inputs and time execution.

No specific command; ./snudown < input.md > output.html, use time command for measurement.

> Times increase linearly with N for malicious; expected output is timing logs.

### Step 3: Plot Results

**Context**: Graph time vs. N.

No specific command; use Python/matplotlib or similar to plot.

> Shows O(1) for random, O(N) for malicious; expected output is visualization confirming DoS.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[OS Exhaustion Flood]] OS Exhaustion

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Snudown]]

## Tags

- [[local-testing]]
- [[performance-measure]]
