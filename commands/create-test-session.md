---
id: cmd-uuid-3
data: 'session = ShopifyAPI::Session.new(''test.myshopify.com'')'
tags:
  - setup
  - shopify
type: command
output: '#<ShopifyAPI::Session:0x... url="test.myshopify.com:80">'
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.758Z'
verified: false
validated: true
submitted: true
---
# create-test-session

## Command

```ruby
session = ShopifyAPI::Session.new('test.myshopify.com')
```

## Description

Creates a new ShopifyAPI::Session instance for a given shop domain, incorporating any prior setup configurations like port.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain | Shop URL (e.g., 'test.myshopify.com') | Yes |

## Examples

### Basic Usage

```ruby
session = ShopifyAPI::Session.new('test.myshopify.com')
```

## Expected Output

Session object with URL including port if set.

## Related

- [[commands/setup-session-with-port]]
