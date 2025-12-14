---
id: cmd-visit-confirmation
data: >-
  curl -X GET
  "https://app.upserve.com/b/test-brand?email_token=2aa7296c678e11e7ab2f0242ac110002"
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
tags:
  - confirmation
  - get-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.081Z'
verified: false
validated: true
submitted: true
---
# visit-email-confirmation-link

## Command

```bash
curl -X GET "https://app.upserve.com/b/test-brand?email_token=2aa7296c678e11e7ab2f0242ac110002" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
```

## Description

GET request to the email confirmation URL to activate a newly created account, persisting any stored data like malicious UUIDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `email_token` | Token from confirmation email | Yes |
| `brand_pretty_url` | Brand in URL path | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/b/brand?email_token=token123"
```

### Advanced Usage

With verbose output:

```bash
curl -v -X GET "https://target.com/b/brand?email_token=token123" -H "User-Agent: Mozilla/5.0"
```

## Expected Output

HTTP 200 or 302 redirect to success page; account activated.

## Related

- [[procedures/Confirm-Account-via-Email-Link]]
