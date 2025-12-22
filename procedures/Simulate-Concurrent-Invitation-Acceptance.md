---
id: proc-uuid-003
tags:
  - race-condition
  - web
  - exploitation
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:18.789Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Simulate-Concurrent-Invitation-Acceptance

## Summary

This procedure exploits a race condition by rapidly submitting invitation acceptance requests from multiple sessions, allowing token reuse before database deletion.

## Description

The core exploitation step targets the invitation acceptance endpoint, where a SQL lookup for the token occurs without locking, followed by processing and deletion. By clicking 'Accept' in quick succession across sessions, both requests find the token valid, join the team, and only one deletion happens post-facto. This occurs in web platforms like HackerOne, requiring concurrent browser actions. Outcomes include multiple unauthorized joins, potentially chaining with token timing issues.

## Requirements

1. Active invitation token from prior setup
2. Multiple authenticated sessions in separate browsers
3. Low-latency network to minimize timing gaps

## Defense

Defensive measures and detection strategies:

- Use database transactions with SELECT FOR UPDATE for token checks
- Implement idempotent checks (e.g., token status flags)
- Log and alert on concurrent token accesses

## Objectives

1. Trigger parallel acceptance requests to bypass token consumption
2. Achieve multiple team joins from one invitation
3. Demonstrate the race window vulnerability

## Instructions

### Step 1: Navigate to Invitation in Both Sessions

**Context**: Position both browsers at the acceptance point.

**Instructions**: In each [[tools/Web-Browser]] session, paste the invitation URL and load the page.

> UI Action: Enter the full invitation link (e.g., https://platform.com/invite?token=abc123).

### Step 2: Rapidly Click Accept

**Context**: Exploit the timing gap between token lookup and deletion.

**Instructions**: Click the 'Accept Invitation' button in both sessions as simultaneously as possible, ideally within milliseconds.

> UI Action: Mouse-click or keyboard shortcut to submit both forms quickly. Observe no immediate error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- race-condition
- web
- exploitation
