---
id: proc-init-project-wiki
tags:
  - gitlab
  - wiki
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
updated_at: '2025-12-14T17:24:15.066Z'
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
# Initialize-GitLab-Project-Wiki

## Summary

This procedure creates a new GitLab project and initializes its wiki to prepare for injecting malicious content.

## Description

GitLab projects can have associated wikis stored as Git repositories. Initializing the wiki creates the default home page, enabling subsequent cloning and modification. This step requires project creation permissions and sets the stage for wiki-based exploitation.

## Requirements

1. GitLab user with project creation access
2. Web access to GitLab instance

## Defense

Defensive measures and detection strategies:

- Limit project creation to trusted users
- Monitor new wiki initializations

## Objectives

1. Establish a target wiki repository
2. Enable push access for exploit file

## Instructions

### Step 1: Create New Project

**Context**: Start a new project to associate with the wiki.

No command; use GitLab UI: New Project > Create blank project, name it (e.g., proj1).

> Project created successfully.

### Step 2: Initialize Wiki

**Context**: Set up the wiki for the project.

No command; navigate to Project > Wiki > Create default home page.

> Wiki initialized with master branch.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- wiki
