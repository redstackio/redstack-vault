---
tags:
  - poc
  - demonstration
  - xss
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.287Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 4f65a869-7f4c-4505-882a-972f58fb78a2
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Demonstrate POC via Video

## Summary

This procedure records a proof-of-concept video showcasing the full XSS exploitation and token theft in Linktree to validate the attack for reporting or verification.

## Description

In a controlled environment, perform the injection and trigger, capturing screen activity. Useful for bug bounties like HackerOne. No code execution beyond prior steps; focuses on documentation.

## Requirements

1. Screen recording software (e.g., OBS Studio)
2. Test Linktree account
3. Completed prior procedures

## Defense

Defensive measures and detection strategies:

- N/A (documentation step)
- Review reports for similar PoCs to patch proactively

## Objectives

1. Visually confirm XSS trigger
2. Show token alert or exfil
3. Provide evidence for remediation

## Instructions

### Step 1: Setup Recording

**Context**: Prepare the test environment and start recording.

No specific command; use built-in procedures to inject and view.

> Record login, injection, profile view, and alert/exfil confirmation.

### Step 2: Execute and Capture

**Context**: Trigger the exploit while recording.

> Expected output: Video file with clear steps and token visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[poc]]
- [[xss]]
