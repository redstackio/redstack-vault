---
tags:
  - docker
  - manifest
  - blobs
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/docker-manifest-retrieve]]'
verified: false
platforms:
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:30.934Z'
sub_techniques: []
id: 6fdedf0f-26f5-4df9-9f22-26e46f406422
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve Docker Image Manifest

## Summary

This procedure fetches the manifest for a specific Docker image tag, extracting blob digests needed to download layers containing source code from an unauthenticated registry.

## Description

Query /v2/<namespace>/<repo>/manifests/<tag> to get the JSON manifest with fsLayers. In the .mil registry scenario, this reveals layer hashes without auth, enabling targeted downloads. Requires tag knowledge; outputs digests for blob access.

## Requirements

1. Repository and tag details
2. curl for HTTP requests
3. Registry accessibility

## Defense

Defensive measures and detection strategies:

- Authenticate manifest requests
- Encrypt or obfuscate manifests
- Monitor for manifest access patterns

## Objectives

1. Obtain image manifest JSON
2. Extract fsLayers blobSums
3. Prepare for layer downloads

## Instructions

### Step 1: Get Manifest

**Context**: Request the manifest using the tag.

**Command** ([[commands/docker-manifest-retrieve]]):
```bash
curl -X GET 'https://TARGET_IP/v2/NAMESPACE/REPO/manifests/3.0.1' -H 'Host: TARGET_IP' -H 'Accept: */*'
```

> Returns JSON with config and fsLayers, including sha256 digests.

### Step 2: Extract Digests

**Context**: Parse the fsLayers for blobSums.

**Command** ([[commands/jq-extract-digests]]):
```bash
curl -s 'https://TARGET_IP/v2/NAMESPACE/REPO/manifests/3.0.1' | jq '.fsLayers[].blobSum'
```

> Lists digests like sha256:abc123...

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/docker-manifest-retrieve]]
- [[commands/jq-extract-digests]]

## Tools Used


## Tags

- docker
- manifest
- blobs
