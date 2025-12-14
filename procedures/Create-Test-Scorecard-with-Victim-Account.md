---
id: proc-create-scorecard-001
tags:
  - scorecard-creation
  - web
  - idor-setup
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
updated_at: '2025-12-14T17:25:23.602Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Test Scorecard with Victim Account

## Summary

This procedure involves logging in as the victim user and creating a new scorecard in the target application to establish an object for IDOR exploitation, capturing the direct URL reference for later unauthorized access.

## Description

To exploit IDOR, a target object like a scorecard must first be created under a controlled account. This step navigates the application's scorecard management interface, submits a new entry with a known name, and observes the resulting URL structure, which embeds the object identifier (name). In demo.sftool.gov, this occurs via the /tws endpoint, leading to a predictable URL pattern that lacks ownership enforcement. Prerequisites include an active victim session; outcomes include a functional scorecard tied to the victim's account.

## Requirements

1. Active victim account login session
2. Access to https://demo.sftool.gov/tws
3. Knowledge of a unique but guessable scorecard name (e.g., 'testdsfdfsf')

## Defense

Defensive measures and detection strategies:

- Enforce server-side ownership checks on object creation and access
- Use non-predictable, UUID-based identifiers instead of human-readable names in URLs
- Audit URL access logs for direct references without session validation

## Objectives

1. Generate a scorecard owned by the victim
2. Capture the direct URL for exploitation
3. Confirm initial access restrictions

## Instructions

### Step 1: Log In as Victim

**Context**: Authenticate to gain access to protected features.

No specific command; enter victim credentials on the login page and submit.

> Successful redirection to the dashboard confirms session.

### Step 2: Navigate to Scorecard Management

**Context**: Access the creation interface.

No specific command; browse to https://demo.sftool.gov/tws and select 'Create New Scorecard'.

> The form for scorecard details appears.

### Step 3: Submit Scorecard with Known Name

**Context**: Create the object with an identifier suitable for direct reference.

No specific command; fill the form with name 'testdsfdfsf' and any required fields, then submit.

> Post-submission, note the URL: https://demo.sftool.gov/TwsHome/ScorecardManage/testdsfdfsf.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[scorecard]]
- [[web-creation]]
- [[vulnerability-setup]]
