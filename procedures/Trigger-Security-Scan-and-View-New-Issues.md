---
id: proc-gitlab-trigger-scan-view-issues
tags:
  - gitlab
  - ci-cd
  - security-scan
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:36.599Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Trigger-Security-Scan-and-View-New-Issues

## Summary

This procedure generates new security scan results in a GitLab project via CI/CD and confirms unauthorized viewing by a demoted guest user through their personal dashboard.

## Description

As owner (User A), upload files to trigger a pipeline with security scanning (e.g., yarn audit on dependencies). As guest (User B), refresh the personal dashboard to see new issues, exposing fresh vulnerabilities, dependencies, and structure. This amplifies the bypass by showing dynamic data post-demotion. Expected outcome: New scan results visible to unauthorized user.

## Requirements

1. Project with CI/CD configured for security scans
2. Files to upload (e.g., .gitlab-ci.yml, package.json with vulnerable deps)
3. Guest access via dashboard

## Defense

Defensive measures and detection strategies:

- Restrict scan result visibility to project members only
- Log and alert on dashboard views of scan data
- Auto-revoke dashboard access on permission changes

## Objectives

1. Produce new vulnerability data for exposure
2. Verify ongoing unauthorized access to dynamic info
3. Enable exploitation planning based on disclosed details

## Instructions

### Step 1: Configure and Upload Files

**Context**: Set up CI/CD to run security scans as owner.

As User A, create/edit .gitlab-ci.yml with security job (e.g., include: dependency_scanning), upload package.json from a vulnerable project like 'yarn-vulnerabilities' via web IDE or repo push.

> Pipeline triggers on commit.

### Step 2: Monitor Pipeline and Refresh Dashboard

**Context**: Wait for scan completion and check unauthorized view.

As User A, view pipeline results (e.g., 1 critical, 8 medium, 8 low issues). As User B, refresh personal security dashboard for the project.

> New issues appear, detailing files, deps, and vulns.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[ci-cd]]
- [[security-scan]]
- [[information-disclosure]]
