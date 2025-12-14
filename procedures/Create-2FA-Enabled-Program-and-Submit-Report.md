---
tags:
  - auth-bypass
  - program-setup
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f08ce243-2143-4c24-8cba-5de5f2bf5656
created_at: '2025-12-14T17:24:45.533Z'
updated_at: '2025-12-14T17:24:45.533Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-2FA-Enabled-Program-and-Submit-Report

## Summary

This procedure sets up a new bug bounty program on HackerOne with 2FA enforcement enabled and submits a sample vulnerability report, creating the conditions for later collaborator invitation bypass.

## Description

In the context of testing HackerOne's security policies, this step involves logging into the platform as a program owner or tester, creating a new program policy that mandates 2FA for all participants, and then submitting a mock vulnerability report. This establishes a controlled environment where 2FA is required, allowing subsequent steps to demonstrate the bypass. The target environment is the HackerOne web application, and success is measured by the program's 2FA status and the report's visibility.

## Requirements

1. Valid HackerOne account with permissions to create programs (e.g., researcher or admin role).
2. Web browser with access to hackerone.com.
3. Basic understanding of HackerOne's program management interface.

## Defense

Defensive measures and detection strategies:

- Enforce strict role-based access controls (RBAC) for program creation.
- Monitor for unusual program setups or report submissions in test environments.
- Audit 2FA policy enforcement logs for compliance.

## Objectives

1. Establish a 2FA-mandated program to simulate a secure policy.
2. Create a report containing sensitive mock data.
3. Prepare the report for collaborator invitations.

## Instructions

### Step 1: Log In and Create New Program

**Context**: Access the HackerOne dashboard and initiate program creation to enable 2FA requirements.

Navigate to hackerone.com, log in with your credentials, and go to the "Programs" section. Click "New Program" and configure the policy to require 2FA for all participants, including collaborators.

> Save the program settings. Expected output: Confirmation of program creation with 2FA enforcement active.

### Step 2: Submit Sample Report

**Context**: Submit a vulnerability report to the newly created program to enable the collaborator feature.

From the program dashboard, select "Submit Report." Enter mock details about a vulnerability (e.g., a fictional XSS issue) and submit it.

> Expected output: Report appears in the program's report list, marked as submitted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[hackerone]]
