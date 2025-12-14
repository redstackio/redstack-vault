---
data: 'curl -b cookies.txt https://chaturbate.com/api/list_whitelabel_subdomains'
tags:
  - web
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.837Z'
id: 90bf6b0a-683b-4417-99fb-ee684acc392a
verified: false
validated: true
submitted: true
---
# curl-list-subdomains

## Command

```bash
curl -b cookies.txt https://chaturbate.com/api/list_whitelabel_subdomains
```

## Description

Retrieves the list of whitelabel subdomains for an authenticated Chaturbate account to verify if the limit bypass was successful.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b cookies.txt` | Load authentication cookies | Yes |

## Examples

### Basic Usage

```bash
curl -b cookies.txt https://example.com/api/list_subdomains
```

### Advanced Usage

```bash
curl -b cookies.txt -H "Accept: application/json" https://example.com/api/list_subdomains | jq '.subdomains[]'
```

## Expected Output

JSON array of subdomains, e.g., {"subdomains": ["sub1.example.com", "sub2.example.com"]}, with count exceeding limits indicating success.

## Related

- [[Related Procedure|procedures/Exploit-TOCTOU-Race-Condition-to-Bypass-Subdomain-Limit]]
