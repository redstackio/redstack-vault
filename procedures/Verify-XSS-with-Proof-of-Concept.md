---
id: proc-camptix-poc-verify-001
tags:
  - xss
  - poc
  - verification
  - wordpress
  - camptix
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.788Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-XSS-with-Proof-of-Concept

## Summary

This procedure provides a method to reproduce and document the XSS vulnerabilities in Camptix using a proof-of-concept video or screenshots, confirming injection and execution for reporting or validation.

## Description

To verify the vulnerabilities, record the steps of payload injection into the Ticket Title and subsequent execution on ticket/coupons pages. This demonstrates the lack of sanitization, with impacts like script alerts or cookie access. Based on the original HackerOne report's video POC, this ensures reproducibility in testing environments.

## Requirements

1. Screen recording tool (e.g., browser extension or software like OBS).
2. Vulnerable WordPress setup with Camptix.
3. Knowledge of basic payloads for demonstration.

## Defense

Defensive measures and detection strategies:

- Patch plugins promptly upon vulnerability disclosure.
- Use vulnerability scanners like WPScan to detect known issues.
- Review admin logs for injection attempts.

## Objectives

1. Reproduce XSS triggers step-by-step.
2. Document evidence of execution.
3. Assess real-world impact like session risks.

## Instructions

### Step 1: Prepare Test Environment

**Context**: Set up a local or staging WordPress site with the vulnerable plugin.

Install WordPress, activate Camptix, and ensure admin access. Create a test event and ticket.

### Step 2: Record Injection and Execution

**Context**: Capture the full workflow for both vulnerabilities.

Start recording: Inject `<script>alert('POC XSS');</script>` into Ticket Title, save, then load ticket page for reflected XSS. Repeat for coupons page self-XSS. Stop recording.

> Expected: Video shows payload entry, page load, and alert popup.

### Step 3: Analyze and Report

**Context**: Review the POC for completeness and impacts.

Play back the video, note execution points, and test advanced payloads (e.g., cookie theft). Include in reports with timestamps.

> Success: Clear demonstration of unsanitized reflection leading to JS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[poc]]
- [[verification]]
- [[wordpress]]
- [[camptix]]
