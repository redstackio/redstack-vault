---
data: 'curl http://localhost:8080/apps/user_oidc/id4me'
tags:
  - web
  - access
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: a84d0f13-f909-40cd-9761-7805873955a7
created_at: '2025-12-13T09:01:26.578Z'
updated_at: '2025-12-13T09:01:26.578Z'
verified: false
validated: true
submitted: true
---
# Curl Access ID4me Endpoint

## Command

```bash
curl http://localhost:8080/apps/user_oidc/id4me
```

## Description

This command accesses the Nextcloud ID4me endpoint directly, useful for testing if the vulnerable path is exposed to unauthenticated users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://localhost:8080/apps/user_oidc/id4me` | The URL of the ID4me endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://localhost:8080/apps/user_oidc/id4me
```

### Advanced Usage

```bash
curl -v http://target-server:8080/apps/user_oidc/id4me
```

## Expected Output

HTML or JSON response from the ID4me authentication page if vulnerable.

## Related

- [[procedures/Access-ID4me-Endpoint-Unauthenticated]]
