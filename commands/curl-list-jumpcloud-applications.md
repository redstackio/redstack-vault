---
data: 'curl -H "x-api-key: ██████" "https://console.jumpcloud.com/api/applications"'
tags:
  - api-enumeration
  - jumpcloud
  - sso-discovery
type: command
executor: bash
platforms:
  - Cloud
id: 34e1ade5-a6c2-4a89-9673-f73e5270e4b5
created_at: '2025-12-14T17:32:48.644Z'
updated_at: '2025-12-14T17:32:48.644Z'
verified: false
validated: true
submitted: true
---
# curl-list-jumpcloud-applications

## Command

```bash
curl -H "x-api-key: ██████" "https://console.jumpcloud.com/api/applications"
```

## Description

This command lists SSO applications configured in JumpCloud, revealing integrations like AWS for potential takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "x-api-key: KEY"` | Header for API authentication | Yes |
| `URL` | Endpoint for applications | Yes |

## Examples

### Basic Usage

```bash
curl -H "x-api-key: ██████" "https://console.jumpcloud.com/api/applications"
```

### Advanced Usage

Filter for specific apps:

```bash
curl -H "x-api-key: ██████" "https://console.jumpcloud.com/api/applications" | jq '.[] | select(.name == "AWS")'
```

## Expected Output

JSON list of application objects with names, IDs, and configurations.

## Related

- [[commands/curl-list-jumpcloud-system-users]]
- [[procedures/Exploit-Leaked-JumpCloud-API-Key]]
