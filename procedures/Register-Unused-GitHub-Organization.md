---
id: proc-uuid-002
tags:
  - github
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitHub
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Email Accounts]]'
updated_at: '2025-12-14T17:33:06.717Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Email Accounts]]'
---
# Register-Unused-GitHub-Organization

## Summary

This procedure demonstrates registering an unused GitHub organization name referenced in external documentation, enabling control over associated repositories for potential malicious hosting.

## Description

GitHub allows public registration of organization names if not already claimed. In this attack scenario, the 'macrosan-csi' organization was unused despite being linked in Kubernetes CSI docs. By registering it, the attacker gains the ability to claim repos under that org. This is a form of account squatting leading to supply chain risks. Prerequisites: A GitHub account with org creation enabled. Expected outcomes: Ownership of the org, setting the stage for repository takeover and malicious code deployment.

## Requirements

1. Active GitHub account
2. Organization creation permissions (default for verified accounts)
3. Knowledge of the target org name from reconnaissance

## Defense

Defensive measures and detection strategies:

- Proactively register all referenced org names in documentation
- Monitor GitHub for squatting on project-related names
- Use GitHub's organization verification features

## Objectives

1. Claim the unused organization
2. Verify control over the org
3. Prepare for repository creation under the org

## Instructions

### Step 1: Navigate to Organization Creation

**Context**: Log in and access GitHub's org setup.

No command required; go to https://github.com/account/organizations/new.

> Enter the name 'macrosan-csi' and complete registration.

### Step 2: Confirm Registration

**Context**: Validate the new org exists.

No command required; visit https://github.com/macrosan-csi.

> Expected output: Organization page under your control, no prior content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Email Accounts]] Compromise Accounts: Social Media Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- GitHub web interface

## Tags

- [[github]]
- [[account-takeover]]
