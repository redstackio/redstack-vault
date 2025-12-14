---
tags:
  - github
  - rest-api
  - repo-transfer
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/curl-github-repo-transfer-rest]]'
verified: false
platforms:
  - Web
  - GitHub Enterprise Server
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:29.340Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 08b47128-c49d-48ff-a045-551eaea6ac6a
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-GitHub-Repository-Transfer-via-REST-API

## Summary

This procedure initiates the transfer of a GitHub repository to another organization using the REST API, creating the initial window for exploiting a race condition in GitHub Enterprise Server.

## Description

In GitHub Enterprise Server 3.8.0+, the repository transfer process via REST API starts asynchronously, leaving a vulnerability window where permissions are not immediately synchronized. An admin with ownership can trigger this to set up concurrent operations. Prerequisites include admin access and a valid token with repo scopes.

## Requirements

1. GitHub Personal Access Token with 'repo' and 'admin:org' scopes
2. Access to the source organization and repository
3. Target organization ID
4. curl or equivalent HTTP client

## Defense

Defensive measures and detection strategies:

- Monitor API logs for concurrent transfer and permission update requests
- Implement rate limiting on transfer endpoints
- Use webhooks to audit permission changes during transfers

## Objectives

1. Begin repository transfer without immediate permission lock
2. Create race window for permission manipulation
3. Ensure transfer initiates successfully

## Instructions

### Step 1: Prepare Transfer Request

**Context**: Authenticate and target the repo transfer endpoint to start the process.

**Command** ([[commands/curl-github-repo-transfer-rest]]):
```bash
curl -X POST \
  -H "Authorization: token YOUR_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://ghe.example.com/api/v3/repos/OWNER/REPO/transfer \
  -d '{"new_owner": "target-org"}'
```

> This command sends a POST request to initiate transfer. Expected output is a JSON confirmation; errors indicate insufficient perms.

### Step 2: Monitor Initiation

**Context**: Verify the transfer has started but not completed.

**Command** ([[commands/curl-github-repo-transfer-rest]]):
```bash
curl -H "Authorization: token YOUR_TOKEN" \
  https://ghe.example.com/api/v3/repos/OWNER/REPO
```

> Check repo status; look for transfer in progress.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-github-repo-transfer-rest]]

## Tools Used


## Tags

- [[github]]
- [[rest-api]]
- [[repo-transfer]]
