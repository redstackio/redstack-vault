---
tags:
  - gitlab
  - setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands//add_contacts]]'
  - '[[commands//remove_contacts]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e66bf6f6-46e3-46e0-8dbe-c7335eefda4f
created_at: '2025-12-11T03:47:49.445Z'
updated_at: '2025-12-11T03:47:49.445Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Create Project in Group

## Summary

This procedure creates a new project within the GitLab group to host issues for vulnerability triggering.

## Description

Projects allow issue creation where quick actions can load vulnerable contact data.

## Requirements

1. Group ownership
2. GitLab access

## Defense

Defensive measures and detection strategies:

- Limit project creation
- Log project activities

## Objectives

1. Provide context for issue-based triggers

## Instructions

### Step 1: Navigate to New Project

**Context**: Go to https://gitlab.com/projects/new#blank_project.

> Select the group and name the project.

### Step 2: Create Project

**Context**: Submit to create.

> Confirm project existence.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #gitlab
- #setup
