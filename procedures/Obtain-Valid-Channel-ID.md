---
id: proc-obtain-channel-id
tags:
  - recon
  - api
  - mattermost
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.360Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Obtain-Valid-Channel-ID

## Summary

This procedure retrieves a valid channel ID from a Mattermost instance to enable targeted file uploads via the API.

## Description

Channel IDs are required for API endpoints like file uploads. This step involves interacting with the Mattermost UI or API to extract an ID, setting up for the malicious upload that exploits the decoding vulnerability.

## Requirements

1. Access to running Mattermost instance
2. User login if authentication is enabled
3. Browser or API client

## Defense

Defensive measures and detection strategies:

- Log API access to channels
- Enforce authentication on all endpoints
- Monitor for unusual channel queries

## Objectives

1. Identify a target channel for upload
2. Obtain ID for API exploitation
3. Ensure compatibility with upload session

## Instructions

### Step 1: Access Mattermost UI

**Context**: Log in and navigate to a channel.

No command; use browser to visit http://localhost:8065, create or join a channel.

> Expected: Channel visible in sidebar.

### Step 2: Extract Channel ID

**Context**: Use developer tools or API.

**Command** (curl example for API):
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" http://localhost:8065/api/v4/channels
```

> Parses JSON response for channel IDs. Expected: List of channels with IDs.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- api
- mattermost
