---
tags:
  - transfer
  - bypass
  - 2fa
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:47.979Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: e4474d91-fb8c-4d63-a551-1a94a767aafd
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Transfer-Report-to-2FA-Required-Program

## Summary

This procedure exploits a validation gap in HackerOne's report transfer feature, allowing a program manager to move a non-2FA report into a 2FA-required program without enforcing the reporter's 2FA status.

## Description

The core vulnerability lies in the report transfer functionality, where no check occurs for the original reporter's 2FA compliance during moves between programs. Using manager privileges on both 'h1R' and 'h1B', this step transfers the report from the former to the latter, bypassing the submission policy. This undermines security by permitting less-secured entries into restricted programs, though limited by the need for privileged access.

## Requirements

1. Program manager access to both 'h1R' and 'h1B'
2. Existing report in 'h1R' from non-2FA account
3. Active session on HackerOne

## Defense

Defensive measures and detection strategies:

- Implement transfer validation to re-check reporter 2FA before acceptance
- Audit all report transfers for policy compliance
- Alert on transfers from non-2FA sources to restricted programs

## Objectives

1. Successfully transfer the report to 'h1B'
2. Confirm bypass of 2FA requirement
3. Demonstrate improper access control impact

## Instructions

### Step 1: Access the Report

**Context**: Locate the submitted report in the source program.

Log in as program manager, go to 'h1R' reports, and open the test report.

### Step 2: Initiate and Complete Transfer

**Context**: Perform the transfer action without additional validation.

Click the 'Transfer' option, select 'h1B' as destination, provide any required notes, and confirm. The transfer should succeed despite the reporter's non-2FA status.

### Step 3: Verify Transfer

**Context**: Check the destination program for the report.

Navigate to 'h1B' reports and confirm the transferred report is present and accepted.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[transfer]]
- [[bypass]]
- [[2fa]]
- [[hackerone]]
