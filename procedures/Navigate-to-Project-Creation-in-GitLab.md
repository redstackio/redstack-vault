---
tags:
  - gitlab
  - navigation
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/gitlab-project-creation-post]]'
platforms:
  - Web
  - GitLab
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b9843273-fd7d-4387-9779-d4940f2d88d9
created_at: '2025-12-11T06:10:15.870Z'
updated_at: '2025-12-11T06:10:15.870Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Navigate to Project Creation in GitLab

## Summary

This procedure involves signing into a secondary GitLab account and accessing the project creation page to prepare for request manipulation in exploitation chains.

## Description

Using a different user account ensures the exploit is tested from an unauthorized perspective. Navigation to the creation page triggers the HTTP request that will be intercepted, allowing parameter modifications for template bypass.

## Requirements

1. Secondary GitLab user account
2. Access to the GitLab instance URL
3. Standard browser for navigation

## Defense

Defensive measures and detection strategies:

- Rate limit project creation attempts
- Log and alert on frequent navigation to creation endpoints

## Objectives

1. Position the attacker in their own namespace
2. Initiate the project creation flow
3. Prepare for HTTP interception

## Instructions

### Step 1: Sign In with Secondary Account

**Context**: Switch to the attacker's perspective.

Sign into GitLab using the second account.

> This isolates the exploit to an unauthorized user.

### Step 2: Access Creation Page

**Context**: Load the form for new project creation.

Go to http://instance/projects/new and start creating a new project.

> This prepares the request for modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[commands/gitlab-project-creation-post]]
- [[navigation]]
