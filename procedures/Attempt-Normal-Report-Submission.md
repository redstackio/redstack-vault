---
id: proc-002
tags:
  - authorization-test
  - 2fa-enforcement
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
updated_at: '2025-12-14T17:24:48.539Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Attempt-Normal-Report-Submission

## Summary

This procedure tests standard vulnerability report submission to a HackerOne program, confirming blockage due to 2FA requirements and other ACL checks.

## Description

Targeting programs like Parrot Sec, this step navigates to the submission interface and attempts to create a report, triggering validations such as 2FA enforcement, rate limits, and blacklists. It highlights the protections in place for normal interact endpoints, setting up the contrast for the embedded form bypass. Expected outcome: Submission failure with specific error, verifying the vulnerability context.

## Requirements

1. HackerOne account with 2FA disabled (from prior procedure)
2. Target program URL (e.g., https://hackerone.com/parrot_sec)
3. Basic knowledge of report content (e.g., test vulnerability description)

## Defense

Defensive measures and detection strategies:

- Implement strict ACL checks on all submission endpoints
- Rate-limit and blacklist suspicious submitters
- Log failed submissions with user details for review

## Objectives

1. Observe 2FA blockage in standard submission flow
2. Confirm active protections like rate limits
3. Validate setup for embedded bypass exploitation

## Instructions

### Step 1: Navigate to Program Page

**Context**: Access the target program's submission interface.

Go to https://hackerone.com/parrot_sec in your browser.

> Program dashboard loads with 'Submit Report' button visible.

### Step 2: Initiate Report Creation

**Context**: Start the submission process to trigger checks.

Click 'Submit Report' and fill in basic fields: title, description (e.g., test vuln), severity.

> Form partially loads, but submission attempts fail.

### Step 3: Attempt Submission

**Context**: Submit to observe enforcement.

Click 'Submit' and note the error.

> Error: 'Submission blocked due to missing 2FA' or similar, confirming ACL trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authorization-test
- 2fa-enforcement
