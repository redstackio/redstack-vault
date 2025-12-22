---
id: proc-mmw-channel-id-001
tags:
  - recon
  - mattermost
  - api
type: procedure
tools:
  - '[[tools/Mattermost-API-v4-Client]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T05:32:10.474Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Obtain-Mattermost-Channel-ID

## Summary

This procedure retrieves a valid channel ID from a running Mattermost instance, necessary for targeting file uploads in the API.

## Description

Channel IDs are used in Mattermost API calls for context-specific actions like file uploads. This step involves logging into the UI or querying the API to extract an ID, such as from the default town-square channel.

## Requirements

1. Running Mattermost server accessible at http://localhost:8065
2. Valid login credentials (e.g., toto/tototo)
3. Browser or API client for access

## Defense

Defensive measures and detection strategies:

- Log and monitor API access patterns for unusual queries
- Enforce authentication and rate limiting on channel-related endpoints
- Use audit logs to track channel ID retrievals

## Objectives

1. Gain access to a specific channel context
2. Extract ID for subsequent API interactions
3. Prepare for targeted upload exploitation

## Instructions

### Step 1: Login to Mattermost UI

**Context**: Authenticate to access channels.

**Command**:

> Navigate to http://localhost:8065, enter credentials toto/tototo, and login.

### Step 2: Extract Channel ID

**Context**: Identify and copy the channel ID from UI or API.

**Command**:

> In the browser, inspect the channel element or use API call like GET /api/v4/channels to list channels. Example ID: '5dtj9hf89ifap8imigbzjc7wjo'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mattermost-API-v4-Client]]

## Tags

- recon
- mattermost
- api
