---
id: cmd-create-session-001
data: 'session = ShopifyAPI::Session.new(''test.myshopify.com'')'
tags:
  - setup
  - session
type: command
output: '#<ShopifyAPI::Session:0x... url="test.myshopify.com:80">'
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.640Z'
verified: false
validated: true
submitted: true
---
---

# create-session-instance

## Command

```ruby
session = ShopifyAPI::Session.new('test.myshopify.com')
```

## Description

Creates a new Session instance with a shop domain, incorporating configured port/protocol into the URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain | Shop URL (e.g., 'test.myshopify.com') | Yes |

## Examples

### Basic Usage

```ruby
session = ShopifyAPI::Session.new('test.myshopify.com')
puts session.url
```

## Expected Output

Session object with url including port.

## Related

- [[commands/setup-session-benign-port]]
- [[procedures/Exploit-Port-Parameter-for-SSRF]]

---
