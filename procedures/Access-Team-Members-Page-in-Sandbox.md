---
id: uuid-access-team-page-1
tags:
  - hackerone
  - sandbox
  - access-control
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Create Account]]'
updated_at: '2025-12-14T17:30:07.397Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Create Account]]'
---
# Access-Team-Members-Page-in-Sandbox

## Summary

This procedure describes navigating to the team members invitation page within a HackerOne sandbox program, exposing the interface intended to be restricted.

## Description

The HackerOne platform's documentation states that sandbox programs do not support team invitations, but the UI remains accessible. This step leverages the program handle from creation to reach the page, setting up for unauthorized actions. The target environment is the web-based HackerOne interface, with no additional tools needed.

## Requirements

1. Existing sandbox program handle from prior creation
2. Logged-in HackerOne session
3. Web browser

## Defense

Defensive measures and detection strategies:

- Backend validation to redirect or block access to invitation pages in sandbox mode
- Audit logs for unauthorized page accesses in sandbox programs

## Objectives

1. Reach the invitation interface without restrictions
2. Confirm UI availability in sandbox context
3. Prepare for invitation submission

## Instructions

### Step 1: Construct and Visit URL

**Context**: Use the program handle to directly access the team members endpoint.

In your browser, enter the URL https://hackerone.com/{YOUR-PROGRAM}/team_members, substituting {YOUR-PROGRAM} with the actual handle.

> The page should load, displaying team management options including invitations.

### Step 2: Verify Page Functionality

**Context**: Ensure the invitation features are interactive.

Inspect the page for invitation forms or buttons; attempt to interact without submitting to confirm no frontend blocks.

> Success is indicated by editable fields and no error messages.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Create Account]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[hackerone]]
- [[sandbox]]
- [[access-control]]
