---
tags:
  - gitlab
  - ci-setup
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[T1213.003]]'
updated_at: '2025-12-14T17:29:36.659Z'
skill_level: intermediate
impact_level: low
sub_techniques: []
id: bb985b63-672b-4fcc-8c60-2bd974a85da1
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1213.003]]'
---
# Setup-GitLab-Project-with-CI

## Summary

This procedure sets up a GitLab project with CI/CD pipelines to prepare for testing visibility restrictions, enabling the creation of a baseline environment where sensitive build information can be generated.

## Description

In a GitLab instance, create a new public project, configure basic CI using a .gitlab-ci.yml file, and push code to trigger pipelines. This simulates a development project with build artifacts, targeting the 'test/cibadges' namespace. The goal is to establish pipelines that produce status and coverage data, which will later be restricted and tested for leakage.

## Requirements

1. Active GitLab account with project creation permissions
2. Access to Git (local installation for pushing code)
3. Basic knowledge of YAML for CI configuration

## Defense

Defensive measures and detection strategies:

- Monitor project creation events in GitLab audit logs
- Enforce role-based access controls (RBAC) for project setup
- Use GitLab's CI variable masking to limit exposed data

## Objectives

1. Create and initialize a GitLab project with functional CI
2. Trigger initial pipeline runs to generate build data
3. Verify project setup before applying restrictions

## Instructions

### Step 1: Create New Project

**Context**: Log in to GitLab and initiate a new repository under the specified namespace.

Navigate to GitLab dashboard, click 'New Project', select 'Create blank project', set namespace to 'test/cibadges', name it appropriately, and set visibility to public initially.

### Step 2: Configure CI Pipeline

**Context**: Add a basic CI configuration to run builds and generate status/coverage.

Create a .gitlab-ci.yml file with a simple job, e.g.,:

```yaml
stages:
  - build

build_job:
  stage: build
  script:
    - echo "Building..."
  coverage: '/coverage: \d+\.\d+%/'
```

Commit this file to the repository.

### Step 3: Push Code and Trigger Pipeline

**Context**: Push the configuration to activate CI.

Use Git to add, commit, and push the files to the master branch, observing the pipeline run in the GitLab UI.

**Expected Output**: Pipeline status shows as 'passed' with optional coverage metrics.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1213.003]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- ci-setup
