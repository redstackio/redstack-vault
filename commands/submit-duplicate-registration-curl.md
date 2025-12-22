---
data: >-
  curl -X POST https://www.████.gov/ioss/site/customer.cfm -d
  "email=user@example.com" -d "prefixRank=Mr" -d "firstName=Test" -d
  "lastName=User" --data-urlencode "other fields as required"
tags:
  - duplicate
  - error-trigger
  - curl
  - post-request
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.909Z'
id: 047c1467-d435-4c96-86ad-21f3164eeee6
verified: false
validated: true
submitted: true
---
# submit-duplicate-registration-curl

## Command

```bash
curl -X POST https://www.████.gov/ioss/site/customer.cfm \
  -d "email=user@example.com" \
  -d "prefixRank=Mr" \
  -d "firstName=Test" \
  -d "lastName=User" \
  --data-urlencode "other fields as required"
```

## Description

This command resubmits the registration POST request with a duplicate email to trigger an error response that reflects form inputs, essential for identifying XSS opportunities in the error handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-d` | Adds form data, reusing email for duplication | Yes |
| `--data-urlencode` | Handles encoding for special characters | No |

## Examples

### Basic Usage

```bash
curl -X POST https://www.████.gov/ioss/site/customer.cfm -d "email=user@example.com" -d "prefixRank=Mr"
```

### Advanced Usage

```bash
curl -X POST https://www.████.gov/ioss/site/customer.cfm -d "email=user@example.com" -d "prefixRank=Mr" -v
```

## Expected Output

HTTP 200 with error HTML, e.g., "this email address already exists in the system", and reflected prefixRank value in the page source.

## Related

- [[commands/submit-initial-registration-curl]]
- [[commands/inject-xss-payload-curl]]
