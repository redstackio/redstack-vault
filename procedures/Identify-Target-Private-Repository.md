---
tags:
  - recon
  - github
  - repository-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - GitHub Enterprise Server
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 48566731-7603-46f3-8734-25f93066c684
created_at: '2025-12-14T17:30:58.326Z'
updated_at: '2025-12-14T17:30:58.326Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify-Target-Private-Repository

## Summary

This procedure involves reconnaissance to identify the name of a target private repository on GitHub Enterprise Server, setting the stage for unauthorized access attempts via IDOR.

## Description

In the context of exploiting access control vulnerabilities, the attacker must first pinpoint a private repository they do not have permission to access. This is typically done through prior knowledge, social engineering, or observing indirect references in shared GitHub features like issues or notifications. The procedure assumes an authenticated session but no direct repo access, focusing on gathering the repository name as a prerequisite for triggering the diff exploit.

## Requirements

1. Authenticated GitHub Enterprise Server session
2. Prior contextual knowledge or reconnaissance of user activities
3. Access to shared GitHub features (e.g., organization overviews)

## Defense

Defensive measures and detection strategies:

- Implement strict repository naming conventions and avoid predictable names
- Monitor for anomalous access patterns to diff features
- Use role-based access controls to limit visibility of repo names

## Objectives

1. Obtain the exact name of a private target repository
2. Confirm lack of direct access permissions
3. Prepare identifiers for subsequent exploit steps

## Instructions

### Step 1: Reconnaissance for Repository Names

**Context**: Leverage existing interactions or public leaks to identify private repo names without direct access.

No specific command; manually review GitHub notifications, issues, or external sources for mentions of private repos.

> Expected output: Noted repository name, e.g., "user/private-project".

### Step 2: Verify Target Isolation

**Context**: Ensure the identified repo is private and inaccessible to confirm exploit viability.

Attempt a direct access check via the web UI; expect a 404 or permission denied.

> Expected output: Access denied confirmation, validating the target.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[github]]
