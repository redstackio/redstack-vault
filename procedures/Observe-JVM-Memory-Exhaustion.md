---
tags:
  - dos-observation
  - memory-exhaustion
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
platforms:
  - Java
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: abd51001-8f45-4555-8d56-d36c2a88cb6f
created_at: '2025-12-13T09:00:27.232Z'
updated_at: '2025-12-13T09:00:27.232Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Observe JVM Memory Exhaustion

## Summary

This procedure monitors the JVM process for signs of memory exhaustion and crash following the entity expansion trigger.

## Description

As the recursive entities expand, heap memory is consumed rapidly, leading to OutOfMemoryError and process termination, achieving DoS.

## Requirements

1. Running Java process to monitor
2. Tools like top or jvisualvm for memory observation
3. Unbounded or sufficient heap to observe crash

## Defense

Defensive measures and detection strategies:

- Set JVM heap limits
- Log and alert on OutOfMemoryErrors

## Objectives

1. Confirm memory spike
2. Verify process crash
3. Validate DoS impact

## Instructions

### Step 1: Monitor Memory Usage

**Context**: Use system tools to watch heap growth.

Run top or jvisualvm while the parsing occurs.

> Look for increasing memory usage.

### Step 2: Check for Crash

**Context**: Wait for the error and termination.

Observe the console for OutOfMemoryError.

> Process should terminate.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[dos-observation]]
- [[memory-exhaustion]]
