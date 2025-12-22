---
id: cmd-uuid-2
data: 'ShopifyAPI::Session.setup port: ''80'', secret: '''''
tags:
  - setup
  - shopify
  - testing
type: command
output: '{:port=>"80", :secret=>""}'
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.760Z'
verified: false
validated: true
submitted: true
---
# setup-session-with-port

## Command

```ruby
ShopifyAPI::Session.setup port: '80', secret: ''
```

## Description

Configures global session parameters for the Shopify API SDK, setting the port to append to shop URLs and an empty client secret for testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| port | Port value to append (e.g., '80') | Yes |
| secret | Client secret (empty for test) | Yes |

## Examples

### Basic Usage

```ruby
ShopifyAPI::Session.setup port: '80', secret: ''
```

### Advanced Usage

With protocol: ShopifyAPI::Session.setup protocol:'https', port: '80', secret: ''

## Expected Output

{:port=>"80", :secret=>""}

## Related

- [[commands/create-test-session]]
