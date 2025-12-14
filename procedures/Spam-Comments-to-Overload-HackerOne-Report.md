---
id: proc-hackerone-spam-comments-dos
tags:
  - dos
  - web
  - hackerone
  - resource-exhaustion
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
updated_at: '2025-12-14T17:26:30.798Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Spam-Comments-to-Overload-HackerOne-Report

## Summary

This procedure floods a HackerOne report with excessive comments (e.g., 450 short 'test' messages or large high-entropy payloads) to set up server overload during view loading, exploiting the lack of quantity or size limits.

## Description

The attack scenario targets the comment system on HackerOne reports, where manual or system-generated comments accumulate without bounds. Using a sandboxed team minimizes rate-limiting issues. Technical approach involves repeated submissions via the web interface, tested on reports like 137508 (short comments), 132450 (large messages), and 138662 (varied methods). Expected outcomes include report bloat leading to DoS on view attempts, with amplification potential from incompressible data.

## Requirements

1. Access to a HackerOne report from the previous procedure.
2. Sandboxed team account to avoid rate limits.
3. Web browser for manual or scripted submissions.

## Defense

Defensive measures and detection strategies:

- Enforce comment limits per report (e.g., max 100 comments).
- Implement size caps on comment payloads and monitor submission rates.

## Objectives

1. Overload the report with comments to exceed server processing capacity.
2. Use high-entropy data for request amplification.
3. Prepare for DoS triggering without detection.

## Instructions

### Step 1: Prepare Comment Payloads

**Context**: Decide on spam method—short repeated messages or large payloads.

For short spam, prepare to enter 'test' 450 times. For large, generate high-entropy strings (e.g., random data) to resist compression.

### Step 2: Submit Comments

**Context**: Flood the report via the comment interface.

In the report page, use the comment box to submit messages repeatedly. Include system-generated comments if possible (e.g., via actions that auto-post). Aim for 450 short ones or 2-3 large (e.g., 1MB each) submissions. Tested examples: Report 137508 with shorts, 132450 with larges.

**Expected Output**: Comments appear in the report history.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dos]]
- [[web]]
- [[hackerone]]
- [[resource-exhaustion]]
