---
tags:
  - setup
  - sandbox
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:46.979Z'
skill_level: basic
impact_level: low
sub_techniques: []
id: bc88355b-2605-46cb-9508-7035bcd77021
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-HackerOne-Sandbox-Program

## Summary

This procedure sets up a sandbox program on the HackerOne platform to create a isolated test environment for simulating private bug bounty programs and testing access control vulnerabilities.

## Description

In the context of testing HackerOne's report management, a sandbox program allows creation of a controlled space with limited disclosure settings. This mimics real-world private programs where reports contain sensitive information like PII or attachments stored in S3. The procedure requires a HackerOne account and focuses on configuring visibility to enable later exploitation testing.

## Requirements

1. Valid HackerOne account with program creation privileges
2. Web browser access to hackerone.com
3. Basic understanding of HackerOne's program settings

## Defense

Defensive measures and detection strategies:

- Enforce strict role-based access controls (RBAC) for program creation
- Monitor for unusual program creation patterns via HackerOne admin logs
- Use multi-factor authentication (MFA) for account access

## Objectives

1. Establish an isolated test program for vulnerability reproduction
2. Configure limited disclosure to simulate sensitive report handling
3. Prepare environment for user invitation and report testing

## Instructions

### Step 1: Log In and Navigate to Programs

**Context**: Access the HackerOne dashboard to initiate program creation.

Log in to your HackerOne account and click on 'Programs' in the navigation menu, then select 'New Program' or equivalent.

> Expected output: Program creation form loads.

### Step 2: Configure Sandbox Settings

**Context**: Set up the program with sandbox-like restrictions to test access controls.

Enter a test name (e.g., 'Test Sandbox'), select 'Private' visibility, enable limited disclosure for reports, and save the program.

> Expected output: Program created with handle (e.g., /test-sandbox), dashboard accessible.

### Step 3: Verify Setup

**Context**: Confirm the sandbox is operational and isolated.

Navigate to the program dashboard and ensure no external access; create a dummy report if needed to test visibility.

> Expected output: Report creation successful, visible only to program members.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- sandbox
