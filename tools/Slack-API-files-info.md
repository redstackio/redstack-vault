---
id: tool-slack-api-files-info
url: 'https://slack.com/api/files.info'
tags:
  - api
  - slack
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.083Z'
validated: true
submitted: true
---
# Slack-API-files-info

**Status**: Unverified

## Overview

Slack API endpoint to fetch file metadata, including private URLs for Posts JSON.

## Description

Returns url_private for direct access and editing.

## Features

- Feature 1: File details retrieval
- Feature 2: URL access
- Feature 3: Auth via token

## Installation

### Requirements

- Slack token

### Install Commands

Use curl or API client.

## Basic Usage

```bash
curl -H "Authorization: Bearer token" https://slack.com/api/files.info?file=ID
```

### Common Options


## Examples

### Example 1: Basic Usage

Retrieve private URL.

## MITRE ATT&CK Mapping

### Techniques

- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Discovery]] Discovery

## Detection

- API usage logs.

## Related Procedures


## Related Tools

- [[tools/Slack-Web-UI]]

## References

- Slack API docs
