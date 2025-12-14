---
tags:
  - race-condition
  - verification
  - github
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/github-check-repo-permissions]]'
verified: false
platforms:
  - Web
  - GitHub Enterprise Server
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:32:29.409Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: de7a959b-0fd4-4806-bf50-17e1673661d1
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Verify-Persistent-Admin-Access-on-Detached-Repository

## Summary

This procedure checks repository permissions post-exploitation to confirm that admin access has been covertly retained despite detachment, validating the race condition success.

## Description

After exploiting the race, query the GitHub API to inspect user or team permissions on the detached repository. In GHES < 3.13, the lack of atomicity allows persistent admin rights. Requires the same admin token and repo details.

## Requirements

1. Admin token used in prior steps
2. Repository and user/team details
3. Access to GHES API

## Defense

Defensive measures and detection strategies:

- Post-operation permission audits on detached repos
- Anomaly detection for retained access after detachment events
- Enforce strict permission revocation on detachment

## Objectives

1. Query and confirm admin permission status
2. Validate exploitation without triggering alerts
3. Document persistent access for further abuse

## Instructions

### Step 1: Query Permissions

**Context**: Retrieve permission details for the user or team on the repository.

**Command** ([[commands/github-check-repo-permissions]]):
```bash
curl -H "Authorization: token YOUR_ADMIN_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://YOUR_GHES_HOST/api/v3/repos/ORG/REPO/collaborators/YOUR_USERNAME/permission
```

> Fetches permission for the specified user. Expected output: JSON with 'permission': 'admin'.

### Step 2: Interpret Results

**Context**: Confirm retention despite detachment.

Look for 'admin' in response; test repo actions if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/github-check-repo-permissions]]

## Tools Used


## Tags

- race-condition
- verification
- github
