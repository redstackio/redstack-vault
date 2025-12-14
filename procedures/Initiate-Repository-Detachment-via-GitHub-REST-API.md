---
tags:
  - race-condition
  - rest-api
  - github
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/github-rest-update-repo-detach]]'
verified: false
platforms:
  - Web
  - GitHub Enterprise Server
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:32:29.419Z'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
id: a9b953b3-6325-44e0-8373-740e37bb76f6
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Initiate-Repository-Detachment-via-GitHub-REST-API

## Summary

This procedure initiates the detachment of a repository from an organization or team using GitHub's Repo Update REST API, creating the initial timing window necessary for exploiting a race condition to retain admin access.

## Description

In GitHub Enterprise Server, the Repo Update REST API allows admins to modify repository settings, including detachment from organizations or teams. This asynchronous process lacks proper locking, enabling concurrent operations. The procedure targets versions prior to 3.13 and requires an admin token. Successful execution starts the detachment without immediate completion, setting up the race.

## Requirements

1. Admin access token for the GitHub Enterprise Server instance
2. Knowledge of the organization/repo names
3. curl or equivalent HTTP client
4. Network access to the GHES API endpoint

## Defense

Defensive measures and detection strategies:

- Implement API request queuing or locking to prevent concurrent modifications
- Monitor for rapid successive API calls from the same token (e.g., REST followed by GraphQL within seconds)
- Audit logs for detachment initiations without completion

## Objectives

1. Trigger repository detachment process via REST API
2. Ensure the process remains in a pending state for overlap with other operations
3. Prepare for race condition exploitation

## Instructions

### Step 1: Prepare API Request

**Context**: Authenticate and target the specific repository for detachment update.

**Command** ([[commands/github-rest-update-repo-detach]]):
```bash
curl -X PATCH \
  -H "Authorization: token YOUR_ADMIN_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://YOUR_GHES_HOST/api/v3/repos/ORG/REPO \
  -d '{"private": true, "archived": true}'
```

> This command updates the repository to archived/private state, initiating detachment. Replace placeholders with actual values. Expected output is a 200 OK with JSON of updated repo details.

### Step 2: Monitor Response

**Context**: Verify the detachment has started but not finalized.

No specific command; parse the JSON response for status indicators like 'archived': true.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/github-rest-update-repo-detach]]

## Tools Used


## Tags

- race-condition
- rest-api
- github
