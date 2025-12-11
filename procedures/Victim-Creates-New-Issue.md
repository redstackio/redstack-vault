---
tags:
  - gitlab
  - victim-action
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
id: cc504322-569b-4978-a0f2-d10e0b16bd35
created_at: '2025-12-11T03:47:49.411Z'
updated_at: '2025-12-11T03:47:49.411Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Victim Creates New Issue

## Summary

This procedure describes the victim creating a new issue in the project, setting the stage for quick action triggers.

## Description

Victim interaction is required to reach the description pane where quick actions are used.

## Requirements

1. Victim membership in group/project

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious invitations

## Objectives

1. Prepare issue for payload trigger

## Instructions

### Step 1: Navigate to Issues

**Context**: Select 'Issues' in project.

> Click 'New Issue'.

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
- #victim-action
