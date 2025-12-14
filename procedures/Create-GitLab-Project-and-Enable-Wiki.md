---
id: proc-create-gitlab-project
tags:
  - gitlab
  - project-setup
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
updated_at: '2025-12-14T17:23:50.179Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-GitLab-Project-and-Enable-Wiki

## Summary

This procedure sets up a new GitLab project and enables its wiki feature, providing a target for injecting malicious MediaWiki content that triggers Lua execution via WikiCloth.

## Description

In GitLab, projects can have associated wikis for documentation. Enabling the wiki creates a separate .wiki.git repository. This step requires an authenticated user with project creation permissions. The wiki uses MediaWiki markup, processed by WikiCloth, which invokes Lua if rubyluabridge is present. Outcomes include a ready wiki for payload deployment, assuming prior setup of the vulnerable extension.

## Requirements

1. Authenticated GitLab account with developer or higher role
2. Access to GitLab web interface
3. Enabled wiki feature in project settings

## Defense

Defensive measures and detection strategies:

- Restrict wiki edit permissions to trusted users
- Monitor project creation events in GitLab audit logs
- Disable wikis for non-essential projects

## Objectives

1. Establish a wiki-enabled project for exploitation
2. Gain edit access for payload injection
3. Prepare for repository cloning

## Instructions

### Step 1: Create New Project

**Context**: Use GitLab UI to initiate a blank project.

**Command** (Web UI):
No CLI; navigate to 'New Project' > 'Create blank project', enter name and visibility.

> Submits form to create project. Expected output: Project dashboard loads with repo URL.

### Step 2: Enable Wiki

**Context**: Activate wiki functionality in project settings.

**Command** (Web UI):
Go to Project Settings > General > Visibility, project features, permissions > Expand 'Pages' and enable 'Wiki'.

> Saves settings. Expected output: Wiki link appears in project sidebar.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- project-setup
