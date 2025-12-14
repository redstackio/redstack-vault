---
id: cmd-uuid-3
data: 'curl https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=xxx'
tags:
  - token-inspect
  - oauth
type: command
output: >-
  JSON with issued_to, audience, scope (e.g., devstorage.read_only,
  monitoring.write, logging.write), expires_in, access_type
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.514Z'
verified: false
validated: true
submitted: true
---
# curl-inspect-token-scopes

## Command

```bash
curl https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=xxx
```

## Description

Validate and retrieve information about the GCP access token, including scopes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `access_token=xxx` | The obtained service account token | Yes |

## Examples

### Basic Usage

```bash
curl https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=xxx
```

## Expected Output

JSON with issued_to, audience, scope (e.g., devstorage.read_only, monitoring.write, logging.write), expires_in, access_type.

## Related

- [[Related Procedure: Inspect-Token-Scopes-and-Retrieve-Project-ID]]
