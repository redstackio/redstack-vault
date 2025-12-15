---
tags:
  - setup
  - api-token
  - hackerone
type: procedure
tools:
  - '[[tools/curl]]'
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
updated_at: '2025-12-14T17:32:29.218Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 64d29560-6cd8-4424-9957-a44e9bddedfe
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Sandbox-Program-and-API-Token

## Summary

This procedure sets up a test environment in HackerOne by creating a sandbox program and generating an API token with assigned roles, enabling isolated testing of API functionality without affecting production data.

## Description

In the context of demonstrating the API timestamp update failure, this procedure involves logging into HackerOne, creating a new sandbox program, navigating to its API settings, and creating a token with standard user and admin roles. This allows subsequent API calls to be authenticated and authorized for operations like reading reports and assigning states. Prerequisites include a valid HackerOne account with program creation permissions. Expected outcomes are a functional token ready for use in API requests.

## Requirements

1. Valid HackerOne account with permissions to create programs
2. Web browser for UI navigation
3. Internet access to HackerOne platform

## Defense

Defensive measures and detection strategies:

- Monitor account activity for unusual program creations in HackerOne logs
- Enforce role-based access controls to limit token creation to trusted users
- Regularly audit API token usage through backend logs, independent of UI displays

## Objectives

1. Establish an isolated test program for vulnerability demonstration
2. Generate and configure an API token for authenticated operations
3. Prepare environment for API usage verification

## Instructions

### Step 1: Create Sandbox Program

**Context**: Initiate a new program to serve as a test bed.

Log in to HackerOne and navigate to the programs dashboard. Click 'New Program' and configure it as a sandbox with minimal settings.

**Expected Output**: Program created with a handle like 'sandbox-test-123'.

### Step 2: Access API Page

**Context**: Reach the API management interface.

Navigate to https://hackerone.com/PROGRAM_HANDLE/api, substituting the handle.

**Expected Output**: API settings page loads.

### Step 3: Generate Token and Assign Roles

**Context**: Create and configure the token for testing.

Click 'Create Token', name it (e.g., 'test-token'), and assign to a user with standard and admin roles.

**Expected Output**: Token secret displayed; roles applied.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- setup
- api-token
