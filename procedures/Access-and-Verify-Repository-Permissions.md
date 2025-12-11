---
tags:
  - repository-access
  - github
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b155d822-b7dc-4949-8354-04b375452551
created_at: '2025-12-11T03:48:06.066Z'
updated_at: '2025-12-11T03:48:06.066Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1087]]'
---
# Access and Verify Repository Permissions

## Summary

This procedure confirms repository access by listing org repos via API and cloning one using the token, providing proof of read/write permissions.

## Description

After token validation, query repo lists and perform a clone to demonstrate unauthorized access potential, such as pushing malicious code.

## Requirements

1. Valid GH_TOKEN
2. git installed
3. Access to GitHub API and repos

## Defense

Defensive measures and detection strategies:

- Enable GitHub audit logs and monitor for anomalous clones
- Restrict token scopes to minimum necessary

## Objectives

1. List private repos
2. Clone for proof
3. Compute file hash for verification

## Instructions

### Step 1: List Organization Repos

**Context**: Query repo list to check permissions.

Use curl to GET https://api.github.com/orgs/Shopify/repos with token headers.

> Returns JSON list of repos with permissions.

### Step 2: Clone Repository

**Context**: Verify access by cloning.

Execute [[commands/git-clone-repo]]:

```bash
git clone https://$GH_TOKEN@github.com/Shopify/shopify.git /tmp/shopify
```

> Clones repo to local directory.

### Step 3: Compute Proof Hash

**Context**: Generate SHA512 of a file.

Navigate to cloned dir and run sha512sum README.md.

> Provides non-destructive proof of access.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques



## Commands Used

- [[commands/git-clone-repo]]

## Tools Used

- #curl
- #git

## Tags

- repository-access
- github
