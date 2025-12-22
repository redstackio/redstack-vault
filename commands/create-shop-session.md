---
id: cmd-uuid-5
data: 'session = ShopifyAPI::Session.new(''some-shop.myshopify.com'')'
tags:
  - exploitation
  - shopify
type: command
output: Session object with manipulated URL
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.730Z'
verified: false
validated: true
submitted: true
---
# create-shop-session

## Command

```ruby
session = ShopifyAPI::Session.new('some-shop.myshopify.com')
```

## Description

Initializes a session after malicious setup, using the injected parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain | Shop domain | Yes |

## Examples

### Basic Usage

```ruby
session = ShopifyAPI::Session.new('some-shop.myshopify.com')
```

## Expected Output

Session with URL influenced by prior setup.

## Related

- [[commands/setup-session-with-malicious-port]]
