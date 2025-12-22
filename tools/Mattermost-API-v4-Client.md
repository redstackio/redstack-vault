---
id: tool-mmw-api-v4-001
url: 'https://github.com/mattermost/mattermost-server/v5/model'
tags:
  - api
  - client
  - mattermost
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T05:32:10.459Z'
validated: true
submitted: true
---
# Mattermost-API-v4-Client

**Status**: Unverified

## Overview

The Mattermost API v4 Client is an SDK for interacting with Mattermost servers, used in POCs to handle authentication, session creation, and file uploads.

## Description

This client library enables Go programs to login, create upload sessions, and post file data to channels, facilitating the delivery of malicious payloads like the OOM GIF in this DoS attack.

## Features

- Feature 1: Authentication via Login method
- Feature 2: Upload session management
- Feature 3: File data posting to channels

## Installation

### Requirements

- Go environment

### Install Commands

```bash
go get github.com/mattermost/mattermost-server/v5/model
go mod tidy
```

## Basic Usage

```bash
go run example.go
```

### Common Options

| Option | Description |
|--------|-------------|
| `NewAPIv4Client(url)` | Initialize client with server URL |
| `Login(username, password)` | Authenticate user |
| `CreateUploadSession(...)` | Start file upload |

## Examples

### Example 1: Basic Usage

```go
client := model.NewAPIv4Client("http://localhost:8065/")
_, _ = client.Login("toto", "tototo")
```

### Example 2: Advanced Usage

```go
session, _ := client.CreateUploadSession(channelId, "file.gif", 31)
client.UploadData(session, gifData)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: API logs showing session creations and uploads
- Detection method 2: Unusual file uploads from scripted clients

## Related Procedures

- [[procedures/Upload-Malicious-GIF-for-OOM-Attack]]

## Related Tools

- [[tools/Go]]

## References

- GitHub repo: https://github.com/mattermost/mattermost-server/v5/model
