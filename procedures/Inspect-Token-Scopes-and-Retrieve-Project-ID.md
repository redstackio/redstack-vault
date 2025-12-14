---
id: proc-uuid-5
tags:
  - token-inspect
  - project-discovery
  - gcp
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-inspect-token-scopes]]'
  - '[[commands/curl-retrieve-gcp-project-id]]'
verified: false
platforms:
  - GCP
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T03:46:09.548Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Inspect-Token-Scopes-and-Retrieve-Project-ID

## Summary

Validate the stolen service account token by querying its scopes via Google's OAuth endpoint and retrieve the GCP project ID from metadata for targeted API calls.

## Description

Send the token to the tokeninfo endpoint to confirm scopes (e.g., devstorage.read_only, monitoring.write, logging.write). Then, access metadata to get the project ID like gitlab-ci-155816, enabling bucket listing.

## Requirements

1. Valid access token from previous step
2. SSRF access to metadata
3. Internet access from CI runner for OAuth query

## Defense

- Rotate service account tokens frequently
- Limit token scopes to minimal required
- Audit tokeninfo API calls in GCP

## Objectives

1. Confirm token permissions
2. Obtain project ID
3. Identify accessible resources

## Instructions

### Step 1: Inspect Token Scopes

**Context**: Query OAuth to get token details.

**Command** ([[commands/curl-inspect-token-scopes]]):
```bash
curl https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=xxx
```

> Replace xxx with actual token. Expected: JSON with scopes, audience, expires_in.

### Step 2: Retrieve Project ID

**Context**: Get project from metadata.

**Command** ([[commands/curl-retrieve-gcp-project-id]]):
```bash
curl http://metadata.google.internal/computeMetadata/v1/project/project-id
```

> Expected: String like gitlab-ci-155816.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Steal Application Access Token]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inspect-token-scopes]]
- [[commands/curl-retrieve-gcp-project-id]]

## Tools Used

- [[tools/curl]]

## Tags

- token-inspect
- gcp
