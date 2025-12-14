---
tags:
  - verification
  - permissions
  - admin-access
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/curl-check-repo-permissions]]'
verified: false
platforms:
  - Web
  - GitHub Enterprise Server
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:29.337Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 37096508-2841-469d-b2dc-05a9ef58e1e4
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Verify-Retained-Admin-Access-on-Transferred-Repository

## Summary

This procedure confirms that the original administrator retains admin permissions on the transferred repository after the race condition exploit in GitHub Enterprise Server.

## Description

Post-transfer, query the API to check collaborator permissions. Successful exploitation shows 'admin' status despite the transfer, indicating persistent access. This validates the bypass of permission revocation.

## Requirements

1. Token with read access to target org repo
2. Username of the original admin
3. Completed transfer

## Defense

Defensive measures and detection strategies:

- Regularly audit post-transfer permissions
- Log all permission queries for anomalies
- Implement automated permission resets after transfers

## Objectives

1. Confirm admin retention
2. Validate exploit success
3. Identify any partial failures

## Instructions

### Step 1: Query Permissions

**Context**: Check the specific user's permission level on the repo.

**Command** ([[commands/curl-check-repo-permissions]]):
```bash
curl -H "Authorization: token YOUR_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://ghe.example.com/api/v3/repos/target-org/REPO/collaborators/USERNAME/permission
```

> Returns permission level; 'admin' confirms success.

### Step 2: Test Access Actions

**Context**: Perform an admin action to verify functionality.

**Command** ([[commands/curl-check-repo-permissions]]):
```bash
curl -X PUT \
  -H "Authorization: token YOUR_TOKEN" \
  https://ghe.example.com/api/v3/repos/target-org/REPO \
  -d '{"name": "REPO-updated"}'
```

> If rename succeeds, access is retained.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-repo-permissions]]

## Tools Used


## Tags

- [[verification]]
- [[permissions]]
- [[admin-access]]
