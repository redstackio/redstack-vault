---
id: proc-phab-create-repo-admin
tags:
  - phabricator
  - setup
  - administration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:44.822Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Repository-as-Admin-in-Phabricator

## Summary

This procedure outlines how an administrator creates a test repository in Phabricator's Diffusion application to set up the environment for testing authorization bypasses.

## Description

In Phabricator, the Diffusion application manages code repositories. Administrators can create new repositories via the web interface. This step is prerequisite for exploiting the mirror deletion vulnerability, as it establishes a target repository with an associated mirror. The process involves logging in with admin credentials and navigating to the Diffusion create form. Expected outcome is a new repository ready for mirror configuration.

## Requirements

1. Administrative credentials for Phabricator
2. Access to the Phabricator web interface (e.g., http://phabricator/)
3. Diffusion application enabled in the instance

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) for repository management
- Monitor admin actions via audit logs in Phabricator
- Use Phabricator's policy system to restrict repository creation to verified users

## Objectives

1. Create a testable repository named 'TEST'
2. Associate a mirror with the repository
3. Prepare environment for guest user exploitation

## Instructions

### Step 1: Log In as Administrator

**Context**: Authenticate with admin privileges to access management features.

Navigate to the Phabricator login page and enter admin credentials.

### Step 2: Create New Repository

**Context**: Use the Diffusion interface to instantiate a new repository.

Navigate to http://phabricator/diffusion/ and select 'Create Repository'. Enter name 'TEST', select type (e.g., Git), and configure VCS details. Submit the form.

> Upon success, the repository will appear in the Diffusion list with a unique short name 'TEST'.

### Step 3: Configure Mirror

**Context**: Add a mirror to the repository to enable the deletion target.

From the repository view, go to the 'Mirrors' tab and add a new mirror (e.g., URI for a test mirror). Save the configuration.

> Expected: Mirror ID (e.g., 1) assigned and visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[phabricator]]
- [[diffusion]]
- [[setup]]
