---
data: 'curl -u anonymous:anonymous https://nexus.imgur.com/service/rest/v1/status'
tags:
  - auth
  - web
  - default-creds
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.499Z'
id: 562fc33f-25d5-41fa-a728-0ac7024f4761
verified: false
validated: true
submitted: true
---
# curl-login-nexus-anonymous

## Command

```bash
curl -u anonymous:anonymous https://nexus.imgur.com/service/rest/v1/status
```

## Description

This command authenticates to Nexus using default anonymous credentials and checks the service status, verifying successful login for unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Username:password for basic auth | Yes |
| `https://nexus.imgur.com/service/rest/v1/status` | Status endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -u anonymous:anonymous https://nexus.imgur.com/service/rest/v1/status
```

### Advanced Usage

```bash
curl -u anonymous:anonymous -c cookies.txt https://nexus.imgur.com/#browse/browse:default
```

## Expected Output

{"apiVersion":"1.0","data":{"version":"3.x.x","edition":"OSS","status":"OK"}}

Confirms authenticated access.

## Related

- [[Related Procedure]]
