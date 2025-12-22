---
id: proc-blob-upload-poisoning
tags:
  - docker
  - poisoning
  - blob-upload
  - registry
type: procedure
tools:
  - '[[tools/docker_fetch]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Resource Hijacking]]'
updated_at: '2025-12-14T17:32:57.734Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Resource Hijacking]]'
---
---
# Test-Blob-Upload-for-Poisoning

## Summary

This procedure tests the registry's blob upload endpoint to upload malicious content, enabling image poisoning and potential compromise of downstream builds.

## Description

The Docker Registry v2 API's /v2/<name>/blobs/uploads/ endpoint accepts POST requests without authentication, returning a UUID for chunked uploads. This allows injecting malicious layers into images like 'lgtm/top', affecting site reliability and enabling escapes.

## Requirements

1. Tunneled registry access
2. Tool or curl for API interaction
3. Knowledge of Docker Registry API specs

## Defense

Defensive measures and detection strategies:

- Enforce auth and validation on upload endpoints
- Scan uploads for malicious content
- Restrict write access in internal registries

## Objectives

1. Confirm unrestricted upload capability
2. Poison images for impact
3. Demonstrate supply chain risk

## Instructions

### Step 1: Initiate Blob Upload

**Context**: Send POST to start upload and get UUID.

Use curl:

```bash
curl -X POST http://127.0.0.1:5555/v2/lgtm/top/blobs/uploads/
```

> Expected: 202 Accepted with Location header containing UUID, e.g., /v2/lgtm/top/blobs/uploads/uuid.

### Step 2: Upload Malicious Blob

**Context**: Use UUID to PUT malicious data chunks.

Follow API: PUT to the location with Content-Range.

> Expected: Successful upload; reference Docker docs for full poisoning workflow.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Resource Hijacking]] Resource Hijacking

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/docker_fetch]]

## Tags

- poisoning
- blob-upload

---
