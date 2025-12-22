---
tags:
  - docker
  - blobs
  - download
  - source-code
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/docker-blob-download]]'
verified: false
platforms:
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:31:30.930Z'
sub_techniques: []
id: 4b0a5742-6bca-4eae-b27f-686cec8636c7
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Download Docker Image Layers

## Summary

This procedure downloads individual Docker image layers (blobs) as .tar.gz archives from an unauthenticated registry, extracting source code and files from confidential repositories.

## Description

Using blob digests from the manifest, GET /v2/<namespace>/<repo>/blobs/<digest> to fetch layers. In the exposed .mil registry attack, this yields archives with tools and code. Requires digest; results in downloadable files for analysis.

## Requirements

1. Blob digest from manifest
2. HTTP client with output redirection
3. Sufficient storage for archives

## Defense

Defensive measures and detection strategies:

- Authenticate blob downloads
- Size-limit and log large transfers
- Scan for anomalous download traffic

## Objectives

1. Download specific image layers
2. Extract contained files and source code
3. Access confidential repository contents

## Instructions

### Step 1: Download Blob

**Context**: Fetch the layer using its digest.

**Command** ([[commands/docker-blob-download]]):
```bash
curl -X GET 'https://TARGET_IP/v2/NAMESPACE/REPO/blobs/sha256:ABC123...' -H 'Host: TARGET_IP' -H 'Accept: */*' -o layer.tar.gz
```

> Downloads the .tar.gz file containing layer data.

### Step 2: Extract Archive

**Context**: Unpack to access source code.

**Command** ([[commands/tar-extract]]):
```bash
tar -xzf layer.tar.gz
```

> Reveals files, directories, and source code from the layer.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used

- [[commands/docker-blob-download]]
- [[commands/tar-extract]]

## Tools Used


## Tags

- docker
- blobs
- download
