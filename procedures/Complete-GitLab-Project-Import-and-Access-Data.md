---
tags:
  - gitlab
  - data-access
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/gitlab-project-creation-post]]'
platforms:
  - Web
  - GitLab
techniques:
  - '[[Data from Cloud Storage]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 320c1c80-53bf-4584-b436-49f4d2f6af52
created_at: '2025-12-11T06:10:15.863Z'
updated_at: '2025-12-11T06:10:15.863Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1530]]'
---
# Complete GitLab Project Import and Access Data

## Summary

This procedure involves waiting for the GitLab background import job to finish and verifying access to the unauthorizedly copied project data.

## Description

After modifying the request, GitLab's Sidekiq processes the export and import without re-checking permissions, resulting in sensitive data like confidential issues and repositories being available in the attacker's project.

## Requirements

1. Successful modified request from prior step
2. Access to the new project page
3. Patience for background job completion (a few minutes)

## Defense

Defensive measures and detection strategies:

- Add permission re-checks in export/import workers
- Audit logs for unexpected project imports

## Objectives

1. Confirm import completion
2. Access copied sensitive data
3. Validate exploit success

## Instructions

### Step 1: Monitor Import Progress

**Context**: Wait for the server to process the request.

Forward the modified request; the server will redirect to an import progress page.

> Monitor for completion status.

### Step 2: Access Copied Data

**Context**: Verify the presence of restricted data.

After a few minutes, refresh the new project page to view the imported repository, issues, snippets, etc.

> Ensure all restricted elements are accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Data from Cloud Storage]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[commands/gitlab-project-creation-post]]
- [[data-access]]
