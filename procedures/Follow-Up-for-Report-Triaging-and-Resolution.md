---
id: proc-follow-up-for-report-triaging-and-resolution
tags:
  - vulnerability-reporting
  - triaging
  - resolution
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
updated_at: '2025-12-14T04:51:10.591Z'
skill_level: beginner
impact_level: low
detection_risk: none
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Follow-Up-for-Report-Triaging-and-Resolution

## Summary

This procedure covers following up on a vulnerability report after PoC submission, leading to reopening, triaging, and resolution, as occurred from June 20 to July 14, 2017, for the Starbucks subdomain takeover.

## Description

Post-PoC, engage with the triage team via comments to provide repro steps and clarify impact. This ensures the flaw in the approval process is addressed through operational changes and code updates. Outcomes include report status updates and confirmation of fixes.

## Requirements

1. Active report on the platform.
2. PoC evidence ready.
3. Patience for response cycles.

## Defense

Defensive measures and detection strategies:

- Establish clear PoC requirements in programs.
- Assign dedicated triage teams.
- Track resolution timelines.

## Objectives

1. Reopen the closed report.
2. Facilitate triaging and fix implementation.
3. Confirm vulnerability mitigation.

## Instructions

### Step 1: Add PoC Comments

**Context**: Respond to closure with evidence.

Comment: "Repro: See attached PoC showing content serve from /unused. Approval flaw allows this."

### Step 2: Provide Repro Steps

**Context**: Detail exact reproduction.

List: 1. Query DNS. 2. Claim resource. 3. Access URL.

### Step 3: Monitor and Escalate if Needed

**Context**: Check status daily.

If delayed, polite follow-up: "Any updates on triaging?"

**Expected Output**: Status to 'Resolved' with fix notes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[follow-up]]
- [[triaging]]
