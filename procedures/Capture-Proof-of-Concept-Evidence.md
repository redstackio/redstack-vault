---
id: proc-004
tags:
  - poc
  - evidence-capture
  - csrf
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.290Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture Proof-of-Concept Evidence

## Summary

This procedure records the entire demonstration of CSRF token reuse in Liberapay, including account actions and network inspections, to provide verifiable evidence of the vulnerability for reporting or validation.

## Description

As the final step in the attack chain, this captures video footage of the process from account creation to token observation across deletions and accounts. It uses built-in browser or OS recording tools to document the generic cookie's role in token persistence. The scenario ensures reproducibility, with focus on Developer Tools views. Outcomes include a comprehensive video proving the issue without actual exploitation.

## Requirements

1. Screen recording tool (e.g., browser extension or OS built-in like QuickTime)
2. Completed prior steps with visible token values
3. Stable internet for uninterrupted recording

## Defense

Defensive measures and detection strategies:

- Review security reports for PoC videos showing token issues and audit cookie configurations
- Implement client-side token validation to prevent reuse demonstrations
- Use rate limiting on account actions to hinder repeated testing

## Objectives

1. Document the full reproduction of token reuse
2. Highlight key evidence like identical token strings
3. Provide material for vulnerability disclosure

## Instructions

### Step 1: Prepare Recording Environment

**Context**: Set up tools to capture both UI actions and Developer Tools.

Open Developer Tools in split view (Network tab active), start screen recording, and ensure audio is off unless narrating steps.

> Expected output: Recording session initiated with full screen or window capture.

### Step 2: Reproduce and Record the Chain

**Context**: Execute prior procedures while recording to show token continuity.

Replay account creation, linking, deletions across accounts, pausing to zoom on token values in requests. End with cookie inspection in Application tab showing the 7-day generic storage.

> Expected output: Video file (e.g., MP4) lasting 5-10 minutes with clear evidence.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[poc]]
- [[evidence-capture]]
- [[csrf]]
