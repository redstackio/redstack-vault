---
tags:
  - 2fa-requirement
  - hackerone
  - setup
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:47.802Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 0cd02d32-053e-48e8-a984-d74860a402dd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Enable 2FA Requirement in HackerOne Program

## Summary

This procedure configures a HackerOne program to require two-factor authentication (2FA) for report submissions, serving as a prerequisite to test the enforcement gap in bounty claiming.

## Description

In the context of identifying business logic flaws, this step involves accessing program settings on the HackerOne platform to enable 2FA mandates. It simulates a secure program environment where submissions require multi-factor auth, but highlights that this is not uniformly enforced across platform features like bounty claims. Prerequisites include a HackerOne account with permission to manage programs, such as a sandbox or test program.

## Requirements

1. Valid HackerOne account with program management privileges
2. Access to the web interface at hackerone.com
3. Internet connectivity for UI interactions

## Defense

Defensive measures and detection strategies:

- Enforce consistent 2FA checks across all sensitive actions (submissions and claims)
- Audit program settings changes via HackerOne logs
- Monitor API token creations for unusual scopes

## Objectives

1. Establish program-level 2FA policy
2. Verify enforcement in submission flow
3. Set up conditions for bypass testing

## Instructions

### Step 1: Access Program Settings

**Context**: Navigate to the specific program's configuration to modify submission requirements.

Log in to HackerOne and go to `https://hackerone.com/{program_handle}/submission_requirements`, replacing `{program_handle}` with your sandbox program's identifier.

### Step 2: Enable 2FA Option

**Context**: Toggle the 2FA enforcement to require it for all submissions.

Locate the 'Require 2FA' option in the submission guidelines section and enable it. Save the changes to apply the policy.

**Expected Output**: Settings page confirms 2FA is now mandatory; test by attempting a submission to see the prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-requirement]]
- [[hackerone]]
