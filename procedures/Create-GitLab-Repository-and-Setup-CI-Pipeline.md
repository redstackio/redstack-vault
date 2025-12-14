---
tags:
  - gitlab
  - repository-setup
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:39.129Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 23e4924a-bc7d-40af-80ca-37d3e0425534
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-GitLab-Repository-and-Setup-CI-Pipeline

## Summary

This procedure sets up a new GitLab repository and configures a basic CI/CD pipeline structure to prepare for generating exploit artifacts in subsequent steps of a stored XSS attack.

## Description

In the context of exploiting GitLab's Mermaid rendering vulnerability, creating a repository provides the foundation for committing malicious Markdown and triggering pipelines. The target environment is GitLab.com or a self-hosted instance with CI/CD enabled. Prerequisites include an authenticated GitLab account. Expected outcomes: A functional project ready for payload deployment, enabling the chain to proceed to artifact generation.

## Requirements

1. Authenticated GitLab session with project creation permissions
2. Web browser access to GitLab UI
3. No special tools required; uses native GitLab interface

## Defense

Defensive measures and detection strategies:

- Monitor new repository creations for suspicious naming or rapid commits
- Enforce project approval workflows for CI/CD in enterprise setups
- Log and alert on pipeline triggers from untrusted repos

## Objectives

1. Establish a project for hosting exploit files
2. Verify CI/CD functionality for artifact production
3. Prepare for embedding XSS payload without detection

## Instructions

### Step 1: Create New Repository

**Context**: Use GitLab's UI to initialize a blank project, avoiding any initial content that might trigger scans.

No command required; navigate to 'New Project' in GitLab dashboard, select 'Create blank project', enter name (e.g., 'mermaid-test'), visibility (private for stealth), and create.

> Successful creation redirects to the empty repo dashboard.

### Step 2: Initialize CI/CD Structure

**Context**: Add a basic .gitlab-ci.yml to test pipeline execution, ensuring artifacts can be generated later.

Commit an empty or template .gitlab-ci.yml via web editor:

```yaml
stages:
  - build

build-job:
  stage: build
  script:
    - echo "Pipeline ready"
  artifacts:
    paths:
      - dummy.txt
```

> Pipeline runs on commit, confirming CI setup; check jobs tab for success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[ci-cd]]
