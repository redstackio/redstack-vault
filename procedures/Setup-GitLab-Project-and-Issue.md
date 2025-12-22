---
tags:
  - setup
  - gitlab
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:26:56.013Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 073a03d5-b944-48c9-be37-e83841dfc8ba
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-GitLab-Project-and-Issue

## Summary

This procedure establishes a test environment in GitLab by authenticating, creating a project, and setting up an issue with baseline comments, preparing for DoS exploitation.

## Description

In the context of testing GitLab vulnerabilities, this setup uses the web UI to create a public project and issue. It requires a valid account and simulates normal user activity to avoid detection. Expected outcomes include a functional issue ready for oversized comment injection, with no immediate impact but enabling subsequent DoS steps.

## Requirements

1. Valid GitLab credentials (username/password or session)
2. Access to GitLab web interface (browser)
3. No elevated privileges needed

## Defense

Defensive measures and detection strategies:

- Monitor for rapid project/issue creation from new accounts
- Rate-limit project and issue creation
- Log authentication and UI actions

## Objectives

1. Gain authenticated access to GitLab
2. Create a target project and issue
3. Establish baseline for normal comment rendering

## Instructions

### Step 1: Sign In to GitLab

**Context**: Authenticate to access project creation features.

No command; use browser to log in at https://gitlab.com/users/sign_in.

> Successful login redirects to dashboard.

### Step 2: Create a New Project

**Context**: Set up a public test project.

No command; in UI, select "New project", name "test01", slug "test01", visibility "Public", initialize with README.

> Project page loads with README.

### Step 3: Create a New Issue

**Context**: Target for comments.

No command; in project, click "Issues" > "New issue", add title/description, submit.

> Issue #1 created.

### Step 4: Post Initial Comments

**Context**: Baseline normal behavior.

No command; add 1-2 short comments via UI.

> Comments render correctly.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- gitlab
