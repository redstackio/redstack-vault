---
tags:
  - verification
  - data-loss
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data Destruction]]'
updated_at: '2025-12-14T17:29:20.438Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 7edd4782-60ec-46f1-9cf1-15186f13c1b8
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Data Destruction]]'
---
# Observe-Project-and-Repository-Deletion

## Summary

This procedure verifies the successful exploitation by checking that the targeted project and its repository have been deleted due to the type confusion in the GraphQL mutation.

## Description

Post-exploitation, access to the project is revoked, and the repository is purged. This confirms the vulnerability's impact on data integrity. In a real attack, this leads to irreversible data loss. Use GitLab UI or API queries to observe changes.

## Requirements

1. Access to GitLab instance post-mutation
2. Knowledge of target project ID
3. Optional: Admin access for logs

## Defense

Defensive measures and detection strategies:

- Implement soft deletes or backups for critical resources
- Alert on sudden project/group deletions
- Review audit logs for GraphQL anomalies

## Objectives

1. Confirm project and repository removal
2. Assess scope of data loss
3. Document impact for reporting

## Instructions

### Step 1: Attempt Project Access

**Context**: Try to view the project in GitLab UI or via API.

**Command** (Browser/API):

Navigate to /projects/<project-id> or query GraphQL for project details.

> Expected output: 404 Not Found or null response.

### Step 2: Check Repository

**Context**: Verify repository contents are inaccessible.

**Command** (Git):

Attempt git clone <repo-url>

> Expected output: Repository not found error.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Data Destruction]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification
- data-loss
