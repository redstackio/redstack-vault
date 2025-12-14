---
id: proc-914331-create-owner-note
tags:
  - setup
  - authentication
  - web
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
updated_at: '2025-12-14T17:25:29.472Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Note-as-Owner-User

## Summary

This procedure authenticates as an 'owner' role user in the Outpost application and creates a new note to generate a target UUID for IDOR exploitation.

## Description

In the context of testing the Outpost notes API, this initial setup step involves logging in with owner privileges and creating a note via the web interface. The note receives a unique UUID, which serves as the target for unauthorized modification in later steps. This simulates a legitimate owner action to establish the vulnerable resource.

## Requirements

1. Valid owner role credentials for the Outpost application
2. Access to the web interface (HTTPS)
3. Browser or API client for interaction

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) to restrict note creation to verified sessions
- Log all note creation events with user IDs for auditing

## Objectives

1. Establish a target note with a known UUID
2. Verify owner authentication works as expected
3. Prepare for IDOR testing without alerting defenses

## Instructions

### Step 1: Authenticate as Owner

**Context**: Log in to the application to gain owner privileges.

Navigate to the Outpost login page and enter owner credentials. Upon successful login, access the notes section.

### Step 2: Create New Note

**Context**: Generate a new note and capture its UUID.

Use the notes interface to create a simple note (e.g., title: "Test Note", body: "Initial content"). After creation, inspect the note details or API response to retrieve the UUID (e.g., b9db186a-c0af-462d-ad71-c30c2bfd7cf5).

**Expected Output**: Note created successfully, UUID noted for reference.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[authentication]]
