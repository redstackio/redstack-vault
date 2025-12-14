---
tags:
  - integration
  - git
  - submodule
type: procedure
tools:
  - '[[tools/git]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/git-init]]'
  - '[[commands/git-submodule-add-atlassian]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:30.379Z'
sub_techniques: []
id: 51441238-3591-4523-b0be-eebd7ddd2cdb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Integrate-Atlassian-Package

## Summary

This procedure adds the vulnerable atlasboard-atlassian-package to the Atlasboard project using Git submodules, enabling the use of JIRA-integrated widgets like the 'blockers' widget that suffers from XSS due to unsanitized input handling.

## Description

The atlasboard-atlassian-package provides widgets for displaying JIRA data on Atlasboard dashboards. By adding it as a submodule, the project gains access to the vulnerable blockers.js file (line 44), where jQuery's .append() inserts raw JIRA summaries into the DOM. Prerequisites include a Git-initialized project directory. The outcome is the package source available locally for configuration.

## Requirements

1. Git installed and configured on the system
2. Existing Atlasboard project directory (from prior setup)
3. Internet access to clone the Bitbucket repository
4. Write permissions in the project directory

## Defense

Defensive measures and detection strategies:

- Audit Git submodules for third-party packages with known vulnerabilities
- Use dependency scanners like npm audit or Snyk on integrated packages
- Restrict submodule additions in CI/CD pipelines

## Objectives

1. Incorporate the vulnerable Atlassian package into the dashboard
2. Enable JIRA data fetching capabilities
3. Prepare for widget configuration exploiting the XSS flaw

## Instructions

### Step 1: Initialize Git Repository

**Context**: Set up version control in the dashboard project to support submodule addition.

**Command** ([[commands/git-init]]):
```bash
git init
```

> Initializes an empty Git repository. Expected output: 'Initialized empty Git repository in /path/to/mywallboard/.git/'.

### Step 2: Add Atlassian Package as Submodule

**Context**: Clone the package repository into the local 'packages/atlassian' path and register it as a submodule.

**Command** ([[commands/git-submodule-add-atlassian]]):
```bash
git submodule add https://bitbucket.org/atlassian/atlasboard-atlassian-package packages/atlassian
```

> Downloads the repository and updates .gitmodules. Expected output: Cloning logs and confirmation of submodule registration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/git-init]]
- [[commands/git-submodule-add-atlassian]]

## Tools Used

- [[tools/git]]

## Tags

- [[integration]]
- [[tools/git]]
- [[submodule]]
