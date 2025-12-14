---
tags:
  - configuration
  - 2fa
  - hackerone
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques: []
updated_at: '2025-12-14T17:24:47.987Z'
skill_level: basic
impact_level: none
sub_techniques: []
id: 9c3e9f1a-7bb9-4813-abb7-7b26232cbf16
validated: true
---
# Configure-2FA-Requirement-for-Program

## Summary

This procedure enables 2FA requirements for new report submissions on a HackerOne program, setting up the policy that will be bypassed in subsequent transfer steps.

## Description

HackerOne allows program managers to enforce 2FA for reporters submitting vulnerabilities. This step configures such a policy on a test program ('h1B') to simulate a secure environment. The configuration occurs via the program's settings UI, and direct submissions to this program should then require 2FA, highlighting the transfer bypass vulnerability.

## Requirements

1. Manager access to the target program ('h1B')
2. Logged-in session on HackerOne
3. Understanding of submission guidelines

## Defense

Defensive measures and detection strategies:

- Regularly audit program settings for unauthorized changes
- Enforce multi-admin approval for policy modifications

## Objectives

1. Activate 2FA enforcement for 'h1B' submissions
2. Validate the policy blocks non-2FA direct submissions
3. Prepare for report transfer testing

## Instructions

### Step 1: Access Program Settings

**Context**: Navigate to the configuration area for policy changes.

Log in as program manager, select 'h1B' from the programs list, and click 'Settings'.

### Step 2: Enable 2FA Requirement

**Context**: Toggle the security feature for submissions.

In the 'Submission Requirements' tab, find the 2FA option and enable it for new reports. Save changes and confirm via a test submission attempt from a non-2FA account (should fail).

## MITRE ATT&CK Mapping

### Tactics

- None (configuration procedure)

### Techniques

- None (configuration procedure)

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[configuration]]
- [[2fa]]
- [[hackerone]]
