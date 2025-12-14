---
tags:
  - project-creation
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
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
updated_at: '2025-12-14T03:46:37.196Z'
sub_techniques: []
id: 38fa1744-f5de-4afe-8e3c-94e13144383d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-New-Project-on-TopCoder

## Summary

This procedure details creating a new project on the TopCoder Connect platform, which requires admin approval and sets up the environment for injecting payloads into associated features like messages.

## Description

After authentication, users can create projects via the Connect interface. Projects are not immediately public and await admin review, providing a window for payload persistence. This step targets https://connect.topcoder.com/new-project/ and generates a project ID for further access. The outcome is a pending project that, once approved, exposes vulnerable messaging.

## Requirements

1. Authenticated session on connect.topcoder.com
2. Web browser access
3. Basic project details (name, description)

## Defense

Defensive measures and detection strategies:

- Review project submissions for suspicious content
- Implement approval workflows with content scanning
- Log project creation events for anomaly detection

## Objectives

1. Generate a project ID for messaging access
2. Trigger admin approval process
3. Establish persistence point for XSS

## Instructions

### Step 1: Navigate to New Project

**Context**: From the dashboard, access the project creation form.

In [[tools/Chrome-Browser]], go to https://connect.topcoder.com/new-project/.

> Enter project name, description, and any required fields, then submit.

### Step 2: Confirm Creation

**Context**: Verify the project is listed as pending.

Check the dashboard for the new project entry with its ID.

> Note the project ID for the next steps; approval may take time.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- project-creation
