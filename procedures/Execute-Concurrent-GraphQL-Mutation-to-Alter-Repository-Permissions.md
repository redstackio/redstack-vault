---
tags:
  - race-condition
  - graphql
  - github
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/github-graphql-update-teams-repo]]'
verified: false
platforms:
  - Web
  - GitHub Enterprise Server
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:32:29.414Z'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
id: b00c541e-3215-4f21-bb0d-41497d7c1008
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Execute-Concurrent-GraphQL-Mutation-to-Alter-Repository-Permissions

## Summary

This procedure performs a GraphQL mutation to update team repository permissions concurrently with a REST API detachment, exploiting the race condition to ensure admin access is retained on the detached repository.

## Description

The updateTeamsRepository GraphQL mutation in GitHub Enterprise Server allows permission changes for teams on repositories. Due to unsynchronized processing with REST API updates, executing this during detachment allows overwriting permissions to preserve admin rights. Targets GHES < 3.13; requires team/repo IDs and admin token.

## Requirements

1. Admin access token
2. Team ID, organization ID, and repository ID
3. curl for GraphQL POST
4. Precise timing (execute within ~1 second of REST call)

## Defense

Defensive measures and detection strategies:

- Add transactional locking between REST and GraphQL endpoints
- Rate-limit concurrent API requests per token
- Log and alert on overlapping repository modification calls

## Objectives

1. Modify team permissions to ADMIN during detachment window
2. Bypass synchronization to retain access
3. Ensure mutation succeeds without rollback

## Instructions

### Step 1: Craft and Send Mutation

**Context**: Time the GraphQL call to overlap with REST detachment processing.

**Command** ([[commands/github-graphql-update-teams-repo]]):
```bash
curl -X POST \
  -H "Authorization: token YOUR_ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  https://YOUR_GHES_HOST/api/v4/graphql \
  -d '{"query": "mutation { updateTeamRepository(input: {teamId: TEAM_ID, ownerId: ORG_ID, repositoryId: REPO_ID, permission: ADMIN}) { clientMutationId } }"}'
```

> Submits the mutation to set ADMIN permission. Use actual IDs. Expected output: JSON with 'data' object confirming mutation.

### Step 2: Validate Timing

**Context**: Ensure no errors from concurrency.

Check response for 'errors': null.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/github-graphql-update-teams-repo]]

## Tools Used


## Tags

- race-condition
- graphql
- github
