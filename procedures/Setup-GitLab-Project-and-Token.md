---
tags:
  - gitlab
  - setup
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Linux
  - Docker
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: a1df9481-1bcd-48e7-a7d8-01bdc3ca363f
created_at: '2025-12-11T03:47:39.680Z'
updated_at: '2025-12-11T03:47:39.680Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Setup GitLab Project and Token

## Summary

This procedure sets up a GitLab project with package registry enabled and generates a personal access token for API interactions, serving as prerequisites for exploiting vulnerabilities in the package registry.

## Description

In a GitLab environment, enabling the package registry and creating a project allows access to vulnerable API endpoints. A personal access token is required for authenticated API calls. This setup is targeted at GitLab EE versions vulnerable to path traversal in the Maven package API due to Grape framework issues.

## Requirements

1. Access to GitLab instance configuration
2. Permissions to create projects and tokens
3. GitLab EE 12.4.2-ee or similar vulnerable version

## Defense

Defensive measures and detection strategies:

- Monitor API token creation and usage logs
- Restrict package registry to trusted projects only

## Objectives

1. Enable package registry for vulnerability exposure
2. Create project and token for API access
3. Prepare for exploitation steps

## Instructions

### Step 1: Enable Package Registry

**Context**: Configure GitLab to enable the package registry feature.

Use GitLab configuration to enable the feature (typically via admin UI or config files).

> This exposes the vulnerable Maven API endpoints.

### Step 2: Create Project

**Context**: Create a new project with package registry enabled.

Use GitLab UI or API to create the project.

> Project ID will be used in API calls.

### Step 3: Generate Token

**Context**: Create a personal access token with API permissions.

Use GitLab UI to generate the token and store it securely.

> Token is used for authentication in curl requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[GitLab UI or API]]

## Tags

- #gitlab-rake
- #setup
