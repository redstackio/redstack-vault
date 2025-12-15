---
id: proc-weblate-configure-race-001
tags:
  - configuration
  - race-setup
type: procedure
tools:
  - '[[tools/Turbo-Intruder]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:18.950Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Turbo-Intruder-for-Race-Attack

## Summary

This procedure customizes Turbo Intruder to perform a race condition attack by adding identifiers and loading a racing script.

## Description

Prepares the tool for sending multiple concurrent POST requests to /trial/, exploiting the lack of proper synchronization. Web-based Django target. Expected outcome: Configured payload for rapid execution.

## Requirements

1. Request loaded in Turbo Intruder
2. race.py script available (built-in or custom)
3. Basic understanding of request headers

## Defense

Defensive measures and detection strategies:

- Use atomic operations or locks in trial activation logic
- Implement per-user request queuing
- Detect duplicate headers like 'Test: %s'

## Objectives

1. Add unique identifier for tracking
2. Load race script for concurrency
3. Validate config before execution

## Instructions

### Step 1: Add Test Header

**Context**: Differentiate concurrent requests for analysis.

In Turbo Intruder's request editor, insert a custom header: 'Test: %s' where %s is a placeholder for threading.

> This helps identify which requests succeed in the race.

### Step 2: Select Race Configuration

**Context**: Enable the racing mode.

Choose the 'race.py' configuration from Turbo Intruder's options to set up multi-threaded sending.

> Interface updates to show threading parameters; adjust threads if needed (default often 10+).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Turbo-Intruder]]

## Tags

- configuration
- race-setup
