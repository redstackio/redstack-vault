---
tags:
  - gitlab
  - setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: dffdc45f-c528-4698-8aa1-94cdffddd648
created_at: '2025-12-14T03:46:09.480Z'
updated_at: '2025-12-14T03:46:09.480Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-GitLab-Repository

## Summary

This procedure sets up a new repository in GitLab, providing the foundation for webhook integration and event triggering in SSRF exploitation scenarios.

## Description

In the context of exploiting GitLab's ToCToU vulnerability, creating a repository allows authenticated users to configure web hooks. This step uses the standard GitLab interface and requires no special privileges beyond basic user access. Expected outcomes include a functional repository ready for commits and webhook setup.

## Requirements

1. Authenticated GitLab account
2. Web browser access to GitLab instance
3. No prior repository access needed

## Defense

Defensive measures and detection strategies:

- Monitor new repository creations for anomalous patterns
- Enforce project approval workflows

## Objectives

1. Establish base for webhook exploitation
2. Enable push event simulation
3. Prepare for ToCToU bypass setup

## Instructions

### Step 1: Access GitLab Dashboard

**Context**: Log in to initiate repository creation.

**Command** (Browser Action):
No CLI command; use web UI to click 'New Project' and select 'Create blank project'.

> Fill in name, description, and visibility. Click 'Create project'.

### Step 2: Verify Repository

**Context**: Confirm creation success.

**Command** (Git Clone Test):
```bash
git clone https://gitlab.com/<user>/<repo>.git
```

> Expected output: Repository cloned locally.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[setup]]
