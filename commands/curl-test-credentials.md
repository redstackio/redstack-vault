---
data: >-
  curl -u 'username:password'
  https://snapchat.jfrog.io/artifactory/api/system/ping
tags:
  - authentication
  - test
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: ba8a33fc-d1ea-440e-8293-2c3042de985d
created_at: '2025-12-11T03:47:56.522Z'
updated_at: '2025-12-11T03:47:56.522Z'
verified: false
validated: true
submitted: true
---
# curl-test-credentials

## Command

```bash
curl -u 'username:password' https://snapchat.jfrog.io/artifactory/api/system/ping
```

## Description

Tests basic authentication against a web endpoint using Curl, useful for validating leaked credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u 'username:password'` | Basic auth credentials | Yes |
| `https://snapchat.jfrog.io/artifactory/api/system/ping` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -u 'username:password' https://snapchat.jfrog.io/artifactory/api/system/ping
```

### Advanced Usage

```bash
curl -u 'username:password' -v https://snapchat.jfrog.io/artifactory/api/system/ping
```

## Expected Output

'OK' if successful, or HTTP status code indicating authentication result.

## Related

- [[commands/jfrog-cli-login]]
- [[procedures/Extract-and-Validate-Leaked-Artifactory-Credentials]]
