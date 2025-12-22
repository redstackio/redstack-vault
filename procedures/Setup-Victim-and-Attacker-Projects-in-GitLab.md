---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - gitlab
  - setup
  - project-creation
type: procedure
tools:
  - '[[tools/Curl-for-API-Testing]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:20.682Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Setup-Victim-and-Attacker-Projects-in-GitLab

## Summary

This procedure sets up the testing environment by creating two authenticated users (victim and attacker), private projects, and external status checks in GitLab to demonstrate the IDOR vulnerability.

## Description

In a GitLab instance, create user accounts for simulation. As the victim user, establish a private project with an external status check configuration. Repeat for the attacker user, recording the project ID for later API exploitation. This prepares the scenario where the attacker can attempt unauthorized access to the victim's status check data via the API.

## Requirements

1. Admin access to GitLab to create users
2. Valid GitLab instance URL (e.g., https://gitlab.domain.com)
3. Browser access for UI interactions

## Defense

Defensive measures and detection strategies:

- Restrict user creation to admins and monitor new account activities
- Enable audit logs for project and status check configurations
- Use role-based access controls to limit project visibility

## Objectives

1. Simulate isolated private projects for victim and attacker
2. Configure external status checks with unique IDs
3. Prepare project IDs for API targeting

## Instructions

### Step 1: Create Users

**Context**: Establish victim01 and attacker01 users to simulate scenarios.

**Instructions**: As admin, navigate to Admin Area > Users > New User and create both accounts with standard developer roles.

### Step 2: Victim Project and Status Check

**Context**: Log in as victim01 to create a private project and status check.

**Instructions**: Access https://gitlab.domain.com/projects/new#blank_project, name it 'victim_project', set visibility to Private. Then go to Settings > General > Merge requests > Status checks > Create new. Name it 'Victim status check', enter external URL 'https://victim.hidden.com', and save.

### Step 3: Attacker Project and Status Check

**Context**: Switch to attacker01, create similar setup, and note project ID.

**Instructions**: Log out and log in as attacker01. Repeat project creation for 'attacker_project' (private). Configure status check similarly, naming it 'Attacker status check' with URL 'https://attacker.hidden.com'. Note the project ID as ATTACKID from the project URL or API.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Curl-for-API-Testing]]

## Tags

- gitlab
- setup
- project-creation
