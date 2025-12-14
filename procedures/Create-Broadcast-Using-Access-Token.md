---
tags:
  - api-abuse
  - broadcast
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-create-broadcast]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:35.121Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f0dbf9ce-0435-4b82-b5ea-1e8defb0d1fa
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create Broadcast Using Access Token

## Summary

This procedure uses the stolen access token to create a new broadcast via the Periscope API, demonstrating unauthorized control over the victim's account.

## Description

With the bearer token, POST to /v1/broadcast/create with title and description. This initiates a broadcast resource under the victim's account, visible in their dashboard.

## Requirements

1. Valid access token
2. curl for API call
3. Broadcast details (title, description)

## Defense

Defensive measures and detection strategies:

- Rate-limit API endpoints
- Audit logs for unusual broadcast creations
- Require additional verification for sensitive actions

## Objectives

1. Initiate unauthorized broadcast
2. Prove API access
3. Prepare for publication

## Instructions

### Step 1: Prepare Broadcast Data

**Context**: Define broadcast params.

Title: "Test Broadcast", Description: "CSRF Demo"

### Step 2: Send Create Request

**Context**: POST to API with auth header.

Execute [[commands/curl-create-broadcast]]:

```bash
curl -X POST https://public-api.periscope.tv/v1/broadcast/create \
  -H "Authorization: Bearer <access_token>" \
  -d "title=Test Broadcast" \
  -d "description=CSRF Demo"
```

> Expected: {"broadcast_id": "12345"}

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-create-broadcast]]

## Tools Used


## Tags

- [[broadcast-create]]
- [[api-execution]]
