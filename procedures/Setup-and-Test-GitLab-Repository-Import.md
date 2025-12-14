---
tags:
  - gitlab
  - setup
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:26.209Z'
sub_techniques: []
id: 32d791ff-2a00-43d0-ae18-2e13e8b3c646
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Setup-and-Test-GitLab-Repository-Import

## Summary

This procedure sets up a fresh GitLab 9.0 CE installation and tests the Repository Import functionality to explore potential vulnerabilities in the import workflow.

## Description

In a controlled environment, deploy GitLab 9.0 CE and access the Repository Import feature for a project. This step simulates legitimate user interaction to baseline the system's behavior, particularly error handling during permission checks. The target is a web-based GitLab instance where import attempts can reveal internal parameters.

## Requirements

1. Access to a server for installing GitLab 9.0 CE (e.g., Ubuntu or similar Linux distro)
2. Administrative privileges on the server
3. A GitLab user account with project creation capabilities
4. Web browser for testing

## Defense

Defensive measures and detection strategies:

- Monitor GitLab installation logs for unauthorized setups
- Enforce strict access controls on import features
- Log all import attempts and parameter manipulations

## Objectives

1. Establish a testable GitLab environment
2. Verify Repository Import accessibility
3. Identify baseline error responses

## Instructions

### Step 1: Install GitLab 9.0 CE

**Context**: Deploy a fresh instance to mimic a vulnerable target.

Follow official GitLab installation guides for version 9.0 CE on your OS. For example, on Ubuntu:

Access the admin panel and create a new project/repository.

**Expected Output**: Running GitLab instance at http://<instance>.

### Step 2: Access Repository Import

**Context**: Navigate to the import feature to test functionality.

Log in with a user account, select a project, and go to Settings > Import/Export > Repository Import.

**Expected Output**: Import interface loads, allowing URL input for repository cloning.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[setup]]
- [[recon]]
