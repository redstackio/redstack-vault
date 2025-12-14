---
id: cmd-setup-benign-001
data: 'ShopifyAPI::Session.setup port: ''80'', secret: '''''
tags:
  - setup
  - testing
type: command
output: '{:port=>"80", :secret=>""}'
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.645Z'
verified: false
validated: true
submitted: true
---
---

# setup-session-benign-port

## Command

```ruby
ShopifyAPI::Session.setup port: '80', secret: ''
```

## Description

Configures global Session parameters with a benign port value and empty secret for testing URL construction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| port | Port string (e.g., '80') | Yes |
| secret | Client secret (empty for test) | Yes |

## Examples

### Basic Usage

```ruby
ShopifyAPI::Session.setup port: '80', secret: ''
```

## Expected Output

{:port=>"80", :secret=>""}

## Related

- [[commands/create-session-instance]]
- [[procedures/Test-Session-Setup-with-Port-Parameter]]

---
