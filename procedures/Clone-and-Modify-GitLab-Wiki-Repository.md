---
id: 25cdfaef-97a1-46c5-802e-54a9eed3e42e
name: Clone and Modify GitLab Wiki Repository
type: procedure
verified: false
submitted: true
created_at: '2025-12-09T00:20:45.031Z'
updated_at: '2025-12-09T00:20:45.031Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - gitlab
  - wiki-clone
commands: []
platforms:
  - Linux
  - Docker
tools: []
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---

# Clone and Modify GitLab Wiki Repository

## Summary

This procedure creates a new GitLab project with a Wiki, clones the Wiki repository, and prepares it for adding malicious content.

## Description

GitLab Wikis are backed by Git repositories. Cloning allows local modification and pushing of files that will be rendered by the server, exploiting vulnerabilities in the rendering process.

## Requirements

1. GitLab account with project creation rights
2. Git installed on local machine
3. SSH access configured for GitLab

## Defense

Defensive measures and detection strategies:

- Monitor project and Wiki creations
- Audit git push events for suspicious commits

## Objectives

1. Establish local Wiki repo
2. Create default Wiki page
3. Prepare for malicious file addition

## Instructions

### Step 1: Create Project and Clone Wiki

**Context**: Clone the Wiki repo after creating a project.

**Command** (#git-clone-wiki-repo):
```bash
git clone git@gitlab-docker.local:root/proj1.wiki.git
```

> This clones the Wiki repository for local editing.

Create a default home page in the Wiki via the web interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- #git-clone-wiki-repo

## Tools Used

- #git

## Tags

- #gitlab
- #git-clone-wiki-repo
