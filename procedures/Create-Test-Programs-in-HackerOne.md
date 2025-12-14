---
tags:
  - setup
  - hackerone
  - program-creation
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
updated_at: '2025-12-14T17:24:48.000Z'
skill_level: basic
impact_level: none
sub_techniques: []
id: 9723eac0-ebae-467e-9485-f57fc11c04e1
validated: true
---
# Create-Test-Programs-in-HackerOne

## Summary

This procedure outlines the creation of two test programs on the HackerOne platform to facilitate vulnerability testing involving report submission and transfer features.

## Description

In the context of testing 2FA bypass via report transfer, this setup step involves logging into HackerOne with administrative privileges and creating isolated test programs. One program will serve as a non-restricted entry point, and the other as a 2FA-enforced target. This ensures controlled reproduction without affecting live programs. Prerequisites include a HackerOne account with program creation capabilities.

## Requirements

1. HackerOne account with program owner or admin privileges
2. Access to the HackerOne dashboard
3. Basic familiarity with the platform's UI

## Defense

Defensive measures and detection strategies:

- Limit program creation to verified users via account verification processes
- Monitor for unusual program creation patterns in audit logs

## Objectives

1. Establish test environments for non-restricted and restricted programs
2. Confirm manager access to both programs
3. Prepare for subsequent configuration and submission steps

## Instructions

### Step 1: Log In and Access Dashboard

**Context**: Gain access to the program management interface.

Log in to hackerone.com with your admin account and navigate to the 'Programs' section in the dashboard.

### Step 2: Create First Program

**Context**: Set up the non-restricted program.

Click 'New Program', name it 'h1R', provide minimal details (e.g., test scope), and save. Verify it's active and you have manager role.

### Step 3: Create Second Program

**Context**: Set up the program for 2FA configuration.

Repeat the process to create 'h1B' with similar details, ensuring manager privileges.

## MITRE ATT&CK Mapping

### Tactics

- None (setup procedure)

### Techniques

- None (setup procedure)

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[setup]]
- [[hackerone]]
- [[program-creation]]
