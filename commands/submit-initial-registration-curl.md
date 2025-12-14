---
data: >-
  curl -X POST https://www.████.gov/ioss/site/customer.cfm -d
  "email=user@example.com" -d "prefixRank=Mr" -d "firstName=Test" -d
  "lastName=User" --data-urlencode "other fields as required"
tags:
  - registration
  - curl
  - post-request
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.912Z'
id: f88b9965-5302-4d6f-b1a5-aad7e59f9827
verified: false
validated: true
submitted: true
---
# submit-initial-registration-curl

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

This command submits an initial HTTP POST request to the DoD registration endpoint to create a new user account, using curl for simplicity. It is used in the first step of XSS exploitation to register an email for later duplicate testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-d` | Adds form data key-value pairs | Yes |
| `--data-urlencode` | URL-encodes additional fields if needed | No |

## Examples

### Basic Usage

```bash
curl -X POST https://www.████.gov/ioss/site/customer.cfm -d "email=user@example.com" -d "prefixRank=Mr"
```

### Advanced Usage

```bash
curl -X POST https://www.████.gov/ioss/site/customer.cfm -d "email=user@example.com" -d "prefixRank=Mr" -H "User-Agent: Mozilla/5.0" --cookie "session=abc123"
```

## Expected Output

HTTP 200 OK response with HTML containing a success message like "Registration complete". No errors, and the email is now registered.

## Related

- [[commands/submit-duplicate-registration-curl]]
- [[commands/inject-xss-payload-curl]]
